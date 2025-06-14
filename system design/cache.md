
# What is cache
A cache's primary purpose is to increase data retrieval performance by reducing the need to access the underlying slower storage layer. Trading off capacity for speed, a cache typically stores a subset of data transiently, in contrast to databases whose data is usually complete and durable.

Caches take advantage of the locality of reference principle "recently requested data is likely to be requested again".

# Caching and Memory
Similar to a computer's memory, a cache is a compact, fast-performing memory that stores data in a hierarchy of levels, starting at level one, and progressing from there sequentially. They are labeled as L1, L2, L3, and so on. A cache also gets written if requested, such as when there has been an update and new content needs to be saved to the cache, replacing the older content that was saved.

No matter whether the cache is read or written, it's done one block at a time. Each block also has a tag that includes the location where the data was stored in the cache. When data is requested from the cache, a search occurs through the tags to find the specific content that's needed in level one (L1) of the memory. If the correct data isn't found, more searches are conducted in L2.

If the data isn't found there, searches are continued in L3, then L4, and so on until it has been found, then, it's read and loaded. If the data isn't found in the cache at all, then it's written into it for quick retrieval the next time.

# Cache hit and Cache miss
## Cache hit
A cache hit describes the situation where content is successfully served from the cache. The tags are searched in the memory rapidly, and when the data is found and read, it's considered a cache hit.

## Cold, Warm, and Hot Caches

A cache hit can also be described as cold, warm, or hot. In each of these, the speed at which the data is read is described.

A hot cache is an instance where data was read from the memory at the fastest possible rate. This happens when the data is retrieved from L1.

A cold cache is the slowest possible rate for data to be read, though, it's still successful so it's still considered a cache hit. The data is just found lower in the memory hierarchy such as in L3, or lower.

A warm cache is used to describe data that's found in L2 or L3. It's not as fast as a hot cache, but it's still faster than a cold cache. Generally, calling a cache warm is used to express that it's slower and closer to a cold cache than a hot one.

# Cache miss
A cache miss refers to the instance when the memory is searched and the data isn't found. When this happens, the content is transferred and written into the cache.

# Cache Invalidation
Cache invalidation is a process where the computer system declares the cache entries as invalid and removes or replaces them. If the data is modified, it should be invalidated in the cache, if not, this can cause inconsistent application behavior. There are three kinds of caching systems:


# write-through-cache

Data is written into the cache and the corresponding database simultaneously.

Pro: Fast retrieval, complete data consistency between cache and storage.

Con: Higher latency for write operations.


# write-around-cache

Where write directly goes to the database or permanent storage, bypassing the cache.

Pro: This may reduce latency.

Con: It increases cache misses because the cache system has to read the information from the database in case of a cache miss. As a result, this can lead to higher read latency in the case of applications that write and re-read the information quickly. Read happen from slower back-end storage and experiences higher latency.


# write-back-cache

Where the write is only done to the caching layer and the write is confirmed as soon as the write to the cache completes. The cache then asynchronously syncs this write to the database.

Pro: This would lead to reduced latency and high throughput for write-intensive applications.

Con: There is a risk of data loss in case the caching layer crashes. We can improve this by having more than one replica acknowledging the write in the cache.

# Eviction policies
Following are some of the most common cache eviction policies:

First In First Out (FIFO): The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.

Last In First Out (LIFO): The cache evicts the block accessed most recently first without any regard to how often or how many times it was accessed before.

Least Recently Used (LRU): Discards the least recently used items first.

Most Recently Used (MRU): Discards, in contrast to LRU, the most recently used items first.

Least Frequently Used (LFU): Counts how often an item is needed. Those that are used least often are discarded first.

Random Replacement (RR): Randomly selects a candidate item and discards it to make space when necessary.

# Distributed-cache

A distributed cache is a system that pools together the random-access memory (RAM) of multiple networked computers into a single in-memory data store used as a data cache to provide fast access to data. While most caches are traditionally in one physical server or hardware component, a distributed cache can grow beyond the memory limits of a single computer by linking together multiple computers.


# Global-cache

As the name suggests, we will have a single shared cache that all the application nodes will use. When the requested data is not found in the global cache, it's the responsibility of the cache to find out the missing piece of data from the underlying data store.

Use cases
Caching can have many real-world use cases such as:

Database Caching
Content Delivery Network (CDN)
Domain Name System (DNS) Caching
API Caching
# When not to use caching?

Let's also look at some scenarios where we should not use cache:

Caching isn't helpful when it takes just as long to access the cache as it does to access the primary data store.

Caching doesn't work as well when requests have low repetition (higher randomness), because caching performance comes from repeated memory access patterns.

Caching isn't helpful when the data changes frequently, as the cached version gets out of sync, and the primary data store must be accessed every time.

It's important to note that a cache should not be used as permanent data storage. They are almost always implemented in volatile memory because it is faster, and thus should be considered transient.

Advantages
Below are some advantages of caching:

Improves performance

Reduce latency

Reduce load on the database

Reduce network cost

Increase Read Throughput

# Content Delivery Networks
# 🌐 Content Delivery Network (CDN)

A **Content Delivery Network (CDN)** is a geographically distributed network of servers that **caches and delivers content** to users from the closest location, improving speed, availability, and security.

---

## 🧠 How a CDN Works

1. User requests a web asset (e.g., image, script, HTML).
2. The CDN routes the request to the **nearest edge server**.
3. If the content is **cached**, it is returned immediately (cache hit).
4. If not, the CDN fetches it from the **origin server** (cache miss), stores it, and serves it.

---

## ✅ Benefits of Using a CDN

| Benefit              | Description |
|----------------------|-------------|
| 🔄 Speed             | Reduces latency by serving from edge servers close to the user. |
| 🔒 Security          | Offers DDoS protection, TLS/SSL offloading, bot filtering. |
| 📈 Scalability       | Handles large traffic spikes by offloading origin server. |
| 🧩 Reliability       | Fallbacks and multiple nodes ensure uptime. |
| 💸 Cost Efficiency   | Reduces origin server bandwidth and compute costs. |

---

## 📁 What Can a CDN Cache?

- Static files (images, JS, CSS, videos, PDFs)
- HTML pages
- Fonts and icons
- API responses (for GET endpoints)
- Software downloads

---

# 🔄 Pull CDN vs Push CDN

## 📥 Pull CDN (Origin Pull)

### 🔹 How It Works
- CDN fetches content **on demand** from the origin when first requested.
- It then caches that content for subsequent requests.

### 🔁 Request Flow

### ✅ Pros
- Easy to set up
- Automatically keeps up with updates from origin
- Good for frequently updated content

### ❌ Cons
- First request may be slow (cache miss)
- Relies on origin being available

### ✅ Best For
- CMS sites
- Dynamic websites
- API caching

---

## 📤 Push CDN (Content Push)

### 🔹 How It Works
- You **manually upload** static files to the CDN.
- CDN **distributes** content to edge nodes in advance.

### 🔁 Request Flow

### ✅ Pros
- Always fast response
- No dependency on origin server
- Ideal for large static assets

### ❌ Cons
- Requires manual management
- Not suitable for frequently changing data

### ✅ Best For
- Static sites
- Video streaming
- Software distribution

---

## 📊 Comparison: Pull vs Push CDN

| Feature              | Pull CDN                      | Push CDN                        |
|----------------------|-------------------------------|----------------------------------|
| Setup                | Auto-fetch from origin        | Manual upload to CDN            |
| Ideal Use Case       | Dynamic or mixed content      | Static, large files             |
| First Request        | May be slow (cache miss)      | Always fast                     |
| Cache Management     | Automatic TTLs                | Manual                          |
| Origin Dependency    | Required                      | Not required                    |

---

## 🏢 Popular CDN Providers

| Provider        | Type(s) Supported     | Notes |
|-----------------|------------------------|-------|
| **Cloudflare**  | Pull (default)         | Free tier, security, edge compute |
| **AWS CloudFront** | Push + Pull         | Integrated with S3, Lambda@Edge |
| **Akamai**      | Push + Pull            | Enterprise-grade, very flexible |
| **Fastly**      | Pull (mainly)          | Great for dynamic APIs and edge compute |
| **Google Cloud CDN** | Pull            | Integrated with Google Cloud Load Balancer |
| **Azure CDN**   | Push + Pull            | Supports blob storage integration |

---

## 📌 CDN Terms You Should Know

| Term           | Meaning |
|----------------|---------|
| **Edge Server** | A CDN node close to the user |
| **Origin Server** | Your main application/server |
| **TTL (Time to Live)** | How long content is cached |
| **Cache Hit** | Content is served from CDN cache |
| **Cache Miss** | Content fetched from origin |
| **Purge** | Manually delete cached content |
| **Invalidation** | Refresh or replace outdated cache |

---

## 🔚 Conclusion

Using a CDN is critical for optimizing web performance and user experience. Choosing between **pull** and **push** CDN depends on your content type, how often it changes, and how much control you want over content distribution.

