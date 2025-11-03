##  Non-relational databases might be the right choice if:
- Your application requires super-low latency.
-  Your data are unstructured, or you do not have any relational data.
- You only need to serialize and deserialize data (JSON, XML, YAML, etc.).
- You need to store a massive amount of data.
  
## Vertical scaling vs horizontal scaling
Vertical scaling, referred to as “scale up”, means the process of adding more power (CPU,
RAM, etc.) to your servers. Horizontal scaling, referred to as “scale-out”, allows you to scale
by adding more servers into your pool of resources.

When traffic is low, vertical scaling is a great option, and the simplicity of vertical scaling is
its main advantage. Unfortunately, it comes with serious limitations.
- Vertical scaling has a hard limit. It is impossible to add unlimited CPU and memory to a
single server.
-  Vertical scaling does not have failover and redundancy. If one server goes down, the website/app goes down with it completely.
  
Horizontal scaling is more desirable for large scale applications due to the limitations of
vertical scaling.

- A private IP is an IP address reachable only
between servers in the same network; however, it is unreachable over the internet. 

## Database replication
Database replication can be used in many database management
systems, usually with a master/slave relationship between the original (master) and the copies (slaves)

A master database generally only supports write operations. A slave database gets copies ofthe data from the master database and only supports read operations. All the data-modifying ommands like insert, delete, or update must be sent to the master database. Most
applications require a much higher ratio of reads to writes; thus, the number of slave databases in a system is usually larger than the number of master databases

## Advantages
- Better performance
- Reliability
- High availability

## Considerations for using cache
- • Decide when to use cache. Consider using cache when data is read frequently but modified infrequently. 
- • Expiration policy. It is a good practice to implement an expiration policy. Once cached data is expired, it is removed from the cache.
- Consistency: This involves keeping the data store and the cache in sync. Inconsistency can happen because data-modifying operations on the data store and cache are not in a single transaction. 
  
A single point of failure (SPOF) is a part of a
system that, if it fails, will stop the entire system from working

## Content delivery network (CDN)
A CDN is a network of geographically dispersed servers used to deliver static content. CDN servers cache static content like images, videos, CSS, JavaScript files, etc.