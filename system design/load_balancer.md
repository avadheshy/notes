# Load Balancing Concepts

## Table of Contents
- [Load Balancing Concepts](#load-balancing-concepts)
  - [Table of Contents](#table-of-contents)
  - [What is a Load Balancer?](#what-is-a-load-balancer)
  - [Types of Load Balancers](#types-of-load-balancers)
    - [Layer 4 (Network) Load Balancer](#layer-4-network-load-balancer)
    - [Layer 7 (Application) Load Balancer](#layer-7-application-load-balancer)
  - [Load Balancing Algorithms](#load-balancing-algorithms)
    - [Stateless vs Stateful Load Balancing](#stateless-vs-stateful-load-balancing)
    - [Round Robin](#round-robin)
    - [Weighted Round Robin](#weighted-round-robin)
    - [IP Hash](#ip-hash)
    - [Least Connection Algorithm](#least-connection-algorithm)
    - [Least Response Time Algorithm](#least-response-time-algorithm)
  - [Consistent Hashing](#consistent-hashing)
  - [Proxy vs Reverse Proxy](#proxy-vs-reverse-proxy)
    - [Forward Proxy](#forward-proxy)
    - [Reverse Proxy](#reverse-proxy)
  - [Rate Limiting](#rate-limiting)

---

## What is a Load Balancer?
Load balancing algorithms decide which server should handle each request, making sure they're divvied up fairly. 

You set up a load balancer that sits between your website's users and your servers. When a customer visits your website, their request goes to the load balancer first.

## Types of Load Balancers
Load balancers are categorized based on the layer of the OSI model at which they operate.

### Layer 4 (Network) Load Balancer
Operates at the transport layer (Layer 4) of the OSI model. Makes decisions based on source/destination IP addresses and port numbers.

**How it works:**
- Receives requests and looks at transport layer data (IPs and ports)
- Distributes TCP/UDP traffic efficiently

**✅ Advantages:**
- High performance and low latency
- Efficient for basic traffic distribution

**❌ Disadvantages:**
- Limited application awareness
- Cannot make content-based decisions

### Layer 7 (Application) Load Balancer
Operates at the application layer (Layer 7). Makes intelligent decisions based on HTTP headers, cookies, URLs.

**How it works:**
- Analyzes request content (HTTP headers, URLs)
- Can perform content-based routing

**✅ Advantages:**
- Application-aware routing
- Supports advanced load balancing
- Enables SSL termination

**❌ Disadvantages:**
- Higher processing overhead
- More complex configuration

## Load Balancing Algorithms

### Stateless vs Stateful Load Balancing
| Feature          | Stateless                     | Stateful                          |
|------------------|-------------------------------|-----------------------------------|
| Session Tracking | No session persistence        | Maintains session stickiness      |
| Complexity      | Simple                        | More complex                      |
| Scalability     | Easier to scale               | Harder to scale                   |
| Use Cases       | Static content, simple apps   | Shopping carts, logged-in sessions|
| Examples        | Round Robin, Random           | IP Hash, Cookie-based persistence |

### Round Robin
Cycles through server list sequentially.

**How it works:**
1. Maintains ordered server list
2. Forwards request to next server in sequence
3. Loops back to first server after last

**✅ Advantages:**
- Simple implementation
- Equal distribution (in theory)

**❌ Disadvantages:**
- Doesn't account for server capacity
- No health monitoring
- Poor handling of persistent connections

### Weighted Round Robin
Enhanced Round Robin with capacity weighting.

**How it works:**
- Assigns weights to servers
- More powerful servers get more requests
- Within same weight, uses standard Round Robin

**✅ Advantages:**
- Accounts for server capacity
- More precise load distribution

**❌ Disadvantages:**
- Requires manual weight configuration
- Doesn't adapt to runtime changes

### IP Hash
Uses client IP to determine server assignment.

**How it works:**
1. Hashes client IP address
2. Maps hash to server
3. Same IP always maps to same server

**✅ Advantages:**
- Session persistence
- Client-consistent routing

**❌ Disadvantages:**
- Uneven distribution with few active IPs
- Problems with NAT environments

### Least Connection Algorithm
Routes to server with fewest active connections.

**How it works:**
- Tracks active connections per server
- Routes new requests to least busy server
- Continuously updates connection counts

**✅ Advantages:**
- Dynamic load distribution
- Adapts to current server load

**❌ Disadvantages:**
- Doesn't consider server capacity
- Connection count spikes can cause imbalance

### Least Response Time Algorithm
Routes to server with fastest response times.

**How it works:**
- Monitors server response times (including TTFB)
- Routes to fastest-responding server
- Continuously updates performance metrics

**✅ Advantages:**
- Optimizes user experience
- Dynamic adaptation

**❌ Disadvantages:**
- Sensitive to temporary spikes
- Requires continuous monitoring
- Higher overhead

## Consistent Hashing
Distributed hashing technique that minimizes remapping when nodes are added/removed.

**Key Concepts:**
- Hash ring structure (circular keyspace)
- Virtual nodes for better distribution
- Minimal disruption during scaling

**How it works:**
1. Nodes and keys are hashed onto ring
2. Keys are assigned to next node clockwise
3. Node addition/removal affects only adjacent keys

**Benefits:**
- Scalability
- Fault tolerance
- Load distribution

## Proxy vs Reverse Proxy

### Forward Proxy
Sits between clients and internet.

**Use Cases:**
- Client anonymity
- Bypassing restrictions
- Content filtering

### Reverse Proxy
Sits between internet and servers.

**Use Cases:**
- Load balancing
- SSL termination
- Security protection
- Caching

## Rate Limiting
Controls request frequency to prevent abuse.

**Common Types:**
- Fixed window (requests per minute)
- Sliding window
- Token bucket
- Leaky bucket

**Purposes:**
- Prevent DDoS attacks
- API fair usage
- Brute force protection
- Resource management
  
https://medium.com/@abhirup.acharya009/load-balancing-system-design-fundamentals-d64674227c36

https://medium.com/@anil.goyal0057/understanding-consistent-hashing-a-robust-approach-to-data-distribution-in-distributed-systems-0e4a0e770897