# MongoDB Interview Notes — Complete Reference

---

## 1. Fundamentals

### What is MongoDB?
A NoSQL, document-oriented database that stores data in **BSON** (Binary JSON) format.

**Key features:** Schema-less, horizontal scaling (sharding), high availability (replica sets), rich query language, GridFS for large files, aggregation pipeline.

### MongoDB vs Relational Databases

| MongoDB | Relational DB (MySQL) |
|---|---|
| Document-based (NoSQL) | Table-based (SQL) |
| Dynamic schema | Fixed schema |
| Collections & documents | Tables & rows |
| Embedded docs / arrays | Foreign keys & joins |
| Horizontal scaling (sharding) | Primarily vertical scaling |
| Configurable consistency | Strict ACID |

### Data Structure
- **Database** → **Collection** → **Document** → **Fields**
- Document = BSON record, max **16MB**, has unique `_id`
- `_id` is auto-generated ObjectId (12 bytes: timestamp + machine + process + counter), immutable, auto-indexed

### BSON vs JSON
BSON extends JSON with extra types (Date, ObjectId, Binary, Decimal128) and stores them in binary format for efficiency.

### Default Ports
- `27017` — mongod / mongos
- `27018` — sharded query routers
- `27019` — config servers

---

## 2. CRUD Operations

### Insert
```javascript
db.users.insertOne({ name: "Alice", age: 25 })

db.users.insertMany([
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 35 }
], { ordered: false })  // ordered: false → continues past errors
```

**`insertOne` vs `insertMany`:** `insertMany` is more efficient for bulk inserts; supports `ordered`/`unordered` execution.

### Read
```javascript
db.users.find({ age: { $gt: 25 } })                         // cursor
db.users.find({}, { name: 1, age: 1, _id: 0 })              // projection
db.users.findOne({ name: "Alice" })                          // single doc or null
db.users.find().sort({ age: -1 }).limit(10).skip(20)        // chaining
```

**`find()` vs `findOne()`:**

| find() | findOne() |
|---|---|
| Returns cursor | Returns document directly |
| Multiple results | First match only |
| Returns empty cursor if no match | Returns `null` if no match |

### Update
```javascript
db.users.updateOne({ name: "Alice" }, { $set: { age: 26 } })
db.users.updateMany({ age: { $lt: 25 } }, { $inc: { age: 1 } })
db.users.replaceOne({ name: "Bob" }, { name: "Bob", age: 31 })
```

**Field Update Operators:**

| Operator | Description |
|---|---|
| `$set` | Set field value |
| `$unset` | Remove field |
| `$inc` | Increment value |
| `$mul` | Multiply value |
| `$rename` | Rename field |
| `$min` / `$max` | Update only if new value is lower/higher |
| `$currentDate` | Set to current date |

**Array Update Operators:**

| Operator | Description |
|---|---|
| `$push` | Add element to array |
| `$addToSet` | Add only if not duplicate |
| `$pop` | Remove first (`-1`) or last (`1`) element |
| `$pull` | Remove elements matching condition |
| `$pullAll` | Remove all specified values |
| `$each` | Add multiple values with `$push`/`$addToSet` |
| `$slice` | Limit array size after push |
| `$position` | Insert at specific position |

**Array Filters (advanced):**
```javascript
db.students.updateOne(
  { _id: 1 },
  { $set: { "grades.$[elem].score": 95 } },
  { arrayFilters: [{ "elem.subject": "math" }] }
)
```

### Delete
```javascript
db.users.deleteOne({ name: "Alice" })
db.users.deleteMany({ age: { $lt: 18 } })
db.users.deleteMany({})   // delete all docs (collection stays)
db.users.drop()           // drop collection entirely
```

### Bulk Operations
```javascript
db.users.bulkWrite([
  { insertOne: { document: { name: "Alice" } } },
  { updateOne: { filter: { name: "Bob" }, update: { $set: { age: 30 } } } },
  { deleteOne: { filter: { name: "Charlie" } } },
  { replaceOne: { filter: { name: "Dave" }, replacement: { name: "David" } } }
], { ordered: false })
```

**`updateMany`/`deleteMany` vs `bulkWrite`:** `bulkWrite` can mix operation types and is more efficient for complex batches.

### Ordered vs Unordered Inserts (⭐ Interview Favourite)
- **Ordered (default):** Stops at first error; docs before error are saved, after are not.
- **Unordered** (`{ordered: false}`): All docs attempted; multiple errors can occur; partial success.
- **No automatic rollback** in either case.

### Pagination
```javascript
// Method 1: skip + limit (simple but slow on large offsets)
db.users.find().skip((page - 1) * pageSize).limit(pageSize)

// Method 2: Range query (efficient for large datasets)
db.users.find({ _id: { $gt: lastId } }).sort({ _id: 1 }).limit(pageSize)
```

---

## 3. Query Operators Cheat Sheet

```javascript
// Comparison
{ age: { $gt: 25, $lte: 50 } }
{ category: { $in: ["News", "Tech"] } }
{ category: { $nin: ["News", "Tech"] } }
{ status: { $ne: "inactive" } }

// Logical
{ $and: [{ age: { $gt: 25 } }, { city: "Delhi" }] }
{ $or:  [{ city: "Delhi" }, { city: "Mumbai" }] }
{ $nor: [{ city: "Delhi" }, { city: "Mumbai" }] }
{ views: { $not: { $lte: 100 } } }

// Element
{ phone: { $exists: true } }
{ age: { $type: "int" } }

// Array
{ tags: { $elemMatch: { $eq: "mongodb" } } }
{ tags: { $size: 3 } }
{ tags: { $all: ["mongodb", "database"] } }
```

---

## 4. Indexing

### Why Indexes?
Speed up queries by avoiding full collection scans (COLLSCAN → IXSCAN).
**Trade-off:** Improve reads, slow down writes (indexes updated on every write).

### Index Types
```javascript
db.users.createIndex({ email: 1 })                        // Single field
db.users.createIndex({ status: 1, age: -1 })              // Compound
db.users.createIndex({ email: 1 }, { unique: true })      // Unique
db.users.createIndex({ content: "text" })                 // Text
db.users.createIndex({ location: "2dsphere" })            // Geospatial
db.users.createIndex({ userId: "hashed" })                // Hashed (sharding)
db.users.createIndex({ email: 1 }, { sparse: true })      // Sparse (skips nulls)
db.users.createIndex({ age: 1 }, { partialFilterExpression: { status: "active" } }) // Partial
db.logs.createIndex({ createdAt: 1 }, { expireAfterSeconds: 2592000 })              // TTL
```

### Compound Index — ESR Rule (⭐ Key Concept)
Order fields as: **Equality → Sort → Range**
```javascript
// Query: { status: "active", age: { $gt: 25 } }.sort({ name: 1 })
db.users.createIndex({ status: 1, name: 1, age: 1 })
//                      Equality   Sort     Range
```

### Covered Query (⭐ Interview Favourite)
A query satisfied entirely from the index — **no document fetch needed**.
```javascript
db.users.createIndex({ name: 1, age: 1 })
db.users.find({ name: "Alice" }, { name: 1, age: 1, _id: 0 })
// Verify: explain() should show totalDocsExamined: 0
```

### explain() Method
```javascript
db.users.find({ age: { $gt: 25 } }).explain("executionStats")
```
- **COLLSCAN** = bad (no index used)
- **IXSCAN** = good (index used)
- Key metrics: `executionTimeMillis`, `totalDocsExamined`, `totalKeysExamined`, `nReturned`
- Efficient ratio: `docsExamined / nReturned` should be close to 1

### Index Management
```javascript
db.users.getIndexes()
db.users.dropIndex("email_1")
db.users.totalIndexSize()
```

**When NOT to index:** High write-to-read ratio, low cardinality fields (e.g., boolean), small collections, memory-constrained environments.

---

## 5. Aggregation Pipeline

### Concept
Documents pass through multiple stages sequentially. Each stage transforms the data.

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },         // Filter (use early — can use indexes)
  { $group: {
      _id: "$customerId",
      totalAmount: { $sum: "$amount" },
      orderCount: { $sum: 1 }
  }},
  { $sort: { totalAmount: -1 } },
  { $limit: 10 }
])
```

### Common Stages

| Stage | Purpose |
|---|---|
| `$match` | Filter documents (like WHERE) |
| `$group` | Group + aggregate (like GROUP BY) |
| `$project` | Reshape / select fields |
| `$sort` | Order results |
| `$limit` / `$skip` | Pagination |
| `$unwind` | Deconstruct arrays → one doc per element |
| `$lookup` | Left outer join with another collection |
| `$addFields` | Add computed fields |
| `$count` | Count documents |
| `$facet` | Run multiple pipelines in parallel |
| `$bucket` | Categorise into ranges |
| `$graphLookup` | Recursive tree/graph traversal |
| `$merge` / `$out` | Write results to a collection |
| `$setWindowFields` | Window functions (analytics) |

### $group Accumulators
```javascript
{ $group: {
  _id: "$category",
  total:    { $sum: "$price" },
  average:  { $avg: "$price" },
  highest:  { $max: "$price" },
  lowest:   { $min: "$price" },
  count:    { $sum: 1 },
  allItems: { $push: "$name" },
  uniqueItems: { $addToSet: "$name" }
}}
```

### $lookup (Join)
```javascript
db.orders.aggregate([
  { $lookup: {
    from: "customers",
    localField: "customerId",
    foreignField: "_id",
    as: "customerDetails"
  }},
  { $unwind: "$customerDetails" }   // flatten the array result
])
```

### $facet (Multiple Pipelines at Once)
```javascript
db.products.aggregate([
  { $facet: {
    "priceStats": [
      { $group: { _id: null, avg: { $avg: "$price" }, count: { $sum: 1 } } }
    ],
    "byCategory": [
      { $group: { _id: "$category", count: { $sum: 1 } } },
      { $sort: { count: -1 } }
    ],
    "paginatedData": [
      { $skip: 0 }, { $limit: 20 }
    ]
  }}
])
```
> **Use case:** Dashboard queries, pagination with total count in one round-trip.

### $bucket
```javascript
db.users.aggregate([
  { $bucket: {
    groupBy: "$age",
    boundaries: [0, 18, 25, 35, 50, 65, 100],
    default: "Other",
    output: { count: { $sum: 1 }, avgAge: { $avg: "$age" } }
  }}
])
```

### $graphLookup (Recursive Traversal)
```javascript
// Org chart — find all subordinates
db.employees.aggregate([
  { $match: { name: "CEO" } },
  { $graphLookup: {
    from: "employees",
    startWith: "$_id",
    connectFromField: "_id",
    connectToField: "managerId",
    as: "subordinates",
    maxDepth: 3,
    depthField: "level"
  }}
])
```
> **Use cases:** Org hierarchies, social networks (friends of friends), category trees, bill of materials.

### $merge (Write Results to Collection)
```javascript
db.orders.aggregate([
  { $group: { _id: "$customerId", totalSpent: { $sum: "$amount" } } },
  { $merge: {
    into: "customerStats",
    on: "_id",
    whenMatched: "merge",      // merge | replace | keepExisting | pipeline
    whenNotMatched: "insert"
  }}
])
```
> **`$merge` vs `$out`:** `$merge` can update existing docs; `$out` replaces the entire collection.

### Pipeline Optimisation Tips
1. Put `$match` as early as possible (uses indexes)
2. Put `$project` early to reduce document size
3. Use `$limit` before `$lookup` when possible
4. Index the `foreignField` in `$lookup`
5. Use `allowDiskUse: true` for pipelines > 100MB memory

---

## 6. Schema Design

### Embed vs Reference

| Factor | Embed | Reference |
|---|---|---|
| Relationship size | One-to-few | One-to-many / Many-to-many |
| Access pattern | Data read together | Data read independently |
| Update frequency | Rare | Frequent |
| Atomicity needed | Yes | No (or use transactions) |

### One-to-Many Patterns
```javascript
// 1. Embed (few related items, accessed together)
{ _id: 1, name: "User", addresses: [{city: "NYC"}, {city: "LA"}] }

// 2. Child references parent (many items, queried independently)
{ _id: 101, category_id: 1, name: "Product" }

// 3. Parent references children (moderate count, two-way navigation)
{ _id: 1, name: "Author", book_ids: [101, 102, 103] }
```

### Important Schema Patterns

**Bucket Pattern** — group time-series data into fixed-size buckets:
```javascript
{ sensorId: "s1", bucket: ISODate("2025-01-01T10:00:00Z"),
  readings: [{time: 0, temp: 22.5}, {time: 60, temp: 22.6}],
  stats: { avg: 22.55, min: 22.5, max: 22.6 } }
```

**Subset Pattern** — embed the most-accessed subset, reference the rest:
```javascript
// Products collection (embed top 3 reviews only)
{ _id: "p1", name: "Laptop", featuredReviews: [...3 reviews...], totalReviews: 15000 }
// Full reviews in separate collection
```

**Computed Pattern** — pre-calculate expensive aggregations and store the result.

**Outlier Pattern** — handle exceptional cases separately (e.g., a celebrity with millions of friends).

### Time-Series Collections (MongoDB 5.0+)
```javascript
db.createCollection("sensorData", {
  timeseries: {
    timeField: "timestamp",
    metaField: "metadata",
    granularity: "minutes"
  }
})
// ~90% storage reduction vs regular collections
```

### Schema Versioning
```javascript
// Add version field to every document
{ schemaVersion: 2, email: "...", profile: { firstName: "...", lastName: "..." } }

// Migrate lazily on read
if (!user.schemaVersion || user.schemaVersion < 2) {
  user = await migrateToV2(user)
}
```

---

## 7. Replication

### Replica Set
A group of mongod instances maintaining the same dataset.

**Components:**
- **Primary** — accepts all writes, records ops to oplog
- **Secondary** — replicates from primary's oplog (async); can serve reads
- **Arbiter** — votes in elections only, stores no data
- **Hidden member** — invisible to app, used for backups
- **Delayed member** — maintains historical snapshot (human error protection)

**Minimum:** 3 members (or 2 + 1 arbiter) for automatic failover.

### Automatic Failover Process
1. Members send heartbeats every 2 seconds
2. If primary unresponsive for 10s → election triggered
3. Secondary with highest priority + most recent data wins
4. Election completes in ~7–12 seconds
5. Old primary rejoins as secondary; uncommitted writes are rolled back to rollback files

### oplog (Operations Log)
- Capped collection at `local.oplog.rs`
- Records all write operations (insert/update/delete/command)
- Secondaries tail the oplog to replicate changes
- Enables point-in-time recovery

```javascript
rs.status()                    // check replica set status
rs.printSecondaryReplicationInfo()  // check replication lag
db.getReplicationInfo()        // oplog window info
```

### Write Concern
```javascript
db.collection.insertOne({ data: "important" }, {
  writeConcern: { w: "majority", j: true, wtimeout: 5000 }
})
// w: 0 = no ack, w: 1 = primary only, w: "majority" = majority of replica set
// j: true = wait for journal write
```

### Read Preferences

| Mode | Behaviour |
|---|---|
| `primary` | Always read from primary |
| `primaryPreferred` | Primary first, fallback to secondary |
| `secondary` | Always secondary |
| `secondaryPreferred` | Secondary first, fallback to primary |
| `nearest` | Lowest network latency |

---

## 8. Sharding

### What & When
Horizontal scaling — distributes data across multiple servers (shards).
**Use when:** Data > single server capacity, write throughput too high, geographic distribution needed, working set > RAM.

### Components
- **Shards** — store data subsets (each is a replica set)
- **mongos** — query router; app connects here; stateless; merges results from multiple shards
- **Config Servers** — store cluster metadata and chunk mappings (CSRS)

### Shard Key Selection (⭐ Critical)
Good shard key = **high cardinality + low frequency + non-monotonic**

```javascript
// BAD — monotonically increasing → hot shard
{ _id: ObjectId() }  // always writes to last chunk
{ timestamp: 1 }

// GOOD — hashed for even distribution
db.users.createIndex({ userId: "hashed" })
sh.shardCollection("mydb.users", { userId: "hashed" })

// GOOD — compound for range queries
sh.shardCollection("mydb.events", { userId: 1, timestamp: 1 })
```

**Enable sharding:**
```javascript
sh.enableSharding("myDatabase")
sh.shardCollection("myDatabase.myCollection", { userId: "hashed" })
sh.status()
```

### Chunk Migration
MongoDB balancer automatically moves chunks between shards for even distribution.
```javascript
sh.getBalancerState()
sh.stopBalancer()   // disable during maintenance
sh.startBalancer()
// Schedule window
db.settings.updateOne({ _id: "balancer" }, { $set: { activeWindow: { start: "23:00", stop: "06:00" } } }, { upsert: true })
```

---

## 9. Transactions

### Multi-Document ACID Transactions (MongoDB 4.0+)
```javascript
const session = client.startSession()
session.startTransaction({
  readConcern: { level: "snapshot" },
  writeConcern: { w: "majority" }
})

try {
  await accounts.updateOne({ _id: "A" }, { $inc: { balance: -100 } }, { session })
  await accounts.updateOne({ _id: "B" }, { $inc: { balance: 100 } }, { session })
  await session.commitTransaction()
} catch (error) {
  await session.abortTransaction()
  throw error
} finally {
  await session.endSession()
}
```

### Transaction Limitations (⭐ Interview Favourite)
- 60-second default timeout
- 16MB oplog entry size limit per transaction
- Cannot use capped collections or system collections
- Higher performance overhead than single-document ops
- Write conflicts use first-write-wins → must implement retry logic

### ACID in MongoDB
- **Atomicity:** Single doc always atomic; multi-doc requires explicit transaction
- **Consistency:** Schema validation + write concerns
- **Isolation:** Snapshot isolation (MVCC) — transactions see consistent state from start time; no phantom reads
- **Durability:** Journal (WAL) + write concern `majority` + replication

### Optimistic Concurrency Control
```javascript
// Version-based approach
const result = await db.products.updateOne(
  { _id: "p1", version: currentVersion },   // check version hasn't changed
  { $inc: { stock: -10 }, $set: { version: currentVersion + 1 } }
)
if (result.matchedCount === 0) {
  throw new Error("Write conflict — retry")
}
```

---

## 10. Storage Engine (WiredTiger)

### WiredTiger vs MMAPv1

| Feature | WiredTiger (default since 3.2) | MMAPv1 (removed 4.2) |
|---|---|---|
| Concurrency | Document-level locking | Collection-level locking |
| Compression | Yes (snappy default) | No |
| Performance | Better concurrent writes | Slower |
| Cache | Configurable (50% RAM - 1GB) | Uses all RAM |

### Journaling (Write-Ahead Log)
1. Write operation arrives
2. Logged to journal (group commit every 100ms)
3. Written to WiredTiger cache
4. Checkpoint flushes dirty pages to disk every 60s
5. On crash: MongoDB replays journal from last checkpoint

```yaml
storage:
  journal:
    enabled: true
    commitIntervalMs: 100
```

### Storage Compression
- **Collection data:** Snappy (default), zlib, zstd, none
- **Index compression:** Prefix compression (default)
- Configure per collection independently

---

## 11. Security

### Authentication Mechanisms

| Mechanism | Edition | Use Case |
|---|---|---|
| SCRAM-SHA-256 | Community | Default, username/password |
| x.509 | Community | Certificate-based, service accounts |
| LDAP | Enterprise | Central user management |
| Kerberos | Enterprise | Windows/AD environments |

```javascript
// Create user
use admin
db.createUser({
  user: "appUser",
  pwd: "securePassword",
  roles: [{ role: "readWrite", db: "myDatabase" }]
})
```

### Role-Based Access Control (RBAC)
**Built-in roles:** `read`, `readWrite`, `dbAdmin`, `userAdmin`, `clusterAdmin`, `root`

```javascript
// Custom role
db.createRole({
  role: "customRole",
  privileges: [{
    resource: { db: "myDB", collection: "orders" },
    actions: ["find", "insert", "update"]
  }],
  roles: []
})
```

### Encryption
- **At rest:** WiredTiger encryption (Enterprise); customer-managed keys via AWS KMS / Azure Key Vault / GCP KMS
- **In transit:** TLS/SSL (`requireTLS` mode)
- **Field-level:** Client-Side Field Level Encryption (CSFLE)
- **Queryable Encryption (MongoDB 7.0+):** Encrypt fields AND query them (equality, range)

```yaml
# TLS configuration
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### IP Whitelisting
```yaml
net:
  bindIp: 127.0.0.1,192.168.1.10   # Restrict to specific IPs
```
Or use OS firewall (`iptables`, `ufw`, AWS Security Groups).

### Audit Logging (Enterprise)
```yaml
auditLog:
  destination: file
  format: JSON
  path: /var/log/mongodb/audit.json
  filter: '{ "atype": { "$in": ["authenticate", "createUser", "dropUser"] } }'
```

---

## 12. Performance & Optimisation

### Diagnosing Slow Queries
```javascript
// 1. explain()
db.collection.find({...}).explain("executionStats")

// 2. Database profiler
db.setProfilingLevel(1, { slowms: 100 })   // log queries > 100ms
db.system.profile.find({ millis: { $gt: 100 } }).sort({ ts: -1 })

// 3. Current operations
db.currentOp({ active: true, secs_running: { $gte: 3 } })
db.killOp(opid)

// 4. Server stats
db.serverStatus()
db.collection.stats()
```

```bash
mongostat --host localhost:27017   # real-time ops/sec, connections, memory
mongotop 10                        # time per collection (read/write)
```

### Covered Query
All queried AND returned fields must be in the index. No document access needed → fastest possible query.

### Index Strategies
- Use `explain()` before adding indexes
- Follow ESR rule for compound indexes
- Remove unused indexes (`$indexStats`)
- Ensure indexes fit in RAM: `db.collection.totalIndexSize()`
- One compound index often beats multiple single-field indexes

### Write Concerns for Performance vs Durability

| Write Concern | Speed | Durability |
|---|---|---|
| `{w: 0}` | Fastest | None |
| `{w: 1}` | Fast | Primary only |
| `{w: 1, j: true}` | Medium | Primary + journal |
| `{w: "majority"}` | Slower | Majority of replica set |

---

## 13. GridFS

For files **larger than 16MB**:
- Splits files into 255KB chunks
- Two collections: `fs.files` (metadata) + `fs.chunks` (data)

```bash
mongofiles -d myDatabase put video.mp4    # upload
mongofiles -d myDatabase get video.mp4    # download
```

```python
import gridfs
from pymongo import MongoClient
fs = gridfs.GridFS(MongoClient().myDatabase)
file_id = fs.put(open('video.mp4', 'rb'), filename='video.mp4')
data = fs.get(file_id).read()
```

**Use when:** Files > 16MB, need partial reads, want files synced with DB.
**Don't use when:** Files < 16MB (use BinData), need high-performance streaming (use CDN/S3 with reference in MongoDB).

---

## 14. Change Streams

Real-time notification of data changes:
```javascript
const changeStream = db.collection.watch([
  { $match: { operationType: { $in: ["insert", "update"] } } }
])

changeStream.on("change", (change) => {
  console.log("Change:", change.operationType, change.documentKey)
})
```
- Resumable (use `resumeToken`)
- Can watch collection, database, or entire cluster
- Use cases: real-time notifications, cache invalidation, audit logging, event-driven architecture

---

## 15. Backup & Restore

### mongodump / mongorestore
```bash
# Backup
mongodump --db myDatabase --gzip --out /backup/

# Restore
mongorestore --db myDatabase --drop /backup/myDatabase/

# Restore specific collection
mongorestore --db myDatabase --collection users /backup/myDatabase/users.bson

# Point-in-time restore (with oplog)
mongodump --oplog --out /backup/
mongorestore --oplogReplay /backup/
```

### mongodump vs Oplog-Based Backups

| Feature | mongodump | Oplog-Based |
|---|---|---|
| Type | Logical snapshot | Continuous |
| Point-in-time recovery | No | Yes |
| Performance impact | Medium-High | Low |
| Transactional | No | Yes |
| Best for | Small DBs, selective backup | Large DBs, minimal downtime |

### mongoexport / mongoimport (for JSON/CSV)
```bash
# Export to CSV
mongoexport --db myDB --collection users --type=csv --fields=name,email --out users.csv

# Import from JSON with upsert
mongoimport --db myDB --collection users --mode=upsert --upsertFields=email --file users.json
```

---

## 16. MongoDB Atlas (Cloud)

**Atlas vs Ops Manager vs Enterprise Advanced:**

| | Atlas | Ops Manager | Enterprise Advanced |
|---|---|---|---|
| Hosting | Fully managed cloud | Self-hosted | Self-hosted |
| Scaling | Auto | Manual | Manual |
| Backups | Automated (PITR) | Manual/Auto | Manual |
| Best For | Simplicity | On-prem + tooling | Full control |

### Key Atlas Features
- Auto-scaling (compute + storage)
- Continuous backups with point-in-time recovery
- Atlas Search (Apache Lucene-powered, supports fuzzy, facets, autocomplete)
- Atlas Data Federation (query across Atlas + S3)
- Change Streams triggers / Atlas App Services

**Atlas Search vs Regular Text Index:**

| | Text Index | Atlas Search |
|---|---|---|
| Fuzzy matching | No | Yes |
| Faceting | No | Yes |
| Autocomplete | No | Yes |
| Language support | Limited | 40+ languages |
| Scoring | Basic | Advanced (Lucene) |

---

## 17. Monitoring

### Key Metrics to Track

| Category | Metrics |
|---|---|
| Performance | Query latency (P95/P99), ops/sec |
| Resources | CPU %, RAM/cache usage, disk I/O |
| Connections | Current vs available (alert > 80%) |
| Replication | Lag in seconds (alert > 10s) |
| Locks | Queue depth for readers/writers |

### Alert Thresholds (Recommended)
- **Critical:** Primary unavailable, replication lag > 60s, connection usage > 90%
- **Warning:** Replication lag > 10s, cache usage > 80%, slow queries P95 > 1000ms

### Prometheus + Grafana Integration
```bash
# Install percona/mongodb_exporter
docker run -d -p 9216:9216 percona/mongodb_exporter \
  --mongodb.uri=mongodb://monitoring_user:pass@mongodb:27017

# Add to prometheus.yml
scrape_configs:
  - job_name: 'mongodb'
    static_configs:
      - targets: ['localhost:9216']
```
Import Grafana dashboard ID **2583** (MongoDB Exporter).

---

## 18. Deployment Automation

### Terraform (Atlas)
```hcl
resource "mongodbatlas_cluster" "cluster" {
  project_id                  = mongodbatlas_project.project.id
  name                        = "prod-cluster"
  provider_name               = "AWS"
  provider_region_name        = "US_EAST_1"
  provider_instance_size_name = "M10"
  auto_scaling_disk_gb_enabled = true
  backup_enabled              = true
  pit_enabled                 = true
}
```

### Ansible (Self-Hosted)
```yaml
- name: Install MongoDB
  apt: { name: mongodb-org, state: present }
- name: Configure replica set
  template: { src: mongod.conf.j2, dest: /etc/mongod.conf }
- name: Start service
  systemd: { name: mongod, state: started, enabled: yes }
```

---

## 19. Real-World Design Examples

### E-commerce Schema Design Principles
- **Users:** Embed addresses (few, accessed with user); reference orders
- **Products:** Embed images and review summary (denormalised avg rating for performance); reference full reviews
- **Orders:** Embed item snapshot (historical record — product name/price at order time); reference user
- **Cart:** TTL index to auto-expire after 30 days

```javascript
// Inventory update with transaction (prevent overselling)
session.startTransaction()
const result = await products.updateOne(
  { _id: productId, "inventory.available": { $gte: qty } },
  { $inc: { "inventory.reserved": qty, "inventory.available": -qty } },
  { session }
)
if (result.matchedCount === 0) throw new Error("Out of stock")
await orders.insertOne({ items, status: "pending" }, { session })
await session.commitTransaction()
```

### Log / IoT Data Design
- Use **Time-Series Collections** (MongoDB 5.0+) for automatic bucketing + 90% storage reduction
- Use **TTL index** for auto-deletion: `{ expireAfterSeconds: 2592000 }`
- Use **Bucket Pattern** for pre-aggregated stats per time window
- Pre-compute aggregations into a summary collection using `$merge`

---

## 20. Troubleshooting Reference

### Slow Query Checklist
1. Run `explain("executionStats")` — look for COLLSCAN
2. Check `totalDocsExamined / nReturned` ratio (should be ≈ 1)
3. Create or refine indexes (follow ESR rule)
4. Add projection to reduce data transfer
5. Check profiler: `db.system.profile.find({ millis: { $gt: 100 } })`
6. Check `db.currentOp()` for blocking operations
7. Consider schema changes (denormalise frequently accessed data)

### E11000 Duplicate Key Error
- Cause: Insert violates unique index constraint
- Fix: Check for duplicate values, use `upsert: true`, or `ordered: false` in bulk ops

### MongoDB Won't Start
1. Check logs: `/var/log/mongodb/mongod.log`
2. Verify port 27017 not in use
3. Check disk space
4. Check permissions on data directory
5. Remove stale lock file: `mongod.lock`
6. Repair: `mongod --repair`

### High Replication Lag
- Causes: Network issues, high write load, underpowered secondary, large transactions, index builds
- Fix: Check `rs.printSecondaryReplicationInfo()`, increase oplog size, scale secondaries

---

## 21. Quick Reference — Shell Commands

```javascript
// Database
show dbs | use myDB | db | db.dropDatabase()

// Collections
show collections | db.createCollection("name") | db.collection.drop()
db.collection.stats() | db.collection.countDocuments()

// Indexes
db.collection.createIndex({ field: 1 })
db.collection.getIndexes()
db.collection.dropIndex("field_1")
db.collection.explain("executionStats").find({...})

// Replica Set
rs.status() | rs.initiate() | rs.add("host:27017")
rs.stepDown() | rs.printSecondaryReplicationInfo()

// Sharding
sh.status() | sh.enableSharding("db")
sh.shardCollection("db.col", { key: 1 })
sh.getBalancerState() | sh.stopBalancer()

// Admin
db.serverStatus() | db.currentOp() | db.killOp(opid)
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find().sort({ ts: -1 }).limit(5)
```

---

## 22. Compliance Certifications

MongoDB Atlas supports: **SOC 2 Type II, ISO 27001, PCI DSS, HIPAA (with BAA), GDPR, FedRAMP (GovCloud)**.

Key compliance features: encryption at rest/in transit, field-level encryption, RBAC, audit logging, network isolation, data residency controls, PITR backups.

---

*This reference covers ~95% of MongoDB interview topics for 1–5 years of experience. Focus especially on: indexing (ESR, covered queries, explain()), aggregation pipeline, replica sets, sharding shard key selection, transactions (ACID + limitations), and schema design patterns.*