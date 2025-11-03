import time
import threading
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum

class RateLimitResult(Enum):
    """Enumeration for rate limiting results"""
    ALLOWED = "allowed"
    RATE_LIMITED = "rate_limited"
    
@dataclass
class RateLimitResponse:
    """Response object for rate limit checks"""
    result: RateLimitResult
    tokens_remaining: int
    retry_after_seconds: Optional[float] = None
    total_requests: int = 0

class TokenBucket:
    """
    Token Bucket Rate Limiter Implementation
    
    The token bucket algorithm works by:
    1. Maintaining a bucket with a maximum capacity of tokens
    2. Refilling tokens at a constant rate
    3. Consuming tokens for each request
    4. Rejecting requests when no tokens are available
    """
    
    def __init__(self, capacity: int, refill_rate: float, initial_tokens: Optional[int] = None):
        """
        Initialize the token bucket
        
        Args:
            capacity: Maximum number of tokens the bucket can hold
            refill_rate: Number of tokens added per second
            initial_tokens: Initial number of tokens (defaults to capacity)
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = initial_tokens if initial_tokens is not None else capacity
        self.last_refill = time.time()
        self._lock = threading.Lock()
        
    def _refill_tokens(self) -> None:
        """Refill tokens based on elapsed time"""
        now = time.time()
        elapsed = now - self.last_refill
        tokens_to_add = elapsed * self.refill_rate
        
        # Add tokens but don't exceed capacity
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now
        
    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens from the bucket
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            True if tokens were successfully consumed, False otherwise
        """
        with self._lock:
            self._refill_tokens()
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
    
    def peek(self) -> int:
        """Get current number of tokens without consuming any"""
        with self._lock:
            self._refill_tokens()
            return int(self.tokens)
    
    def time_until_tokens(self, required_tokens: int) -> float:
        """
        Calculate time until specified number of tokens will be available
        
        Args:
            required_tokens: Number of tokens needed
            
        Returns:
            Time in seconds until tokens will be available (0 if already available)
        """
        with self._lock:
            self._refill_tokens()
            
            if self.tokens >= required_tokens:
                return 0.0
                
            tokens_needed = required_tokens - self.tokens
            return tokens_needed / self.refill_rate

class RateLimiter:
    """
    Multi-client rate limiter using token buckets
    
    Supports different rate limiting strategies:
    - Per-client rate limiting
    - Global rate limiting
    - Custom bucket configurations per client
    """
    
    def __init__(self, default_capacity: int = 10, default_refill_rate: float = 1.0):
        """
        Initialize the rate limiter
        
        Args:
            default_capacity: Default bucket capacity for new clients
            default_refill_rate: Default refill rate for new clients
        """
        self.default_capacity = default_capacity
        self.default_refill_rate = default_refill_rate
        self.buckets: Dict[str, TokenBucket] = {}
        self.request_counts: Dict[str, int] = {}
        self._lock = threading.Lock()
        
    def get_or_create_bucket(self, client_id: str, 
                           capacity: Optional[int] = None,
                           refill_rate: Optional[float] = None) -> TokenBucket:
        """Get existing bucket or create new one for client"""
        with self._lock:
            if client_id not in self.buckets:
                cap = capacity or self.default_capacity
                rate = refill_rate or self.default_refill_rate
                self.buckets[client_id] = TokenBucket(cap, rate)
                self.request_counts[client_id] = 0
            return self.buckets[client_id]
    
    def is_allowed(self, client_id: str, tokens: int = 1,
                   capacity: Optional[int] = None,
                   refill_rate: Optional[float] = None) -> RateLimitResponse:
        """
        Check if request is allowed for client
        
        Args:
            client_id: Unique identifier for the client
            tokens: Number of tokens to consume
            capacity: Custom bucket capacity (optional)
            refill_rate: Custom refill rate (optional)
            
        Returns:
            RateLimitResponse with result and metadata
        """
        bucket = self.get_or_create_bucket(client_id, capacity, refill_rate)
        
        with self._lock:
            self.request_counts[client_id] = self.request_counts.get(client_id, 0) + 1
        
        if bucket.consume(tokens):
            return RateLimitResponse(
                result=RateLimitResult.ALLOWED,
                tokens_remaining=bucket.peek(),
                total_requests=self.request_counts[client_id]
            )
        else:
            retry_after = bucket.time_until_tokens(tokens)
            return RateLimitResponse(
                result=RateLimitResult.RATE_LIMITED,
                tokens_remaining=bucket.peek(),
                retry_after_seconds=retry_after,
                total_requests=self.request_counts[client_id]
            )
    
    def get_client_stats(self, client_id: str) -> Dict:
        """Get statistics for a specific client"""
        if client_id not in self.buckets:
            return {"error": "Client not found"}
            
        bucket = self.buckets[client_id]
        return {
            "client_id": client_id,
            "tokens_available": bucket.peek(),
            "bucket_capacity": bucket.capacity,
            "refill_rate": bucket.refill_rate,
            "total_requests": self.request_counts.get(client_id, 0)
        }
    
    def reset_client(self, client_id: str) -> bool:
        """Reset a client's bucket to full capacity"""
        if client_id in self.buckets:
            bucket = self.buckets[client_id]
            with bucket._lock:
                bucket.tokens = bucket.capacity
                bucket.last_refill = time.time()
            return True
        return False
    
    def remove_client(self, client_id: str) -> bool:
        """Remove a client's bucket and stats"""
        with self._lock:
            removed_bucket = self.buckets.pop(client_id, None)
            removed_count = self.request_counts.pop(client_id, None)
            return removed_bucket is not None

# Example usage and testing
def demonstrate_rate_limiter():
    """Demonstrate various rate limiter features"""
    print("=== Token Bucket Rate Limiter Demo ===\n")
    
    # Create rate limiter: 5 requests per second, burst of 10
    limiter = RateLimiter(default_capacity=10, default_refill_rate=5.0)
    
    print("1. Testing burst capacity...")
    client_id = "user_123"
    
    # Test burst - should allow up to 10 requests immediately
    burst_results = []
    for i in range(12):
        result = limiter.is_allowed(client_id)
        burst_results.append(result.result == RateLimitResult.ALLOWED)
        print(f"Request {i+1}: {'✓ Allowed' if result.result == RateLimitResult.ALLOWED else '✗ Rate Limited'} "
              f"(Tokens remaining: {result.tokens_remaining})")
    
    print(f"\nBurst test: {sum(burst_results)}/12 requests allowed")
    
    print("\n2. Testing token refill...")
    print("Waiting 2 seconds for tokens to refill...")
    time.sleep(2)
    
    # Should have ~10 tokens available after 2 seconds
    result = limiter.is_allowed(client_id)
    print(f"After 2s wait: {'✓ Allowed' if result.result == RateLimitResult.ALLOWED else '✗ Rate Limited'} "
          f"(Tokens: {result.tokens_remaining})")
    
    print("\n3. Testing multiple clients...")
    
    # Test different clients with different limits
    clients_config = [
        ("premium_user", 20, 10.0),  # 20 burst, 10 per second
        ("basic_user", 5, 2.0),      # 5 burst, 2 per second
        ("api_service", 100, 50.0)   # 100 burst, 50 per second
    ]
    
    for client, capacity, rate in clients_config:
        result = limiter.is_allowed(client, capacity=capacity, refill_rate=rate)
        stats = limiter.get_client_stats(client)
        print(f"{client}: {result.result.value}, Capacity: {stats['bucket_capacity']}, "
              f"Rate: {stats['refill_rate']}/s, Available: {stats['tokens_available']}")
    
    print("\n4. Testing retry-after calculation...")
    
    # Exhaust tokens for a client
    test_client = "test_user"
    for _ in range(10):
        limiter.is_allowed(test_client)
    
    # Try one more request to get retry-after
    result = limiter.is_allowed(test_client)
    if result.result == RateLimitResult.RATE_LIMITED:
        print(f"Rate limited. Retry after: {result.retry_after_seconds:.2f} seconds")

# Decorator for easy function rate limiting
def rate_limit(capacity: int = 10, refill_rate: float = 1.0, 
               key_func=None, limiter_instance=None):
    """
    Decorator to add rate limiting to functions
    
    Args:
        capacity: Token bucket capacity
        refill_rate: Tokens per second
        key_func: Function to generate client key (defaults to using arguments)
        limiter_instance: Existing RateLimiter instance (creates new if None)
    """
    if limiter_instance is None:
        limiter_instance = RateLimiter(capacity, refill_rate)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Generate client key
            if key_func:
                client_key = key_func(*args, **kwargs)
            else:
                client_key = f"{func.__name__}_{hash(str(args) + str(sorted(kwargs.items())))}"
            
            # Check rate limit
            result = limiter_instance.is_allowed(client_key)
            
            if result.result == RateLimitResult.RATE_LIMITED:
                raise Exception(f"Rate limit exceeded. Retry after {result.retry_after_seconds:.2f} seconds")
            
            return func(*args, **kwargs)
        
        wrapper.limiter = limiter_instance
        return wrapper
    return decorator

# Example of decorator usage
@rate_limit(capacity=5, refill_rate=2.0, key_func=lambda user_id: f"api_call_{user_id}")
def api_call(user_id: str, data: str):
    """Simulated API call with rate limiting"""
    return f"Processing {data} for user {user_id}"

# Advanced: Sliding window counter (alternative approach)
class SlidingWindowCounter:
    """
    Alternative rate limiting using sliding window counter
    More memory intensive but provides smoother rate limiting
    """
    
    def __init__(self, limit: int, window_seconds: int, granularity_seconds: int = 1):
        """
        Initialize sliding window counter
        
        Args:
            limit: Maximum requests per window
            window_seconds: Window size in seconds  
            granularity_seconds: Bucket granularity in seconds
        """
        self.limit = limit
        self.window_seconds = window_seconds
        self.granularity_seconds = granularity_seconds
        self.buckets_count = window_seconds // granularity_seconds
        self.client_windows: Dict[str, Dict[int, int]] = {}
        self._lock = threading.Lock()
    
    def is_allowed(self, client_id: str) -> bool:
        """Check if request is allowed under sliding window"""
        with self._lock:
            now = int(time.time())
            bucket_time = now // self.granularity_seconds
            
            if client_id not in self.client_windows:
                self.client_windows[client_id] = {}
            
            window = self.client_windows[client_id]
            
            # Clean old buckets
            cutoff_time = bucket_time - self.buckets_count
            self.client_windows[client_id] = {
                t: count for t, count in window.items() 
                if t > cutoff_time
            }
            
            # Count requests in current window
            current_count = sum(window.values())
            
            if current_count >= self.limit:
                return False
            
            # Add current request
            window[bucket_time] = window.get(bucket_time, 0) + 1
            return True

if __name__ == "__main__":
    # Run demonstration
    demonstrate_rate_limiter()
    
    print("\n=== Testing Function Decorator ===")
    
    # Test the decorator
    try:
        for i in range(7):  # Try 7 requests (limit is 5)
            result = api_call("user123", f"request_{i}")
            print(f"✓ {result}")
    except Exception as e:
        print(f"✗ {e}")
    
    print("\n=== Rate Limiter Implementation Complete ===")