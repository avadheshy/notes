# What is Pub/Sub Architecture?

Consider a scenario of synchronous message passing. You have two components sender and receiver in your system that communicate with each other.

The receiver asks for a service from the sender and the sender serves the request and waits for an acknowledgment from the receiver.

There is another receiver that requests a service from the same sender. The sender might get blocked if it hasn’t yet received any acknowledgment from the first receiver. Therefore the sender isn’t able to serve the second receiver. To solve this drawback, the Pub-Sub model was introduced.

The Pub/Sub (Publisher/Subscriber) model is a messaging pattern used in software architecture which uses a message broker. The message broker routes messages from publishers to subscribers based on subscriptions, ensuring correct delivery, persistence, and scalability.

# Components of Pub/Sub Architecture?
In the Pub/Sub (Publish/Subscribe) model, there are several key components that work together to enable communication between publishers and subscribers. These components include:

Publisher: Creates and sends messages to topics without knowing subscribers.

Subscriber: Receives messages from subscribed topics without knowing publishers.

Topic: A named channel that categorizes messages. Publishers send messages to topics, and subscribers subscribe to them.

Message Broker: Routes messages from publishers to subscribers based on subscriptions, ensuring delivery, persistence, and scalability.

Message: The data unit exchanged, which can be text, JSON, or binary.

Subscription: Links subscribers to topics, defining which messages are received and delivery guarantees (e.g., at-most-once, at-least-once).

# How does Pub/Sub Architecture work?
Below is how the Pub/Sub architecture works:

Step 1: Publishers create messages and send them to the Pub/Sub system. They sort these messages into topics or channels based on what the messages are about.

Step 2: Subscribers let the system know which topics they're interested in. They’ll get messages only from those topics.

Step 3: Topics are basically channels for messages. Publishers send their messages to specific topics, and subscribers can choose one or more topics to follow.

Step 4: Message brokers act as go-betweens, managing how messages get from publishers to subscribers. They take messages from publishers and send them to the subscribers who are interested.

Step 5: When a publisher sends a message to a topic, the message broker grabs it and sends it out to all the subscribers who have signed up for that topic.

Step 6: The Pub/Sub system allows for asynchronous communication. This means publishers can send messages without waiting for subscribers to be ready, and subscribers can pick up messages whenever it suits them, without needing the publisher to be around

# Real-World Example of Pub/Sub Architecture
A real-life example of Pub/Sub architecture can be seen in the operation of a social media platform like Twitter.

Publishers: Users post tweets, which are published to the Twitter platform.

Subscribers: Followers of a user subscribe to their tweets to receive updates.

Topics: Each user's tweets can be considered a topic, and subscribers receive updates for the topics they are interested in.

Message Broker: Twitter's backend infrastructure acts as the message broker, routing tweets from publishers to subscribers.

Message: Each tweet is a message that is published by the user and received by their followers.
In this example, the Pub/Sub architecture allows for scalable and efficient distribution of tweets to followers. Publishers (users) can publish tweets without knowing who will receive them, and subscribers (followers) receive updates in real-time without the need for direct communication with the publishers.

# Use-cases of Pub/Sub Architecture
The Pub/Sub (Publisher/Subscriber) architecture is widely used in various scenarios where asynchronous and scalable communication between components is required. Some common use cases of Pub/Sub architecture include:

**Real-time Data Streaming**: It’s often used in applications that deal with real-time data, like IoT devices and sensor networks, allowing multiple subscribers to get data streams right away.

**Event-driven Architectures**: This setup works well for systems that react to events instead of constantly checking for updates, making applications more responsive.

**Message Queues**: Pub/Sub can act as a message queue, temporarily holding messages until subscribers can process them, which helps manage how messages are delivered.

**Notifications and Alerts**: It’s used for sending notifications and alerts, letting publishers send important updates that subscribers can receive instantly.

**Scalable Web Applications**: In web apps, Pub/Sub supports features like real-time updates and chat, so many users can receive information at the same time without overloading the server.

**Microservices Communication**: Finally, it helps microservices talk to each other, allowing them to communicate without being tightly connected, which improves scalability and reliability.

# Types of Pub/Sub Services
Below are the two types of Pub/Sub Services:

## 1. Pub/Sub Service
This is the main messaging service that most users and applications choose. It provides:

High Reliability: Ensures that messages are delivered consistently.

Integrations: Supports a wide range of integrations with other services.

Automatic Capacity Management: Handles scaling automatically based on demand.

Data Replication: Synchronously replicates all data to at least two zones and offers best-effort replication to a third zone for added reliability.
## 2. Pub/Sub Lite Service
This is a separate messaging service designed to be more cost-effective but comes with some trade-offs:

Lower Reliability: Offers less reliability compared to the standard Pub/Sub service.

Zonal or Regional Storage: Zonal Lite topics are stored in one zone, while Regional Lite topics replicate data to a second zone asynchronously.

Pre-provisioning Required: You need to manage and provision your own storage and throughput capacity.

Cost-Effective: Consider this option if keeping costs low is essential, and you can accept the lower reliability and some extra management tasks.

# Comparing Pub/Sub to other Messaging Technologies
Below is the comparison of Pub/Sub to other messaging Technologies:

Pub/Sub vs. Message Queues:
Message Queues deliver messages to one consumer at a time (point-to-point), ensuring order and delivery. Pub/Sub broadcasts messages to multiple subscribers simultaneously, ideal for event-driven systems.
Pub/Sub vs. Streaming Platforms:

Streaming platforms (e.g., Kafka) handle continuous data streams with long-term retention and complex processing. Pub/Sub focuses on simpler, real-time message delivery.

Pub/Sub vs. WebSockets:
WebSockets enable real-time, bidirectional client-server communication (e.g., chat). Pub/Sub decouples publishers and subscribers, supporting multiple subscribers without direct connections.

Pub/Sub vs. HTTP APIs:
HTTP APIs use synchronous request-response communication. Pub/Sub supports asynchronous messaging, allowing publishers to send without waiting for subscriber responses.

When and When not to Use Pub/Sub Architecture
# 1. When to Use the Pub/Sub Architecture
Use Pub/Sub Architecture when:

Subscribers don’t need to know about each other, making the system more flexible and easier to scale.
Pub/Sub helps you build systems that can grow easily. You can add more publishers or subscribers without disrupting the existing setup.

If you want parts of your system to communicate without waiting for each other, Pub/Sub is a great option. Publishers can send messages without needing to wait for subscribers.

This approach is perfect for event-driven systems. Publishers can send out events, and subscribers can respond to those events without being tightly linked together.

With Pub/Sub, subscribers can change their interests at runtime. They can subscribe to different topics or types of messages, adding more flexibility to the system.

# 2. When Not to Use the Pub/Sub Architecture
Do not use Pub/Sub Architecture when:

If you need very quick communication between parts of your system, Pub/Sub might not be the best option. The process of routing messages and managing subscriptions can slow things down.

Using Pub/Sub can make your system more complicated, especially when it comes to routing messages and handling subscriptions.

Pub/Sub doesn’t guarantee that messages will be delivered in the order they were sent. If your application needs messages to arrive in a specific sequence, Pub/Sub may not work for you.

For smaller applications where a few components communicate directly, using Pub/Sub could add unnecessary complexity that isn’t needed.

# How Scalable and Secure is Pub/Sub Architecture?
The scalability and security of the Pub/Sub model depend on the implementation and the specific requirements of the system. However, in general, the Pub/Sub model can be both scalable and secure if implemented correctly.

**Scalability**:
Horizontal scaling allows adding more publishers, subscribers, or brokers to handle increased load. Load balancing distributes messages evenly across brokers for efficient resource use.
**Security**:
Access control restricts message access to authorized users. Encryption protects data in transit using TLS or similar methods. Authentication and authorization verify identities and permissions of publishers and subscribers.
**Challenges**:
Message ordering is difficult to guarantee strictly in distributed setups. Delivery guarantees are usually at-least-once or at-most-once, which may not suit all use cases.

# Benefits and Challenges of Pub/Sub Architecture
## 1. Benefits of Pub/Sub Architecture
Below are the benefits of Pub/Sub Architecture:

Scalability: Easily scales with many publishers, subscribers, and messages via decoupled components and message brokers.

Decoupling: Publishers and subscribers operate independently, simplifying system design and maintenance.

Asynchronous Communication: Enables non-blocking message exchange, improving responsiveness and efficiency.

Reliability: Ensures message delivery with acknowledgments, retries, and fault-handling mechanisms.
## 2. Challenges of Pub/Sub Architecture
Below are the challenges of Pub/Sub Architecture:

Message Ordering: Messages may arrive out of order, causing issues for apps requiring strict sequencing.
Exactly-once Delivery: Ensuring no duplicates despite failures is difficult and complex.

Latency: Message routing can introduce delays, making low latency hard to balance with scalability and reliability.

Complexity: Managing subscriptions, routing, and consistency in large-scale setups requires careful planning.

# Pub/Sub Vs. Point to Point Messaging
Below are the differences between Pub/Sub and Point to Point Messaging:

| Aspect              | Pub/Sub Messaging                                                     | Point-to-Point Messaging                                      |
|---------------------|-----------------------------------------------------------------------|----------------------------------------------------------------|
| Message Delivery    | Messages are broadcast to multiple subscribers                       | Messages are delivered to a single receiver                    |
| Subscriber Knowledge| Publishers do not need to know about subscribers                     | Sender needs to know the receiver                              |
| Scalability         | Scalable, as new subscribers can be added without affecting publishers | Less scalable, as each message is sent directly to a specific receiver |
| Coupling            | Loosely coupled, as publishers and subscribers are decoupled         | Tightly coupled, as sender and receiver are directly connected |
| Use Case            | Suitable for broadcasting messages to multiple recipients            | Suitable for one-to-one communication                           |
| Example Technology  | Google Cloud Pub/Sub, Amazon SNS/SQS, Kafka                          | JMS, AMQP, RabbitMQ                                            |


