# Clustering and Distributed Systems

## What is Clustering?

**Clustering** is a technique where multiple computers (nodes) work together as a single system to ensure high availability, load balancing, and fault tolerance. Clusters are typically tightly coupled, located in the same physical location, and managed as a unified resource.

### Characteristics of Clustering

* Tightly coupled nodes
* Centralized management
* Shared storage
* High availability and failover support
* Appears as a single system to users

### Examples

* Hadoop YARN Cluster
* Kubernetes Cluster
* MySQL Cluster

---

## What is a Distributed System?

A **Distributed System** is a system where multiple independent computers communicate and coordinate via a network to achieve a common goal. Unlike clustering, distributed systems can be loosely coupled and geographically separated.

### Characteristics of Distributed Systems

* Loosely coupled nodes
* Decentralized or independent management
* Nodes do not share memory or storage
* Highly scalable and fault-tolerant
* Concurrency and message passing

---

## Types of Distributed Systems

### 1. Client-Server Systems

* **Description**: Clients request services from centralized servers.
* **Examples**: Web servers, database servers

### 2. Three-Tier / N-Tier Architecture

* **Description**: Systems separated into presentation, logic, and data layers.
* **Examples**: Web applications

### 3. Peer-to-Peer (P2P) Systems

* **Description**: All nodes act as both clients and servers.
* **Examples**: BitTorrent, blockchain

### 4. Distributed Computing Systems

* **Description**: Distribute computational tasks across many machines.
* **Examples**: Apache Hadoop, Spark

### 5. Distributed File Systems

* **Description**: Provide access to files across multiple machines as if from one system.
* **Examples**: HDFS, GFS

### 6. Distributed Databases

* **Description**: Databases that store and manage data across multiple nodes.
* **Examples**: Cassandra, MongoDB (sharded), Amazon DynamoDB

### 7. Cloud-Based Distributed Systems

* **Description**: Systems hosted on cloud infrastructure offering scalability and resilience.
* **Examples**: AWS Lambda, Google Cloud Functions, Azure Functions

---

## Summary Table

| Type                    | Description                                | Examples                    |
| ----------------------- | ------------------------------------------ | --------------------------- |
| Client-Server           | Central server responds to client requests | Web server, DB server       |
| Three-Tier / N-Tier     | Separate presentation, logic, and data     | Web apps                    |
| Peer-to-Peer            | All nodes act as clients and servers       | Blockchain, BitTorrent      |
| Distributed Computing   | Distributed computational tasks            | Hadoop, Spark               |
| Distributed File System | Unified file access over multiple nodes    | HDFS, Ceph                  |
| Distributed Database    | Distributed data management                | Cassandra, DynamoDB         |
| Cloud-Based Systems     | Scalable services on cloud infrastructure  | AWS Lambda, Azure Functions |

---
# Load balancing vs Clustering

Load balancing shares some common traits with clustering, but they are different processes. Clustering provides redundancy and boosts capacity and availability. Servers in a cluster are aware of each other and work together toward a common purpose. But with load balancing, servers are not aware of each other. Instead, they react to the requests they receive from the load balancer.

We can employ load balancing in conjunction with clustering, but it also is applicable in cases involving independent servers that share a common purpose such as to run a website, business application, web service, or some other IT resource.