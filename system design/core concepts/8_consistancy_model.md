# Consistency Models: A Complete Guide

## What are Consistency Models?

**A consistency model defines the rules about when and how updates to data become visible to different parts of a distributed system.**

In single-machine systems, consistency is straightforward: when you write a value, you immediately read that value. But in distributed systems with multiple replicas across different servers or data centers, things get complicated:

- What happens when you write to one replica and immediately read from another?
- If two users update the same data simultaneously on different servers, which value wins?
- How long does it take for an update to propagate to all replicas?
- Can you read your own writes?

Consistency models provide answers to these questions and define the guarantees a system makes about data visibility and ordering.

---

## Why Consistency Models Matter

### The Fundamental Challenge

In distributed systems, you cannot have:
- **Perfect consistency** (all nodes see the same data at the same time)
- **100% availability** (system responds to every request)
- **Partition tolerance** (system continues despite network failures)

...all at once. This is known as the **CAP theorem**.

### Real-World Implications

**Example 1: Bank Account Balance**
```
User checks balance: $100
User makes two simultaneous withdrawals of $60 each from different ATMs
Both ATMs see $100 and allow the withdrawal
Result: Account overdrawn by $20

Strong consistency prevents this.
Eventual consistency allows this temporarily.
```

**Example 2: Social Media Post**
```
User posts a photo
User's friend immediately checks their feed
Friend doesn't see the photo yet (it's propagating)
Result: Confusing but not critical

Eventual consistency is acceptable here.
Strong consistency would be too expensive.
```

**Example 3: Collaborative Editing**
```
User A types "Hello" 
User B types "World" at the same time
Without proper consistency: "HWeolrllod"
With causal consistency: "Hello World" or "World Hello"
```

### The Trade-offs

**Strong Consistency**:
- ✅ Simple to reason about (behaves like single machine)
- ✅ No surprises for users
- ❌ Higher latency (coordination required)
- ❌ Lower availability (may block on network issues)
- ❌ Doesn't scale as well

**Weak Consistency**:
- ✅ Lower latency (no coordination needed)
- ✅ Higher availability (always responsive)
- ✅ Better scalability
- ❌ Complex to reason about
- ❌ Potential for conflicts
- ❌ May confuse users

---

## The CAP Theorem

**CAP Theorem states that in the presence of a network partition, you must choose between Consistency and Availability.**

### The Three Properties

**Consistency (C)**: All nodes see the same data at the same time
- Every read receives the most recent write
- All clients see the same view of the data
- Like a single, non-distributed system

**Availability (A)**: Every request receives a response (success or failure)
- System remains operational
- Requests don't hang or timeout
- May return stale data

**Partition Tolerance (P)**: System continues operating despite network failures
- Network can lose messages
- Nodes can become unreachable
- System doesn't fail completely

### Why You Can't Have All Three

When a network partition occurs (nodes can't communicate):

**Choose CP (Consistency + Partition Tolerance)**:
- Block requests to maintain consistency
- System becomes unavailable in some partitions
- Example: Banking systems, inventory management

**Choose AP (Availability + Partition Tolerance)**:
- Respond to all requests, even with stale data
- Risk inconsistency between partitions
- Example: Social media feeds, caching layers

**Note**: You must have P (partition tolerance) in distributed systems because network failures are inevitable. The real choice is between C and A during partitions.

### Real-World CAP Choices

| System | Choice | Reasoning |
|--------|--------|-----------|
| **Traditional SQL (single master)** | CP | Blocks writes during partition to maintain consistency |
| **MongoDB (default)** | CP | Majority writes ensure consistency, may block |
| **Cassandra** | AP | Always available, eventual consistency |
| **DynamoDB** | AP (default) | Tunable, but optimized for availability |
| **Consul** | CP | Consistent service discovery critical |
| **DNS** | AP | Availability more important than perfect consistency |

---

## The Consistency Spectrum

Consistency models exist on a spectrum from **strongest** (most restrictive, easiest to reason about) to **weakest** (least restrictive, most performant).

```
Strongest                                                      Weakest
    |                                                              |
    v                                                              v
Linearizability → Sequential → Causal → Eventual → Weak
```

---

## Strong Consistency Models

### 1. Linearizability (Strict Consistency)

**The strongest consistency model. The gold standard.**

**Guarantee**: Operations appear to execute atomically and instantaneously at some point between invocation and completion. Once a write completes, all subsequent reads must return that value (or a newer one).

**In simple terms**: The system behaves as if there's only one copy of the data, and operations happen in real-time order.

#### How It Works

```
Timeline:
---------
10:00:00.000  Client A writes X = 1
10:00:00.100  Write completes
10:00:00.200  Client B reads X → MUST return 1 or newer
10:00:00.300  Client C writes X = 2
10:00:00.400  Write completes
10:00:00.500  Client A reads X → MUST return 2 or newer

Any read after a write completes MUST see that write or a newer one.
```

#### Characteristics

**Guarantees**:
- Real-time ordering of operations
- Single system image (behaves like one machine)
- Reads always return latest value
- No time-travel paradoxes

**Costs**:
- High latency (coordination required)
- Limited scalability
- Reduced availability during partitions
- Requires synchronous replication or consensus

#### Implementation Techniques

**Synchronous Replication**:
```
Write request arrives
  ↓
Write to ALL replicas synchronously
  ↓
Wait for ALL to acknowledge
  ↓
Respond to client
```

**Consensus Protocols** (Paxos, Raft):
- Require majority agreement
- Tolerate some failures
- But add coordination latency

**Single Leader**:
- All writes go through one node
- Reads from followers may lag
- Leader is single point of failure

#### Use Cases

**When to use**:
- Financial transactions (prevent double-spending)
- Inventory management (prevent overselling)
- Leader election
- Distributed locks
- Any scenario where inconsistency = data corruption

**Examples**:
- Google Spanner (globally distributed)
- etcd, Consul (service coordination)
- Zookeeper (distributed coordination)

#### Example: Banking Transaction

```
CORRECT (Linearizable):
Account balance: $100

10:00:00  ATM 1: Withdraw $60 → Success → Balance: $40
10:00:01  ATM 2: Withdraw $60 → DENIED (sees $40) ✓

INCORRECT (Non-linearizable):
Account balance: $100

10:00:00  ATM 1: Withdraw $60 → Success (sees $100)
10:00:00  ATM 2: Withdraw $60 → Success (sees $100)
Result: Both succeed → Balance: -$20 ✗
```

### 2. Sequential Consistency

**Slightly weaker than linearizability. Operations appear in some sequential order, but not necessarily real-time order.**

**Guarantee**: All operations appear to execute in some sequential order, and operations from each individual process appear in the order specified by its program.

**Key difference from linearizability**: Doesn't respect real-time ordering across different clients.

#### How It Works

```
Client A: Write X=1, Write X=2
Client B: Read X, Read X

Linearizable requires:
- If B reads X=2, next read cannot see X=1 (real-time order)

Sequential allows:
B might see: X=1, X=2 (ordered, but delayed)
B might see: X=2, X=2 (saw latest immediately)
B might NOT see: X=2, X=1 (violates sequential order)
```

#### Example

```
Timeline:
---------
10:00:00  Client A writes X = 1
10:00:05  Client A writes X = 2
10:00:10  Client B reads X

Linearizable: MUST return 2 (real-time order)
Sequential: Could return 1 (if replication delayed)
            But future reads can't go backwards!
```

#### Characteristics

**Guarantees**:
- Program order within each process preserved
- All processes see same order of operations
- No real-time guarantees

**Costs**:
- Still requires coordination
- Lower latency than linearizability
- More scalable than linearizability

#### Use Cases

- Multi-core processor memory models
- Distributed caches with update propagation
- Systems where eventual order matters but real-time doesn't

### 3. Serializability

**A consistency model for transactions, not single operations.**

**Guarantee**: Concurrent transactions appear to execute in some serial (sequential) order, as if no concurrency existed.

**Important distinction**: 
- **Serializability**: About transactions, any order is fine
- **Linearizability**: About operations, respects real-time order

#### Example

```
Account A: $100, Account B: $100

Transaction 1: Transfer $50 from A to B
  Read A ($100)
  A = A - 50 ($50)
  Read B ($100)
  B = B + 50 ($150)

Transaction 2: Add 10% interest to all accounts
  Read A ($100)
  A = A * 1.1 ($110)
  Read B ($100)
  B = B * 1.1 ($110)

Serializable result (either order):
- T1 then T2: A=$55, B=$165, Total=$220 ✓
- T2 then T1: A=$60, B=$160, Total=$220 ✓

Non-serializable result:
- Interleaved: A=$55, B=$110, Total=$165 ✗ (money lost!)
```

#### Implementation: Isolation Levels

**Strict Serializable**: Serializability + Linearizability
- Strongest possible guarantee
- Examples: Google Spanner, CockroachDB

**Serializable** (without linearizable):
- Snapshot Isolation with Serializable Snapshot Isolation (SSI)
- Two-phase locking (2PL)
- Optimistic concurrency control (OCC)

---

## Weak Consistency Models

### 4. Causal Consistency

**Preserves cause-and-effect relationships but allows concurrent operations to be seen in different orders.**

**Guarantee**: If operation A causally influences operation B, all processes see A before B. Concurrent operations (no causal relationship) can be seen in any order.

#### Causal Relationships

**Causally related**:
- Same process: Write X=1, then Write X=2 (sequential)
- Read-then-write: Read X, then Write Y based on X
- Transitive: A→B and B→C implies A→C

**Concurrent (not causally related)**:
- Different processes with independent operations
- Can be seen in any order by different observers

#### Example: Social Media Comments

```
User A posts: "I got a new puppy!"
User B comments: "What's their name?"
User A replies: "Luna!"

Causal consistency ensures:
- Everyone sees the post before the comment
- Everyone sees the comment before the reply
- Order preserved: Post → Comment → Reply ✓

Without causal consistency:
Someone might see:
- "Luna!" (the reply)
- "What's their name?" (the comment)
- "I got a new puppy!" (the original post)
Order broken: Reply → Comment → Post ✗ (confusing!)
```

#### Concurrent Operations Example

```
User A: Posts photo 1
User B: Posts photo 2 (independent, concurrent)

User C might see: Photo 1, then Photo 2
User D might see: Photo 2, then Photo 1

Both are valid under causal consistency (no causal relationship)
```

#### Implementation

**Vector Clocks**: Track causality
```
Each client maintains vector of logical clocks
[ClientA: 3, ClientB: 1, ClientC: 2]

Operation includes vector clock
System can determine: causally related or concurrent
```

**Dependency Tracking**:
- Track which operations depend on which
- Ensure dependencies satisfied before showing operation

#### Characteristics

**Guarantees**:
- Cause comes before effect
- Reads see writes that happened-before
- No time-travel anomalies

**Costs**:
- More complex than eventual consistency
- Requires tracking causality metadata
- Some coordination needed

#### Use Cases

- Collaborative editing (Google Docs style)
- Comment threads and conversations
- Distributed databases with causal relationships
- Shopping cart operations

**Systems**:
- MongoDB (with causal consistency sessions)
- Cassandra (with lightweight transactions)
- Azure Cosmos DB (session consistency)

### 5. Eventual Consistency

**The weakest useful consistency model. Guarantees convergence, not immediacy.**

**Guarantee**: If no new updates are made, eventually all replicas will converge to the same value. No guarantees about *when*.

#### How It Works

```
Time:     T0      T1      T2      T3      T4
-------------------------------------------------
Replica A: 1       2       2       2       2
Replica B: 1       1       1       2       2
Replica C: 1       1       1       1       2

At T1: Write X=2 to Replica A
Eventually (T4): All replicas converge to 2

During propagation (T1-T3):
- Reads may return stale data
- Different replicas show different values
- No guarantees about staleness duration
```

#### Characteristics

**Guarantees**:
- All replicas will eventually agree
- No data loss (updates eventually propagate)
- Monotonic reads (per-session): don't go backwards

**No Guarantees**:
- When convergence happens
- What value you'll read before convergence
- Read-your-writes (may not see your own update)

**Benefits**:
- Lowest latency (no coordination)
- Highest availability (always responsive)
- Best scalability (no synchronization)

**Costs**:
- Complex application logic
- Potential for conflicts
- User confusion (stale data)

#### Conflict Resolution Strategies

**Last-Write-Wins (LWW)**:
```
Replica A: Write X=1 at timestamp T1
Replica B: Write X=2 at timestamp T2

Resolution: X=2 (latest timestamp wins)
Problem: May lose legitimate updates
```

**Version Vectors**:
```
Track version per replica
Detect concurrent conflicting writes
Application resolves conflict
```

**CRDTs (Conflict-free Replicated Data Types)**:
```
Data structures designed to merge automatically
No application-level conflict resolution needed
Examples: Counters, Sets, Registers
```

**Application-Level Resolution**:
```
Present both versions to user
User chooses correct value
Example: Amazon shopping cart shows all items
```

#### Use Cases

**Ideal for**:
- Social media feeds (staleness acceptable)
- Product catalogs (eventual correctness okay)
- DNS records (propagation delay expected)
- Caching layers (stale data temporarily acceptable)
- Analytics and metrics (approximate data okay)

**Not suitable for**:
- Financial transactions
- Inventory management (can't oversell)
- Booking systems (double-booking risk)
- Access control (security implications)

#### Real-World Examples

**DNS**:
```
Update nameserver record: example.com → 1.2.3.4
Propagation time: Minutes to hours (TTL-dependent)
Different DNS servers return different IPs during propagation
Eventually consistent ✓
```

**Amazon Shopping Cart**:
```
Add item on phone: Cart shows 1 item
Open laptop: Cart might show 0 items (not yet propagated)
Wait a moment: Laptop shows 1 item (eventual consistency)

Conflict: Add item A on phone, item B on laptop simultaneously
Resolution: Show both (merge), user decides
```

**Cassandra**:
```
Write to node A with replication factor 3
Nodes A, B, C get the write asynchronously
Read might hit node C before replication completes
Returns stale data temporarily
Eventually converges
```

### 6. Read-Your-Writes Consistency

**A practical middle ground: you always see your own updates.**

**Guarantee**: After a client writes a value, subsequent reads by that same client will see that value (or a newer one).

**Note**: Other clients may see stale data.

#### Example

```
User writes: "Update profile picture"
User immediately refreshes page: See new picture ✓ (read-your-writes)

Different user views profile: Might see old picture (eventual consistency)
```

#### Implementation

**Session-Based**:
```
Track writes in user session
Route reads to replica with user's writes
Or wait for write propagation before responding
```

**Timestamp-Based**:
```
Write returns timestamp
Read includes "need data at least as new as timestamp T"
System ensures read sees write
```

#### Use Cases

- User profile updates
- Settings changes
- Content publishing (author sees immediately)
- Shopping cart (user sees their additions)

---

## Tunable Consistency

Some systems allow you to choose consistency level per operation.

### Cassandra Consistency Levels

**Write Consistency Levels**:

| Level | Description | Replicas Written |
|-------|-------------|-----------------|
| **ONE** | Only one replica must ack | 1 |
| **QUORUM** | Majority must ack | ⌈N/2⌉ + 1 |
| **ALL** | All replicas must ack | N |

**Read Consistency Levels**:

| Level | Description | Replicas Read |
|-------|-------------|---------------|
| **ONE** | Return first response | 1 |
| **QUORUM** | Wait for majority | ⌈N/2⌉ + 1 |
| **ALL** | Wait for all | N |

**Achieving Strong Consistency**:
```
If: Read + Write > Replication Factor
Then: Strong consistency guaranteed

Example (Replication Factor = 3):
- Write QUORUM (2) + Read QUORUM (2) = 4 > 3 ✓
- Write ONE (1) + Read ALL (3) = 4 > 3 ✓
- Write ONE (1) + Read ONE (1) = 2 < 3 ✗ (eventual)
```

### DynamoDB Consistency

**Eventually Consistent Reads** (default):
- Fastest
- Might return stale data
- Half the cost of strongly consistent reads

**Strongly Consistent Reads**:
- Returns most recent data
- Higher latency
- May fail if replica unavailable

**Transactional Reads/Writes**:
- ACID guarantees
- Multiple items updated atomically
- Highest cost

---

## Choosing a Consistency Model

### Decision Framework

```
Start here: What happens if data is inconsistent?

├─ Data corruption or financial loss?
│  └─ Use Strong Consistency (Linearizable/Serializable)
│     Examples: Banking, inventory, payments
│
├─ User confusion but no data loss?
│  ├─ Same user needs to see own changes?
│  │  └─ Use Read-Your-Writes + Eventual
│  │     Examples: User profiles, settings
│  │
│  └─ Cause-effect relationships matter?
│     └─ Use Causal Consistency
│        Examples: Comments, conversations
│
└─ Temporary inconsistency is fine?
   └─ Use Eventual Consistency
      Examples: Metrics, analytics, caching
```

### Application Patterns

**E-commerce System**:

| Operation | Consistency Level | Reasoning |
|-----------|------------------|-----------|
| **Product catalog** | Eventual | Stale price/description acceptable temporarily |
| **Inventory** | Strong | Can't oversell items |
| **Shopping cart** | Read-your-writes | User must see their additions |
| **Order placement** | Serializable | Prevent double-charging |
| **Reviews** | Eventual | Delay in showing reviews okay |

**Social Media**:

| Operation | Consistency Level | Reasoning |
|-----------|------------------|-----------|
| **News feed** | Eventual | Missing post for 30s acceptable |
| **Post creation** | Read-your-writes | Author sees own post |
| **Comments** | Causal | Reply must come after original |
| **Likes counter** | Eventual | Approximate count okay |
| **Follow relationship** | Strong | Prevent duplicate follows |

**Collaborative Editing**:

| Operation | Consistency Level | Reasoning |
|-----------|------------------|-----------|
| **Text edits** | Causal | Maintain edit order |
| **Cursor position** | Eventual | Slight delay okay |
| **Save document** | Strong | No data loss allowed |
| **Presence** | Eventual | "User typing" can lag |

---

## Consistency in Practice

### Popular Database Consistency Models

**PostgreSQL** (Single-node):
- **Default**: Serializable (single node)
- Multi-node (with replication): Tunable (async/sync replication)

**MySQL** (Single-node):
- **Default**: Serializable (single node)
- InnoDB: Repeatable Read with gap locking
- Multi-node: Various (depends on setup)

**MongoDB**:
- **Default**: Eventual consistency (async replication)
- **With Read Concern "majority"**: Linearizable
- **Causal Consistency**: Available in sessions

**Cassandra**:
- **Default**: Eventual (ONE/ONE)
- **Tunable**: QUORUM/QUORUM for strong consistency
- **Lightweight Transactions**: Linearizable (Paxos-based)

**DynamoDB**:
- **Default**: Eventual consistency
- **Optional**: Strong consistency per-read
- **Transactions**: Serializable

**Redis**:
- **Single-node**: Strong consistency
- **Cluster mode**: Eventual consistency
- **Sentinel**: Promotes new master (brief inconsistency)

**Kafka**:
- **Within partition**: Ordered (sequential consistency)
- **Across partitions**: No ordering guarantee
- **With transactions**: Exactly-once semantics

**Cosmos DB**:
- **Five levels**: Strong, Bounded staleness, Session, Consistent prefix, Eventual
- Tunable per-operation
- Clear latency/availability tradeoffs

### Implementing Strong Consistency

**Approaches**:

**1. Single Leader (Master)**:
```
All writes → Single master
Replicas follow master
Simple but single point of failure
```

**2. Consensus Protocols (Raft, Paxos)**:
```
Majority agreement required
Tolerates failures
Higher latency (coordination)
Examples: etcd, Consul, Spanner
```

**3. Two-Phase Commit (2PC)**:
```
Coordinator asks: "Ready to commit?"
All participants: "Yes" or "No"
Coordinator: "Commit" or "Abort"
Blocking if coordinator fails
```

**4. Two-Phase Locking (2PL)**:
```
Acquire locks before accessing data
Hold locks until transaction completes
Prevents conflicts
Risk of deadlocks
```

---

## Common Pitfalls and Misconceptions

### Misconception 1: "NoSQL = Eventual Consistency"

**Reality**: Many NoSQL databases offer tunable or strong consistency.
- MongoDB: Linearizable with proper configuration
- Cassandra: Strong consistency with QUORUM
- DynamoDB: Strongly consistent reads available

### Misconception 2: "Strong Consistency = Always Slower"

**Reality**: Depends on access patterns and locality.
- Local strong consistency can be fast
- Global eventual consistency can be slow
- Network latency matters more than consistency model sometimes

### Misconception 3: "My Database is Consistent, So My App Is"

**Reality**: Application logic can violate consistency.
```
Example:
Database: Linearizable
Application:
  1. Read user balance: $100
  2. Do business logic (5 seconds)
  3. Write balance - $50: $50

Problem: Balance could change between read and write!
Solution: Use transactions or optimistic locking
```

### Misconception 4: "CAP Theorem Means Pick Two"

**Reality**: It's not a binary choice.
- You MUST have partition tolerance (P)
- Choice is between C and A *during partitions only*
- When network is healthy, you can have all three
- Consistency/availability is a spectrum, not binary

### Misconception 5: "Eventual Consistency Means Always Fast"

**Reality**: Poor conflict resolution can make it slower.
- Frequent conflicts require resolution
- Complex CRDTs have overhead
- Some operations may need coordination anyway

---

## Testing Consistency

### How to Test Your Consistency Model

**1. Jepsen Testing**:
```
Jepsen is a framework for testing distributed systems
- Introduces network partitions
- Checks for consistency violations
- Famous for finding bugs in databases
```

**2. Consistency Checker**:
```
Write known sequence of operations
Read from multiple replicas
Check if reads violate consistency guarantees
```

**3. Chaos Engineering**:
```
Kill random nodes
Partition network
Delay messages
Verify system maintains consistency guarantees
```

**4. Audit Logs**:
```
Log all operations with timestamps
Replay and verify ordering
Check for causality violations
```

---

## Best Practices

### 1. Choose the Right Consistency for Each Operation

Don't use one-size-fits-all. Different operations have different requirements.

```
Shopping Cart:
- Add item: Read-your-writes (user sees addition)
- View cart: Eventual (slight delay okay)
- Checkout: Strong (must be accurate)
```

### 2. Design for Eventual Consistency When Possible

Even if your database supports strong consistency, eventual consistency scales better.

**Techniques**:
- Idempotent operations (safe to retry)
- Commutative operations (order doesn't matter)
- CRDTs for automatic merging
- Application-level conflict resolution

### 3. Use Transactions Sparingly

Transactions are powerful but expensive. Use only when necessary.

**When transactions are worth it**:
- Financial operations
- Inventory updates
- Multi-step operations that must succeed/fail together

**Alternatives**:
- Compensating transactions (saga pattern)
- Event sourcing
- Optimistic concurrency control

### 4. Monitor Replication Lag

For eventual consistency, know how "eventual" it is.

**Metrics to track**:
- Replication lag (time between write and replica update)
- Staleness of reads
- Conflict rate
- Failed conflict resolutions

### 5. Document Your Consistency Model

Make it explicit what guarantees your system provides.

**In documentation**:
- Consistency model per operation
- Expected lag times
- Conflict resolution strategy
- What happens during partitions

---

## Emerging Trends

### 1. Deterministic Databases

**Concept**: Pre-determine transaction order before execution
- Eliminates coordination overhead
- Strong consistency with better performance
- Example: Calvin protocol

### 2. Geo-Distributed Consistency

**Spanner-style systems**:
- Global strong consistency
- Uses atomic clocks (TrueTime)
- Expensive but powerful

### 3. Hybrid Consistency

**Combining models**:
- Strong consistency for critical data
- Eventual for everything else
- Automatic tier selection

### 4. Application-Aware Consistency

**Database knows application semantics**:
- Automatically choose consistency level
- Based on operation type
- Optimize for common patterns

---

## Conclusion

**Key Takeaways**:

1. **There is no perfect consistency model** — only tradeoffs between correctness, performance, and availability

2. **Stronger consistency = higher latency** — coordination takes time

3. **CAP theorem is real** — you can't have perfect consistency and availability during network partitions

4. **Choose per-operation** — different operations need different guarantees

5. **Eventual consistency is hard** — conflicts and stale data require careful handling

6. **Test your assumptions** — consistency bugs are subtle and dangerous

**Practical Guidance**:

- **Start with the strongest consistency you can afford**, then weaken only where necessary
- **Measure replication lag and staleness** in eventual systems
- **Use transactions for critical operations**, even if expensive
- **Design for idempotency** to handle retries safely
- **Test with network failures** to verify behavior during partitions

**Remember**:
- Consistency models are about guarantees, not implementations
- The right model depends on your specific use case
- Stronger isn't always better — it's about matching guarantees to requirements
- Document and communicate your consistency choices to your team

The goal is not to achieve the strongest consistency possible, but to provide the right guarantees for your application while maintaining acceptable performance and availability.