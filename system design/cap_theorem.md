# What is a Distibuted System ?
A distributed system is a group of computers working together, communicating over a network, to perform a task as if they were a single system.
# Key Characteristics of Distributed System
```
Feature	                                                            Description
Multiple Nodes	                                    Consists of multiple computers or servers.
Concurrency	                                        Nodes run in parallel, handling tasks simultaneously.
No Shared Clock/Memory	                            Each node has its own memory and timing.
Communication via Network	                        Nodes talk to each other over a network (e.g., HTTP, RPC).
Fault Tolerance	                                    Designed to continue working even if some nodes fail.
Scalability                                         Easy to add more nodes to handle more load.
```
# Challenges in Distributed Systems

## Network latency and partitions
## Data consistency (CAP theorem)
## Concurrency and coordination
## Security and authentication
## Failure handling and recovery

# CAP Theorem
The CAP Theorem, also known as Brewer's Theorem, is a concept in distributed systems that states that it is impossible for a distributed data system to simultaneously provide all three of the following guarantees:

# Consistency (C):

Every read receives the most recent write or an error.
In simpler terms, all nodes in the system have the same data at the same time.
# Availability (A):

Every request (read or write) receives a response, even if some nodes are down.
The system remains operational, and no request will time out indefinitely.
# Partition Tolerance (P):

The system continues to function despite network partitions (communication breakdowns between nodes).

A partition occurs when some nodes in the system cannot communicate with others due to network issues.
# Key Insight of CAP Theorem:
In the presence of a network partition, a distributed system can provide only two of the three guarantees: Consistency, Availability, or Partition Tolerance.

Since network partitions are unavoidable in distributed systems (e.g., due to hardware failures, network issues, or scaling across data centers), the theorem implies that you must choose between:

Consistency and Partition Tolerance (CP): The system sacrifices availability during a partition.

Availability and Partition Tolerance (AP): The system sacrifices consistency during a partition.

# Types fo Consistancy
In distributed systems and databases, consistency refers to the guarantee about how up-to-date and synchronized copies of data are across multiple nodes. Here's a breakdown of weak, eventual, and strong consistency:

## 1. Strong Consistency
### Definition: 
Every read returns the most recent write.

### Guarantee: 
As soon as a write is acknowledged, any subsequent read (from any node) will return that updated value.

### Analogy: 
Like reading from a single up-to-date copy of the data.

### Example Systems: 
Traditional relational databases (e.g., PostgreSQL, MySQL with single instance), Google Spanner.

### Use Case: 
Banking, inventory management — where stale data can lead to incorrect decisions.

## 2. Eventual Consistency
### Definition: 
If no new updates are made, all replicas will eventually converge to the same value.

### Guarantee:
 Reads might return stale data temporarily, but the system will become consistent over time.

### Analogy:
 Like spreading news among friends — eventually everyone knows, but not all at once.

### Example Systems: 
Amazon DynamoDB, Cassandra, Couchbase, S3.

### Use Case: 

Social media feeds, shopping carts — where temporary inconsistency is tolerable.

## 3. Weak Consistency
### Definition:
 The system does not guarantee that subsequent reads will return the latest or even a consistent value.

### Guarantee: 
There may be no consistency guarantees; the system may prioritize availability or performance.

### Analogy: 
Like checking a whiteboard that multiple people are writing on — you might see partial or outdated information.

### Example Systems:
 Some custom caches, high-throughput logging systems.

### Use Case: 
Real-time analytics, telemetry, or systems where speed is more critical than accuracy.

# Types of availabilty
The terms "three nines", "four nines", "five nines", etc., refer to availability percentages — how much uptime a system guarantees over a year. The more nines, the higher the availability, and the less downtime allowed.

Here’s a breakdown:
```
Term	            Availability %	        Max Downtime per Year	            Max Downtime per Month	            Max Downtime per Day
Three 9s (99.9%)	99.9%	                ~8.76 hours	                        ~43.8 minutes	                    ~1.44 minutes
Four 9s (99.99%)	99.99%	                ~52.6 minutes	                    ~4.38 minutes	                    ~8.6 seconds
Five 9s (99.999%)	99.999%	                ~5.26 minutes	                    ~26.3 seconds	                    ~0.86 seconds
Six 9s (99.9999%)	99.9999%	            ~31.5 seconds	                    ~2.63 seconds	                    ~0.086 seconds
```

# What It Means Practically
Three 9s (99.9%): Common for many web applications; allows a few hours of downtime a year.

Four 9s (99.99%): Typical for high-reliability services like cloud infrastructure (e.g., AWS, Azure SLA levels).

Five 9s (99.999%): Used in mission-critical systems like telecommunication switches, hospitals, or banking systems.

Six 9s (99.9999%): Extremely rare — used for highly redundant and expensive systems (e.g., space tech, defense).

# Trade-offs
Higher nines mean more cost, complexity, and redundancy.

You must consider maintenance, failover, backups, monitoring, and disaster recovery to get close to five or six nines.

# Exploring Different Availability Patterns
Availability patterns in distributed systems are design strategies that aim to improve the availability, reliability, and fault tolerance of the system. These patterns provide a structured approach to designing and implementing systems that can handle failures, scale effectively, and provide a consistent user experience. Let’s explore some of these patterns in more detail.

# Active-Active Pattern
The active-active pattern is a strategy where multiple instances of an application are running simultaneously, and all instances are actively serving user requests. This pattern provides high availability and scalability, as it allows the system to distribute the workload across multiple instances and handle increased traffic or load.

The key advantage of the active-active pattern is that it provides redundancy and failover capability. If one instance fails, the other instances can continue serving requests, ensuring that the system remains available. However, this pattern requires careful design and implementation to ensure data consistency and synchronization between the instances.

# Active-Passive Pattern
The active-passive pattern involves running one instance of an application as the active instance, serving requests, while the other instance is passive and ready to take over in case of a failure. This pattern provides failover capability and efficient resource utilization, but it may have higher latency during failover.

The main advantage of the active-passive pattern is its simplicity and cost-effectiveness. It requires fewer resources than the active-active pattern, making it a good choice for smaller systems or applications with lower traffic.

# Failover Pattern
The failover pattern involves switching from a primary system to a secondary system when the primary system fails. This pattern ensures continuous availability and minimizes downtime.

The failover pattern is particularly useful in scenarios where the primary system has a single point of failure. It provides a backup system that can take over in case of a failure, ensuring that the system remains available. However, the failover process needs to be fast and seamless to avoid disrupting the user experience.

# Replication Pattern
The replication pattern involves replicating data across multiple servers or data centers to ensure redundancy and availability. This pattern allows multiple instances of the application to serve user requests simultaneously, improving performance and fault tolerance.

The replication pattern is effective in handling data consistency and availability in distributed systems. However, it requires careful design and implementation to ensure data synchronization and handle conflicts.

# Sharding Pattern
The sharding pattern involves dividing a large dataset into smaller, manageable parts called shards, which are distributed across multiple servers. This pattern improves performance and availability by distributing the data and workload across multiple resources.

The sharding pattern is beneficial for systems with large datasets or high traffic, as it allows the system to scale horizontally and handle increased load. However, it requires careful data partitioning and routing to ensure data consistency and performance.

# Load Balancing Pattern
The load balancing pattern involves distributing incoming requests across multiple servers or resources to ensure optimal utilization and availability. This pattern prevents any single server from being overwhelmed with traffic, improving performance and availability.

The load balancing pattern is crucial for handling high traffic and ensuring that the system can scale effectively. However, it requires a load balancer and may have higher complexity for session management.

In conclusion, availability patterns provide structured strategies for ensuring high availability in distributed systems. By understanding and implementing these patterns, we can design systems that are resilient, scalable, and reliable. In the next section, we will discuss how to implement these patterns and test their effectiveness.

# Latency vs Throughput
Latency and throughput are two core performance metrics in systems, especially in networking, databases, and distributed systems. They measure different aspects:
## Latency — "How fast?"
Definition: The time it takes to complete a single operation from start to finish.

Measured in: milliseconds (ms), microseconds (µs), or seconds.

Think of it as: Delay or response time.

Example:

A database query takes 120 ms to return.

A ping to a server returns in 20 ms.

## Throughput — "How much?"
Definition: The number of operations a system can handle in a given time.

Measured in: requests per second (RPS), transactions per second (TPS), Mbps, etc.

Think of it as: Capacity or volume.

Example:

A web server can handle 10,000 requests per second.

A network link has 100 Mbps throughput.

 Relationship
They are not the same: A system can have:

Low latency, low throughput (e.g., a fast single-threaded service)

High throughput, high latency (e.g., batch processing)

Improving one may harm the other:

Adding parallelism can increase throughput but increase latency for individual tasks.

Reducing latency often involves more CPU or memory, which might limit throughput.

# Performance vs Scalabilty
Performance — "How fast is the system right now?"
Definition: How efficiently a system completes tasks under a given workload.

Focus: Speed and responsiveness (e.g., response time, latency, throughput).

Measured by:

Latency: Time taken to respond to a single request.

Throughput: Number of operations per second.

Example:
A web app handles 500 requests/sec with 200 ms response time → that’s its current performance.

Scalability — "How well does the system handle growing workload?"
Definition: The system’s ability to maintain performance as the load increases.

Focus: Growth — how well the system adapts to more users, data, or traffic.

Types:

Vertical Scalability: Add more resources (CPU, RAM) to a single server.

Horizontal Scalability: Add more servers to share the load.

Example:
Your app handles 500 requests/sec today. Can it handle 10,000 requests/sec tomorrow by adding more machines or resources?

