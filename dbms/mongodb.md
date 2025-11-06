update
lookup unwind
what is ordered/unordered insert
bulk & many in detail

# Mongodb fundamentals
1. what is mongodb and what are its main features ?
2. How does mongodb differ from relational databases ?
3. can you describe structure of data in mongodb ?
4. What is a document in mongodb ?
5. How data are stored in collections in mongodb ?
6. Describe what mongodb database is ?
7. what is default port on which mongodb listen ?
8. how does mongodb provides high availability and disaster recovery ?
9. what are index in mongodb  why they are used ?
10. what is the role of id in mongodb document ?
# Crud operations
11. how do you create a new mongodb collection ?
12. what is the syntax to insert a new document in mongodb ?
13. How do you read data from a mongodb collection ?
14. Explain how to update data in mongodb ?
15. what are mongodb commands to delete documents ?
16. can you join 2 collections in mongodb ? if yes how ?
17. How can you limit the number of documents return by mongodb query ?
18. what is the difference between find and findone in mongodb ?
19. How can you achieve pagination in mongodb ?
20. what is the difference between insertOne and insertMany method in mongodb ?
21. What happens when a bulk or insert/delete/update operation failes in middle of operation ?
22. what is the difference between updateMany/deleteMany and bulk operation ?
# Indexing and aggregation
23.  describe compound indexing in mongodb ?
24.  what is aggregation pipeline in mongodb ?
25.  How can you create an index in mongodb and when should do it ?
26.  Explain how match group and sort operation works in aggregation pipeline ?
27.  What is the purpose of Explain method ?
# Replivcation and sharding 
28.  Can you explain replication in mongodb ?
29.  Explain purpose and components of replica set ?
30.  What is sharding in mongodb and it should be used ?
31.  How does mongodb perform automatic failover ?
32.  Explaine the difference between horizontal and vertocal scalling and how mongodb support that?
# Performance and Optimization
33.  How mongodb handles large data volume ?
34.  What techniques you use dignose and addres performance inssue in mongodb ?
34.  How do you ensure indexes fit into ram ?
35.  can you explain mongodb write concerns ?
36.  what is covered query in mongodb ?
# Mongodb security
37.  what are the security features available in mongodb ?
38.  How do you enable authentication in mongodb ?
39.  Explain role based access controll in mongodb ?
40.  Explain how to encrypt data in mongodb ?
41.  How do you setup mongodb to use tls/ssl connections ? 
# Mongodb storage engine
42.  What differnt starage engine are available in mongodb ?
43.  How does Wiredtriggerd storage engine is different from MMAPv1 ?
44.  Can you switch between storage engine in mongodb ?
# advance mongodb concepts
45.  What is oplog in mongodb and how it works ?
46.  How do you use lookup operation in mongodb ?
47.  explain the role of mongoes server in shareded mongodb architeture ?
48.  What is jornlling in monogdb why it is important ?
49.  Explain Gridfs specifications in mongodb ?
# Mongodb schema design
50.  How does schema design impacts performance in mongodb ?
51.  Compare embaded vs linking documents in mongodb ?
52.  What factors do you consider when designing schema in mongodb ?
53.  How do you handel one to many modeling in mongodb ?
# database management & maintainance
54.  How do you perform data backup in mongodb ?
55.  What techniques can be used to restore data in mongodb ?
56.  How do you monitor performance of mongodb instance ?
57.  What factors leads you to defregment mongodb collection ?
# working with datatypes
58.  What are the different datatype supported in mongodb ?
59.  how mongodb stores different types of numerical data ?
60.  How does mongodb handles date time data in mongodb ?
61.  Can you store multimedia files in mongodb ?
# Mongodb and programing
62.  How do you connect mongodb with python script ?
63.  what is monges and it is related to mongodb ?
64.  How do you create and you stored procedure in mongodb ?
65.  Describe how to use mongodb shell in mongodb ?
# Mongodb Drivers and ODMs
66.  What is the use of Mongodb ODM/ ORM frameworks ?
67.  how do you perform mongodb operation using nodejs ?
68.  list popular library to integrate with mongodb ?
# Mongodb and Bigdatq
69.  How mongodb is used in big data analytics ?
70.  can mongodb handles realtime data analytics workload ?
71.  How do you stream large quanities of data into and out in mongodb ?
# Mongodb internals
72.  How does mongodb handles locking and concurency ?
73.  What is the relationship between bson and mongodb ?
74.  Explain the concept of cursor in mongodb ?
75.  How does mongodb manges memory ?
# mongodb deployment
76.  What is the best practice for securing mongodb instance ?
77.  How do you scale a mongodb deployment ?
78.  what is Ops manager in mongodb ?
# Mongodb errors and troubleshoutings
79.  How do you troubleshoot a slow running query in mongodb ?
80.  What is the cause of mongodb server error E1100 duplicate key error ?
81.  How do you handle a senorio where mongodb service dont start ?
# mongodb in the clouds
82.  What are some mongodb cloud housted solutions ?
83.  How does mongodb atlas inhnce mongodb capability ?
# APi and tools
84.  Describe the use of atlas in mongodb ?
85.  Explaine the use of ROBO 3t ?
86.  Can you work with mongodb with command line if yes how ?
# Contemprary mongodb chalanges and considerations
87.  What factores to consider when deploying a containerise mongodb environment ?
88.  How does mongodb works with microservice artchiture ?
89.  What are the change streams in mongodb ?
# Mongodb updates and evolutions
89.  What are the major fetaure added in latest mongodb release ?
90.  How does mongodb handles version upgrade in production environment ?
# usecase for mongodb
91.  In what senorios mongodb is favrable over mysql ?
92.  What are some comman pattern of data access in applications of mongodb ?
# mongodb query optimizations
93.  How can you prevent slow query in mongodb ?
94.  Explaine the role of profiler in mongodb ?
95.  How b-tree index are implemented in mongodb ?
# advance query and data processing 
96.  How do you hanles complex transactions in mongodb ?
97.  Explaine the mongodb Mapreduce operation ?
98.  Can you perform text search in mongodb ?
# mongodb Integrations
99.   How can you integrate mongodb with 3rd party applications ?
100.   Describe how to synchronize data between mongodb and mysql ?
# MongoDB Interview Questions & Answers

## MongoDB Fundamentals

### 1. What is MongoDB and what are its main features?

MongoDB is a NoSQL document-oriented database that stores data in flexible, JSON-like documents. Main features include:

- **Document-Oriented Storage**: Data stored in BSON (Binary JSON) format
- **Schema Flexibility**: Dynamic schemas allow fields to vary between documents
- **Scalability**: Horizontal scaling through sharding
- **High Availability**: Replication with automatic failover
- **Rich Query Language**: Supports complex queries, aggregations, and indexing
- **High Performance**: In-memory processing and efficient indexing
- **GridFS**: For storing large files
- **Ad-hoc Queries**: Support for field, range, and regular expression searches

### 2. How does MongoDB differ from relational databases?

| MongoDB | Relational Databases |
|---------|---------------------|
| Document-based (NoSQL) | Table-based (SQL) |
| Dynamic schema | Fixed schema |
| Collections and documents | Tables and rows |
| Embedded documents and arrays | Foreign keys and joins |
| Horizontal scaling (sharding) | Primarily vertical scaling |
| Eventual consistency (configurable) | ACID transactions (strict) |
| Flexible data models | Normalized data models |

### 3. Can you describe the structure of data in MongoDB?

MongoDB organizes data in a hierarchical structure:

- **Database**: Top-level container for collections
- **Collection**: Group of MongoDB documents (analogous to tables)
- **Document**: A record in a collection, stored as BSON
- **Field**: Key-value pairs within a document
- **Embedded Documents**: Documents nested within documents
- **Arrays**: Ordered lists that can contain values or documents

### 4. What is a document in MongoDB?

A document is a basic unit of data in MongoDB, similar to a row in relational databases. It's a set of key-value pairs stored in BSON format. Documents have:

- Dynamic schemas (fields can vary)
- Maximum size of 16MB
- Unique `_id` field (auto-generated if not provided)
- Support for nested documents and arrays

Example:
```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  },
  "hobbies": ["reading", "coding"]
}
```

### 5. How are data stored in collections in MongoDB?

Collections store documents in MongoDB:

- Collections are schema-less (documents can have different structures)
- Created automatically when first document is inserted
- Documents in a collection are stored as BSON
- Collections are analogous to tables in RDBMS
- Each collection has indexes for efficient querying
- Collections are organized within databases
- No strict relationships enforced between collections

### 6. Describe what a MongoDB database is?

A MongoDB database is:

- A container for collections
- Each database has its own set of files on the filesystem
- A single MongoDB server can have multiple databases
- Default databases: `admin`, `local`, `config`
- Database names are case-sensitive
- Naming restrictions: cannot contain spaces, dots, or special characters
- Each database can have different access controls

### 7. What is the default port on which MongoDB listens?

MongoDB listens on **port 27017** by default. Other common ports:

- **27018**: For sharded cluster query routers (mongos)
- **27019**: For config servers
- The port can be changed using `--port` option or in configuration file

### 8. How does MongoDB provide high availability and disaster recovery?

MongoDB provides high availability through:

- **Replica Sets**: Multiple copies of data across different servers
- **Automatic Failover**: Primary election when primary node fails
- **Read Preferences**: Distribute read operations across replicas
- **Write Concerns**: Ensure data durability
- **Backups**: Regular backups using mongodump, filesystem snapshots, or Atlas backups
- **Oplog**: Operation log for replication and point-in-time recovery
- **Geographic Distribution**: Deploy replicas across data centers

### 9. What are indexes in MongoDB and why are they used?

Indexes are special data structures that improve query performance:

- **Purpose**: Speed up query execution by reducing document scanning
- **Types**: Single field, compound, multikey, text, geospatial, hashed
- **_id Index**: Automatically created on _id field
- **Trade-offs**: Improve read performance but slow down writes
- **Memory**: Indexes should fit in RAM for optimal performance
- **Creation**: Can be created in foreground or background

### 10. What is the role of _id in a MongoDB document?

The `_id` field:

- **Primary Key**: Unique identifier for each document
- **Automatic Generation**: MongoDB creates ObjectId if not provided
- **Immutable**: Cannot be changed after document creation
- **Indexed**: Automatically indexed for fast lookups
- **ObjectId**: 12-byte identifier (timestamp + machine + process + counter)
- **Custom Values**: Can be set to any unique value
- **Required**: Every document must have an _id field

## CRUD Operations

### 11. How do you create a new MongoDB collection?

Collections can be created explicitly or implicitly:

**Implicit Creation** (automatic on first insert):
```javascript
db.myCollection.insertOne({name: "John"})
```

**Explicit Creation**:
```javascript
db.createCollection("myCollection", {
  capped: true,
  size: 5242880,
  max: 5000
})
```

Options include validation rules, capped collections, and storage engine configuration.

### 12. What is the syntax to insert a new document in MongoDB?

**Insert One Document**:
```javascript
db.collection.insertOne({
  name: "Alice",
  age: 25,
  email: "alice@example.com"
})
```

**Insert Multiple Documents**:
```javascript
db.collection.insertMany([
  {name: "Bob", age: 30},
  {name: "Charlie", age: 35}
])
```

**Legacy Insert** (deprecated):
```javascript
db.collection.insert({name: "Dave"})
```

### 13. How do you read data from a MongoDB collection?

**Find All Documents**:
```javascript
db.collection.find()
```

**Find with Query**:
```javascript
db.collection.find({age: {$gt: 25}})
```

**Find with Projection**:
```javascript
db.collection.find({}, {name: 1, age: 1, _id: 0})
```

**Find One Document**:
```javascript
db.collection.findOne({name: "Alice"})
```

**With Sorting and Limiting**:
```javascript
db.collection.find().sort({age: -1}).limit(10)
```

### 14. Explain how to update data in MongoDB?

**Update One Document**:
```javascript
db.collection.updateOne(
  {name: "Alice"},
  {$set: {age: 26}}
)
```

**Update Multiple Documents**:
```javascript
db.collection.updateMany(
  {age: {$lt: 25}},
  {$inc: {age: 1}}
)
```

**Replace Document**:
```javascript
db.collection.replaceOne(
  {name: "Bob"},
  {name: "Bob", age: 31, email: "bob@example.com"}
)
```

**Update Operators**: `$set`, `$unset`, `$inc`, `$push`, `$pull`, `$addToSet`

### 15. What are MongoDB commands to delete documents?

**Delete One Document**:
```javascript
db.collection.deleteOne({name: "Alice"})
```

**Delete Multiple Documents**:
```javascript
db.collection.deleteMany({age: {$lt: 18}})
```

**Delete All Documents**:
```javascript
db.collection.deleteMany({})
```

**Remove Collection**:
```javascript
db.collection.drop()
```

### 16. Can you join 2 collections in MongoDB? If yes, how?

Yes, using the **$lookup** aggregation operator:

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "customer_details"
    }
  }
])
```

This performs a left outer join. MongoDB also supports:
- Multiple joins using multiple $lookup stages
- $unwind to flatten joined arrays
- Correlated subqueries with pipeline in $lookup

### 17. How can you limit the number of documents returned by a MongoDB query?

**Using limit()**:
```javascript
db.collection.find().limit(10)
```

**With skip() for pagination**:
```javascript
db.collection.find().skip(20).limit(10)
```

**In aggregation**:
```javascript
db.collection.aggregate([
  {$limit: 10}
])
```

### 18. What is the difference between find() and findOne() in MongoDB?

| find() | findOne() |
|--------|-----------|
| Returns a cursor to all matching documents | Returns a single document |
| Can return multiple documents | Returns only the first match |
| Requires iteration or methods like toArray() | Returns document object directly |
| Returns empty cursor if no match | Returns null if no match |
| Can be chained with limit(), sort() | No chaining needed for single doc |

### 19. How can you achieve pagination in MongoDB?

**Method 1: Skip and Limit**:
```javascript
// Page 1
db.collection.find().limit(10)

// Page 2
db.collection.find().skip(10).limit(10)

// Page n
db.collection.find().skip((pageNum - 1) * pageSize).limit(pageSize)
```

**Method 2: Range Queries** (more efficient for large datasets):
```javascript
// First page
db.collection.find().sort({_id: 1}).limit(10)

// Next page (using last _id from previous page)
db.collection.find({_id: {$gt: lastId}}).sort({_id: 1}).limit(10)
```

### 20. What is the difference between insertOne() and insertMany() methods in MongoDB?

| insertOne() | insertMany() |
|-------------|--------------|
| Inserts a single document | Inserts multiple documents |
| Accepts one document object | Accepts array of documents |
| Faster for single insertions | More efficient for bulk inserts |
| Returns single inserted ID | Returns array of inserted IDs |
| Simpler error handling | Can specify ordered/unordered inserts |

**Example**:
```javascript
// insertOne
db.collection.insertOne({name: "Alice"})

// insertMany
db.collection.insertMany([
  {name: "Bob"},
  {name: "Charlie"}
], {ordered: false})
```

### 21. What happens when a bulk or insert/delete/update operation fails in the middle of operation?

**Ordered Operations** (default):
- Stops at first error
- Documents before error are processed
- Documents after error are not processed
- Partial success possible

**Unordered Operations**:
```javascript
db.collection.insertMany([...], {ordered: false})
```
- Continues processing after errors
- All documents attempted
- Multiple errors can occur
- Returns all errors in result

**No automatic rollback** - successfully processed documents remain in the database.

### 22. What is the difference between updateMany/deleteMany and bulk operations?

**updateMany/deleteMany**:
- Single operation type per command
- Simple syntax for uniform updates/deletes
- All documents match same filter
- Less flexible

**Bulk Operations**:
```javascript
db.collection.bulkWrite([
  {insertOne: {document: {name: "Alice"}}},
  {updateOne: {filter: {name: "Bob"}, update: {$set: {age: 30}}}},
  {deleteOne: {filter: {name: "Charlie"}}},
  {replaceOne: {filter: {name: "Dave"}, replacement: {name: "David"}}}
], {ordered: false})
```
- Mix different operation types
- More flexible and efficient
- Better performance for complex operations
- Can specify ordered/unordered execution

## Indexing and Aggregation

### 23. Describe compound indexing in MongoDB?

A compound index includes multiple fields:

```javascript
db.collection.createIndex({field1: 1, field2: -1})
```

**Characteristics**:
- Order matters: {a: 1, b: 1} ≠ {b: 1, a: 1}
- Supports queries on prefix fields
- Can have up to 32 fields
- Direction (1 or -1) matters for sorting

**ESR Rule** (Equality, Sort, Range):
- Put equality filters first
- Sort fields next
- Range filters last

**Example**:
```javascript
// For query: {status: "active", age: {$gt: 25}}.sort({name: 1})
// Best index:
db.users.createIndex({status: 1, name: 1, age: 1})
```

### 24. What is aggregation pipeline in MongoDB?

The aggregation pipeline processes documents through multiple stages:

```javascript
db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {
    _id: "$customer_id",
    totalAmount: {$sum: "$amount"},
    orderCount: {$sum: 1}
  }},
  {$sort: {totalAmount: -1}},
  {$limit: 10}
])
```

**Common Stages**:
- `$match`: Filter documents
- `$group`: Group by field and perform aggregations
- `$project`: Reshape documents
- `$sort`: Order documents
- `$limit`/`$skip`: Pagination
- `$lookup`: Join collections
- `$unwind`: Deconstruct arrays
- `$addFields`: Add computed fields

### 25. How can you create an index in MongoDB and when should you do it?

**Create Index**:
```javascript
// Single field
db.collection.createIndex({fieldName: 1})

// Compound index
db.collection.createIndex({field1: 1, field2: -1})

// Unique index
db.collection.createIndex({email: 1}, {unique: true})

// Text index
db.collection.createIndex({content: "text"})

// Background index (non-blocking)
db.collection.createIndex({field: 1}, {background: true})
```

**When to Create Indexes**:
- Fields frequently used in queries
- Fields used in sort operations
- Fields used in $lookup joins
- High read-to-write ratio collections
- After analyzing query patterns with explain()
- Before bulk data operations

**Avoid indexing when**:
- High write-to-read ratio
- Fields with low cardinality
- Small collections
- Memory constraints

### 26. Explain how match, group, and sort operations work in aggregation pipeline?

**$match** - Filters documents:
```javascript
{$match: {
  status: "active",
  age: {$gte: 18}
}}
```
- Use early in pipeline for efficiency
- Can use indexes
- Similar to find() filter

**$group** - Groups and aggregates:
```javascript
{$group: {
  _id: "$category",
  total: {$sum: "$amount"},
  avg: {$avg: "$price"},
  count: {$sum: 1}
}}
```
- `_id` specifies grouping key
- Accumulator operators: $sum, $avg, $min, $max, $push, $addToSet

**$sort** - Orders documents:
```javascript
{$sort: {
  totalAmount: -1,  // descending
  name: 1           // ascending
}}
```
- 1 for ascending, -1 for descending
- Use indexes when possible
- Memory limit: 100MB (use $sort before $group when possible)

### 27. What is the purpose of explain() method?

The `explain()` method provides query execution information:

```javascript
db.collection.find({age: {$gt: 25}}).explain("executionStats")
```

**Verbosity Modes**:
- `"queryPlanner"`: Shows query plan only
- `"executionStats"`: Includes execution statistics
- `"allPlansExecution"`: Shows all candidate plans

**Key Metrics**:
- **executionTimeMillis**: Query execution time
- **totalDocsExamined**: Documents scanned
- **totalKeysExamined**: Index keys scanned
- **nReturned**: Documents returned
- **stage**: COLLSCAN (bad) vs IXSCAN (good)
- **indexName**: Which index was used

**Use Cases**:
- Identify slow queries
- Verify index usage
- Optimize query performance
- Compare different query strategies

## Replication and Sharding

### 28. Can you explain replication in MongoDB?

Replication maintains multiple copies of data across different servers:

**Replica Set Components**:
- **Primary**: Receives all write operations
- **Secondary**: Maintains copies through oplog
- **Arbiter**: Participates in elections (no data)

**Benefits**:
- High availability
- Automatic failover
- Data redundancy
- Read scaling
- Disaster recovery

**How it Works**:
1. Writes go to primary
2. Primary logs operations to oplog
3. Secondaries replicate oplog asynchronously
4. If primary fails, secondaries elect new primary

**Configuration**:
```javascript
rs.initiate({
  _id: "myReplicaSet",
  members: [
    {_id: 0, host: "mongodb0.example.net:27017"},
    {_id: 1, host: "mongodb1.example.net:27017"},
    {_id: 2, host: "mongodb2.example.net:27017"}
  ]
})
```

### 29. Explain purpose and components of replica set?

**Purpose**:
- Provide redundancy and high availability
- Automatic failover
- Disaster recovery
- Read scalability

**Components**:

1. **Primary Node**:
   - Accepts all write operations
   - Only one primary per replica set
   - Records changes in oplog

2. **Secondary Nodes**:
   - Maintain copies of primary's data
   - Can serve read operations
   - Eligible to become primary
   - Replicate from primary's oplog

3. **Arbiter** (optional):
   - No data, only votes in elections
   - Breaks ties in elections
   - Uses minimal resources

4. **Hidden Members**:
   - Not visible to applications
   - Used for backups or reporting
   - Cannot become primary

5. **Delayed Members**:
   - Maintain historical snapshot
   - Protection against human errors

**Minimum**: 3 members (or 2 members + 1 arbiter) for automatic failover

### 30. What is sharding in MongoDB and when should it be used?

Sharding is horizontal scaling that distributes data across multiple servers:

**Components**:
- **Shards**: Store subset of data (each can be a replica set)
- **Mongos**: Query router (application connects here)
- **Config Servers**: Store cluster metadata

**Shard Key**: Field(s) that determine data distribution

**When to Use Sharding**:
- Data exceeds single server capacity
- Working set exceeds RAM
- Write throughput exceeds single server
- Geographic data distribution needed
- Typically after reaching 200GB+ per server

**Example**:
```javascript
// Enable sharding on database
sh.enableSharding("myDatabase")

// Shard collection
sh.shardCollection("myDatabase.myCollection", {userId: 1})
```

**Considerations**:
- Choose shard key carefully (immutable after sharding)
- High cardinality keys
- Even distribution of queries and data
- Avoid monotonically increasing keys

### 31. How does MongoDB perform automatic failover?

**Failover Process**:

1. **Heartbeat Detection**:
   - Members send heartbeats every 2 seconds
   - If primary unresponsive for 10 seconds, election triggered

2. **Election Process**:
   - Secondary nodes request votes
   - Majority votes needed to become primary
   - Highest priority member with most recent data wins
   - Election typically completes in 7-12 seconds

3. **New Primary**:
   - Elected secondary becomes primary
   - Starts accepting writes
   - Other secondaries sync from new primary

4. **Rollback**:
   - Old primary rejoins as secondary
   - Rolls back uncommitted writes
   - Rolled back operations saved to rollback files

**Configuration Options**:
```javascript
{
  _id: 0,
  host: "mongodb0.example.net:27017",
  priority: 1,
  votes: 1
}
```

- **priority**: Higher priority members more likely elected
- **votes**: 0 or 1 (for voting participation)

### 32. Explain the difference between horizontal and vertical scaling and how MongoDB supports them?

**Vertical Scaling** (Scale Up):
- Add more CPU, RAM, or storage to single server
- Simpler to implement
- Limited by hardware constraints
- MongoDB supports through better hardware

**Horizontal Scaling** (Scale Out):
- Add more servers to cluster
- Nearly unlimited scaling potential
- More complex architecture
- MongoDB supports through sharding

**MongoDB's Support**:

**For Horizontal Scaling**:
- **Sharding**: Distribute data across multiple servers
- **Replica Sets**: Distribute reads across secondaries
- Automatic data balancing
- Query routing through mongos

**For Vertical Scaling**:
- Optimize for larger RAM (working set)
- Support for high-performance storage
- Efficient use of CPU cores

**Best Practice**: Start with vertical scaling, move to horizontal (sharding) when:
- Single server capacity reached
- Cost-effectiveness of adding servers
- Geographic distribution needed

## Performance and Optimization

### 33. How does MongoDB handle large data volumes?

**Storage Mechanisms**:
- **WiredTiger**: Compression reduces storage footprint
- **Document-level locking**: High concurrency
- **Memory-mapped files**: Fast data access
- **Journaling**: Crash recovery

**Scaling Strategies**:
- **Sharding**: Distribute data across servers
- **Replication**: Distribute read load
- **Indexes**: Fast data access
- **Aggregation Pipeline**: Server-side processing

**Optimization Techniques**:
- **Working Set Management**: Keep frequently accessed data in RAM
- **Index Optimization**: Proper indexing strategy
- **Query Optimization**: Efficient query patterns
- **Data Modeling**: Embed vs reference based on access patterns
- **Capped Collections**: For fixed-size, high-throughput scenarios
- **GridFS**: For files larger than 16MB

**Best Practices**:
- Monitor with mongostat and mongotop
- Use profiler to identify slow queries
- Archive old data
- Compress data at storage level
- Use appropriate read/write concerns

### 34. What techniques do you use to diagnose and address performance issues in MongoDB?

**Diagnostic Tools**:

1. **explain()**: Analyze query execution
   ```javascript
   db.collection.find({}).explain("executionStats")
   ```

2. **Database Profiler**:
   ```javascript
   db.setProfilingLevel(2)  // Log all operations
   db.system.profile.find().sort({ts: -1})
   ```

3. **mongostat**: Real-time statistics
   ```bash
   mongostat --host localhost:27017
   ```

4. **mongotop**: Track time spent per collection
   ```bash
   mongotop 10  // Update every 10 seconds
   ```

5. **currentOp()**: View running operations
   ```javascript
   db.currentOp()
   ```

**Common Issues & Solutions**:

- **Slow Queries**: Add indexes, optimize query structure
- **High Memory Usage**: Review working set, add RAM, or shard
- **Lock Contention**: Upgrade to WiredTiger, optimize writes
- **Disk I/O**: Use SSDs, optimize indexes, add sharding
- **Network Latency**: Deploy closer to application, use appropriate read preference

**Monitoring Metrics**:
- Query execution time
- Index usage and efficiency
- Memory usage and page faults
- Disk I/O
- Replication lag
- Connection pool size

### 35. How do you ensure indexes fit into RAM?

**Check Index Size**:
```javascript
db.collection.stats()  // Look at indexSizes
db.collection.totalIndexSize()
```

**Monitor RAM Usage**:
```javascript
db.serverStatus().wiredTiger.cache
```

**Strategies**:

1. **Index Selection**:
   - Only create necessary indexes
   - Remove unused indexes
   - Use sparse indexes where applicable
   - Consider partial indexes for subset of documents

2. **Compound Indexes**:
   - One compound index instead of multiple single-field indexes
   - Follow ESR rule (Equality, Sort, Range)

3. **Index Compression**:
   - WiredTiger compresses indexes by default
   - Prefix compression for compound indexes

4. **Data Modeling**:
   - Reduce document size
   - Consider embedding vs referencing
   - Remove unnecessary fields

5. **Hardware**:
   - Add more RAM
   - Use high-performance storage

**Monitor with**:
```javascript
db.collection.aggregate([
  {$indexStats: {}}
])
```

### 36. Can you explain MongoDB write concerns?

Write concern determines acknowledgment level for write operations:

**Syntax**:
```javascript
db.collection.insertOne(
  {name: "Alice"},
  {writeConcern: {w: "majority", j: true, wtimeout: 5000}}
)
```

**Parameters**:

1. **w (Write Acknowledgment)**:
   - `w: 1`: Acknowledged from primary only (default)
   - `w: "majority"`: Acknowledged from majority of replica set
   - `w: 0`: No acknowledgment
   - `w: 3`: Acknowledged from 3 members

2. **j (Journaling)**:
   - `j: true`: Wait for journal commit
   - `j: false`: Don't wait for journal

3. **wtimeout**:
   - Maximum time to wait for acknowledgment (milliseconds)
   - Prevents indefinite blocking

**Trade-offs**:
- **Higher write concern**: More durable, slower
- **Lower write concern**: Faster, less durable

**Use Cases**:
- `{w: 1}`: Default, balance of performance and durability
- `{w: "majority", j: true}`: Critical data, maximum durability
- `{w: 0}`: Logging, analytics where some data loss acceptable

### 37. What is a covered query in MongoDB?

A covered query is satisfied entirely by an index without examining documents:

**Requirements**:
1. All query fields in index
2. All returned fields in index
3. No fields in document need to be accessed

**Example**:
```javascript
// Create index
db.users.createIndex({name: 1, age: 1})

// Covered query (only returns indexed fields)
db.users.find(
  {name: "Alice"},
  {name: 1, age: 1, _id: 0}
)
```

**Benefits**:
- Extremely fast (no disk access)
- Lower I/O
- Index data already in memory

**Verification**:
```javascript
db.users.find(
  {name: "Alice"},
  {name: 1, age: 1, _id: 0}
).explain("executionStats")
```
- Look for `totalDocsExamined: 0`
- Stage should be `IXSCAN` followed by `PROJECTION_COVERED`

**Limitations**:
- Cannot cover queries on array fields (multikey indexes)
- Cannot cover queries including `_id` unless explicitly in projection
- Cannot cover geospatial queries

## MongoDB Security

### 37. What are the security features available in MongoDB?

**Authentication**:
- SCRAM (default)
- x.509 certificates
- LDAP (Enterprise)
- Kerberos (Enterprise)

**Authorization**:
- Role-Based Access Control (RBAC)
- Built-in roles and custom roles
- Database and collection-level permissions

**Encryption**:
- **At Rest**: Encrypted storage engine (Enterprise)
- **In Transit**: TLS/SSL for connections
- **Field-Level**: Client-side field encryption

**Network Security**:
- IP whitelisting
- Firewall configuration
- VPC/Private networks
- SSL/TLS certificates

**Auditing** (Enterprise):
- Track database activities
- Compliance requirements
- Security monitoring

**Security Checklist**:
```javascript
// Enable authentication
// Use SSL/TLS
// Run with least privilege
// Enable auditing
// Regular security updates
// Firewall configuration
// Encrypt backups
```

### 38. How do you enable authentication in MongoDB?

**Steps to Enable Authentication**:

1. **Start MongoDB without auth**:
   ```bash
   mongod --port 27017 --dbpath /data/db
   ```

2. **Create admin user**:
   ```javascript
   use admin
   db.createUser({
     user: "adminUser",
     pwd: "securePassword",
     roles: [{role: "userAdminAnyDatabase", db: "admin"}]
   })
   ```

3. **Shutdown and restart with auth**:
   ```bash
   mongod --auth --port 27017 --dbpath /data/db
   ```

4. **Or use configuration file**:
   ```yaml
   security:
     authorization: enabled
   ```

5. **Connect with authentication**:
   ```bash
   mongo --username adminUser --password securePassword --authenticationDatabase admin
   ```

6. **Create database-specific users**:
   ```javascript
   use myDatabase
   db.createUser({
     user: "myUser",
     pwd: "myPassword",
     roles: [{role: "readWrite", db: "myDatabase"}]
   })
   ```

### 39. Explain role-based access control in MongoDB?

RBAC provides fine-grained access control through roles:

**Built-in Roles**:

**Database Level**:
- `read`: Read data from all non-system collections
- `readWrite`: Read and write data
- `dbAdmin`: Database administration tasks
- `userAdmin`: Create and modify users/roles

**Cluster Level**:
- `clusterAdmin`: Full cluster administration
- `clusterManager`: Cluster management
- `hostManager`: Monitor and manage servers

**All Databases**:
- `readAnyDatabase`
- `readWriteAnyDatabase`
- `userAdminAnyDatabase`
- `dbAdminAnyDatabase`

**Superuser**:
- `root`: Full access to all resources

**Create Custom Role**:
```javascript
use admin
db.createRole({
  role: "customReadWriteRole",
  privileges: [
    {
      resource: {db: "myDatabase", collection: "myCollection"},
      actions: ["find", "insert", "update"]
    }
  ],
  roles: []
})
```

**Assign Role to User**:
```javascript
db.grantRolesToUser("myUser", [
  {role: "customReadWriteRole", db: "myDatabase"}
])
```

### 40. Explain how to encrypt data in MongoDB?

**Encryption at Rest** (Enterprise Edition):

1. **Configure encryption**:
   ```yaml
   security:
     enableEncryption: true
     encryptionKeyFile: /path/to/keyfile
   ```

2. **Generate key file**:
   ```bash
   openssl rand -base64 32 > /path/to/keyfile
   chmod 600 /path/to/keyfile
   ```

**Encryption in Transit** (TLS/SSL):

1. **Generate certificates**:
   ```bash
   openssl req -newkey rsa:2048 -nodes -keyout mongodb.key -x509 -days 365 -out mongodb.crt
   cat mongodb.key mongodb.crt > mongodb.pem
   ```

2. **Configure MongoDB**:
   ```yaml
   net:
     tls:
       mode: requireTLS
       certificateKeyFile: /path/to/mongodb.pem
   ```

**Client-Side Field Level Encryption**:

```javascript
const clientEncryption = new ClientEncryption(keyVault, kmsProviders)

// Encrypt field
const encryptedField = await clientEncryption.encrypt(
  sensitiveData,
  {
    algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
    keyId: dataKey
  }
)

// Insert encrypted data
db.collection.insertOne({
  name: "Alice",
  ssn: encryptedField
})
```

**Encryption Key Management**:
- AWS KMS
- Azure Key Vault
- Google Cloud KMS
- Local key file (testing only)

### 41. How do you setup MongoDB to use TLS/SSL connections?

**Server Configuration**:

1. **Generate SSL Certificates**:
   ```bash
   # Generate private key
   openssl genrsa -out mongodb.key 2048
   
   # Generate certificate signing request
   openssl req -new -key mongodb.key -out mongodb.csr
   
   # Generate self-signed certificate
   openssl x509 -req -days 365 -in mongodb.csr -signkey mongodb.key -out mongodb.crt
   
   # Combine key and certificate
   cat mongodb.key mongodb.crt > mongodb.pem
   ```

2. **MongoDB Configuration File**:
   ```yaml
   net:
     port: 27017
     tls:
       mode: requireTLS
       certificateKeyFile: /etc/ssl/mongodb.pem
       CAFile: /etc/ssl/ca.pem
       allowConnectionsWithoutCertificates: false
   ```

3. **Or use command line**:
   ```bash
   mongod --tlsMode requireTLS \
          --tlsCertificateKeyFile /etc/ssl/mongodb.pem \
          --tlsCAFile /etc/ssl/ca.pem
   ```

**Client Connection**:
```bash
mongo --tls --host mongodb.example.com \
      --tlsCertificateKeyFile /etc/ssl/client.pem \
      --tlsCAFile /etc/ssl/ca.pem
```

**Connection String**:
```
mongodb://hostname:27017/?tls=true&tlsCertificateKeyFile=/path/to/client.pem&tlsCAFile=/path/to/ca.pem
```

**TLS Modes**:
- `disabled`: No TLS
- `allowTLS`: TLS optional
- `preferTLS`: TLS preferred
- `requireTLS`: TLS mandatory

## MongoDB Storage Engine

### 42. What different storage engines are available in MongoDB?

**WiredTiger** (Default since MongoDB 3.2):
- Document-level concurrency
- Compression (data and indexes)
- Checkpoint-based persistence
- Write-ahead transaction log (journal)
- Better performance for most workloads

**In-Memory Storage Engine** (Enterprise):
- All data stored in RAM
- No disk I/O
- Extremely fast reads and writes
- Data lost on restart
- Use case: Caching, real-time analytics

**Encrypted Storage Engine** (Enterprise):
- Based on WiredTiger
- Native encryption at rest
- Transparent to applications

**MMAPv1** (Deprecated, removed in 4.2):
- Legacy storage engine
- Collection-level locking
- Memory-mapped files
- No compression

**Choosing Storage Engine**:
```javascript
// Check current storage engine
db.serverStatus().storageEngine

// Set storage engine (configuration file)
storage:
  engine: wiredTiger
  wiredTiger:
    engineConfig:
      cacheSizeGB: 2
```

### 43. How does WiredTiger storage engine differ from MMAPv1?

| Feature | WiredTiger | MMAPv1 |
|---------|-----------|---------|
| **Concurrency** | Document-level locking | Collection-level locking |
| **Compression** | Supports compression | No compression |
| **Performance** | Better overall | Slower for concurrent writes |
| **Memory Usage** | Configurable cache | Uses all available RAM |
| **Journal** | Write-ahead log | Journal file |
| **Disk Space** | Less (compression) | More (no compression) |
| **Default Since** | MongoDB 3.2+ | MongoDB 3.0 and earlier |
| **Status** | Active | Deprecated (removed 4.2) |

**WiredTiger Advantages**:
- Higher concurrency
- Better write performance
- Compression saves disk space
- Configurable cache size
- Checkpoint-based durability

**WiredTiger Configuration**:
```yaml
storage:
  engine: wiredTiger
  wiredTiger:
    engineConfig:
      cacheSizeGB: 2
      journalCompressor: snappy
    collectionConfig:
      blockCompressor: snappy
    indexConfig:
      prefixCompression: true
```

### 44. Can you switch between storage engines in MongoDB?

**Yes, but requires data migration**:

**Method 1: mongodump/mongorestore**:

1. **Export data**:
   ```bash
   mongodump --out /backup/dump
   ```

2. **Stop MongoDB**:
   ```bash
   mongod --shutdown
   ```

3. **Change storage engine**:
   ```yaml
   storage:
     engine: wiredTiger
     dbPath: /data/db_wiredtiger
   ```

4. **Start with new storage engine**:
   ```bash
   mongod --config /etc/mongod.conf
   ```

5. **Restore data**:
   ```bash
   mongorestore /backup/dump
   ```

**Method 2: Replica Set Rolling Migration**:

1. Change storage engine on secondary
2. Let it sync with primary
3. Step down primary
4. Repeat for all members

**Method 3: Sync from another member**:

1. Add new member with different storage engine
2. Let it perform initial sync
3. Remove old member

**Important Notes**:
- Cannot switch engines in-place
- Requires downtime or replica set
- Indexes need to be rebuilt
- Test thoroughly before production
- Backup data before switching

## Advanced MongoDB Concepts

### 45. What is oplog in MongoDB and how it works?

The **oplog (operations log)** is a special capped collection that records all write operations:

**Location**: `local.oplog.rs` (on replica set members)

**Purpose**:
- Replication mechanism
- Records all data modifications
- Enables secondaries to replicate primary's operations
- Point-in-time recovery

**Structure**:
```javascript
{
  "ts": Timestamp(1234567890, 1),  // Operation timestamp
  "h": NumberLong("123456789"),    // Unique operation identifier
  "v": 2,                           // Oplog version
  "op": "i",                        // Operation type (i/u/d/c/n)
  "ns": "mydb.mycollection",        // Namespace
  "o": {...},                       // Operation document
  "o2": {...}                       // Update query (for updates)
}
```

**Operation Types**:
- `i`: Insert
- `u`: Update
- `d`: Delete
- `c`: Command
- `n`: No-op

**How Replication Works**:
1. Primary logs operations to oplog
2. Secondaries tail the primary's oplog
3. Secondaries apply operations in same order
4. Asynchronous replication

**Oplog Size**:
```javascript
// Check oplog size
use local
db.oplog.rs.stats()

// Check oplog window (how much time covered)
db.getReplicationInfo()
```

**Configure Oplog Size**:
```yaml
replication:
  oplogSizeMB: 2048
```

**Best Practices**:
- Size based on workload and desired window
- Typically 5-10% of data size
- Monitor oplog lag on secondaries

### 46. How do you use lookup operation in MongoDB?

**$lookup** performs left outer join between collections:

**Basic Syntax**:
```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",           // Collection to join
      localField: "customer_id",   // Field from orders
      foreignField: "_id",         // Field from customers
      as: "customer_info"          // Output array field
    }
  }
])
```

**With Pipeline** (more powerful):
```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      let: {order_items: "$items"},
      pipeline: [
        {
          $match: {
            $expr: {
              $in: ["$_id", "$order_items"]
            }
          }
        },
        {
          $project: {name: 1, price: 1}
        }
      ],
      as: "product_details"
    }
  }
])
```

**Uncorrelated Subquery**:
```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "inventory",
      pipeline: [
        {$match: {inStock: true}},
        {$project: {item: 1, qty: 1}}
      ],
      as: "available_items"
    }
  }
])
```

**Multiple Lookups**:
```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "customer"
    }
  },
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "_id",
      as: "product"
    }
  },
  {
    $unwind: "$customer"  // Flatten array
  }
])
```

### 47. Explain the role of mongos server in sharded MongoDB architecture?

**mongos** is the query router in sharded clusters:

**Responsibilities**:

1. **Query Routing**:
   - Receives queries from applications
   - Determines which shards contain data
   - Routes queries to appropriate shards
   - Merges results from multiple shards

2. **Metadata Management**:
   - Caches cluster metadata from config servers
   - Knows shard key ranges
   - Maintains shard topology information

3. **Load Distribution**:
   - Distributes writes based on shard key
   - Balances query load across shards
   - Handles broadcast operations

4. **Aggregation**:
   - Coordinates aggregation pipeline across shards
   - Performs final merge of results

**Architecture**:
```
Application → mongos → [Shard1, Shard2, Shard3]
                ↓
           Config Servers
```

**Deployment**:
```bash
mongos --configdb configReplSet/cfg1:27019,cfg2:27019,cfg3:27019
```

**Connection**:
```javascript
// Application connects to mongos, not directly to shards
mongodb://mongos1:27017,mongos2:27017/myDatabase
```

**Multiple mongos**:
- Deploy multiple mongos for high availability
- Stateless - can add/remove without data migration
- Applications can connect to any mongos

**Best Practices**:
- Run mongos on application servers
- Deploy at least 2 mongos instances
- No data storage on mongos
- Monitor mongos performance

### 48. What is journaling in MongoDB and why is it important?

**Journaling** is write-ahead logging for crash recovery:

**How it Works**:
1. Before applying write to data files, MongoDB writes to journal
2. Journal entries written every 100ms (configurable)
3. In case of crash, MongoDB replays journal on restart
4. Ensures data consistency and durability

**Journal Files**:
- Located in `dbPath/journal/` directory
- Binary log files (journal.**)
- Compressed by default
- Rotated automatically

**Benefits**:
- **Crash Recovery**: Prevent data loss
- **Data Durability**: Ensure writes persisted
- **Fast Recovery**: Quick startup after crash
- **Consistency**: Maintain database integrity

**Configuration**:
```yaml
storage:
  journal:
    enabled: true
    commitIntervalMs: 100
```

**Disable Journaling** (not recommended):
```yaml
storage:
  journal:
    enabled: false
```

**Write Concern with Journaling**:
```javascript
db.collection.insertOne(
  {data: "important"},
  {writeConcern: {w: 1, j: true}}  // Wait for journal
)
```

**Performance Considerations**:
- Journal adds small write overhead
- Use SSD for journal directory
- Keep journal on separate disk for performance

**When to Disable**:
- Development environments
- When using replica sets (replication provides durability)
- Performance testing scenarios

### 49. Explain GridFS specifications in MongoDB?

**GridFS** is a specification for storing and retrieving large files (>16MB):

**How it Works**:
- Files split into chunks (default 255KB)
- Two collections used:
  - `fs.files`: File metadata
  - `fs.chunks`: File chunks

**Files Collection Structure**:
```javascript
{
  "_id": ObjectId("..."),
  "length": 123456,
  "chunkSize": 261120,
  "uploadDate": ISODate("..."),
  "filename": "myfile.pdf",
  "contentType": "application/pdf",
  "metadata": {...}  // Custom metadata
}
```

**Chunks Collection Structure**:
```javascript
{
  "_id": ObjectId("..."),
  "files_id": ObjectId("..."),  // Reference to fs.files
  "n": 0,                        // Chunk number
  "data": BinData(...)          // Chunk data
}
```

**Using GridFS**:

**Upload File**:
```bash
mongofiles -d myDatabase put myfile.pdf
```

**Download File**:
```bash
mongofiles -d myDatabase get myfile.pdf
```

**Using Driver (Python)**:
```python
import gridfs
from pymongo import MongoClient

client = MongoClient()
db = client.myDatabase
fs = gridfs.GridFS(db)

# Upload
with open('myfile.pdf', 'rb') as f:
    file_id = fs.put(f, filename='myfile.pdf')

# Download
file_data = fs.get(file_id)
with open('downloaded.pdf', 'wb') as f:
    f.write(file_data.read())
```

**When to Use GridFS**:
- Files larger than 16MB (BSON limit)
- Files need to be accessed by ranges
- Want to keep files synchronized with database
- Need to update parts of large files

**When NOT to Use**:
- Small files (<16MB) - use regular documents
- Files stored in filesystem with references in MongoDB
- Need high-performance file serving

**Advantages**:
- No file size limit
- Automatic chunking
- Efficient partial reads
- Integrated with MongoDB

**Indexes**:
```javascript
db.fs.files.createIndex({filename: 1})
db.fs.chunks.createIndex({files_id: 1, n: 1})
```

## MongoDB Schema Design

### 50. How does schema design impact performance in MongoDB?

**Key Impact Areas**:

1. **Read Performance**:
   - Embedded documents: Single query, faster
   - Referenced documents: Multiple queries, slower
   - Proper indexing critical

2. **Write Performance**:
   - Embedded: Update entire document
   - Referenced: Update specific document
   - Document growth considerations

3. **Memory Usage**:
   - Larger documents = more memory per operation
   - Working set size affects RAM requirements

4. **Storage**:
   - Duplication in embedded model
   - Normalization reduces duplication

**Design Patterns**:

**Embed When**:
```javascript
// One-to-few, data accessed together
{
  _id: 1,
  name: "John",
  addresses: [
    {street: "123 Main", city: "NYC"},
    {street: "456 Oak", city: "LA"}
  ]
}
```

**Reference When**:
```javascript
// One-to-many, large subdocuments
// User document
{_id: 1, name: "John"}

// Orders collection
{_id: 101, user_id: 1, total: 100}
{_id: 102, user_id: 1, total: 200}
```

**Performance Considerations**:
- Query patterns drive design
- Avoid unbounded arrays
- Consider document growth
- 16MB document size limit
- Index selectivity
- Update patterns

### 51. Compare embedded vs referenced documents in MongoDB?

**Embedded Documents**:

```javascript
{
  _id: 1,
  name: "Blog Post",
  comments: [
    {user: "Alice", text: "Great!"},
    {user: "Bob", text: "Thanks!"}
  ]
}
```

**Advantages**:
- Single query retrieves all data
- Better read performance
- Atomic updates
- Data locality

**Disadvantages**:
- Document size limit (16MB)
- Duplication if data shared
- Difficult to query subdocuments independently
- Array growth issues

**Referenced Documents**:

```javascript
// Post
{_id: 1, name: "Blog Post"}

// Comments
{_id: 101, post_id: 1, user: "Alice", text: "Great!"}
{_id: 102, post_id: 1, user: "Bob", text: "Thanks!"}
```

**Advantages**:
- No document size limit concerns
- No duplication
- Can query independently
- Flexible relationships

**Disadvantages**:
- Multiple queries or $lookup needed
- Slower reads
- No atomic updates across documents
- More complex queries

**Decision Matrix**:

| Factor | Embed | Reference |
|--------|-------|-----------|
| Data size | Small | Large |
| Relationship | One-to-few | One-to-many |
| Access pattern | Together | Independently |
| Update frequency | Rare | Frequent |
| Duplication | Acceptable | Avoid |

### 52. What factors do you consider when designing schema in MongoDB?

**1. Access Patterns**:
- How is data queried?
- Read vs write ratio
- Common query patterns
- Data accessed together

**2. Data Relationships**:
- One-to-one: Embed or reference
- One-to-few: Embed
- One-to-many: Reference or hybrid
- Many-to-many: Reference

**3. Data Size**:
- Individual document size
- Collection size
- Growth rate
- 16MB document limit

**4. Update Patterns**:
- Atomic updates needed?
- Update frequency
- Partial updates
- Document growth

**5. Cardinality**:
- High cardinality: Good for indexing
- Low cardinality: Consider embedding

**6. Data Lifecycle**:
- TTL requirements
- Archival needs
- Data retention policies

**7. Consistency Requirements**:
- Atomic operations needed?
- Eventual consistency acceptable?
- Transaction requirements

**8. Performance Goals**:
- Query response time
- Write throughput
- Read throughput
- Index strategy

**9. Application Requirements**:
- Programming model
- ORM/ODM constraints
- Business logic

**Design Process**:
1. Identify use cases
2. Model relationships
3. Consider access patterns
4. Apply design patterns
5. Test and iterate
6. Monitor and optimize

### 53. How do you handle one-to-many modeling in MongoDB?

**Three Approaches**:

**1. Embedding (One-to-Few)**:
```javascript
// When "many" side is limited (<100)
{
  _id: 1,
  name: "John Doe",
  addresses: [
    {street: "123 Main St", city: "NYC"},
    {street: "456 Oak Ave", city: "LA"}
  ]
}
```

**Use When**:
- Few related items
- Data accessed together
- Need atomic updates
- Related data doesn't grow unbounded

**2. Referencing - Child References Parent**:
```javascript
// Parent
{_id: 1, name: "Product Category"}

// Children
{_id: 101, category_id: 1, name: "Product 1"}
{_id: 102, category_id: 1, name: "Product 2"}
```

**Use When**:
- Many related items
- Need to query children independently
- Children updated frequently
- Avoid document growth

**3. Parent References Children (Array of References)**:
```javascript
// Parent
{
  _id: 1,
  name: "Author",
  book_ids: [101, 102, 103]
}

// Children
{_id: 101, title: "Book 1"}
{_id: 102, title: "Book 2"}
```

**Use When**:
- Need to access all children from parent
- Moderate number of children
- Two-way navigation needed

**4. Hybrid Approach**:
```javascript
// Embed most recent, reference historical
{
  _id: 1,
  name: "User",
  recent_orders: [
    {order_id: 501, date: "2025-01-01", total: 100}
  ],
  all_order_ids: [501, 502, 503, ...]
}
```

**Query Examples**:

**Find all children**:
```javascript
// Referenced
db.products.find({category_id: 1})

// Array of references
db.books.find({_id: {$in: author.book_ids}})
```

**Considerations**:
- Number of related documents
- Growth rate
- Query patterns
- Update frequency
- Need for atomic operations

## Database Management & Maintenance

### 54. How do you perform data backup in MongoDB?

**Method 1: mongodump**:
```bash
# Backup entire database
mongodump --out /backup/dump

# Backup specific database
mongodump --db myDatabase --out /backup/dump

# Backup specific collection
mongodump --db myDatabase --collection myCollection --out /backup/dump

# With authentication
mongodump --username user --password pass --authenticationDatabase admin --out /backup/dump

# Compressed backup
mongodump --gzip --out /backup/dump
```

**Method 2: Filesystem Snapshots**:
```bash
# For WiredTiger with journaling
# 1. Flush writes
db.fsyncLock()

# 2. Take filesystem snapshot (LVM, EBS, etc.)
lvcreate --size 1G --snapshot --name db-snapshot /dev/vg/mongodb

# 3. Unlock
db.fsyncUnlock()
```

**Method 3: Replica Set Backup**:
- Backup from secondary to avoid impacting primary
- Use hidden secondary for backups
- No impact on production traffic

**Method 4: MongoDB Atlas Backup** (Cloud):
- Continuous backup
- Point-in-time recovery
- Automated snapshots
- Cross-region backups

**Method 5: Cloud Provider Snapshots**:
- AWS EBS snapshots
- Azure Managed Disks
- Google Persistent Disk snapshots

**Best Practices**:
- Automate backups (cron, scheduled tasks)
- Test restore procedures regularly
- Store backups off-site
- Encrypt backups
- Monitor backup success
- Document backup/restore procedures
- Keep multiple backup versions
- Use mongodump for logical backups
- Use snapshots for large databases

### 55. What techniques can be used to restore data in MongoDB?

**Method 1: mongorestore**:
```bash
# Restore entire backup
mongorestore /backup/dump

# Restore specific database
mongorestore --db myDatabase /backup/dump/myDatabase

# Restore specific collection
mongorestore --db myDatabase --collection myCollection /backup/dump/myDatabase/myCollection.bson

# Drop existing data before restore
mongorestore --drop /backup/dump

# With authentication
mongorestore --username user --password pass --authenticationDatabase admin /backup/dump

# From gzip
mongorestore --gzip /backup/dump

# To different database
mongorestore --nsFrom "sourceDB.*" --nsTo "targetDB.*" /backup/dump
```

**Method 2: Filesystem Restore**:
```bash
# Stop MongoDB
systemctl stop mongod

# Restore from snapshot
# Copy files to dbPath

# Start MongoDB
systemctl start mongod
```

**Method 3: Point-in-Time Recovery** (Enterprise/Atlas):
```bash
# Using oplog
mongorestore --oplogReplay --oplogLimit 1234567890:1 /backup/dump
```

**Method 4: Replica Set Member Restore**:
1. Remove member from replica set
2. Restore data to that member
3. Let it perform initial sync from primary
4. Or use restored data and let it catch up via oplog

**Method 5: Partial Restore**:
```bash
# Restore only specific documents
mongorestore --db myDB --collection users --query '{"status":"active"}' /backup/dump
```

**Restore Strategies**:

**Full Restore**:
- Complete database replacement
- System failure recovery

**Selective Restore**:
- Specific collections or databases
- Data corruption recovery

**Merge Restore**:
- Add data without dropping existing
- Data migration scenarios

**Best Practices**:
- Test restores regularly
- Restore to staging environment first
- Verify data integrity after restore
- Check indexes and validation rules
- Document restore procedures
- Time the restore process
- Have rollback plan

### 56. How do you monitor performance of a MongoDB instance?

**Built-in Tools**:

**1. mongostat**:
```bash
mongostat --host localhost:27017
# Shows: inserts, queries, updates, deletes, connections, memory
```

**2. mongotop**:
```bash
mongotop 10  # Update every 10 seconds
# Shows: time spent reading/writing per collection
```

**3. Database Profiler**:
```javascript
// Enable profiling
db.setProfilingLevel(2)  // 0=off, 1=slow, 2=all

// Query slow operations
db.system.profile.find({millis: {$gt: 100}}).sort({ts: -1})

// Analyze specific operation
db.system.profile.find({op: "query", ns: "mydb.mycollection"})
```

**4. currentOp()**:
```javascript
// View current operations
db.currentOp()

// Find long-running queries
db.currentOp({
  "active": true,
  "secs_running": {$gte: 10}
})

// Kill slow operation
db.killOp(opid)
```

**5. serverStatus()**:
```javascript
db.serverStatus()
// Returns: connections, memory, locks, network, opcounters
```

**6. dbStats()** and **collStats()**:
```javascript
db.stats()  // Database statistics
db.collection.stats()  // Collection statistics
```

**Key Metrics to Monitor**:

**Performance**:
- Query execution time
- Operations per second
- Index usage efficiency
- Page faults

**Resources**:
- CPU utilization
- Memory usage (resident, virtual, mapped)
- Disk I/O
- Network traffic

**Database Health**:
- Connection count
- Replication lag
- Lock percentage
- Queue lengths

**Third-Party Tools**:

**MongoDB Cloud Manager / Ops Manager**:
- Real-time monitoring
- Automated alerts
- Performance advisor
- Index suggestions

**Third-Party APM**:
- New Relic
- Datadog
- Prometheus + Grafana
- AppDynamics

**Monitoring Setup Example**:
```javascript
// Set up monitoring user
db.createUser({
  user: "monitoring",
  pwd: "password",
  roles: [{role: "clusterMonitor", db: "admin"}]
})
```

**Alert Thresholds**:
- Query execution > 1000ms
- Replication lag > 10 seconds
- Connections > 80% of max
- Memory usage > 80%
- Disk usage > 80%

### 57. What factors lead you to defragment a MongoDB collection?

**When to Consider Defragmentation**:

1. **High Storage Fragmentation**:
   - Large difference between storage size and data size
   - Check with `db.collection.stats()`

2. **Frequent Deletions**:
   - Many documents deleted
   - Creates empty space in data files

3. **Document Updates with Growth**:
   - Documents grow beyond allocated space
   - MongoDB relocates documents, leaving gaps

4. **Performance Degradation**:
   - Slower query performance
   - Increased disk I/O

5. **Disk Space Issues**:
   - Want to reclaim unused space
   - High storage size vs data size ratio

**Check Fragmentation**:
```javascript
let stats = db.collection.stats()
let fragmentation = (stats.storageSize - stats.size) / stats.storageSize * 100
print("Fragmentation: " + fragmentation + "%")
```

**Defragmentation Methods**:

**Method 1: compact command**:
```javascript
// Blocks all operations on collection
db.runCommand({compact: "myCollection"})

// With padding factor (deprecated in newer versions)
db.runCommand({compact: "myCollection", paddingFactor: 1.5})
```

**Method 2: Rebuild Indexes**:
```javascript
db.collection.reIndex()
```

**Method 3: Export and Reimport**:
```bash
# Export
mongodump --db myDB --collection myCollection

# Drop and recreate
db.myCollection.drop()

# Import
mongorestore --db myDB --collection myCollection dump/myDB/myCollection.bson
```

**Method 4: Replica Set Rolling Compaction**:
1. Compact secondary
2. Let it catch up
3. Step down primary
4. Compact former primary
5. Repeat for all members

**Considerations**:
- `compact` requires exclusive lock
- Causes downtime for collection
- Can take significant time
- Use during maintenance window
- Test in staging first
- Monitor disk space during operation

**Best Practices**:
- Schedule during low-traffic periods
- Use replica set for availability
- Monitor progress
- Ensure sufficient disk space
- Document the process

## Working with Datatypes

### 58. What are the different datatypes supported in MongoDB?

MongoDB BSON supports these datatypes:

**Basic Types**:
- **String**: UTF-8 strings
- **Integer**: 32-bit (Int32) and 64-bit (Int64)
- **Double**: 64-bit floating point
- **Boolean**: true/false
- **Null**: Null value

**Complex Types**:
- **Object**: Embedded documents
- **Array**: Ordered list of values
- **ObjectId**: 12-byte unique identifier
- **Date**: UTC datetime (64-bit integer milliseconds)
- **Timestamp**: Internal type for replication/sharding
- **Binary Data**: Binary content
- **Regular Expression**: Regex patterns
- **JavaScript**: JavaScript code
- **JavaScript with Scope**: JS code with scope

**Numeric Types**:
- **Int32**: 32-bit integer
- **Int64**: 64-bit integer (Long)
- **Double**: 64-bit floating point
- **Decimal128**: 128-bit decimal (precise decimal calculations)

**Special Types**:
- **MinKey**: Lowest BSON value
- **MaxKey**: Highest BSON value

**Example**:
```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John Doe",                          // String
  age: 30,                                    // Int32
  salary: 50000.50,                           // Double
  isActive: true,                             // Boolean
  joinDate: new Date("2025-01-01"),          // Date
  skills: ["JavaScript", "Python"],           // Array
  address: {street: "123 Main", city: "NYC"}, // Object
  avatar: BinData(0, "base64data"),          // Binary
  metadata: null,                             // Null
  price: NumberDecimal("19.99")              // Decimal128
}
```

### 59. How does MongoDB store different types of numerical data?

**Integer Types**:

**Int32** (32-bit integer):
```javascript
db.collection.insertOne({count: NumberInt(100)})
// Range: -2,147,483,648 to 2,147,483,647
```

**Int64** (64-bit integer / Long):
```javascript
db.collection.insertOne({count: NumberLong("9223372036854775807")})
// Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
```

**Floating Point**:

**Double** (64-bit IEEE 754):
```javascript
db.collection.insertOne({price: 19.99})
// Default numeric type in MongoDB shell
// Limited precision for decimal calculations
```

**Decimal128** (128-bit decimal):
```javascript
db.collection.insertOne({price: NumberDecimal("19.99")})
// Exact decimal representation
// Use for financial/monetary calculations
// Supports 34 decimal digits of precision
```

**Storage Behavior**:
- Numbers without decimal → stored as Double by default (shell)
- Use NumberInt() or NumberLong() for integers
- Use NumberDecimal() for precise decimal calculations
- Drivers handle type conversion automatically

**Type Conversion**:
```javascript
// Convert types
db.collection.updateMany(
  {},
  [{$set: {age: {$toInt: "$age"}}}]
)
```

**Best Practices**:
- Use Decimal128 for money/currency
- Use Int64 for large counters
- Use Double for scientific calculations
- Be explicit about numeric types in inserts

### 60. How does MongoDB handle date and time data?

**Date Type**:
MongoDB stores dates as 64-bit integers representing milliseconds since Unix epoch (Jan 1, 1970):

```javascript
// Current date
db.collection.insertOne({
  createdAt: new Date()
})

// Specific date
db.collection.insertOne({
  birthDate: new Date("1990-05-15")
})

// ISO date string
db.collection.insertOne({
  eventDate: ISODate("2025-01-01T10:30:00Z")
})

// From timestamp
db.collection.insertOne({
  timestamp: new Date(1609459200000)
})
```

**Date Operations**:

**Query by Date**:
```javascript
// Find documents after specific date
db.collection.find({
  createdAt: {$gt: new Date("2025-01-01")}
})

// Date range
db.collection.find({
  createdAt: {
    $gte: new Date("2025-01-01"),
    $lt: new Date("2025-02-01")
  }
})
```

**Date Aggregation Operators**:
```javascript
db.collection.aggregate([
  {
    $project: {
      year: {$year: "$createdAt"},
      month: {$month: "$createdAt"},
      day: {$dayOfMonth: "$createdAt"},
      hour: {$hour: "$createdAt"},
      dayOfWeek: {$dayOfWeek: "$createdAt"}
    }
  }
])

// Date arithmetic
db.collection.aggregate([
  {
    $project: {
      expiryDate: {
        $add: ["$createdAt", 30 * 24 * 60 * 60 * 1000]  // Add 30 days
      }
    }
  }
])
```

**Date Formatting**:
```javascript
db.collection.aggregate([
  {
    $project: {
      formattedDate: {
        $dateToString: {
          format: "%Y-%m-%d %H:%M:%S",
          date: "$createdAt"
        }
      }
    }
  }
])
```

**Timezone Handling**:
```javascript
// With timezone
db.collection.aggregate([
  {
    $project: {
      localTime: {
        $dateToString: {
          format: "%Y-%m-%d %H:%M:%S",
          date: "$createdAt",
          timezone: "America/New_York"
        }
      }
    }
  }
])
```

**Important Notes**:
- Dates stored in UTC
- No timezone information stored with date
- Handle timezones in application layer
- Millisecond precision
- Range: approximately ±290 million years from epoch

### 61. Can you store multimedia files in MongoDB?

**Yes, using GridFS**:

**For Small Files (<16MB)**:
Store as Binary Data (BinData):
```javascript
// Store small image
const fs = require('fs');
const imageBuffer = fs.readFileSync('photo.jpg');

db.images.insertOne({
  filename: 'photo.jpg',
  contentType: 'image/jpeg',
  data: new Binary(imageBuffer)
})
```

**For Large Files (>16MB)**:
Use GridFS:

```javascript
// Node.js example
const { MongoClient, GridFSBucket } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
const db = client.db('myDatabase');

// Upload
const bucket = new GridFSBucket(db);
fs.createReadStream('video.mp4')
  .pipe(bucket.openUploadStream('video.mp4', {
    contentType: 'video/mp4',
    metadata: {
      description: 'Sample video',
      uploadedBy: 'user123'
    }
  }));

// Download
bucket.openDownloadStreamByName('video.mp4')
  .pipe(fs.createWriteStream('downloaded-video.mp4'));
```

**Command Line GridFS**:
```bash
# Upload
mongofiles -d myDatabase put video.mp4

# Download
mongofiles -d myDatabase get video.mp4

# List files
mongofiles -d myDatabase list

# Delete
mongofiles -d myDatabase delete video.mp4
```

**Supported File Types**:
- Images (JPEG, PNG, GIF, etc.)
- Videos (MP4, AVI, MOV, etc.)
- Audio (MP3, WAV, etc.)
- Documents (PDF, DOCX, etc.)
- Any binary data

**Best Practices**:
- **Small files (<1MB)**: Store as BinData in documents
- **Medium files (1-16MB)**: Consider BinData or GridFS
- **Large files (>16MB)**: Use GridFS (required)
- **Very large files**: Consider cloud storage (S3, Azure Blob) with reference in MongoDB

**Advantages of GridFS**:
- No 16MB limit
- Efficient chunked storage
- Range queries supported
- Metadata storage

**Disadvantages**:
- Slower than filesystem
- More overhead than direct file storage
- Not suitable for frequently updated files

**Alternative Approach**:
```javascript
// Store reference to external storage
db.media.insertOne({
  filename: 'video.mp4',
  url: 'https://cdn.example.com/videos/video.mp4',
  storageProvider: 'AWS S3',
  bucket: 'my-bucket',
  key: 'videos/video.mp4',
  metadata: {
    size: 52428800,
    contentType: 'video/mp4'
  }
})
```

## MongoDB and Programming

### 62. How do you connect MongoDB with Python script?

**Using PyMongo** (Official MongoDB Python Driver):

**Installation**:
```bash
pip install pymongo
```

**Basic Connection**:
```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Or with explicit parameters
client = MongoClient(host='localhost', port=27017)

# Access database
db = client['myDatabase']
# Or
db = client.myDatabase

# Access collection
collection = db['myCollection']
# Or
collection = db.myCollection
```

**With Authentication**:
```python
client = MongoClient(
    'mongodb://username:password@localhost:27017/',
    authSource='admin',
    authMechanism='SCRAM-SHA-256'
)
```

**Connection String**:
```python
client = MongoClient(
    'mongodb://user:pass@host1:27017,host2:27017/myDB?replicaSet=rs0&authSource=admin'
)
```

**CRUD Operations**:
```python
# Insert
result = collection.insert_one({'name': 'Alice', 'age': 25})
print(f"Inserted ID: {result.inserted_id}")

# Insert many
collection.insert_many([
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
])

# Find
for doc in collection.find({'age': {'$gt': 25}}):
    print(doc)

# Find one
doc = collection.find_one({'name': 'Alice'})

# Update
collection.update_one(
    {'name': 'Alice'},
    {'$set': {'age': 26}}
)

# Delete
collection.delete_one({'name': 'Bob'})

# Count
count = collection.count_documents({'age': {'$gt': 25}})
```

**Connection Pooling**:
```python
client = MongoClient(
    'mongodb://localhost:27017/',
    maxPoolSize=50,
    minPoolSize=10
)
```

**Error Handling**:
```python
from pymongo.errors import ConnectionFailure, OperationFailure

try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("Connected successfully")
except ConnectionFailure:
    print("Failed to connect to MongoDB")
except OperationFailure as e:
    print(f"Authentication failed: {e}")
```

**Close Connection**:
```python
client.close()
```

**Context Manager**:
```python
with MongoClient('mongodb://localhost:27017/') as client:
    db = client.myDatabase
    # Perform operations
# Connection automatically closed
```

### 63. What is mongos and how is it related to MongoDB?

**mongos** is the MongoDB Sharded Cluster Query Router:

**Role**:
- Application entry point for sharded clusters
- Routes queries to appropriate shards
- Merges results from multiple shards
- No data storage (stateless)

**Architecture**:
```
Application
    ↓
mongos (Query Router)
    ↓
[Shard1] [Shard2] [Shard3]
    ↓
Config Servers (metadata)
```

**Responsibilities**:

1. **Query Routing**:
   - Analyzes queries
   - Determines target shards using shard key
   - Routes to specific shard or broadcasts to all

2. **Result Aggregation**:
   - Collects results from multiple shards
   - Merges and sorts results
   - Returns to application

3. **Metadata Caching**:
   - Caches cluster topology from config servers
   - Maintains shard key ranges
   - Updates cache when topology changes

4. **Load Balancing**:
   - Distributes queries across shards
   - Manages connection pools

**Starting mongos**:
```bash
mongos --configdb configReplSet/cfg1:27019,cfg2:27019,cfg3:27019 --port 27017
```

**Configuration File**:
```yaml
sharding:
  configDB: configReplSet/cfg1:27019,cfg2:27019,cfg3:27019
net:
  port: 27017
  bindIp: 0.0.0.0
```

**Connecting to mongos**:
```javascript
mongo mongodb://mongos1:27017,mongos2:27017/myDatabase
```

**Multiple mongos Instances**:
- Deploy multiple for high availability
- Applications can connect to any mongos
- Load balancer can distribute connections
- No coordination needed between mongos instances

**Best Practices**:
- Run mongos on application servers
- Deploy at least 2 mongos instances
- No data on mongos machines
- Monitor mongos performance
- Use connection pooling

**Differences from mongod**:
- mongos: Query router (no data)
- mongod: Database server (stores data)

### 64. How do you create and use stored procedures in MongoDB?

MongoDB doesn't have traditional stored procedures like SQL databases, but offers alternatives:

**1. Server-Side JavaScript Functions** (Deprecated in 4.2+):
```javascript
// Store function (old method, deprecated)
db.system.js.save({
  _id: "myFunction",
  value: function(x, y) {
    return x + y;
  }
})

// Call function
db.eval("myFunction(5, 3)")
```

**⚠️ NOT RECOMMENDED**: `db.eval()` and server-side JavaScript removed in MongoDB 4.2+

**2. Modern Alternatives**:

**Aggregation Pipeline** (Recommended):
```javascript
// Create reusable aggregation pipeline
const calculateTotalSales = [
  {
    $group: {
      _id: "$customer_id",
      totalSales: {$sum: "$amount"},
      orderCount: {$sum: 1}
    }
  },
  {
    $match: {totalSales: {$gt: 1000}}
  },
  {
    $sort: {totalSales: -1}
  }
];

// Use pipeline
db.orders.aggregate(calculateTotalSales);

// Store in application code as reusable function
function getTopCustomers() {
  return db.orders.aggregate(calculateTotalSales);
}
```

**Application-Level Functions**:
```javascript
// Node.js example
class OrderRepository {
  constructor(db) {
    this.orders = db.collection('orders');
  }

  async calculateCustomerTotal(customerId) {
    const result = await this.orders.aggregate([
      {$match: {customer_id: customerId}},
      {$group: {_id: null, total: {$sum: "$amount"}}}
    ]).toArray();
    
    return result[0]?.total || 0;
  }

  async getTopCustomers(minAmount) {
    return this.orders.aggregate([
      {$group: {
        _id: "$customer_id",
        total: {$sum: "$amount"}
      }},
      {$match: {total: {$gte: minAmount}}},
      {$sort: {total: -1}}
    ]).toArray();
  }
}
```

**MongoDB Atlas Functions** (Serverless):
```javascript
// Define function in Atlas
exports = function(customer_id) {
  const collection = context.services.get("mongodb-atlas")
    .db("myDB").collection("orders");
  
  return collection.aggregate([
    {$match: {customer_id: customer_id}},
    {$group: {_id: null, total: {$sum: "$amount"}}}
  ]).toArray();
};
```

**3. Change Streams with Triggers**:
```javascript
// Atlas Trigger example
exports = function(changeEvent) {
  const doc = changeEvent.fullDocument;
  
  if (doc.amount > 10000) {
    // Send notification
    context.services.get("email").send({
      to: "manager@example.com",
      subject: "Large Order Alert",
      body: `Order ${doc._id} for ${doc.amount}`
    });
  }
};
```

**Best Practices**:
- Implement business logic in application layer
- Use aggregation pipelines for complex queries
- Consider MongoDB Atlas Functions for serverless
- Store reusable pipelines as application functions
- Use change streams for reactive operations

### 65. Describe how to use MongoDB shell?

**Starting MongoDB Shell**:
```bash
# Connect to local MongoDB
mongo

# Connect to specific host/port
mongo --host localhost --port 27017

# Connect to specific database
mongo myDatabase

# With authentication
mongo --username user --password pass --authenticationDatabase admin

# Connection string
mongo "mongodb://user:pass@host:27017/myDB"
```

**Basic Commands**:

**Database Operations**:
```javascript
// Show all databases
show dbs

// Switch/create database
use myDatabase

// Show current database
db

// Drop database
db.dropDatabase()

// Database stats
db.stats()
```

**Collection Operations**:
```javascript
// Show collections
show collections

// Create collection
db.createCollection("myCollection")

// Drop collection
db.myCollection.drop()

// Collection stats
db.myCollection.stats()
```

**CRUD Operations**:
```javascript
// Insert
db.users.insertOne({name: "Alice", age: 25})
db.users.insertMany([
  {name: "Bob", age: 30},
  {name: "Charlie", age: 35}
])

// Find
db.users.find()
db.users.find({age: {$gt: 25}})
db.users.find({}, {name: 1, _id: 0})
db.users.findOne({name: "Alice"})

// Update
db.users.updateOne({name: "Alice"}, {$set: {age: 26}})
db.users.updateMany({age: {$lt: 30}}, {$inc: {age: 1}})

// Delete
db.users.deleteOne({name: "Bob"})
db.users.deleteMany({age: {$lt: 18}})
```

**Useful Shell Commands**:
```javascript
// Help
help
db.help()
db.collection.help()

// Pretty print
db.users.find().pretty()

// Count documents
db.users.countDocuments()

// Distinct values
db.users.distinct("age")

// Explain query
db.users.find({age: {$gt: 25}}).explain()

// Index operations
db.users.createIndex({name: 1})
db.users.getIndexes()
db.users.dropIndex("name_1")

// Bulk operations
var bulk = db.users.initializeUnorderedBulkOp()
bulk.insert({name: "Dave"})
bulk.find({name: "Alice"}).update({$set: {age: 27}})
bulk.execute()
```

**Aggregation**:
```javascript
db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {_id: "$customer_id", total: {$sum: "$amount"}}},
  {$sort: {total: -1}},
  {$limit: 10}
])
```

**Administrative Commands**:
```javascript
// Server status
db.serverStatus()

// Current operations
db.currentOp()

// Kill operation
db.killOp(opid)

// Profiling
db.setProfilingLevel(1, {slowms: 100})
db.system.profile.find().sort({ts: -1})

// Replication status
rs.status()

// Sharding status
sh.status()
```

**Shell Configuration**:
```javascript
// .mongorc.js file in home directory
prompt = function() {
  return db + "> ";
}

// Disable automatic pretty print
DBQuery.prototype._prettyShell = false;
```

**Scripting**:
```javascript
// Load script
load("script.js")

// Exit shell
exit
```

**Shell Variables**:
```javascript
// Store results
var results = db.users.find({age: {$gt: 25}}).toArray()

// Iterate
results.forEach(function(doc) {
  print(doc.name)
})
```

## MongoDB Drivers and ODMs

### 66. What is the use of MongoDB ODM/ORM frameworks?

**ODM (Object-Document Mapper)** frameworks provide:

**Purpose**:
- Map application objects to MongoDB documents
- Provide abstraction layer over MongoDB driver
- Schema validation and type casting
- Built-in validation and hooks
- Simplified queries and operations

**Popular ODM/ORM Frameworks**:

**Mongoose (Node.js)**:
```javascript
const mongoose = require('mongoose');

// Define schema
const userSchema = new mongoose.Schema({
  name: {type: String, required: true},
  email: {type: String, unique: true},
  age: {type: Number, min: 0, max: 120},
  createdAt: {type: Date, default: Date.now}
});

// Add methods
userSchema.methods.getFullInfo = function() {
  return `${this.name} (${this.email})`;
};

// Create model
const User = mongoose.model('User', userSchema);

// Use model
const user = new User({name: 'Alice', email: 'alice@example.com', age: 25});
await user.save();

// Query
const users = await User.find({age: {$gt: 20}});
```

**MongoEngine (Python)**:
```python
from mongoengine import Document, StringField, IntField, connect

connect('myDatabase')

class User(Document):
    name = StringField(required=True, max_length=50)
    email = StringField(required=True, unique=True)
    age = IntField(min_value=0, max_value=120)
    
    meta = {'collection': 'users'}

# Create
user = User(name='Alice', email='alice@example.com', age=25)
user.save()

# Query
users = User.objects(age__gt=20)
```

**Morphia (Java)**:
```java
@Entity("users")
public class User {
    @Id
    private ObjectId id;
    private String name;
    private String email;
    private int age;
    
    // Getters and setters
}

Datastore datastore = morphia.createDatastore(mongoClient, "myDatabase");
User user = new User();
user.setName("Alice");
datastore.save(user);

List<User> users = datastore.find(User.class).filter("age >", 20).asList();
```

**Advantages**:
- Type safety and validation
- Schema enforcement
- Middleware/hooks for business logic
- Relationship management
- Query builder
- Migration support
- Reduced boilerplate code

**Disadvantages**:
- Performance overhead
- Learning curve
- Less flexibility than raw driver
- Can obscure MongoDB features
- Additional dependency

**When to Use ODM**:
- Complex application models
- Need schema validation
- Want type safety
- Team prefers OOP patterns
- Rapid development needed

**When to Use Raw Driver**:
- Maximum performance needed
- Simple data models
- Need full MongoDB feature access
- Microservices with simple operations

### 67. How do you perform MongoDB operations using Node.js?

**Using Native MongoDB Driver**:

**Installation**:
```bash
npm install mongodb
```

**Connection and CRUD**:
```javascript
const { MongoClient } = require('mongodb');

// Connection string
const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri);

async function main() {
  try {
    // Connect
    await client.connect();
    console.log('Connected to MongoDB');
    
    const db = client.db('myDatabase');
    const collection = db.collection('users');
    
    // Insert one
    const insertResult = await collection.insertOne({
      name: 'Alice',
      email: 'alice@example.com',
      age: 25
    });
    console.log('Inserted ID:', insertResult.insertedId);
    
    // Insert many
    await collection.insertMany([
      {name: 'Bob', age: 30},
      {name: 'Charlie', age: 35}
    ]);
    
    // Find
    const users = await collection.find({age: {$gt: 25}}).toArray();
    console.log('Users:', users);
    
    // Find one
    const user = await collection.findOne({name: 'Alice'});
    console.log('User:', user);
    
    // Update
    const updateResult = await collection.updateOne(
      {name: 'Alice'},
      {$set: {age: 26}}
    );
    console.log('Modified:', updateResult.modifiedCount);
    
    // Update many
    await collection.updateMany(
      {age: {$lt: 30}},
      {$inc: {age: 1}}
    );
    
    // Delete
    const deleteResult = await collection.deleteOne({name: 'Bob'});
    console.log('Deleted:', deleteResult.deletedCount);
    
    // Aggregation
    const pipeline = [
      {$match: {age: {$gte: 25}}},
      {$group: {_id: null, avgAge: {$avg: '$age'}}},
      {$project: {_id: 0, avgAge: 1}}
    ];
    const aggResult = await collection.aggregate(pipeline).toArray();
    console.log('Aggregation:', aggResult);
    
    // Count
    const count = await collection.countDocuments({age: {$gte: 25}});
    console.log('Count:', count);
    
    // Indexes
    await collection.createIndex({email: 1}, {unique: true});
    const indexes = await collection.indexes();
    console.log('Indexes:', indexes);
    
  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

main();
```

**Using Mongoose**:
```javascript
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/myDatabase');

const userSchema = new mongoose.Schema({
  name: String,
  email: {type: String, unique: true},
  age: Number
});

const User = mongoose.model('User', userSchema);

// Insert
const user = new User({name: 'Alice', email: 'alice@example.com', age: 25});
await user.save();

// Find
const users = await User.find({age: {$gt: 25}});

// Update
await User.updateOne({name: 'Alice'}, {$set: {age: 26}});

// Delete
await User.deleteOne({name: 'Bob'});
```

**Connection Pooling**:
```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 50,
  minPoolSize: 10,
  maxIdleTimeMS: 30000
});
```

**Error Handling**:
```javascript
try {
  await collection.insertOne(doc);
} catch (error) {
  if (error.code === 11000) {
    console.error('Duplicate key error');
  } else {
    console.error('Insert error:', error);
  }
}
```

**Transactions**:
```javascript
const session = client.startSession();
try {
  await session.withTransaction(async () => {
    await collection1.insertOne({...}, {session});
    await collection2.updateOne({...}, {...}, {session});
  });
} finally {
  await session.endSession();
}
```

### 68. List popular libraries to integrate with MongoDB?

**Node.js**:
- **mongodb**: Official Node.js driver
- **mongoose**: ODM with schema validation
- **monk**: Simplified MongoDB wrapper
- **mongoist**: Promises-based wrapper

**Python**:
- **pymongo**: Official Python driver
- **motor**: Async Python driver
- **mongoengine**: ODM for Python
- **ming**: MongoDB ORM
- **umongo**: marshmallow-based ODM

**Java**:
- **MongoDB Java Driver**: Official driver
- **Morphia**: Type-safe ODM
- **Spring Data MongoDB**: Spring integration
- **Jongo**: Query in Java as in Mongo shell

**C#/.NET**:
- **MongoDB.Driver**: Official .NET driver
- **MongoFramework**: Entity Framework-like ODM
- **MongoDB.Entities**: Simplified .NET ODM

**PHP**:
- **mongodb**: Official PHP driver
- **Doctrine MongoDB ODM**: ODM for PHP
- **Laravel MongoDB**: Laravel integration

**Ruby**:
- **mongo-ruby-driver**: Official Ruby driver
- **Mongoid**: ODM for Ruby/Rails
- **MongoMapper**: ActiveRecord-style ODM

**Go**:
- **mongo-go-driver**: Official Go driver
- **mgo**: Community Go driver (deprecated)

**Additional Tools**:
- **Mongoose Aggregate Paginate**: Pagination
- **mongoose-autopopulate**: Auto-population
- **mongoose-bcrypt**: Password hashing
- **mongoose-paginate-v2**: Advanced pagination

**Example with Express.js**:
```javascript
const express = require('express');
const { MongoClient } = require('mongodb');

const app = express();
const client = new MongoClient('mongodb://localhost:27017');

app.get('/users', async (req, res) => {
  const db = client.db('myDatabase');
  const users = await db.collection('users').find().toArray();
  res.json(users);
});

app.listen(3000);
```

## MongoDB and Big Data

### 69. How is MongoDB used in big data analytics?

**Use Cases**:

1. **Real-Time Analytics**:
```javascript
// Aggregation pipeline for analytics
db.events.aggregate([
  {$match: {
    timestamp: {$gte: new Date(Date.now() - 3600000)}
  }},
  {$group: {
    _id: {
      event: "$event_type",
      hour: {$hour: "$timestamp"}
    },
    count: {$sum: 1},
    avgDuration: {$avg: "$duration"}
  }},
  {$sort: {count: -1}}
])
```

2. **Log Analytics**:
- Store application logs
- Analyze patterns and trends
- Identify errors and anomalies

3. **IoT Data Storage**:
- Time-series data from sensors
- Device telemetry
- High-volume writes

4. **User Behavior Analytics**:
```javascript
// Track user sessions
db.sessions.aggregate([
  {$match: {date: {$gte: ISODate("2025-01-01")}}},
  {$group: {
    _id: "$user_id",
    totalSessions: {$sum: 1},
    avgDuration: {$avg: "$duration"},
    pages: {$addToSet: "$pages"}
  }}
])
```

**Integration with Big Data Tools**:

**Hadoop/Spark**:
```python
# PySpark with MongoDB
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MongoDB-Spark") \
    .config("spark.mongodb.input.uri", "mongodb://localhost/db.collection") \
    .config("spark.mongodb.output.uri", "mongodb://localhost/db.collection") \
    .getOrCreate()

# Read from MongoDB
df = spark.read.format("mongo").load()

# Process data
result = df.groupBy("category").count()

# Write back to MongoDB
result.write.format("mongo").mode("append").save()
```

**MongoDB Connector for Apache Kafka**:
```javascript
// Stream changes to Kafka
db.collection.watch().on('change', (change) => {
  kafkaProducer.send({
    topic: 'mongodb-changes',
    messages: [JSON.stringify(change)]
  });
});
```

**Analytics Features**:

**Time-Series Collections**:
```javascript
db.createCollection("sensor_data", {
  timeseries: {
    timeField: "timestamp",
    metaField: "sensor_id",
    granularity: "seconds"
  }
})
```

**Materialized Views**:
```javascript
db.createView(
  "daily_stats",
  "events",
  [
    {$group: {
      _id: {$dateToString: {format: "%Y-%m-%d", date: "$timestamp"}},
      count: {$sum: 1}
    }}
  ]
)
```

**Atlas Data Lake**:
- Query data across MongoDB and AWS S3
- Federated queries
- Cost-effective analytics on historical data

**Advantages for Big Data**:
- Flexible schema for varied data
- Horizontal scalability through sharding
- High write throughput
- Real-time query capabilities
- Integration with analytics tools

# MongoDB Interview Questions and Answers

### 70. Can MongoDB handle real-time data analytics workload?

Yes, MongoDB can handle real-time data analytics workloads effectively through:
- **Aggregation Pipeline**: Processes data in real-time with stages like $match, $group, $sort
- **Change Streams**: Allows applications to access real-time data changes
- **Indexing**: Speeds up query performance for analytics
- **In-Memory Storage Engine**: Provides high-speed data access
- **Atlas Analytics Nodes**: Dedicated nodes for analytical workloads without impacting operational performance

### 71. How do you stream large quantities of data into and out of MongoDB?

**Streaming Data Into MongoDB:**
- Use bulk write operations (insertMany, bulkWrite)
- Implement batch processing with proper batch sizes
- Use MongoDB connectors (Kafka Connector, Spark Connector)
- Implement change data capture (CDC) tools
- Use mongoimport for file-based imports

**Streaming Data Out:**
- Use Change Streams to capture real-time changes
- Implement cursor-based iteration for large result sets
- Use aggregation pipeline with $out or $merge
- Export using mongoexport
- Integrate with streaming platforms like Kafka or Apache Flink

### 72. How does MongoDB handle locking and concurrency?

MongoDB uses document-level locking:
- **WiredTiger Storage Engine**: Implements optimistic concurrency control with document-level locks
- **Read/Write Locks**: Multiple readers can access simultaneously, but writes lock at document level
- **Intent Locks**: Used at database and collection levels to indicate intended operations
- **Lock Yielding**: Long-running operations yield locks periodically
- **MVCC (Multi-Version Concurrency Control)**: Provides snapshot isolation for reads

### 73. What is the relationship between BSON and MongoDB?

BSON (Binary JSON) is MongoDB's native data format:
- **Binary Encoding**: More efficient than JSON for storage and transmission
- **Extended Data Types**: Supports types not in JSON (Date, ObjectId, Binary, Decimal128)
- **Traversable**: Can be scanned efficiently without full parsing
- **Size-Prefixed**: Each element has size information for quick skipping
- MongoDB stores all documents as BSON internally

### 74. Explain the concept of cursor in MongoDB?

A cursor is a pointer to the result set of a query:
- **Batch Processing**: Returns documents in batches (default 101 documents in first batch)
- **Iteration**: Allows iterating through large result sets without loading all data
- **Timeout**: Cursors timeout after 10 minutes of inactivity (can be disabled with noCursorTimeout)
- **Methods**: hasNext(), next(), forEach()
- **Memory Efficient**: Doesn't load entire result set into memory

```javascript
const cursor = db.collection.find({});
while(cursor.hasNext()) {
    const doc = cursor.next();
    // process document
}
```

### 75. How does MongoDB manage memory?

MongoDB memory management includes:
- **WiredTiger Cache**: Default 50% of RAM minus 1GB, or 256MB minimum
- **Operating System Cache**: File system cache for frequently accessed data
- **Connection Memory**: Each connection uses memory (~1MB per connection)
- **Index Memory**: Indexes should fit in RAM for optimal performance
- **Memory-Mapped Files**: MMAPv1 engine uses memory-mapped files
- **Automatic Management**: WiredTiger automatically manages cache eviction

### 76. What are the best practices for securing a MongoDB instance?

**Security Best Practices:**
- Enable authentication and authorization
- Use Role-Based Access Control (RBAC)
- Enable encryption at rest and in transit (TLS/SSL)
- Run MongoDB with a dedicated user account
- Bind to specific IP addresses, not 0.0.0.0
- Enable auditing for compliance
- Regular security updates and patches
- Use firewall rules to restrict access
- Implement network segmentation
- Disable unused MongoDB features
- Regular backup and disaster recovery testing

### 77. How do you scale a MongoDB deployment?

**Vertical Scaling:**
- Increase CPU, RAM, or storage capacity
- Limited by hardware constraints

**Horizontal Scaling (Sharding):**
- Distribute data across multiple servers
- Choose appropriate shard key
- Add shards as data grows
- Use zone sharding for geo-distribution

**Read Scaling:**
- Add replica set members
- Route read operations to secondaries
- Use read preferences appropriately

### 78. What is Ops Manager in MongoDB?

Ops Manager is MongoDB's enterprise management platform:
- **Monitoring**: Real-time performance metrics and alerts
- **Backup**: Automated continuous backup and point-in-time recovery
- **Automation**: Automates deployment, upgrades, and configuration
- **Query Optimization**: Identifies slow queries and suggests indexes
- **On-Premise Solution**: Self-hosted alternative to Atlas
- **Integration**: Works with existing infrastructure

### 79. How do you troubleshoot a slow running query in MongoDB?

**Troubleshooting Steps:**
1. Use `explain()` to analyze query execution
2. Check if proper indexes exist
3. Review query plan for collection scans (COLLSCAN)
4. Enable profiler to identify slow queries
5. Check server resource utilization (CPU, memory, disk I/O)
6. Analyze query patterns and optimize schema
7. Review index usage with `db.collection.stats()`
8. Check for lock contention
9. Optimize aggregation pipeline stages
10. Consider sharding for large collections

```javascript
db.collection.find({field: value}).explain("executionStats")
```

### 80. What is the cause of MongoDB error E11000 duplicate key error?

This error occurs when:
- Attempting to insert a document with a duplicate `_id`
- Violating unique index constraints
- Bulk operations containing duplicate keys

**Solutions:**
- Ensure unique values for indexed fields
- Use `upsert: true` for update operations
- Handle duplicates in application logic
- Use `ordered: false` in bulk operations to continue after errors

### 81. How do you handle a scenario where MongoDB service doesn't start?

**Troubleshooting Steps:**
1. Check MongoDB log files (`/var/log/mongodb/mongod.log`)
2. Verify port availability (27017 not in use)
3. Check disk space availability
4. Verify data directory permissions
5. Review configuration file for errors
6. Check if lock file exists and remove if stale (`mongod.lock`)
7. Repair database if corrupted: `mongod --repair`
8. Verify network configuration and firewall rules
9. Check system resource limits (ulimit)
10. Review recent changes or updates

### 82. What are some MongoDB cloud hosted solutions?

**Popular Cloud Solutions:**
- **MongoDB Atlas**: Official MongoDB cloud platform (AWS, Azure, GCP)
- **AWS DocumentDB**: MongoDB-compatible service
- **Azure Cosmos DB**: Multi-model database with MongoDB API
- **Google Cloud Platform**: MongoDB on Compute Engine/Kubernetes
- **IBM Cloud Databases for MongoDB**
- **DigitalOcean Managed MongoDB**
- **ScaleGrid**: Multi-cloud MongoDB hosting

### 83. How does MongoDB Atlas enhance MongoDB capability?

Atlas provides:
- **Automated Operations**: Automatic backups, updates, and scaling
- **Global Clusters**: Multi-region deployments with low latency
- **Serverless**: Pay-per-use pricing model
- **Full-Text Search**: Integrated search capabilities
- **Data Lake**: Query data from Atlas and S3
- **Charts**: Built-in data visualization
- **Triggers**: Database event-driven functions
- **App Services**: Backend-as-a-Service functionality
- **Performance Advisor**: Automated optimization suggestions
- **Security Features**: Encryption, network isolation, compliance

### 84. Describe the use of Atlas in MongoDB?

MongoDB Atlas is a fully managed cloud database service:
- **Database Deployment**: Deploy clusters in minutes
- **Monitoring**: Real-time performance metrics and alerts
- **Backup and Recovery**: Continuous backups with point-in-time recovery
- **Security**: Built-in encryption, VPC peering, IP whitelisting
- **Scalability**: Automatic or manual scaling
- **Multi-Cloud**: Deploy across AWS, Azure, and GCP
- **Developer Tools**: Integration with IDEs and CI/CD pipelines
- **Analytics**: Built-in analytics nodes for reporting

### 85. Explain the use of Robo 3T?

Robo 3T (formerly Robomongo) is a MongoDB GUI client:
- **Shell-Centric**: Embedded MongoDB shell
- **Cross-Platform**: Works on Windows, macOS, Linux
- **Connection Management**: Manage multiple MongoDB connections
- **Query Building**: Visual query builder
- **JSON View**: View documents in tree or text mode
- **Auto-Completion**: IntelliSense for MongoDB commands
- **Free and Open Source**: Community edition available
- **Lightweight**: Minimal resource footprint

### 86. Can you work with MongoDB with command line? If yes, how?

Yes, using the MongoDB Shell (mongosh):

```bash
# Connect to MongoDB
mongosh "mongodb://localhost:27017"

# Use a database
use myDatabase

# Insert document
db.users.insertOne({name: "John", age: 30})

# Query documents
db.users.find({age: {$gt: 25}})

# Update document
db.users.updateOne({name: "John"}, {$set: {age: 31}})

# Delete document
db.users.deleteOne({name: "John"})

# Create index
db.users.createIndex({email: 1}, {unique: true})

# Show collections
show collections

# Show databases
show dbs
```

### 87. What factors to consider when deploying a containerized MongoDB environment?

**Key Considerations:**
- **Persistent Storage**: Use volumes for data persistence
- **Resource Limits**: Set appropriate CPU and memory limits
- **Networking**: Configure proper port mapping and service discovery
- **Security**: Use secrets for credentials, enable authentication
- **Backup Strategy**: Implement backup solutions for containers
- **Orchestration**: Use Kubernetes StatefulSets for replica sets
- **Monitoring**: Implement container-aware monitoring
- **Health Checks**: Configure liveness and readiness probes
- **Data Migration**: Plan for data portability
- **Performance**: Consider storage driver performance impact

### 88. How does MongoDB work with microservice architecture?

MongoDB fits well with microservices:
- **Database per Service**: Each microservice can have its own MongoDB database
- **Schema Flexibility**: Supports independent schema evolution
- **Horizontal Scaling**: Sharding supports service-specific scaling
- **API Integration**: Easy integration via drivers and REST APIs
- **Change Streams**: Enable event-driven architecture
- **Aggregation**: Supports service-specific data processing
- **Replication**: Provides high availability per service
- **Document Model**: Aligns with microservice data ownership

### 89. What are change streams in MongoDB?

Change streams allow applications to access real-time data changes:
- **Real-Time Updates**: Subscribe to insert, update, delete, replace operations
- **Resumable**: Can resume from a specific point after disconnection
- **Cluster-Wide**: Can watch entire cluster, database, or collection
- **Filtering**: Use aggregation pipeline to filter events
- **Ordered**: Changes delivered in order they occurred

```javascript
const changeStream = db.collection.watch();
changeStream.on('change', (change) => {
    console.log('Change detected:', change);
});
```

**Use Cases:**
- Real-time notifications
- Data synchronization
- Audit logging
- Cache invalidation

### 90. What are the major features added in latest MongoDB releases?

**Recent Major Features (MongoDB 5.x - 7.x):**
- **Time Series Collections**: Optimized for time-stamped data
- **Queryable Encryption**: Field-level encryption with querying
- **Clustered Collections**: Store data ordered by _id
- **Native Date Arithmetic**: $dateAdd, $dateSubtract operators
- **Window Functions**: $setWindowFields for analytics
- **Versioned API**: Stable API for applications
- **Atlas Search**: Integrated full-text search
- **Aggregation Improvements**: New operators and optimizations
- **Enhanced Sharding**: Improved balancer and chunk operations
- **Multi-Document ACID Transactions**: Enhanced transaction support

### 91. How does MongoDB handle version upgrades in production environment?

**Upgrade Process:**
1. **Review Release Notes**: Check compatibility and breaking changes
2. **Test in Staging**: Thoroughly test in non-production environment
3. **Backup Data**: Complete backup before upgrade
4. **Rolling Upgrade**: Upgrade replica set members one at a time
   - Upgrade secondaries first
   - Step down primary and upgrade last
5. **Feature Compatibility Version**: Set after all nodes upgraded
6. **Monitor Performance**: Watch for issues post-upgrade
7. **Downgrade Plan**: Have rollback strategy ready

```javascript
// Check version
db.version()

// Set feature compatibility
db.adminCommand({setFeatureCompatibilityVersion: "6.0"})
```

### 92. In what scenarios is MongoDB favorable over MySQL?

**MongoDB is Better For:**
- **Flexible Schema**: Rapid development with changing requirements
- **Hierarchical Data**: Nested/embedded documents
- **Horizontal Scaling**: Sharding for massive datasets
- **Real-Time Analytics**: Aggregation pipeline
- **Content Management**: Document-centric applications
- **IoT Applications**: High write throughput
- **Catalog Management**: Product catalogs with varying attributes
- **JSON/BSON Data**: Native JSON support

**MySQL is Better For:**
- Complex multi-table joins
- Strong ACID requirements across tables
- Mature ecosystem and tooling
- Structured, relational data

### 93. What are some common patterns of data access in MongoDB applications?

**Common Patterns:**
- **Embedding**: Store related data in single document
- **Referencing**: Store references to documents in other collections
- **Bucket Pattern**: Group documents into buckets (time series)
- **Outlier Pattern**: Handle exceptional cases separately
- **Computed Pattern**: Pre-calculate and store aggregated values
- **Subset Pattern**: Store frequently accessed data in main document
- **Extended Reference Pattern**: Duplicate frequently accessed fields
- **Approximation Pattern**: Use approximations for large counts
- **Tree/Graph Pattern**: Model hierarchical relationships
- **Polymorphic Pattern**: Store documents with different schemas in one collection

### 94. How can you prevent slow queries in MongoDB?

**Prevention Strategies:**
1. **Create Appropriate Indexes**: Index frequently queried fields
2. **Use Covered Queries**: Return only indexed fields
3. **Limit Result Sets**: Use limit() and projection
4. **Optimize Aggregation**: Place $match early in pipeline
5. **Avoid Large Documents**: Keep documents reasonably sized
6. **Use Profiler**: Identify and optimize slow queries
7. **Regular Index Maintenance**: Remove unused indexes
8. **Schema Design**: Embed frequently accessed data
9. **Connection Pooling**: Reduce connection overhead
10. **Monitor Working Set**: Ensure indexes fit in RAM

### 95. Explain the role of profiler in MongoDB?

The database profiler collects query execution data:
- **Profiling Levels**:
  - 0: Profiler off
  - 1: Log slow operations (threshold-based)
  - 2: Log all operations

```javascript
// Enable profiler for slow queries (>100ms)
db.setProfilingLevel(1, 100)

// View profiled queries
db.system.profile.find().sort({ts: -1}).limit(5)

// Disable profiler
db.setProfilingLevel(0)
```

**Usage:**
- Identify slow queries
- Analyze query patterns
- Optimize index strategy
- Debug performance issues

### 96. How are B-tree indexes implemented in MongoDB?

MongoDB uses B-tree indexes:
- **Balanced Tree Structure**: All leaf nodes at same level
- **Sorted Order**: Keys stored in sorted order
- **Efficient Searches**: O(log n) search time
- **Range Queries**: Efficient range scans
- **Multiple Indexes**: Compound and multi-key indexes supported
- **WiredTiger**: Uses B+ tree variant
- **Index Entries**: Point to document locations
- **Prefix Compression**: Reduces index size

### 97. How do you handle complex transactions in MongoDB?

MongoDB supports multi-document ACID transactions:

```javascript
const session = db.getMongo().startSession();
session.startTransaction();

try {
    const accountsCol = session.getDatabase('bank').accounts;
    
    // Debit from account A
    accountsCol.updateOne(
        {account: "A"},
        {$inc: {balance: -100}},
        {session}
    );
    
    // Credit to account B
    accountsCol.updateOne(
        {account: "B"},
        {$inc: {balance: 100}},
        {session}
    );
    
    session.commitTransaction();
} catch (error) {
    session.abortTransaction();
} finally {
    session.endSession();
}
```

**Best Practices:**
- Keep transactions short
- Use appropriate write concerns
- Handle transaction errors properly
- Prefer document model to minimize transactions

### 98. Explain the MongoDB MapReduce operation?

MapReduce processes large datasets (deprecated in favor of aggregation):

```javascript
db.collection.mapReduce(
    // Map function
    function() {
        emit(this.category, this.price);
    },
    // Reduce function
    function(key, values) {
        return Array.sum(values);
    },
    {
        out: "result_collection",
        query: {status: "active"}
    }
)
```

**Components:**
- **Map**: Emits key-value pairs
- **Reduce**: Aggregates values for each key
- **Finalize**: Optional final processing

**Note**: Aggregation pipeline is now preferred for better performance.

### 99. Can you perform text search in MongoDB?

Yes, using text indexes:

```javascript
// Create text index
db.articles.createIndex({title: "text", content: "text"})

// Search
db.articles.find({$text: {$search: "mongodb database"}})

// Search with score
db.articles.find(
    {$text: {$search: "mongodb"}},
    {score: {$meta: "textScore"}}
).sort({score: {$meta: "textScore"}})

// Exact phrase search
db.articles.find({$text: {$search: "\"exact phrase\""}})

// Exclude words
db.articles.find({$text: {$search: "mongodb -sql"}})
```

**Features:**
- Language-specific stemming
- Case-insensitive search
- Diacritic-insensitive
- Stop word filtering
- Text score ranking

### 100. How can you integrate MongoDB with 3rd party applications?

**Integration Methods:**
1. **Native Drivers**: Official drivers for various languages
2. **REST APIs**: Create REST endpoints using frameworks
3. **GraphQL**: Use tools like Apollo Server
4. **ETL Tools**: Talend, Apache NiFi, Pentaho
5. **BI Tools**: Tableau, Power BI, Looker
6. **Messaging Systems**: Kafka Connect, RabbitMQ
7. **ODM/ORM**: Mongoose, Spring Data MongoDB
8. **Webhooks**: MongoDB Realm triggers
9. **Change Streams**: Real-time data synchronization
10. **Atlas Data API**: HTTP-based data access

### 101. Describe how to synchronize data between MongoDB and MySQL?

**Synchronization Approaches:**

**1. Change Data Capture (CDC):**
- Use MongoDB Change Streams
- Capture changes and write to MySQL
- Tools: Debezium, Maxwell

**2. ETL Tools:**
- Apache NiFi
- Talend
- Pentaho Data Integration

**3. Custom Sync Scripts:**
```javascript
// MongoDB Change Stream
const changeStream = db.collection.watch();
changeStream.on('change', async (change) => {
    if (change.operationType === 'insert') {
        // Insert into MySQL
        await mysqlConnection.query(
            'INSERT INTO table VALUES (?)', 
            [change.fullDocument]
        );
    }
});
```

**4. Third-Party Services:**
- Fivetran
- Stitch Data
- Airbyte

**5. Considerations:**
- Schema mapping
- Data type conversion
- Conflict resolution
- Performance impact
- Monitoring and error handling

---
