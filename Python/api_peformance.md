# Slow API Optimization — Reference Guide

A comprehensive checklist for diagnosing and fixing slow APIs across the full stack.

---

## 1. Database Query Optimization

### Indexing
- Add indexes on columns used in `WHERE`, `JOIN`, `IN`, range conditions, `GROUP BY`, and `ORDER BY`.
- Prefer **composite indexes** when multiple columns are frequently queried together.
- Use **partial indexes** to index only a subset of rows (e.g., `WHERE status = 'active'`).
- Avoid over-indexing — every index slows down `INSERT`/`UPDATE`/`DELETE` operations.

### Query Analysis
- Run `EXPLAIN ANALYZE` to identify slow steps (sequential scans, hash joins, sort operations).
- Look for high `cost`, `rows`, and `actual time` values in the output.
- Use tools like **pgBadger** (PostgreSQL) or **slow query log** (MySQL) to surface problematic queries automatically.

### Query Writing Best Practices
- Avoid `SELECT *` — fetch only the columns you need.
- Use `WHERE` to filter rows **before** grouping; use `HAVING` only to filter **after** aggregation (it's more expensive).
- Use `EXISTS` instead of `IN` for subqueries when you only need to check presence — `EXISTS` short-circuits on the first match.
- Join smaller tables first to reduce intermediate result set sizes.
- Prefer `UNION ALL` over `UNION` — `UNION` performs duplicate elimination, which is extra work.
- Avoid `SELECT DISTINCT` — enforce uniqueness at the schema/index level instead.
- Replace `OR` conditions with `UNION` or `IN` where possible, as `OR` can prevent index usage.
- Minimize wildcard patterns: use `LIKE 'abc%'` instead of `LIKE '%abc%'` — leading wildcards prevent index use.
- Avoid functions on indexed columns in `WHERE` clauses (e.g., `WHERE YEAR(created_at) = 2024` prevents index use; rewrite as a range condition).
- Use **batch operations** (`INSERT INTO ... VALUES (),(),()`...) instead of row-by-row inserts.

### The N+1 Problem
The N+1 problem occurs when an application makes N additional database calls to fetch related data for each of the 1 initial results. Fix by using:
- **Eager loading** (e.g., `JOIN` or ORM `include`/`prefetch_related`)
- **Batch fetching** — collect all IDs first, then query in one `WHERE id IN (...)` call.

### Connection Management
- Use **connection pooling** (e.g., PgBouncer, HikariCP, SQLAlchemy pool) to reuse existing connections instead of creating a new one per request. Connection setup is expensive.
- Tune pool size based on your database's `max_connections` and workload.

### Read vs. Write Separation
- Use **read replicas** for read-heavy operations (reports, search, analytics).
- Route writes to the primary and reads to replicas using a load balancer or ORM config.

### Schema-Level Improvements
- Use appropriate data types — smaller types (`INT` vs. `BIGINT`, `VARCHAR(50)` vs. `TEXT`) reduce storage and speed comparisons.
- Normalize to reduce redundancy, but consider **denormalization** for hot read paths where joins are a bottleneck.
- Partition large tables by date or range to limit the rows scanned per query.

---

## 2. Network & Payload Reduction

- **Compression:** Enable GZIP or Brotli compression on your web server to reduce response sizes (often 60–80% for JSON/HTML).
- **Pagination:** Never return unbounded result sets. Use `limit` + `offset`, or cursor-based pagination for large datasets (cursor pagination is more efficient at scale).
- **Data Serialization:** Prefer lightweight JSON over XML. For high-throughput internal services, consider **Protocol Buffers** or **MessagePack** for binary serialization.
- **Sparse Fieldsets:** Let clients request only the fields they need (e.g., GraphQL or a `fields=id,name` query param in REST).
- **Avoid chatty APIs:** Batch multiple small requests into one endpoint where possible to reduce round trips.
- **CDN for static assets:** Offload images, JS, CSS, and static files to a CDN to reduce origin server load and latency.

---

## 3. Caching

### Response Caching
- Cache full API responses for frequently accessed, rarely changing data using **Redis** or **Memcached**.
- Use **HTTP cache headers** (`Cache-Control`, `ETag`, `Last-Modified`) to let clients and proxies cache responses.

### Fragment / Object Caching
- Cache expensive computation results or partial data at the object level (e.g., a user's profile, a product's inventory count).
- Invalidate or TTL-expire cached data on writes.

### Database Query Caching
- Use your ORM's query cache or cache the result of repeated identical queries.
- For read replicas under heavy load, a query cache layer (e.g., ProxySQL) can help.

### Cache Strategies
| Strategy | Use Case |
|---|---|
| **Cache-aside** | App checks cache first; on miss, fetches from DB and populates cache |
| **Write-through** | Writes go to cache and DB simultaneously |
| **Write-behind** | Writes go to cache first; DB is updated asynchronously |
| **TTL-based expiry** | Simple invalidation for time-sensitive data |

### Common Pitfalls
- **Cache stampede:** Many requests hit the DB simultaneously on a cache miss — use locking or probabilistic early expiry.
- **Stale data:** Always define a TTL; never cache indefinitely without an invalidation strategy.

---

## 4. Asynchronous Processing

- **Background Jobs:** Move long-running or non-blocking tasks (email sending, PDF generation, report building) out of the request cycle using job queues like **Celery**, **RabbitMQ**, **Amazon SQS**, or **BullMQ** (Node.js).
- **Non-Blocking I/O:** Use async frameworks like **FastAPI**, **Node.js**, or **Go** to handle many concurrent connections without spawning a thread per request.
- **Webhooks:** Instead of keeping HTTP connections open for slow operations, respond immediately with a `202 Accepted` and push results back via a webhook when done.
- **Streaming Responses:** For large payloads, stream the response progressively rather than buffering the entire output before sending.
- **Event-Driven Architecture:** Decouple services using message brokers (Kafka, RabbitMQ) so each service processes at its own pace.

---

## 5. Infrastructure Tuning

- **Load Balancing:** Distribute traffic evenly across multiple instances using Nginx, HAProxy, or a cloud load balancer. Use health checks to avoid routing to unhealthy nodes.
- **Horizontal Scaling:** Add more server instances behind the load balancer instead of just scaling up a single machine.
- **HTTP/2 or HTTP/3:** Upgrade protocols to allow multiplexing (multiple requests over one connection), header compression, and server push.
- **Keep-Alive:** Keep TCP connections open between client and server to avoid repeated TLS handshake and connection setup overhead.
- **Auto-scaling:** Use cloud auto-scaling rules to spin up instances under high load and scale down during off-peak hours.
- **Timeout & Retry Policies:** Set appropriate timeouts at every layer (DB, external APIs, load balancer) and implement exponential backoff with jitter for retries to prevent thundering herd.
- **Resource Limits:** Set CPU and memory limits per service to prevent one slow endpoint from starving others (important in containerized environments).

---

## 6. Code Optimization

### Profiling First
Always profile before optimizing. Identify the actual bottleneck — don't guess.
- **Python:** `cProfile`, `py-spy`, `timeit`, `memory_profiler`
- **Node.js:** `--prof` flag, clinic.js, Chrome DevTools
- **Java/JVM:** JProfiler, YourKit, async-profiler

### General Principles
- Avoid unnecessary work inside hot loops — move invariant calculations outside the loop.
- Use **built-in data structures** (dicts, sets) for O(1) lookups instead of scanning lists.
- Prefer **list comprehensions** and generator expressions over manual loops in Python.
- Avoid repeated attribute lookups in loops — cache the reference locally.

### Memory & Data Efficiency
- Use **generators** instead of lists for large datasets that are processed sequentially — they produce items lazily without loading everything into memory.
- Use **NumPy** or **Pandas** for numerical operations on large datasets — they use optimized C implementations.
- Release references to large objects when done to allow garbage collection.

### Language-Level Optimizations
- For computation-heavy Python code, consider **Cython**, **PyPy**, or calling into C extensions.
- Use **connection and client reuse** — don't instantiate heavy clients (HTTP clients, DB connections) per request; share them across the application lifecycle.
- Avoid **blocking calls** on async threads — always use async-compatible libraries in async frameworks.

### Algorithm Complexity
- Review time complexity of critical paths. An O(n²) algorithm at scale is often worse than a slow DB call.
- Use appropriate data structures: `set` for membership tests, `deque` for queues, `heapq` for priority queues.

---

## 7. API Design Improvements

- **Rate Limiting:** Protect your API from abuse and reduce unnecessary load with rate limiting (e.g., token bucket or leaky bucket algorithm).
- **Request Validation Early:** Reject invalid requests at the gateway/middleware level before they hit business logic or the database.
- **Idempotency:** Design write endpoints to be idempotent so safe retries don't cause duplicate processing.
- **GraphQL / BFF (Backend for Frontend):** Tailor data-fetching to client needs to avoid over-fetching and under-fetching in REST.
- **Versioning:** Keep API versions stable so clients aren't forced to re-fetch data due to unexpected contract changes.

---

## 8. Observability & Monitoring

Without visibility, you can't optimize effectively.

- **Distributed Tracing:** Use tools like **Jaeger**, **Zipkin**, or **Datadog APM** to trace a request across all services and pinpoint the slowest span.
- **Metrics:** Track p50, p95, p99 latency — averages hide tail latency problems. Tools: Prometheus + Grafana, Datadog, New Relic.
- **Logging:** Structured JSON logs with request IDs allow correlation across services. Log slow queries, cache misses, and error rates.
- **Alerting:** Set SLO-based alerts (e.g., error rate > 1%, p99 latency > 500ms) rather than reacting after users complain.
- **Synthetic Monitoring:** Run periodic health checks against critical API endpoints to detect regressions before users do.

---

## Quick Reference Checklist

| Layer | Key Actions |
|---|---|
| **Database** | Index hot columns, run EXPLAIN ANALYZE, fix N+1, use connection pool, read replicas |
| **Cache** | Cache hot reads, set TTLs, pick the right strategy |
| **Network** | Enable compression, paginate, reduce payload size |
| **Async** | Offload slow tasks to queues, use non-blocking I/O |
| **Infrastructure** | Load balance, use HTTP/2, enable keep-alive, auto-scale |
| **Code** | Profile first, optimize loops, use generators, right data structures |
| **API Design** | Rate limit, validate early, avoid chatty patterns |
| **Observability** | Trace requests, track p99 latency, alert on SLOs |