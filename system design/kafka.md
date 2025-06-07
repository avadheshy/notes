# What is Kafka
Apache Kafka is a distributed streaming platform designed to handle large volumes of real-time data. It’s an open-source system used for stream processing, real-time data pipelines and data integration.

It was built on the concept of publish/subscribe model and provides high throughput, reliability and fault tolerance. It can handle over a million messages per second, or trillions of messages per day.

# Kafka Core Concepts and Message Flow (Python-centric Overview)

This guide explains the core Kafka concepts and how they interact using an example relevant for Python developers. It does **not include code**, only concepts and flow.

---

## Core Kafka Concepts

### 1. **Producer**

A **producer** is a client that sends data (messages) to Kafka topics.

* Sends messages as key-value pairs.
* Can define a **key** so messages with the same key go to the same partition (helps preserve order).

### 2. **Consumer**

A **consumer** reads messages from Kafka topics.

* Can be one of many in a **consumer group**.
* Reads from one or more **partitions** assigned to it.

### 3. **Consumer Group**

A **consumer group** is a logical group of consumers sharing the workload:

* Each partition of a topic is assigned to only one consumer **within a group**.
* Kafka rebalances partitions among consumers as instances scale up/down.

### 4. **Topic**

A **topic** is a category/feed name to which records are published.

* A topic is split into multiple **partitions** for parallel processing.

### 5. **Partition**

* A unit of parallelism.
* Messages within a partition are **ordered**.
* Each partition has a growing sequence of **offsets**.

### 6. **Offset**

An **offset** is the position of a message in a partition.

* Consumers track offsets to know where they left off.
* Can be auto-committed or manually committed.

### 7. **Broker**

* A Kafka server storing data and serving producers and consumers.
* Kafka cluster consists of multiple brokers.

### 8. **Zookeeper** *(used in Kafka versions <3.0)*

* Coordinates brokers and handles metadata, leader election, and cluster management.
* Kafka post 3.x supports **KRaft mode** (Kafka without Zookeeper).

### 9. **Replication**

* Kafka replicates topic partitions across brokers.
* Helps with fault tolerance.
* One partition is the **leader**, others are **followers**.

---

## Example: Order Processing System

### Scenario:

You're tracking e-commerce orders using Kafka.

#### 1. Create Topic

`orders` topic is created with 3 partitions:

* `orders-0`
* `orders-1`
* `orders-2`

#### 2. Producer Sends Messages

Your Python service (producer) sends messages like:

```json
{ "order_id": 1234, "user_id": 678, "total": 1499 }
```

* If a **key** is provided (e.g., `user_id`), all messages from same user go to same partition.
* Kafka assigns messages to partitions using round-robin (if no key).

#### 3. Message Storage in Partitions

| Partition  | Offset | Message    |
| ---------- | ------ | ---------- |
| `orders-0` | 0      | order 1234 |
| `orders-1` | 0      | order 1235 |
| `orders-2` | 0      | order 1236 |
| `orders-0` | 1      | order 1237 |

#### 4. Consumers in a Group

Consumer Group: `order-processing-group`

* 2 instances of a Python consumer app.
* Kafka assigns partitions:

  * Consumer A → `orders-0`, `orders-1`
  * Consumer B → `orders-2`

Each consumer:

* Reads messages in order.
* Processes (e.g., stores to DB).
* Commits offsets (auto or manual).

#### 5. Scaling Consumers

* Add more consumers → Kafka rebalances partitions.
* Can also increase **partitions** to scale out load.

#### 6. Multiple Groups

Another team wants to run analytics → starts a new group `analytics-group`.

* Consumes same `orders` topic from beginning (if `auto.offset.reset=earliest`).
* Independent processing; does not interfere with `order-processing-group`.

---

## Final Flow Summary

```plaintext
Producer → Kafka Topic (orders) → Partitioned (0,1,2) →
Stored with offsets →
Consumers in a Group → Assigned partitions →
Reads & Processes messages → Commits offset
```

Kafka ensures **high-throughput, reliable, scalable message streaming**. Python clients (like `confluent-kafka-python` or `kafka-python`) let you easily implement this architecture.
