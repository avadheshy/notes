# Rate Limiting Algorithms in Python + Redis

> A practical guide to all 5 major rate limiting algorithms implemented with Python and Redis.

---

## Setup

```bash
pip install redis
```

```python
import redis
import time
import uuid
import math

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

---

## 1. Fixed Window Counter

### Concept
Divides time into fixed windows (e.g., every 60 seconds). Counts requests per window. Simple but suffers from **boundary burst** — a client can send 2x the limit by hitting the end of one window and the start of the next.

```
|--- window 1 ---|--- window 2 ---|
  ^limit=10 ok    ^limit=10 ok
         ^^^ burst of 20 at boundary!
```

### Implementation

```python
def fixed_window_is_allowed(user_id: str, limit: int, window_seconds: int) -> bool:
    """
    Returns True if the request is allowed, False if rate limited.
    
    :param user_id: Unique identifier for the client
    :param limit: Max requests allowed per window
    :param window_seconds: Window size in seconds
    """
    # Key includes the current window timestamp to auto-segment windows
    current_window = int(time.time()) // window_seconds
    key = f"fixed_window:{user_id}:{current_window}"

    # Increment counter atomically; set TTL on first request
    pipe = r.pipeline()
    pipe.incr(key)
    pipe.expire(key, window_seconds)
    results = pipe.execute()

    count = results[0]
    return count <= limit


# --- Usage ---
user = "user:42"
for i in range(13):
    allowed = fixed_window_is_allowed(user, limit=10, window_seconds=60)
    print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
```

### Output
```
Request 1-10:  ✅ Allowed
Request 11-13: ❌ Blocked
```

### Pros & Cons
| ✅ Pros | ❌ Cons |
|---|---|
| Simple, O(1) operations | Boundary burst problem |
| Low memory usage | Not smooth — all quota resets at once |
| Easy to reason about | |

---

## 2. Sliding Window Log

### Concept
Stores a **timestamp log** of every request in a sorted set. On each request, removes old timestamps outside the window, then checks the count. Accurate but memory-heavy.

```
Now = T
Window = 60s
Log: [T-55, T-40, T-20, T-5]  → count = 4
```

### Implementation

```python
def sliding_window_log_is_allowed(user_id: str, limit: int, window_seconds: int) -> bool:
    """
    Uses Redis Sorted Set: score = timestamp, member = unique request ID.
    
    :param user_id: Unique identifier for the client
    :param limit: Max requests allowed in the sliding window
    :param window_seconds: Window size in seconds
    """
    key = f"sliding_log:{user_id}"
    now = time.time()
    window_start = now - window_seconds

    # Create a unique member identifier to prevent overwriting at the same millisecond
    unique_member = f"{now}:{uuid.uuid4()}"

    pipe = r.pipeline()
    # Remove timestamps outside the window
    pipe.zremrangebyscore(key, '-inf', window_start)
    # Add current request with current timestamp as score and a unique member string
    pipe.zadd(key, {unique_member: now})
    # Count requests in window
    pipe.zcard(key)
    # Auto-expire the key after the window
    pipe.expire(key, window_seconds + 1)
    results = pipe.execute()

    count = results[2]
    return count <= limit


# --- Usage ---
user = "user:42"
for i in range(5):
    allowed = sliding_window_log_is_allowed(user, limit=3, window_seconds=10)
    print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
    time.sleep(0.5)
```

### Pros & Cons
| ✅ Pros | ❌ Cons |
|---|---|
| Perfectly accurate | High memory — stores every request timestamp |
| No boundary burst problem | Not suitable for very high traffic |
| Intuitive | |

---

## 3. Sliding Window Counter

### Concept
A **hybrid** of Fixed Window + Sliding Window Log. Uses two adjacent fixed windows and interpolates. Memory-efficient and approximately accurate (typically within 1% error).

```
prev_window  |  curr_window
[-----------|-----|--------]
            ^     ^
         window  now
         start

rate = prev_count * overlap_ratio + curr_count
```

### Implementation

```python
def sliding_window_counter_is_allowed(user_id: str, limit: int, window_seconds: int) -> bool:
    """
    Approximates sliding window using two fixed windows + weighted interpolation.
    
    :param user_id: Unique identifier for the client
    :param limit: Max requests allowed
    :param window_seconds: Window size in seconds
    """
    now = time.time()
    current_window = int(now) // window_seconds
    prev_window = current_window - 1

    curr_key = f"sw_counter:{user_id}:{current_window}"
    prev_key = f"sw_counter:{user_id}:{prev_window}"

    pipe = r.pipeline()
    pipe.get(prev_key)
    pipe.get(curr_key)
    pipe.incr(curr_key)
    pipe.expire(curr_key, window_seconds * 2)
    results = pipe.execute()

    prev_count = int(results[0] or 0)
    curr_count = int(results[2])  # after incr

    # How far into the current window are we? (0.0 → 1.0)
    elapsed_in_window = (now % window_seconds) / window_seconds

    # Weight: how much of the previous window overlaps our sliding window
    prev_weight = 1.0 - elapsed_in_window

    estimated_count = prev_count * prev_weight + curr_count
    return estimated_count <= limit


# --- Usage ---
user = "user:42"
for i in range(12):
    allowed = sliding_window_counter_is_allowed(user, limit=10, window_seconds=60)
    print(f"Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
```

### Pros & Cons
| ✅ Pros | ❌ Cons |
|---|---|
| Memory-efficient (only 2 counters) | Slight approximation (~1% error) |
| Better than fixed window | Slightly more complex logic |
| Good for production use | |

---

## 4. Token Bucket

### Concept
A **bucket** holds tokens up to a max capacity. Tokens are added at a fixed **refill rate**. Each request consumes one token. If no tokens → request is denied. Allows **bursting** up to bucket capacity.

```
Bucket capacity: 10
Refill rate: 2 tokens/sec

t=0: [🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙] → 10 tokens
t=1: burst 10 requests → bucket empty
t=1.5: 1 new token added
t=2: 1 more token added → can accept 2 requests
```

### Implementation

```python
def token_bucket_is_allowed(
    user_id: str,
    capacity: int,
    refill_rate: float  # tokens per second
) -> bool:
    """
    Token bucket using Redis hash to store {tokens, last_refill_time}.
    
    :param user_id: Unique identifier for the client
    :param capacity: Maximum tokens the bucket can hold
    :param refill_rate: Tokens added per second
    """
    key = f"token_bucket:{user_id}"
    now = time.time()

    # Lua script for atomicity — read, compute, write in one shot
    lua_script = """
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local refill_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])

    local data = redis.call('HMGET', key, 'tokens', 'last_refill')
    local tokens = tonumber(data[1]) or capacity
    local last_refill = tonumber(data[2]) or now

    -- Calculate tokens to add based on elapsed time
    local elapsed = now - last_refill
    local new_tokens = math.min(capacity, tokens + elapsed * refill_rate)

    if new_tokens >= 1 then
        new_tokens = new_tokens - 1
        redis.call('HMSET', key, 'tokens', new_tokens, 'last_refill', now)
        redis.call('EXPIRE', key, 3600)
        return 1  -- allowed
    else
        redis.call('HMSET', key, 'tokens', new_tokens, 'last_refill', now)
        redis.call('EXPIRE', key, 3600)
        return 0  -- blocked
    end
    """

    script = r.register_script(lua_script)
    result = script(keys=[key], args=[capacity, refill_rate, now])
    return result == 1


# --- Usage ---
user = "user:42"
print("Burst test (10 requests instantly):")
for i in range(12):
    allowed = token_bucket_is_allowed(user, capacity=10, refill_rate=2.0)
    print(f"  Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")

print("\nWaiting 3 seconds for refill (6 tokens)...")
time.sleep(3)
for i in range(4):
    allowed = token_bucket_is_allowed(user, capacity=10, refill_rate=2.0)
    print(f"  Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
```

> **Why Lua?** Redis executes Lua scripts atomically — no race conditions between the read-modify-write cycle. Critical for correctness under concurrent load.

### Pros & Cons
| ✅ Pros | ❌ Cons |
|---|---|
| Allows controlled bursting | Slightly complex implementation |
| Smooth token replenishment | Burst can still overwhelm downstream |
| Used by AWS, Stripe, etc. | |

---

## 5. Leaky Bucket

### Concept
Requests enter a **queue (bucket)** and are processed at a **fixed outflow rate**, regardless of how fast they arrive. Excess requests overflow and are dropped. Produces a **perfectly smooth** output rate — no bursting.

```
Requests → [🪣 bucket/queue] → processed at fixed rate
                   ↓ overflow dropped
```

### Implementation

```python
def leaky_bucket_is_allowed(
    user_id: str,
    capacity: int,
    leak_rate: float  # requests leaked (processed) per second
) -> bool:
    """
    Leaky bucket: tracks last_leak_time and current queue level.
    Uses Lua for atomic read-modify-write.
    
    :param user_id: Unique identifier for the client
    :param capacity: Max queue size (bucket size)
    :param leak_rate: Requests processed per second (outflow rate)
    """
    key = f"leaky_bucket:{user_id}"
    now = time.time()

    lua_script = """
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local leak_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])

    local data = redis.call('HMGET', key, 'level', 'last_leak')
    local level = tonumber(data[1]) or 0
    local last_leak = tonumber(data[2]) or now

    -- Drain the bucket based on elapsed time
    local elapsed = now - last_leak
    local leaked = elapsed * leak_rate
    level = math.max(0, level - leaked)

    if level < capacity then
        level = level + 1
        redis.call('HMSET', key, 'level', level, 'last_leak', now)
        redis.call('EXPIRE', key, 3600)
        return 1  -- allowed (queued)
    else
        redis.call('HMSET', key, 'level', level, 'last_leak', now)
        redis.call('EXPIRE', key, 3600)
        return 0  -- blocked (overflow)
    end
    """

    script = r.register_script(lua_script)
    result = script(keys=[key], args=[capacity, leak_rate, now])
    return result == 1


# --- Usage ---
user = "user:42"
print("Burst test (15 requests instantly):")
for i in range(15):
    allowed = leaky_bucket_is_allowed(user, capacity=10, leak_rate=2.0)
    print(f"  Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")

print("\nWaiting 3 seconds for leak (6 slots freed)...")
time.sleep(3)
for i in range(4):
    allowed = leaky_bucket_is_allowed(user, capacity=10, leak_rate=2.0)
    print(f"  Request {i+1}: {'✅ Allowed' if allowed else '❌ Blocked'}")
```

### Pros & Cons
| ✅ Pros | ❌ Cons |
|---|---|
| Perfectly smooth output rate | No burst tolerance |
| Protects downstream services | Queue adds latency |
| Simple mental model | Requests may wait or be dropped |

---

## Quick Comparison

| Algorithm | Memory | Burst? | Accuracy | Best For |
|---|---|---|---|---|
| Fixed Window | O(1) | Yes (boundary) | ✅ Exact | Simple APIs, internal tools |
| Sliding Window Log | O(n) | No | ✅ Exact | Low-traffic, high-accuracy needs |
| Sliding Window Counter | O(1) | No | ~99% | Production APIs (recommended) |
| Token Bucket | O(1) | ✅ Controlled | ✅ Exact | User-facing APIs (Stripe, AWS) |
| Leaky Bucket | O(1) | No | ✅ Exact | Smooth queue processing, messaging |

---

## FastAPI Integration Example

Plug any algorithm into FastAPI as a dependency:

```python
from fastapi import FastAPI, Request, HTTPException, Depends

app = FastAPI()

def get_user_id(request: Request) -> str:
    # Use IP or auth token as identifier
    return request.client.host

def rate_limit(user_id: str = Depends(get_user_id)):
    # Swap in any algorithm here
    if not token_bucket_is_allowed(user_id, capacity=10, refill_rate=2.0):
        raise HTTPException(status_code=429, detail="Too Many Requests")

@app.get("/api/data", dependencies=[Depends(rate_limit)])
def get_data():
    return {"data": "ok"}
```

---

## Redis Key Design Summary

| Algorithm | Key Pattern | Data Structure |
|---|---|---|
| Fixed Window | `fixed_window:{user}:{window_ts}` | String (counter) |
| Sliding Window Log | `sliding_log:{user}` | Sorted Set |
| Sliding Window Counter | `sw_counter:{user}:{window_ts}` | String (counter) |
| Token Bucket | `token_bucket:{user}` | Hash |
| Leaky Bucket | `leaky_bucket:{user}` | Hash |

> **Golden rule**: Always use Lua scripts (or `MULTI/EXEC` pipelines) for multi-step Redis operations to avoid race conditions under concurrent load.