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

# MongoDB Interview Questions - Complete Guide

## MongoDB Fundamentals

### 1. What is MongoDB and what are its main features?

MongoDB is a NoSQL, document-oriented database that stores data in flexible, JSON-like documents. Main features include:
- Document-oriented storage (BSON format)
- Dynamic schema design
- High performance and scalability
- Horizontal scalability through sharding
- Replication and high availability
- Rich query language with aggregation framework
- Support for geospatial queries
- Auto-sharding capabilities
- Built-in map-reduce functionality

### 2. How does MongoDB differ from relational databases?

Key differences include:
- **Schema**: MongoDB has flexible schema vs fixed schema in RDBMS
- **Data Model**: Document-based vs table-based with rows and columns
- **Relationships**: Embedded documents or references vs foreign keys and joins
- **Scalability**: Horizontal scaling (sharding) vs primarily vertical scaling
- **Query Language**: MongoDB query language vs SQL
- **Transactions**: Multi-document ACID transactions (v4.0+) vs traditional ACID
- **Performance**: Better for unstructured data and rapid development

### 3. Can you describe structure of data in MongoDB?

MongoDB data structure hierarchy:
- **Database**: Container for collections
- **Collection**: Group of MongoDB documents (analogous to table)
- **Document**: A record in BSON format (analogous to row)
- **Field**: Key-value pair within a document (analogous to column)
- **Embedded Documents**: Nested documents within documents
- **Arrays**: Can contain multiple values or embedded documents

### 4. What is a document in MongoDB?

A document is a basic unit of data in MongoDB, similar to a row in RDBMS. It is stored in BSON (Binary JSON) format and consists of field-value pairs. Documents have:
- Dynamic schema (fields can vary between documents)
- Maximum size of 16MB
- Unique `_id` field
- Support for various data types including nested documents and arrays

Example:
```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John Doe",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York"
  },
  hobbies: ["reading", "gaming"]
}
```

### 5. How data are stored in collections in MongoDB?

Collections store documents and have these characteristics:
- Documents within a collection can have different structures
- No schema enforcement by default (can be enabled with validation rules)
- Indexed for efficient querying
- Stored in a single database
- Collection names are case-sensitive
- Cannot contain null characters or start with "system."

### 6. Describe what MongoDB database is?

A MongoDB database is a physical container for collections. Each database:
- Has its own set of files on the file system
- Can contain multiple collections
- Has separate authentication and authorization
- Default databases include `admin`, `local`, and `config`
- Database names are case-insensitive but best practice is lowercase

### 7. What is default port on which MongoDB listens?

The default port for MongoDB is **27017**. Additional related ports:
- 27018: Used by shards
- 27019: Used by config servers
- 28017: HTTP status interface (deprecated)

### 8. How does MongoDB provide high availability and disaster recovery?

MongoDB provides HA and DR through:
- **Replica Sets**: Multiple copies of data across servers
- **Automatic Failover**: Primary election when primary node fails
- **Data Redundancy**: Multiple data copies across nodes
- **Oplog**: Operation log for replication
- **Backup Solutions**: mongodump, filesystem snapshots, Atlas backups
- **Point-in-Time Recovery**: Available in enterprise edition
- **Geographically Distributed Replicas**: For disaster recovery

### 9. What are indexes in MongoDB and why they are used?

Indexes are special data structures that store a small portion of data for efficient queries. They:
- Improve query performance significantly
- Reduce query execution time
- Support efficient sorting
- Enable unique constraints
- Can be single field, compound, multikey, text, or geospatial
- Trade-off: Improve read performance but add overhead to writes

### 10. What is the role of _id in MongoDB document?

The `_id` field:
- Serves as the primary key for documents
- Must be unique within a collection
- Automatically created if not provided (as ObjectId)
- Immutable once set
- Can be any BSON type except arrays
- Automatically indexed
- ObjectId contains timestamp, machine ID, process ID, and counter

## CRUD Operations

### 11. How do you create a new MongoDB collection?

Collections are created implicitly when you insert data, or explicitly:

```javascript
// Implicit creation
db.myCollection.insertOne({name: "test"})

// Explicit creation
db.createCollection("myCollection")

// With options
db.createCollection("myCollection", {
  capped: true,
  size: 100000,
  max: 5000,
  validator: { $jsonSchema: {...} }
})
```

### 12. What is the syntax to insert a new document in MongoDB?

```javascript
// Insert one document
db.collection.insertOne({
  name: "John",
  age: 30
})

// Insert multiple documents
db.collection.insertMany([
  {name: "John", age: 30},
  {name: "Jane", age: 25}
])

// Legacy insert (deprecated)
db.collection.insert({name: "John"})
```

### 13. How do you read data from a MongoDB collection?

```javascript
// Find all documents
db.collection.find()

// Find with filter
db.collection.find({age: {$gt: 25}})

// Find with projection
db.collection.find({}, {name: 1, age: 1, _id: 0})

// Find one document
db.collection.findOne({name: "John"})

// With sorting and limiting
db.collection.find().sort({age: -1}).limit(10)
```

### 14. Explain how to update data in MongoDB?

```javascript
// Update one document
db.collection.updateOne(
  {name: "John"},
  {$set: {age: 31}}
)

// Update multiple documents
db.collection.updateMany(
  {status: "pending"},
  {$set: {status: "processed"}}
)

// Replace entire document
db.collection.replaceOne(
  {name: "John"},
  {name: "John", age: 31, city: "NYC"}
)

// Update with upsert
db.collection.updateOne(
  {name: "Mike"},
  {$set: {age: 28}},
  {upsert: true}
)
```

### 15. What are MongoDB commands to delete documents?

```javascript
// Delete one document
db.collection.deleteOne({name: "John"})

// Delete multiple documents
db.collection.deleteMany({status: "inactive"})

// Delete all documents
db.collection.deleteMany({})

// Remove (deprecated)
db.collection.remove({name: "John"})

// Drop entire collection
db.collection.drop()
```

### 16. Can you join 2 collections in MongoDB? If yes how?

Yes, using `$lookup` aggregation operator:

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customerDetails"
    }
  }
])

// With pipeline (v3.6+)
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      let: { customerId: "$customerId" },
      pipeline: [
        { $match: { $expr: { $eq: ["$_id", "$$customerId"] } } }
      ],
      as: "customerDetails"
    }
  }
])
```

### 17. How can you limit the number of documents returned by MongoDB query?

```javascript
// Limit to 10 documents
db.collection.find().limit(10)

// Skip first 20 and limit to 10
db.collection.find().skip(20).limit(10)

// With sorting
db.collection.find().sort({createdAt: -1}).limit(5)
```

### 18. What is the difference between find and findOne in MongoDB?

- **find()**: Returns a cursor to all matching documents
  - Can retrieve multiple documents
  - Returns cursor object
  - Requires iteration
  
- **findOne()**: Returns a single document
  - Returns only first matching document
  - Returns document object or null
  - No need for iteration
  - More efficient for single document retrieval

### 19. How can you achieve pagination in MongoDB?

```javascript
// Method 1: Using skip and limit
const page = 2;
const pageSize = 10;
db.collection.find()
  .skip((page - 1) * pageSize)
  .limit(pageSize)

// Method 2: Range query (more efficient)
db.collection.find({
  _id: { $gt: lastSeenId }
}).limit(10)

// Method 3: Using aggregation
db.collection.aggregate([
  { $skip: (page - 1) * pageSize },
  { $limit: pageSize }
])
```

### 20. What is the difference between insertOne and insertMany method in MongoDB?

- **insertOne()**:
  - Inserts a single document
  - Returns inserted document's _id
  - Faster for single inserts
  
- **insertMany()**:
  - Inserts multiple documents in one operation
  - More efficient than multiple insertOne calls
  - Can be ordered (stops on error) or unordered (continues on error)
  - Returns array of inserted _ids
  - Supports bulk write optimization

```javascript
// insertOne
db.collection.insertOne({name: "John"})

// insertMany
db.collection.insertMany([
  {name: "John"},
  {name: "Jane"}
], {ordered: false})
```

### 21. What happens when a bulk or insert/delete/update operation fails in middle of operation?

Behavior depends on operation mode:

**Ordered Operations** (default):
- Stops at first error
- Documents before error are processed
- Documents after error are not processed
- Returns error information

**Unordered Operations**:
- Continues processing despite errors
- All documents attempted
- Collects all errors
- More efficient for large batches

```javascript
db.collection.insertMany([...], {ordered: false})
```

### 22. What is the difference between updateMany/deleteMany and bulk operation?

**updateMany/deleteMany**:
- Single operation type
- Simpler syntax
- One filter condition
- Automatic optimization

**Bulk Operations**:
- Multiple operation types in one call
- Can mix inserts, updates, deletes
- Multiple filter conditions
- More control over execution
- Better performance for mixed operations

```javascript
// Bulk operations
const bulk = db.collection.initializeOrderedBulkOp();
bulk.insert({name: "John"});
bulk.find({age: {$lt: 18}}).update({$set: {minor: true}});
bulk.find({status: "deleted"}).remove();
bulk.execute();
```

## Indexing and Aggregation

### 23. Describe compound indexing in MongoDB?

Compound indexes include multiple fields in a single index:

```javascript
// Create compound index
db.collection.createIndex({
  lastName: 1,
  firstName: 1,
  age: -1
})
```

**Characteristics**:
- Order of fields matters (index prefix rule)
- Supports queries on prefix combinations
- Can optimize sorting
- 1 for ascending, -1 for descending
- Maximum 32 fields per index
- More efficient than multiple single-field indexes

**Index Prefix Rule**: Index on {a:1, b:1, c:1} supports queries on:
- {a}
- {a, b}
- {a, b, c}
But NOT {b} or {c} alone

### 24. What is aggregation pipeline in MongoDB?

The aggregation pipeline processes documents through multiple stages, with each stage transforming the documents:

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { 
      _id: "$customerId", 
      total: { $sum: "$amount" } 
  }},
  { $sort: { total: -1 } },
  { $limit: 10 }
])
```

**Common stages**:
- $match: Filter documents
- $group: Group by field(s)
- $project: Reshape documents
- $sort: Sort documents
- $limit/$skip: Pagination
- $lookup: Join collections
- $unwind: Deconstruct arrays
- $addFields: Add new fields

### 25. How can you create an index in MongoDB and when should you do it?

**Creating indexes**:
```javascript
// Single field index
db.collection.createIndex({fieldName: 1})

// Compound index
db.collection.createIndex({field1: 1, field2: -1})

// Unique index
db.collection.createIndex({email: 1}, {unique: true})

// Sparse index
db.collection.createIndex({phone: 1}, {sparse: true})

// TTL index
db.collection.createIndex({createdAt: 1}, {expireAfterSeconds: 3600})

// Text index
db.collection.createIndex({description: "text"})
```

**When to create indexes**:
- Frequently queried fields
- Fields used in sorting
- Fields used in joins
- Unique constraints needed
- Before large data imports
- When query performance is poor
- Fields used in range queries

**Avoid over-indexing**: Each index adds write overhead

### 26. Explain how match, group and sort operations work in aggregation pipeline?

**$match**: Filters documents (like WHERE clause)
```javascript
{ $match: { 
  status: "active", 
  age: { $gte: 18 } 
}}
```
- Place early in pipeline for efficiency
- Uses indexes if first stage
- Reduces documents for subsequent stages

**$group**: Groups documents by expression
```javascript
{ $group: {
  _id: "$category",
  count: { $sum: 1 },
  avgPrice: { $avg: "$price" },
  total: { $sum: "$quantity" }
}}
```
- _id field defines grouping key
- Accumulator operators: $sum, $avg, $min, $max, $push

**$sort**: Orders documents
```javascript
{ $sort: { 
  totalSales: -1,  // -1 for descending
  name: 1          // 1 for ascending
}}
```
- Can use index if early in pipeline
- Memory limit of 100MB (use allowDiskUse: true)

### 27. What is the purpose of Explain method?

The `explain()` method provides query execution information:

```javascript
db.collection.find({age: 30}).explain("executionStats")
```

**Modes**:
- **queryPlanner**: Shows winning plan
- **executionStats**: Execution statistics
- **allPlansExecution**: All candidate plans

**Key information**:
- Query execution time
- Index usage
- Documents examined vs returned
- Execution stages
- Query optimization decisions

**Use for**:
- Query performance analysis
- Index effectiveness
- Identifying slow queries
- Optimization decisions

## Replication and Sharding

### 28. Can you explain replication in MongoDB?

Replication maintains multiple copies of data across servers:

**Components**:
- **Primary**: Receives all write operations
- **Secondary**: Replicates primary's data
- **Arbiter**: Votes in elections (no data)

**Process**:
1. Writes go to primary
2. Operations recorded in oplog
3. Secondaries replicate oplog
4. Automatic failover if primary fails

**Benefits**:
- High availability
- Data redundancy
- Read scalability
- Disaster recovery
- Zero-downtime maintenance

### 29. Explain purpose and components of replica set?

A replica set is a group of MongoDB instances maintaining the same data:

**Components**:
- **Primary Node**: Handles all writes
- **Secondary Nodes**: Replicate primary data, can serve reads
- **Arbiter**: Participates in elections only (optional)

**Configuration**:
```javascript
rs.initiate({
  _id: "myReplicaSet",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})
```

**Purposes**:
- Automatic failover
- Data redundancy
- Read scaling
- Geographic distribution
- Maintenance without downtime

### 30. What is sharding in MongoDB and when it should be used?

Sharding distributes data across multiple machines:

**Components**:
- **Shard**: Subset of data
- **Config Servers**: Store metadata
- **Mongos**: Query router

**When to use**:
- Dataset exceeds single server capacity
- Working set exceeds RAM
- High throughput requirements
- Geographic data distribution needed
- Vertical scaling is insufficient

**Shard Key**: Field used to distribute data
```javascript
sh.shardCollection("mydb.collection", {userId: 1})
```

**Considerations**:
- Choose shard key carefully (immutable)
- Ensure even distribution
- Consider query patterns
- Adds complexity

### 31. How does MongoDB perform automatic failover?

**Failover Process**:

1. **Detection**: Heartbeat monitors detect primary failure (default 10 seconds)
2. **Election**: Remaining members vote for new primary
3. **Promotion**: Secondary with highest priority and most recent data becomes primary
4. **Notification**: Clients reconnect to new primary
5. **Recovery**: Old primary rejoins as secondary

**Election factors**:
- Member priority (0-1000)
- Data recency
- Network connectivity
- Arbiter votes (if present)

**Timing**:
- Detection: ~10 seconds
- Election: ~12 seconds
- Total: ~20-30 seconds typical

**Requirements**:
- Minimum 3 members for automatic failover
- Majority must be available
- Network connectivity between members

### 32. Explain the difference between horizontal and vertical scaling and how MongoDB supports that?

**Vertical Scaling** (Scale Up):
- Add more resources to single server (CPU, RAM, storage)
- MongoDB support: Runs on larger machines
- Limitations: Hardware limits, single point of failure
- Simpler but less flexible

**Horizontal Scaling** (Scale Out):
- Add more servers to distribute load
- MongoDB support: Sharding, replica sets
- Benefits: Virtually unlimited scaling, better availability
- More complex but highly scalable

**MongoDB's Approach**:
- **Replication**: High availability, read scaling
- **Sharding**: Data distribution, write scaling
- **Combination**: Both for optimal performance

```javascript
// Sharding configuration
sh.enableSharding("mydb")
sh.shardCollection("mydb.users", {userId: "hashed"})
```

## Performance and Optimization

### 33. How MongoDB handles large data volumes?

**Strategies**:

1. **Sharding**: Horizontal data partitioning
2. **Indexing**: Efficient data access
3. **Compression**: WiredTiger compression
4. **Working Set Management**: Keep frequently accessed data in RAM
5. **Document Size Limits**: 16MB max per document
6. **GridFS**: For files >16MB
7. **Aggregation Pipeline**: Efficient data processing
8. **Connection Pooling**: Reuse connections

**Best Practices**:
- Design schema for access patterns
- Use appropriate indexes
- Monitor working set size
- Scale horizontally when needed
- Use bulk operations
- Implement data archiving

### 34. What techniques you use to diagnose and address performance issues in MongoDB?

**Diagnostic Tools**:

1. **Database Profiler**:
```javascript
db.setProfilingLevel(2) // Profile all operations
db.system.profile.find().sort({ts: -1})
```

2. **Explain Plans**:
```javascript
db.collection.find({...}).explain("executionStats")
```

3. **Monitoring Tools**:
- mongostat: Real-time stats
- mongotop: Collection-level stats
- MongoDB Atlas monitoring
- CloudWatch/Prometheus integration

4. **Slow Query Log**: Analyze slow operations

**Solutions**:
- Add missing indexes
- Optimize queries
- Increase memory
- Adjust working set
- Scale horizontally
- Review schema design
- Use aggregation pipeline
- Implement caching

### 35. How do you ensure indexes fit into RAM?

**Monitoring**:
```javascript
db.collection.stats()
db.collection.totalIndexSize()
```

**Strategies**:

1. **Choose Selective Indexes**: Index high-cardinality fields
2. **Remove Unused Indexes**: Regular audit
3. **Use Prefix Compression**: Enabled in WiredTiger
4. **Compound Indexes**: Instead of multiple single-field indexes
5. **Partial Indexes**: Index subset of documents
```javascript
db.collection.createIndex(
  {status: 1},
  {partialFilterExpression: {status: "active"}}
)
```

6. **Monitor Index Size**: Use db.stats()
7. **Increase RAM**: If indexes are necessary
8. **Use Covered Queries**: Query only indexed fields

**Rule of Thumb**: Index size should be < available RAM for optimal performance

### 36. Can you explain MongoDB write concerns?

Write concern specifies acknowledgment level for write operations:

**Levels**:

```javascript
// w: 0 - Unacknowledged
db.collection.insertOne({...}, {writeConcern: {w: 0}})

// w: 1 - Acknowledged by primary (default)
db.collection.insertOne({...}, {writeConcern: {w: 1}})

// w: "majority" - Acknowledged by majority
db.collection.insertOne({...}, {writeConcern: {w: "majority"}})

// w: <number> - Acknowledged by n nodes
db.collection.insertOne({...}, {writeConcern: {w: 3}})

// With journal
db.collection.insertOne({...}, {
  writeConcern: {w: "majority", j: true, wtimeout: 5000}
})
```

**Parameters**:
- **w**: Number of nodes to acknowledge
- **j**: Journal sync (true/false)
- **wtimeout**: Max wait time in milliseconds

**Trade-offs**:
- Higher write concern = More durability, less performance
- Lower write concern = Better performance, less durability

### 37. What is covered query in MongoDB?

A covered query is satisfied entirely by an index without examining documents:

**Requirements**:
- All query fields in index
- All returned fields in index
- No field in _id unless explicitly included

**Example**:
```javascript
// Create index
db.users.createIndex({name: 1, age: 1})

// Covered query
db.users.find(
  {name: "John", age: 30},
  {name: 1, age: 1, _id: 0}
)
```

**Benefits**:
- Extremely fast (no disk I/O)
- Only index accessed
- Reduces memory usage
- Scalable performance

**Verification**:
```javascript
db.users.find(...).explain("executionStats")
// Look for "totalDocsExamined": 0
```

## MongoDB Security

### 38. What are the security features available in MongoDB?

**Authentication & Authorization**:
- SCRAM, LDAP, Kerberos, x.509
- Role-based access control (RBAC)
- Custom roles

**Encryption**:
- At-rest encryption
- In-transit encryption (TLS/SSL)
- Client-side field level encryption

**Network Security**:
- IP whitelisting
- VPC/VPN support
- Firewalls

**Auditing**:
- System event auditing
- Authentication logs
- Authorization logs

**Additional Features**:
- Redaction for sensitive data
- Security checklist
- MongoDB Security Architecture

### 39. How do you enable authentication in MongoDB?

**Steps**:

1. **Create Admin User**:
```javascript
use admin
db.createUser({
  user: "admin",
  pwd: "securePassword",
  roles: [{role: "userAdminAnyDatabase", db: "admin"}]
})
```

2. **Enable Authentication**:
Edit mongod.conf:
```yaml
security:
  authorization: enabled
```

Or start with flag:
```bash
mongod --auth --port 27017 --dbpath /data/db
```

3. **Restart MongoDB**

4. **Connect with Authentication**:
```bash
mongo -u admin -p securePassword --authenticationDatabase admin
```

5. **Create Database Users**:
```javascript
use myDatabase
db.createUser({
  user: "appUser",
  pwd: "password",
  roles: [{role: "readWrite", db: "myDatabase"}]
})
```

### 40. Explain role-based access control in MongoDB?

RBAC provides granular permissions through roles:

**Built-in Roles**:

**Database User Roles**:
- `read`: Read data
- `readWrite`: Read and write data

**Database Admin Roles**:
- `dbAdmin`: Schema, indexing
- `userAdmin`: User management
- `dbOwner`: All database privileges

**Cluster Admin Roles**:
- `clusterAdmin`: Full cluster access
- `clusterManager`: Cluster management
- `hostManager`: Server monitoring

**Backup Roles**:
- `backup`: Backup operations
- `restore`: Restore operations

**All-Database Roles**:
- `readAnyDatabase`
- `readWriteAnyDatabase`
- `userAdminAnyDatabase`
- `dbAdminAnyDatabase`

**Custom Roles**:
```javascript
db.createRole({
  role: "customRole",
  privileges: [{
    resource: {db: "mydb", collection: "mycoll"},
    actions: ["find", "insert"]
  }],
  roles: []
})
```

**Assign Roles**:
```javascript
db.grantRolesToUser("username", ["readWrite", "dbAdmin"])
```

### 41. Explain how to encrypt data in MongoDB?

**1. Encryption at Rest**:

Configure in mongod.conf:
```yaml
security:
  enableEncryption: true
  encryptionKeyFile: /path/to/keyfile
```

Or with KMIP:
```yaml
security:
  enableEncryption: true
  kmip:
    serverName: kmip.example.com
    port: 5696
    clientCertificateFile: /path/to/client.pem
```

**2. Encryption in Transit (TLS/SSL)**:
```yaml
net:
  ssl:
    mode: requireSSL
    PEMKeyFile: /path/to/cert.pem
    CAFile: /path/to/ca.pem
```

**3. Client-Side Field Level Encryption**:
```javascript
const clientEncryption = new ClientEncryption(keyVault, kmsProviders);

// Encrypt field
const encryptedField = await clientEncryption.encrypt(
  sensitiveData,
  {
    algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
    keyId: dataKeyId
  }
);
```

**Key Management**:
- Local key file
- AWS KMS
- Azure Key Vault
- Google Cloud KMS
- KMIP servers

### 42. How do you setup MongoDB to use TLS/SSL connections?

**1. Generate Certificates**:
```bash
# Self-signed for testing
openssl req -newkey rsa:2048 -nodes -keyout mongodb.key \
  -x509 -days 365 -out mongodb.crt

# Combine key and cert
cat mongodb.key mongodb.crt > mongodb.pem
```

**2. Configure MongoDB**:
```yaml
# mongod.conf
net:
  port: 27017
  ssl:
    mode: requireSSL
    PEMKeyFile: /path/to/mongodb.pem
    CAFile: /path/to/ca.pem
    allowConnectionsWithoutCertificates: false
    allowInvalidCertificates: false
```

**3. Start MongoDB**:
```bash
mongod --config /etc/mongod.conf
```

**4. Connect with SSL**:
```bash
mongo --ssl --host mongodb.example.com \
  --sslCAFile /path/to/ca.pem \
  --sslPEMKeyFile /path/to/client.pem
```

**Connection String**:
```
mongodb://host:27017/db?ssl=true&sslCAFile=/path/ca.pem
```

## MongoDB Storage Engine

### 43. What different storage engines are available in MongoDB?

**1. WiredTiger** (Default since 3.2):
- Document-level concurrency
- Compression (snappy, zlib, none)
- Checkpoints for consistency
- Better performance
- Supports encryption at rest

**2. In-Memory**:
- Stores data in RAM
- No persistence
- Extremely fast
- For caching/testing
- Available in Enterprise

**3. MMAPv1** (Deprecated, removed in 4.2):
- Legacy storage engine
- Collection-level locking
- No compression
- Memory-mapped files

**Comparison**:
- WiredTiger: Best for production
- In-Memory: Caching, temporary data
- MMAPv1: Legacy (avoid)

### 44. How does WiredTiger storage engine differ from MMAPv1?

**WiredTiger**:
- Document-level concurrency control
- Compression support
- Better write performance
- Lower storage overhead
- Snapshots for point-in-time consistency
- Journaling enabled by default
- Cache management

**MMAPv1**:
- Collection-level locking
- No compression
- Higher storage usage
- Memory-mapped file approach
- Power-of-2 allocation
- Padding factor
- Deprecated and removed

**Performance**: WiredTiger significantly outperforms MMAPv1 in most scenarios

### 45. Can you switch between storage engines in MongoDB?

Yes, but requires data migration:

**Method 1: mongodump/mongorestore**:
```bash
# Backup with old engine
mongodump --out /backup

# Stop MongoDB
mongod --shutdown

# Remove old data
rm -rf /data/db/*

# Start with new engine
mongod --storageEngine wiredTiger

# Restore data
mongorestore /backup
```

**Method 2: Initial Sync via Replica Set**:
1. Add new member with desired storage engine
2. Let it sync
3. Step down primary
4. Remove old members
5. Repeat for all members

**Note**: Cannot directly switch storage engine on existing data files

## Advanced MongoDB Concepts

### 46. What is oplog in MongoDB and how it works?

The oplog (operations log) is a capped collection that records all write operations:

**Characteristics**:
- Located in `local.oplog.rs`
- Capped collection (fixed size)
- Stores operations in order
- Idempotent operations

**How it works**:
1. Write operation occurs on primary
2. Operation recorded in oplog
3. Secondaries read oplog from primary
4. Secondaries apply operations in order
5. Ensures consistency across replica set

**View oplog**:
```javascript
use local
db.oplog.rs.find().sort({$natural: -1}).limit(10)
```

**Size Considerations**:
- Default: 5% of free disk
- Should hold operations for maintenance window
- Too small: Secondaries can't catch up
- Resize with replSetResizeOplog command

**Oplog Entry Structure**:
```javascript
{
  ts: Timestamp,    // Operation timestamp
  h: NumberLong,    // Unique identifier
  v: 2,             // Oplog version
  op: "i",          // Operation type (i=insert, u=update, d=delete)
  ns: "db.collection",
  o: {...}          // Operation document
}
```

### 47. How do you use lookup operation in MongoDB?

The `$lookup` performs left outer join between collections:

**Basic Syntax**:
```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "