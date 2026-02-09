# System Availability: A Comprehensive Guide

## What is Availability?

Availability measures how often your system is operational and accessible to users. A highly available system continues functioning even when individual components fail.

**Key distinction**: Availability is not the same as reliability. A system can be highly available (always up) but unreliable (sometimes gives wrong answers). Availability measures uptime; reliability measures correctness.

Availability is typically expressed as a percentage of uptime over a given period.

## Understanding the Nines

The industry often refers to availability in terms of "nines" — the number of 9s in the percentage. Here's what different levels actually mean in terms of downtime:

| Availability | Common Name | Downtime/Year | Downtime/Month | Downtime/Week |
|--------------|-------------|---------------|----------------|---------------|
| 99% | Two nines | 3.65 days | 7.3 hours | 1.68 hours |
| 99.9% | Three nines | 8.76 hours | 43.8 minutes | 10.1 minutes |
| 99.99% | Four nines | 52.6 minutes | 4.38 minutes | 1.01 minutes |
| 99.999% | Five nines | 5.26 minutes | 26.3 seconds | 6.05 seconds |
| 99.9999% | Six nines | 31.5 seconds | 2.63 seconds | 0.6 seconds |

Each additional nine increases cost exponentially. Most consumer services target three or four nines. Five nines is typically reserved for critical infrastructure like financial systems or emergency services.

## Calculating System Availability

### Components in Series

When components are arranged in series (all must work for the system to function), their availabilities multiply. This means the overall system availability is always *lower* than the least available component.

**Example**: A web server (99.9% available) connects to a database (99.9% available). The system availability is 0.999 × 0.999 = 0.998 or 99.8%.

With each additional component in the chain, availability decreases. This is why minimizing dependencies is crucial for high availability.

### Components in Parallel

When components are in parallel (any one can handle the request), availability improves dramatically. For both to be down, both must fail simultaneously.

The formula for parallel availability is: 1 - (unavailability₁ × unavailability₂)

**Example**: Two servers, each 99% available (1% unavailable). System availability = 1 - (0.01 × 0.01) = 99.99%.

This is the mathematical foundation of redundancy. Adding a second component of equal reliability moves you from two nines to four nines.

## Common Failure Modes

### Hardware Failures

Everything physical eventually breaks. The question is when, not if. Understanding failure patterns helps you plan for them.

**Mean Time Between Failures (MTBF)**: The average time a component operates before failing. Hard drives might have an MTBF of 3-5 years, but that's an average. In a datacenter with 10,000 drives, you'll see failures every day.

### Software Failures

Software doesn't wear out, but it can fail due to bugs, memory leaks, resource exhaustion, or unexpected inputs. Unlike hardware, software failures can be systematic — the same bug might crash all instances simultaneously, defeating redundancy.

### Network Failures

Networks fail in complex ways: partitions, packet loss, high latency, asymmetric failures. A network partition can split your system into isolated islands that each think they're the only survivor.

### Human Error

Studies suggest 40-70% of outages are caused by human error during deployments, configuration changes, or maintenance. This is why automation and change management processes are critical.

## Redundancy: The Foundation of Availability

Redundancy means having backup components that can take over when primary components fail. However, redundancy comes in different flavors, each with different tradeoffs.

### Active-Passive (Standby)

In active-passive configuration, one component handles all the work while another waits as a backup. When the active component fails, the passive one takes over.

Active-passive is commonly used for databases, stateful services, and systems requiring a single leader to maintain consistency.

#### Cold Standby

The backup server is not running. Failover requires booting the machine, starting services, and potentially restoring data from backups.

- **Failover time**: 5-15 minutes
- **Cost**: Lowest (no running backup)
- **Use case**: Disaster recovery where some downtime is acceptable

#### Warm Standby

The backup is running and configured, possibly receiving replicated data, but not actively processing requests.

- **Failover time**: Seconds to a few minutes
- **Cost**: Medium (running server, partial data sync)
- **Use case**: Production systems with moderate availability requirements

#### Hot Standby

The backup is fully synchronized and ready to serve immediately. For databases, this typically means synchronous replication where every write is confirmed on both primary and standby before acknowledging the client.

- **Failover time**: Sub-second to seconds
- **Cost**: Highest (fully running, synchronous replication)
- **Use case**: Critical systems requiring minimal downtime

### Active-Active

In active-active configuration, all components handle traffic simultaneously. There's no distinction between primary and backup because every node is doing real work.

When one node fails, the load balancer simply stops sending traffic to it. The remaining nodes absorb the additional load — there's no failover process.

**Requirements for active-active**:
- Requests can be handled by any node (stateless), OR
- Shared storage (database, Redis, distributed cache), OR
- Sticky sessions (reduces availability benefits)

**Benefits**:
- No failover delay
- Better resource utilization (no idle backups)
- Scales horizontally by adding nodes

**Challenges**:
- State management complexity
- Load balancer becomes critical dependency
- Requires careful capacity planning (N+1 or N+2 redundancy)

### Geographic Redundancy

Geographic redundancy distributes your system across multiple physical locations: different datacenters, availability zones, or regions.

This protects against large-scale failures: power outages, natural disasters, datacenter network issues, or regional ISP problems.

**Availability zones** are separate datacenters within a region, typically with independent power and networking but low-latency connections (1-2ms).

**Regions** are geographically separated (different cities or countries), with higher latency (20-100ms) but protection from large-scale disasters.

The tradeoff is latency vs disaster resilience. Writing to multiple regions adds significant latency but provides the highest level of protection.

## Redundancy Across Layers

A chain is only as strong as its weakest link. If you have redundant app servers but a single database, the database is your single point of failure (SPOF).

True high availability requires redundancy at every layer:

- **Load balancers**: Multiple LBs with health checks and failover
- **Web servers**: Multiple instances behind the load balancer
- **Application servers**: Horizontal scaling with shared state
- **Databases**: Replication with automatic failover
- **Caches**: Multiple cache nodes, or accept cache miss on failure
- **Message queues**: Clustered or replicated queues
- **Network**: Multiple network paths, redundant switches
- **Power**: Multiple power supplies, backup generators, UPS

> **The Cost of Redundancy**: Redundancy is not free. Every backup server, every replica, every additional availability zone costs money. The question is whether that cost is justified by the reduction in downtime risk. For a personal blog, 99% availability might be fine. For payment processing, five nines might be necessary.

## High Availability Patterns

### Pattern 1: Load Balancer with Multiple Backends

The most fundamental pattern for stateless services. A load balancer distributes traffic across multiple servers, automatically routing around failures.

**How it provides high availability**:
- Load balancer continuously health-checks backends (every few seconds)
- Failed servers automatically removed from rotation
- Traffic redistributes to healthy servers within seconds
- New servers can be added without downtime

**Health checks**: The load balancer sends periodic requests (HTTP, TCP, or custom) to each backend. Consecutive failures mark the server as unhealthy. Consecutive successes mark it as recovered.

**Load balancing algorithms**:
- Round robin: Simple rotation through servers
- Least connections: Send to server with fewest active connections
- Response time: Send to fastest-responding server
- Consistent hashing: Same client always hits same server (for session affinity)

#### Load Balancer Redundancy

The load balancer itself can be a single point of failure. For true high availability, you need redundant load balancers.

**Common approaches**:
- **DNS round-robin**: Multiple A records pointing to different load balancers (slow failover, 30-60s)
- **Floating IP**: A virtual IP that moves between load balancers during failover (fast, seconds)
- **Anycast**: Multiple load balancers advertising the same IP, network routes to nearest (complex but powerful)
- **Cloud load balancers**: Managed services with built-in redundancy (AWS ALB, GCP Load Balancing)

### Pattern 2: Database Replication with Automatic Failover

Databases are stateful and cannot simply be load-balanced like web servers. Database high availability requires replication and careful failover management.

**Replication types**:

**Synchronous replication** guarantees zero data loss but adds latency. Every write must wait for the replica to confirm. If your replica is in a different region, this adds 50-100ms per write.

**Asynchronous replication** has no performance impact but can lose data. If the primary fails, any writes not yet replicated are lost. Replication lag is typically seconds but can grow during high load.

**Best practice**: Use synchronous replication for the failover target (to prevent data loss) and asynchronous replication for read replicas and analytics (to avoid performance impact).

**Automatic failover process**:
1. Health check detects primary database failure
2. Failover controller elects a replica to promote
3. Replica is promoted to primary (may require write-ahead log replay)
4. Application connections redirect to new primary
5. Old primary becomes replica when it recovers

**Challenges**:
- **Split-brain**: Network partition makes both nodes think they're primary
- **Data consistency**: Ensuring failover doesn't lose or duplicate data
- **Connection handling**: Applications must reconnect or use connection pooling
- **Automated vs manual**: Automatic failover is faster but risks split-brain; manual is safer but slower

### Pattern 3: Queue-Based Load Leveling

When downstream services cannot handle peak load, use a queue to buffer requests and process them at a sustainable rate.

**How it provides high availability**:
- Decouples producers from consumers
- Buffers traffic spikes that would overwhelm downstream systems
- Workers can fail and restart without losing messages
- Can scale workers independently based on queue depth
- Provides graceful degradation under load

**Example scenario**: A flash sale generates 100x normal traffic for a few minutes. Without a queue, the database would be overwhelmed and potentially crash. With a queue, orders accumulate and are processed at a sustainable rate. Customers might wait a bit longer, but the system stays up.

**Implementation considerations**:
- **Message durability**: Persist messages to disk so they survive broker restarts
- **Queue redundancy**: Replicate queues across multiple brokers
- **Ordering guarantees**: Decide if strict ordering is necessary (reduces throughput)
- **Retry logic**: Handle worker failures with exponential backoff
- **Dead letter queues**: Move repeatedly failing messages aside for investigation

### Pattern 4: Circuit Breaker

When a dependency fails, continuing to call it wastes resources and can cause cascading failures. The circuit breaker pattern prevents this by failing fast.

**States**:
- **Closed**: Normal operation, requests pass through
- **Open**: Dependency is failing, requests fail immediately without calling dependency
- **Half-open**: Testing if dependency has recovered

**State transitions**:
1. After N consecutive failures, circuit opens
2. After timeout period, circuit enters half-open state
3. In half-open, allow one test request
4. If test succeeds, close circuit; if it fails, open again

**Benefits**:
- Prevents resource exhaustion from waiting on dead dependencies
- Stops cascading failures before they spread
- Gives failing service time to recover without traffic
- Provides fast feedback to callers (fail immediately vs timeout)

**Implementation tips**:
- Set thresholds based on actual failure rates in production
- Monitor circuit breaker state as a health metric
- Provide fallback behavior (cached data, degraded functionality)
- Consider per-user vs global circuit breakers

### Pattern 5: Bulkhead Isolation

Inspired by ship compartments that prevent one leak from sinking the entire vessel, bulkheads isolate failures to prevent them from affecting the entire system.

**How it works**: Separate thread pools, connection pools, or resource quotas for different parts of the system. If one component exhausts its resources, others continue functioning.

**Example**: An e-commerce site has separate thread pools for product search, checkout, and user accounts. If search experiences a traffic spike that exhausts its threads, checkout and accounts continue working normally.

**Types of bulkheads**:
- Thread pool isolation (separate pools for different operations)
- Connection pool isolation (separate database connections)
- Process isolation (separate services or containers)
- Resource quotas (CPU, memory limits per component)

### Pattern 6: Health Checks and Monitoring

You can't fix what you don't know is broken. Comprehensive health checks and monitoring are essential for availability.

**Health check types**:
- **Shallow**: Does the process respond? (HTTP 200 from /health)
- **Deep**: Can the process do its job? (Can connect to database, cache, dependencies)
- **Synthetic transactions**: Can the system complete real user workflows?

**Monitoring layers**:
- Infrastructure (CPU, memory, disk, network)
- Application (request rate, error rate, latency)
- Business (orders/minute, revenue, user signups)

**Alerting best practices**:
- Alert on symptoms (customers affected) not causes (disk usage)
- Include enough context to triage without additional investigation
- Reduce alert fatigue by aggregating related alerts
- Set up escalation for unacknowledged critical alerts

## Designing for High Availability

### Eliminate Single Points of Failure

Walk through your architecture and identify every component that, if it fails, would bring down the system. Systematically add redundancy to each one.

### Plan for Failure

Assume everything will fail and design accordingly. Practice failure scenarios with chaos engineering: randomly kill processes, partition networks, exhaust resources. See what breaks and fix it before customers do.

### Automate Recovery

Humans are slow and make mistakes under pressure. Automate detection and recovery. Manual intervention should be the exception, not the rule.

### Measure and Improve

Track your actual availability. Calculate your error budget (100% - SLA%). When you exceed your budget, make availability the top priority. When you're under budget, you can take more risks.

### Accept Tradeoffs

Perfect availability is impossible and infinitely expensive. Define your requirements based on business impact, then build the simplest system that meets those requirements. Over-engineering wastes resources; under-engineering loses customers.

---

*High availability is not a feature you add at the end. It's an architectural property that must be designed in from the beginning. Start with your availability requirements, understand your failure modes, then systematically eliminate single points of failure and build in redundancy at every layer.*