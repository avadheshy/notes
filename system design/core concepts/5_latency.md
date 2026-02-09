# Latency, Throughput, and Bandwidth: A Complete Guide

Understanding the relationship between latency, throughput, and bandwidth is fundamental to designing and optimizing distributed systems. While related, these concepts measure different aspects of system performance and have distinct implications for user experience.

## Quick Definitions

- **Latency**: How long it takes for a single request to complete (delay)
- **Throughput**: How many requests can be processed per unit time (rate)
- **Bandwidth**: The maximum data transfer capacity available (theoretical limit)

**Key Insight**: A system can have high bandwidth but poor throughput due to high latency, or low latency but limited throughput due to insufficient bandwidth.

---

## Latency

**Latency is the time it takes for a single request to travel from source to destination and back. It measures delay.**

In networking, latency is often called **round-trip time (RTT)**, the time from sending a request to receiving a response.

### Components of Latency

Every network request experiences multiple types of delay that combine to create total latency:

#### 1. Propagation Delay

The time for signals to travel through the physical medium at the speed of light.

**Speed limits**:
- Light in fiber optic: ~200,000 km/s (⅔ speed of light in vacuum)
- Copper wire: slightly slower than fiber
- Wireless: varies by medium

**Example**: Cross-Atlantic request (New York to London, ~6,000 km)
- One-way propagation: 6,000 km ÷ 200,000 km/s = 30ms
- Round-trip minimum: 60ms

**Important**: This is a fundamental physical limit. No amount of optimization can make data travel faster than light through the medium.

#### 2. Transmission Delay

The time required to push all bits of a packet onto the wire.

**Formula**: `Transmission Delay = Packet Size / Link Bandwidth`

**Example**: 1,500-byte packet on 1 Gbps link
- 1,500 bytes = 12,000 bits
- 12,000 bits ÷ 1,000,000,000 bps = 0.012ms

**Impact**: Negligible on high-speed networks, more significant on slower connections (mobile networks, satellite).

#### 3. Processing Delay

Time for network devices and servers to process packets.

**Contributors**:
- Router forwarding decisions (routing table lookup)
- Load balancer routing and health checks
- Server request parsing
- Application logic execution
- Security checks (firewall, DDoS protection)

**Typical values**:
- Modern router: <1ms
- Load balancer: 1-5ms
- Application processing: 10-100ms (varies widely)

#### 4. Queuing Delay

Time spent waiting in buffers when components are busy.

**Causes**:
- Network congestion (packets waiting at routers)
- Server overload (requests in queue)
- Database connection pool exhaustion
- Thread pool saturation

**Characteristics**:
- Highly variable (can be zero or very large)
- Increases non-linearly with load
- Main source of latency spikes
- Can be reduced by adding capacity or load balancing

### Total Latency

```
Total Latency = Propagation + Transmission + Processing + Queuing
```

For a typical web request across the internet:
- Propagation: 30-100ms
- Transmission: <1ms (on modern networks)
- Processing: 10-50ms (routers, load balancers)
- Application processing: 20-200ms
- Queuing: 0-500ms+ (depends on load)

**Total**: 60-850ms+ depending on distance, load, and processing complexity

---

## Measuring Latency

### Why Percentiles Matter More Than Averages

Latency in distributed systems is typically measured using **percentiles** rather than averages to better reflect real user experience.

**The problem with averages**: A few extreme outliers can make average latency meaningless, while the median tells you nothing about worst-case experience.

**Example scenario**:
- 99 requests: 10ms each
- 1 request: 1,000ms

**Average**: (99 × 10 + 1 × 1,000) / 100 = 19.9ms  
**Median (p50)**: 10ms  
**p99**: 1,000ms

The average (19.9ms) doesn't represent any actual user experience. The median (10ms) hides the fact that 1% of users had a terrible experience.

### Common Latency Percentiles

| Percentile | Name | Meaning | Use Case |
|-----------|------|---------|----------|
| p50 | Median | 50% of requests are faster | Typical user experience |
| p90 | 90th percentile | 90% of requests are faster | Good user experience |
| p95 | 95th percentile | 95% of requests are faster | Common SLA metric |
| p99 | 99th percentile | 99% of requests are faster | Detecting outliers |
| p99.9 | 99.9th percentile | 99.9% of requests are faster | Worst-case performance |
| p99.99 | 99.99th percentile | 99.99% of requests are faster | Critical systems only |

### What Percentile Should You Track?

**For user-facing services**: Track p95 and p99
- p50 is often too optimistic
- p99.9+ can be too noisy and hard to improve

**For internal APIs**: Track p50 and p99
- p50 shows typical performance
- p99 catches degradation early

**For critical systems**: Track p99 and p99.9
- Financial transactions
- Real-time communication
- Life-critical systems

### Real-World Example

A web application reports these latency metrics:

```
p50:  25ms  ← Half of users experience this
p90:  50ms  ← 90% of users get this or better
p95: 100ms  ← Still acceptable
p99: 500ms  ← 1 in 100 requests is slow
p99.9: 2s   ← 1 in 1000 requests times out
```

**Diagnosis**: The system performs well for most users but has a long tail. This suggests:
- Database query outliers
- Garbage collection pauses
- Occasional queuing delays
- Backend service timeouts

**Action**: Investigate the slowest 1% of requests, not the average.

---

## Factors Affecting Latency

| Factor | Impact | Typical Addition | Mitigation |
|--------|--------|------------------|------------|
| Geographic distance | Direct proportional | 1ms per ~100km | CDN, edge computing |
| Network congestion | Causes queuing | 10-500ms | Traffic shaping, QoS |
| Server load | Increases processing time | 10-200ms | Auto-scaling, load balancing |
| Database queries | Slow queries add latency | 10-1000ms | Indexes, query optimization |
| DNS resolution | First request only | 20-120ms | DNS caching, low TTL |
| TLS handshake | Initial connection | 50-100ms | Connection pooling, session resumption |
| Number of round trips | Multiplies latency | N × RTT | Batching, protocol optimization |
| Cold starts | First request penalty | 100-5000ms | Keep-alive, warm standby |

### The Impact of Round Trips

Each additional round trip adds one full RTT to latency.

**Example**: Loading a web page with 100ms RTT

```
Traditional HTTP/1.1 (without optimization):
1. DNS lookup:        100ms (1 RTT)
2. TCP handshake:     100ms (1 RTT)
3. TLS handshake:     200ms (2 RTTs)
4. HTTP request:      100ms (1 RTT)
5. Resource requests: 500ms (5 RTTs for 5 resources)
---
Total: 1,000ms before any content displays
```

**With optimization**:
```
HTTP/2 with connection reuse and multiplexing:
1. DNS (cached):       0ms
2. Connection reuse:   0ms
3. Parallel requests: 100ms (1 RTT for all resources)
---
Total: 100ms
```

**10x improvement** just by reducing round trips!

---

## Reducing Latency: Strategies and Techniques

### 1. Geographic Distribution

**Deploy services closer to users to minimize propagation delay.**

**Approaches**:
- **CDN (Content Delivery Network)**: Cache static content at edge locations
- **Edge computing**: Run application logic at edge
- **Multi-region deployment**: Deploy full application stack in multiple regions
- **Anycast routing**: Route to nearest available server

**Impact**: Can reduce latency by 50-200ms for international users

**Example**:
- User in Tokyo → US-based server: 150ms RTT
- User in Tokyo → Japan edge server: 10ms RTT
- **Improvement**: 140ms reduction (93% faster)

### 2. Caching

**Store frequently accessed data closer to where it's needed.**

**Caching layers** (from closest to furthest from user):
1. **Browser cache**: Eliminates server request entirely (0ms latency)
2. **CDN cache**: Serves from edge (10-50ms)
3. **Application cache** (Redis/Memcached): Avoids database query (1-5ms)
4. **Database query cache**: Avoids disk I/O (1-10ms)

**Best practices**:
- Cache at multiple layers
- Set appropriate TTLs (time-to-live)
- Use cache-control headers
- Implement cache invalidation strategy
- Monitor cache hit rates

**Example**:
```
Without cache:
User → Server → Database query (50ms) → Response
Total: 100ms

With cache:
User → Server → Cache hit (1ms) → Response
Total: 25ms
```

### 3. Connection Pooling and Reuse

**Avoid expensive connection setup costs by reusing existing connections.**

**Connection costs**:
- TCP handshake: 1 RTT (50-100ms)
- TLS handshake: 2 RTTs (100-200ms)
- Total: 150-300ms per new connection

**Solutions**:
- **HTTP Keep-Alive**: Reuse HTTP connections
- **Connection pooling**: Maintain pool of database connections
- **TLS session resumption**: Skip full TLS handshake

**Database connection pooling**:
```
Without pooling (each request opens new connection):
Request → Open connection (50ms) → Query (10ms) → Close
Total: 60ms

With pooling:
Request → Get from pool (1ms) → Query (10ms) → Return to pool
Total: 11ms
```

### 4. Database Optimization

**Slow database queries are often the largest source of latency.**

**Optimization techniques**:

**Add indexes**: Turn O(n) scans into O(log n) lookups
```
Without index: SELECT * FROM users WHERE email = 'user@example.com'
Scans 1M rows: 200ms

With index on email:
Index lookup: 5ms
```

**Avoid N+1 queries**: Fetch related data in one query, not N separate queries
```
N+1 pattern (slow):
- Get 100 posts: 1 query (10ms)
- Get author for each post: 100 queries × 5ms = 500ms
Total: 510ms

Optimized with JOIN or IN clause:
- Get posts with authors: 1 query (15ms)
Total: 15ms
```

**Use read replicas**: Route read queries to replicas
- Reduces load on primary
- Can place replicas geographically closer to users
- Accepts eventual consistency

**Denormalize for reads**: Trade storage for query speed
- Pre-compute aggregations
- Store redundant data to avoid JOINs
- Use materialized views

### 5. Protocol Optimization

**Use modern protocols that reduce round trips and improve efficiency.**

**HTTP/1.1 → HTTP/2**:
- Multiplexing: Multiple requests over single connection
- Header compression: Reduces bandwidth
- Server push: Proactively send resources
- Impact: 30-50% latency reduction for typical websites

**HTTP/2 → HTTP/3 (QUIC)**:
- Built on UDP instead of TCP
- Eliminates head-of-line blocking
- Faster connection establishment (1 RTT vs 2-3 RTT)
- Better handling of packet loss
- Impact: 10-30% additional improvement, especially on poor networks

**Protocol comparison for new connection**:
```
HTTP/1.1:
TCP handshake (1 RTT) + TLS handshake (2 RTT) + Request (1 RTT) = 4 RTT

HTTP/2:
Same as HTTP/1.1 = 4 RTT (but better multiplexing)

HTTP/3 (QUIC):
Combined handshake + Request = 1-2 RTT
```

### 6. Asynchronous Processing

**Don't make users wait for non-critical operations.**

**Pattern**: Immediately acknowledge request, process in background

**Examples**:
- Email sending: Queue and send async
- Image processing: Upload, process later
- Report generation: Generate in background, notify when ready
- Analytics: Log events async

**Implementation**:
```
Synchronous (slow):
User submits order → Save to DB → Send email → Process payment → Respond
Total: 500ms

Asynchronous (fast):
User submits order → Save to DB → Queue background jobs → Respond immediately
Total: 50ms (background jobs complete in next few seconds)
```

### 7. Batching and Prefetching

**Reduce round trips by sending multiple items at once.**

**Batching**: Group multiple operations into one request
```
Individual requests:
3 database queries × 10ms each = 30ms

Batch request:
1 query with multiple items = 12ms
```

**Prefetching**: Load data before it's needed
- Load next page while user reads current page
- Preload common navigation destinations
- Warm up caches proactively

---

## Throughput

**Throughput is the number of requests or operations a system can handle per unit of time. It measures rate of processing.**

For web systems, throughput is typically expressed as:
- **Requests per second (RPS)**
- **Transactions per second (TPS)**
- **Queries per second (QPS)**

### Throughput vs Bandwidth

A common confusion: **bandwidth** is the theoretical maximum capacity, while **throughput** is the actual achieved rate.

**Key relationship**: You can never have throughput higher than bandwidth, but throughput is almost always lower.

**Why throughput < bandwidth**:
- Protocol overhead (headers, acknowledgments, retransmissions)
- Network congestion and packet loss
- CPU and memory limitations
- Inefficient resource utilization
- Queuing and serialization

**Example**:
- Network bandwidth: 1 Gbps = 125 MB/s
- Actual throughput: 100 MB/s (80% utilization)
- Lost to: 20% overhead from TCP/IP headers, retransmissions, and processing

### Calculating Throughput

#### Single-Threaded System

**Formula**: `Throughput = 1 / Latency`

**Example**: If latency = 10ms per request
```
Throughput = 1 / 0.01s = 100 requests/second
```

This is the theoretical maximum for a single-threaded system. Adding more requests won't increase throughput, they'll just queue up.

#### Multi-Threaded/Concurrent System

**Formula**: `Throughput = Concurrent Workers / Latency`

**Example**: Latency = 10ms, 50 concurrent workers
```
Throughput = 50 / 0.01s = 5,000 requests/second
```

**Important**: This assumes all workers can execute in parallel without contention. Real-world throughput will be lower due to:
- Shared resource contention (database connections, locks)
- CPU and memory limits
- I/O bottlenecks

### Little's Law

A fundamental relationship in queuing theory:

```
L = λ × W

Where:
L = Average number of items in system (queue + processing)
λ = Average arrival rate (throughput)
W = Average time in system (latency)
```

**Applications**:
- **Capacity planning**: If latency is 100ms and you need 1,000 RPS, you need at least 100 concurrent workers
- **Performance tuning**: If you have 50 workers and 10ms latency, max throughput is 5,000 RPS
- **Bottleneck identification**: High L with low λ means high latency (queue buildup)

**Example**:
```
Current state:
- 200 requests in system (L = 200)
- 100ms average latency (W = 0.1s)

Throughput:
λ = L / W = 200 / 0.1 = 2,000 requests/second
```

---

## What Limits Throughput?

**The bottleneck determines maximum throughput. A system is only as fast as its slowest component.**

### Common Bottlenecks

#### 1. CPU

**Symptoms**:
- High CPU utilization (>80%)
- Requests taking longer to process
- Increased latency under load

**Causes**:
- Inefficient algorithms
- Excessive serialization/deserialization
- Cryptographic operations
- Regular expressions

**Solutions**:
- Optimize hot code paths
- Use profiling to find CPU-intensive operations
- Vertical scaling (more powerful CPUs)
- Horizontal scaling (more instances)

#### 2. Memory

**Symptoms**:
- High memory utilization
- Frequent garbage collection
- Out of memory errors
- Swapping to disk

**Causes**:
- Memory leaks
- Large object allocations
- Excessive caching
- Poor garbage collection tuning

**Solutions**:
- Fix memory leaks
- Use object pooling
- Tune garbage collector
- Add more RAM
- Horizontal scaling

#### 3. Network

**Symptoms**:
- Network saturation
- Packet loss
- High retransmission rates
- Connection timeouts

**Causes**:
- Insufficient bandwidth
- Too many small requests (overhead)
- Large payload sizes
- Network congestion

**Solutions**:
- Increase bandwidth
- Use compression
- Batch requests
- Implement CDN
- Optimize payload sizes

#### 4. Database

**Symptoms**:
- Slow queries
- Connection pool exhaustion
- High query queue depth
- Lock contention

**Causes**:
- Missing indexes
- Inefficient queries
- Too few connections
- Serializable isolation causing locks

**Solutions**:
- Add indexes
- Optimize queries
- Increase connection pool
- Use read replicas
- Cache frequently accessed data

#### 5. Disk I/O

**Symptoms**:
- High I/O wait time
- Disk queue depth increasing
- Slow read/write operations

**Causes**:
- Slow storage (HDD vs SSD)
- Frequent random access
- Insufficient IOPS
- Large writes blocking reads

**Solutions**:
- Use SSDs or NVMe
- Increase IOPS (more disks, better storage)
- Use write-ahead logging
- Separate read and write workloads

---

## Improving Throughput

### 1. Horizontal Scaling

**Add more servers to distribute load.**

**Characteristics**:
- Linear scaling for stateless services
- More complex for stateful services
- Requires load balancing
- No single point of failure (if done right)

**Example**:
```
1 server: 1,000 RPS
2 servers: ~2,000 RPS
4 servers: ~4,000 RPS
```

**Challenges**:
- State synchronization
- Consistent hashing for distributed caches
- Database scaling (hardest part)

### 2. Vertical Scaling

**Add more resources (CPU, memory, network) to existing servers.**

**Characteristics**:
- Simpler than horizontal scaling
- Limited by hardware maximums
- Single point of failure
- Downtime required for upgrades

**When to use**:
- Quick fix for immediate capacity issues
- Database primary (hard to horizontally scale)
- Before rewriting for horizontal scaling

**Limits**:
- CPU: ~96 cores in commodity servers
- Memory: ~1-2 TB in commodity servers
- Network: 100 Gbps practical limit
- Eventually hits diminishing returns

### 3. Asynchronous Processing

**Don't block on slow operations.**

**Techniques**:

**Non-blocking I/O**: Handle multiple requests without threads per request
- Node.js event loop
- Java NIO, Python async/await
- Can handle 10,000+ concurrent connections

**Message queues**: Process requests asynchronously
- User request → Queue → Background worker
- Decouples request handling from processing
- Naturally load-leveling

**Event-driven architecture**: React to events rather than polling
- Webhooks instead of polling
- Database triggers
- Stream processing

**Example**:
```
Synchronous (1 request at a time):
Throughput = 1 / 100ms = 10 RPS

Asynchronous (100 concurrent):
Throughput = 100 / 100ms = 1,000 RPS
```

### 4. Batching

**Process multiple items together to amortize overhead.**

**Where to batch**:
- Database inserts (bulk insert)
- API calls (batch API)
- Network packets (Nagle's algorithm)
- Disk writes (write coalescing)

**Example - Database Inserts**:
```
Individual inserts:
100 rows × 5ms each = 500ms
Throughput: 200 rows/second

Batch insert:
100 rows in 1 query = 20ms
Throughput: 5,000 rows/second
```

**Tradeoffs**:
- Increases latency for individual items
- Complexity in error handling
- Need to tune batch size
- May delay time-sensitive operations

### 5. Caching

**Reduce work by reusing results.**

**Caching benefits for throughput**:
- Eliminates expensive operations
- Reduces database load
- Decreases CPU usage
- Lowers network traffic

**Impact on throughput**:
```
Without cache (DB query):
Throughput: 1,000 RPS (database limited)

With cache (90% hit rate):
10% to DB: 1,000 RPS
90% from cache: 10,000 RPS
Effective throughput: 9,100 RPS
```

### 6. Connection Pooling

**Reuse expensive connections instead of creating new ones.**

**Why it matters for throughput**:
- Creating connections is expensive (100-300ms)
- Limited number of connections available
- Connection creation itself consumes resources

**Example - Database Connections**:
```
Without pooling:
Each request opens connection (50ms) + query (10ms) = 60ms
Throughput: 16 RPS per worker

With pooling:
Each request reuses connection (1ms) + query (10ms) = 11ms
Throughput: 90 RPS per worker
```

**Configuration**:
- Min pool size: Keep minimum connections warm
- Max pool size: Limit based on database capacity
- Idle timeout: Close unused connections
- Max wait time: How long to wait for available connection

### 7. Load Balancing

**Distribute work evenly across resources.**

**Algorithms**:

**Round Robin**: Distribute requests sequentially
- Simple, fair
- Doesn't account for server capacity or current load

**Least Connections**: Send to server with fewest active connections
- Better for variable request duration
- Requires tracking connection state

**Response Time**: Send to fastest-responding server
- Adapts to server performance
- More complex

**Consistent Hashing**: Same key always goes to same server
- Good for caching
- Maintains affinity

**Impact**:
```
Without load balancing:
Server 1: 100% utilized (bottleneck)
Server 2: 20% utilized (wasted)
Server 3: 30% utilized (wasted)
Throughput: Limited by Server 1

With load balancing:
All servers: ~50% utilized
Throughput: 3x improvement
```

---

## Bandwidth

**Bandwidth is the maximum rate at which data can be transferred over a connection. It measures capacity.**

Bandwidth is typically expressed in **bits per second (bps)**: Kbps, Mbps, Gbps, Tbps.

### Types of Bandwidth

| Type | Description | Typical Values | Bottleneck Impact |
|------|-------------|----------------|-------------------|
| **Network bandwidth** | Capacity of network links | 100 Mbps - 100 Gbps | Limits data transfer rate |
| **Memory bandwidth** | Rate of data transfer to/from RAM | 25-100 GB/s (DDR4/DDR5) | Limits computation speed |
| **Disk bandwidth** | Read/write speed of storage | HDD: 100-200 MB/s<br>SSD: 500-3,500 MB/s<br>NVMe: 3,000-7,000 MB/s | Limits I/O operations |
| **Bus bandwidth** | Internal data transfer rate | PCIe 3.0: 32 GB/s<br>PCIe 4.0: 64 GB/s<br>PCIe 5.0: 128 GB/s | Limits device communication |

### Network Bandwidth Examples

**Consumer connections**:
- DSL: 1-25 Mbps
- Cable: 50-1,000 Mbps
- Fiber: 100-10,000 Mbps
- 4G LTE: 5-50 Mbps
- 5G: 100-1,000 Mbps

**Enterprise connections**:
- Ethernet: 1 Gbps
- 10 Gigabit Ethernet: 10 Gbps
- 100 Gigabit Ethernet: 100 Gbps

**Datacenter backbone**:
- 40-400 Gbps between racks
- 100 Gbps - 1 Tbps between datacenters

### Bandwidth vs Throughput

**Example scenario**:
- Available bandwidth: 1 Gbps = 125 MB/s
- Actual throughput: 100 MB/s

**Why the difference?**
- TCP/IP overhead: ~10-15%
- Packet loss and retransmissions: ~5%
- Application overhead: ~5%
- Network contention: ~5%

**Achieving high bandwidth utilization**:
- Use efficient protocols (HTTP/2, QUIC)
- Minimize overhead (larger packets)
- Parallel connections
- Reduce packet loss (better network quality)

---

## Bandwidth-Delay Product

An important concept that connects bandwidth and latency.

**Formula**: `Bandwidth-Delay Product (BDP) = Bandwidth × Round-Trip Time`

**BDP represents the amount of data that can be "in flight" at any given moment** — the data that has been sent but not yet acknowledged.

### Why BDP Matters

For optimal throughput, your **TCP window size must be at least as large as the BDP**. Otherwise, you'll be limited by the window size, not the available bandwidth.

**Example 1 - Cross-country Connection**:
```
Bandwidth: 1 Gbps = 125 MB/s
Latency: 60ms (coast-to-coast US, round-trip)
BDP: 125 MB/s × 0.06s = 7.5 MB

This means 7.5 MB of data can be traveling through the pipe at any instant.
```

**If TCP window size is only 1 MB**:
- Sender transmits 1 MB
- Sender must wait 60ms for acknowledgment
- Sender can transmit next 1 MB
- Effective throughput: 1 MB / 60ms = 16.7 MB/s (only 13% of available bandwidth!)

**With TCP window size of 7.5 MB**:
- Sender can continuously transmit
- Effective throughput: ~125 MB/s (full bandwidth utilization)

### Example 2 - Satellite Connection

```
Bandwidth: 50 Mbps = 6.25 MB/s
Latency: 600ms (geostationary satellite round-trip)
BDP: 6.25 MB/s × 0.6s = 3.75 MB

Despite "only" 50 Mbps bandwidth, you need a 3.75 MB window due to high latency.
```

### Example 3 - Local Network

```
Bandwidth: 10 Gbps = 1,250 MB/s
Latency: 1ms (local network)
BDP: 1,250 MB/s × 0.001s = 1.25 MB

High bandwidth but low latency means smaller window is sufficient.
```

### TCP Window Scaling

Default TCP window size is 64 KB, which is insufficient for high BDP networks.

**TCP Window Scaling** (RFC 1323) allows windows up to 1 GB:
- Enabled by default in modern operating systems
- Automatically negotiated during connection establishment
- Critical for long-distance, high-bandwidth connections

**Checking your TCP window**:
```bash
# Linux
sysctl net.ipv4.tcp_rmem
sysctl net.ipv4.tcp_wmem

# Typical modern values
net.ipv4.tcp_rmem = 4096 87380 6291456  (min default max)
net.ipv4.tcp_wmem = 4096 16384 4194304
```

---

## The Relationship Between Latency, Throughput, and Bandwidth

Understanding how these three metrics interact is key to system optimization.

### Key Relationships

**1. Latency limits throughput when bandwidth is sufficient**

If you have 1 Gbps bandwidth but 500ms latency:
- Single connection throughput is limited by latency, not bandwidth
- Solution: Parallel connections to fill bandwidth

**2. Bandwidth limits throughput when latency is low**

If you have 1ms latency but only 10 Mbps bandwidth:
- Throughput is limited by bandwidth, not latency
- Solution: Increase bandwidth or reduce data size

**3. Throughput is bounded by both**

```
Maximum Throughput ≤ min(Bandwidth, Data Size / Latency)
```

### Optimization Priority Matrix

| Scenario | Primary Bottleneck | Solution |
|----------|-------------------|----------|
| High latency, high bandwidth | Latency | Reduce round trips, parallel requests, caching |
| Low latency, low bandwidth | Bandwidth | Compression, reduce payload size, upgrade link |
| High latency, low bandwidth | Both | Multi-pronged approach needed |
| Low latency, high bandwidth | Neither | Optimize application logic |

### Real-World Examples

#### Example 1: Web Page Load

**Scenario**: Loading a page with 100 small resources

**Problem**: High latency (100ms), sufficient bandwidth (100 Mbps)

**Bottleneck**: Round trips, not bandwidth
- Each resource requires 1 RTT
- Serial loading: 100 × 100ms = 10 seconds
- Bandwidth barely utilized (small resources)

**Solution**:
- HTTP/2 multiplexing (load all resources in parallel)
- Resource bundling (combine into fewer files)
- Inline critical resources
- Result: Load time reduced to ~200ms

#### Example 2: Large File Transfer

**Scenario**: Transferring 1 GB file

**Problem**: Sufficient bandwidth (1 Gbps), moderate latency (50ms)

**Bottleneck**: Bandwidth (file is large)
- Latency impact: Negligible after connection established
- Transfer time: 1 GB / 125 MB/s = 8 seconds
- Connection setup: 50ms (0.6% of total time)

**Solution**:
- Bandwidth is the limit, latency doesn't matter much
- Could increase bandwidth
- Or compress file to reduce data size

#### Example 3: Database Query Response

**Scenario**: Many small queries to remote database

**Problem**: High latency (80ms), low bandwidth usage

**Bottleneck**: Round trips
- Each query: 80ms regardless of result size
- 100 queries: 8 seconds (serial)
- Bandwidth: Mostly idle (results are small)

**Solution**:
- Batch queries into single request
- Use caching for repeated queries
- Deploy read replicas closer to application
- Result: 100 queries in 100ms (batched)

#### Example 4: Video Streaming

**Scenario**: Streaming 4K video (25 Mbps)

**Problem**: Need consistent bandwidth, latency less critical

**Bottleneck**: Bandwidth consistency
- Minimum bandwidth: 25 Mbps
- Latency: Can buffer 5-10 seconds, so 100ms latency is fine
- Jitter: More problematic than latency

**Solution**:
- Ensure sufficient bandwidth (25+ Mbps)
- Implement adaptive bitrate (ABR) streaming
- Use buffering to handle jitter
- Result: Smooth playback even with latency variation

---

## Practical Guidelines

### When to Optimize Latency

**Indicators**:
- Users complain about "slowness"
- High percentile latencies (p95, p99)
- Interactive applications (search, chat, gaming)
- Many round trips per user action
- Low bandwidth utilization

**Focus on**:
- Reducing round trips
- Caching
- Geographic distribution
- Connection reuse
- Async processing

### When to Optimize Throughput

**Indicators**:
- System can't handle current load
- Requests queuing up
- CPU, memory, or I/O saturated
- Need to support more users
- Batch processing too slow

**Focus on**:
- Horizontal scaling
- Optimizing hot code paths
- Database optimization
- Async processing
- Load balancing

### When to Optimize Bandwidth

**Indicators**:
- Network links saturated
- High bandwidth utilization (>80%)
- Large data transfers
- Video/media delivery
- Peak usage patterns

**Focus on**:
- Compression
- CDN usage
- Upgrading network links
- Reducing payload sizes
- Caching at edge

### Monitoring Best Practices

**Essential metrics**:
```
Latency:
- p50, p95, p99 response times
- Request duration breakdown
- Time to first byte (TTFB)

Throughput:
- Requests per second
- Transactions per second
- Bytes per second

Bandwidth:
- Network utilization %
- Bytes sent/received
- Packet loss rate
```

**Set alerts**:
- p99 latency > SLO threshold
- Throughput drops > 20%
- Bandwidth utilization > 80%
- Error rate increases

---

## Conclusion

**Latency, throughput, and bandwidth are interconnected but distinct concepts:**

- **Latency**: How long a single operation takes (optimize for user experience)
- **Throughput**: How many operations per second (optimize for scale)
- **Bandwidth**: Maximum transfer capacity (optimize for data volume)

**Key Takeaways**:

1. **Measure what matters**: Use percentiles for latency, not averages
2. **Identify bottlenecks**: Optimize the limiting factor first
3. **Understand tradeoffs**: Optimizing one may require sacrificing another
4. **Think holistically**: Consider all three metrics together
5. **Monitor continuously**: Performance characteristics change with load and scale

**Remember**: 
- You can't improve what you don't measure
- Optimization without measurement is guessing
- The best optimization is often eliminating unnecessary work
- Sometimes the cheapest solution is upgrading hardware/bandwidth

The goal is not to achieve perfect latency, throughput, or bandwidth, but to meet your specific requirements cost-effectively while maintaining reliability and good user experience.