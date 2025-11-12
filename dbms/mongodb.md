update
lookup unwind
what is ordered/unordered insert
bulk & many in detail
gridfs


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
     
#  Architecture & Internals
101. What is the role of mongod, mongos, and config servers in a MongoDB cluster?

102. How does MongoDB manage journaling and checkpoints internally?

103. How does MongoDB write data to disk in WiredTiger?

104. What are write-ahead logs (WAL) in MongoDB?

105. Explain the difference between storage compression and index compression in WiredTiger.

# Performance Tuning

106. How would you identify and fix a performance bottleneck in MongoDB?

107. How do you decide which fields to index?

108. How do you detect index scans vs collection scans?

109. What are the performance implications of $lookup?

110. What are “hot” documents and how does MongoDB handle them?

#  Data Modeling (Real-world Scenarios)

111. How would you model user posts and comments (1:N relation)?

112. When would you use $lookup vs embedding?
113. How do you handle large arrays in MongoDB?
114. What are bucket pattern and subset pattern in schema design?
115. How do you design schema for time-series data in MongoDB?

#  Transactions & Concurrency

116. How are multi-document transactions implemented in MongoDB?
117. What are the limitations of MongoDB transactions?
118. How does MongoDB maintain ACID properties in a replica set?
119. How does optimistic concurrency control work in MongoDB?
120. How does snapshot isolation work in MongoDB?

# Aggregation Framework Deep Dive

121. Explain $facet and $bucket stages with examples.
122. What’s the difference between $group and $accumulator operators?
123. How can $merge be used to write aggregation results into another collection?
124. What is $graphLookup and when would you use it?
125. How can you optimize an aggregation pipeline?

#  Replica Set and Sharding

126. How do you force a MongoDB replica set failover?
127. What is the difference between primaryPreferred and secondaryPreferred read preferences?
128. How do you rebalance chunks in a sharded cluster?
129. What is a chunk migration and how does it affect performance?
130. How do you handle shard key selection and what are the best practices?

#  Backup, Restore & Monitoring

131. What’s the difference between mongodump and oplog-based backups?
132. How do you restore a specific collection from a dump?
133. How do you monitor replication lag?
134. What metrics do you track for MongoDB health?
135. How do you integrate MongoDB with Prometheus / Grafana for monitoring?

# Security & Compliance

136. What are MongoDB’s authentication mechanisms (SCRAM, x.509, LDAP, Kerberos)?
137. What are field-level and queryable encryption features in MongoDB 7.0+?
138. How do you implement IP whitelisting for MongoDB?
139. What is audit logging and how do you enable it?
140. What are MongoDB’s compliance certifications (HIPAA, GDPR, etc.)?

# Deployment & Cloud

141. What’s the difference between MongoDB Atlas, Ops Manager, and Enterprise Advanced?
142. How does auto-scaling work in Atlas?
143. How do you set up continuous backups in Atlas?
144. What is Atlas Data Federation?
145. How does MongoDB Atlas Search differ from regular text indexes?

# Tools & Ecosystem

146. What is Compass and how does it differ from Robo 3T?
147. What is MongoMirror used for?
148. How do you use mongostat and mongotop for performance monitoring?
149. What’s the use of mongoexport and mongoimport commands?
150. How do you automate MongoDB deployments using Terraform or Ansible?

# Bonus — Real Interview Scenarios

151. Describe a situation where you optimized a slow query.
152. How would you migrate a 500GB MongoDB database to a new cluster with minimal downtime?
153. How would you design MongoDB for an ecommerce site (products, users, orders)?
154. How would you store and query logs or IoT data efficiently?
155. What’s your strategy for schema versioning and backward compatibility?
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
# 🧩 MongoDB Update Operations — Complete Guide

MongoDB's **update operations** allow you to modify documents flexibly — from updating individual fields to performing mathematical calculations, manipulating arrays, or even transforming entire documents.

---

## 1️⃣ Field Update Operators
Used to set, unset, rename, or modify field values.

| Operator | Description | Example |
|-----------|--------------|----------|
| `$set` | Sets the value of a field | `{ $set: { age: 25 } }` |
| `$unset` | Removes a field from a document | `{ $unset: { age: "" } }` |
| `$rename` | Renames a field | `{ $rename: { "oldName": "newName" } }` |
| `$inc` | Increments a field value by a specified amount | `{ $inc: { views: 1 } }` |
| `$mul` | Multiplies the value of a field by a number | `{ $mul: { price: 1.1 } }` |
| `$min` | Updates a field only if the specified value is less than the current value | `{ $min: { score: 80 } }` |
| `$max` | Updates a field only if the specified value is greater than the current value | `{ $max: { score: 90 } }` |
| `$currentDate` | Sets a field to the current date/time | `{ $currentDate: { updatedAt: true } }` |

---

## 2️⃣ Array Update Operators
Used to add, remove, or modify elements in array fields.

| Operator | Description | Example |
|-----------|--------------|----------|
| `$push` | Adds an element to an array | `{ $push: { tags: "mongodb" } }` |
| `$addToSet` | Adds element to an array only if it doesn’t already exist | `{ $addToSet: { tags: "database" } }` |
| `$pop` | Removes the first (`-1`) or last (`1`) element of an array | `{ $pop: { tags: 1 } }` |
| `$pull` | Removes elements matching a condition | `{ $pull: { tags: "old" } }` |
| `$pullAll` | Removes all specified values from an array | `{ $pullAll: { tags: ["old", "temp"] } }` |
| `$each` | Used with `$push` or `$addToSet` to add multiple values | `{ $push: { tags: { $each: ["nodejs", "python"] } } }` |
| `$position` | Sets the position for inserting elements | `{ $push: { tags: { $each: ["new"], $position: 0 } } }` |
| `$slice` | Limits the size of an array after push | `{ $push: { logs: { $each: [newLog], $slice: -10 } } }` |

---

## 3️⃣ Array Filters (Advanced Updates)
Update specific elements inside arrays using **array filters**.

```javascript
db.students.updateOne(
  { _id: 1 },
  { $set: { "grades.$[elem].score": 95 } },
  { arrayFilters: [ { "elem.subject": "math" } ] }
);


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
- If a document has an array field, $unwind splits that document into multiple documents, one per array element.
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
// Find Alice's network up to 2 degrees
db.users.aggregate([
  {$match: {_id: "alice"}},
  {$graphLookup: {
    from: "users",
    startWith: "$friends",
    connectFromField: "friends",
    connectToField: "_id",
    as: "network",
    maxDepth: 2,
    depthField: "connectionDegree"
  }},
  {$project: {
    name: 1,
    directFriends: "$friends",
    extendedNetwork: "$network"
  }}
])

// Result: Alice's friends + friends of friends (up to 2 levels)
```

---

**Example 3: Category Tree Navigation**
```javascript
// categories collection
{_id: 1, name: "Electronics", parent: null}
{_id: 2, name: "Computers", parent: 1}
{_id: 3, name: "Laptops", parent: 2}
{_id: 4, name: "Desktops", parent: 2}
{_id: 5, name: "Gaming Laptops", parent: 3}

// Find all subcategories under "Electronics"
db.categories.aggregate([
  {$match: {name: "Electronics"}},
  {$graphLookup: {
    from: "categories",
    startWith: "$_id",
    connectFromField: "_id",
    connectToField: "parent",
    as: "subcategories",
    depthField: "depth"
  }},
  {$unwind: "$subcategories"},
  {$sort: {"subcategories.depth": 1}},
  {$group: {
    _id: "$_id",
    name: {$first: "$name"},
    tree: {$push: {
      name: "$subcategories.name",
      depth: "$subcategories.depth"
    }}
  }}
])
```

---

**Example 4: Bill of Materials (BOM)**
```javascript
// parts collection
{_id: "car", name: "Car", components: ["engine", "chassis"]}
{_id: "engine", name: "Engine", components: ["pistons", "crankshaft"]}
{_id: "chassis", name: "Chassis", components: ["frame", "suspension"]}
{_id: "pistons", name: "Pistons", components: []}

// Find all parts needed to build a car
db.parts.aggregate([
  {$match: {_id: "car"}},
  {$graphLookup: {
    from: "parts",
    startWith: "$components",
    connectFromField: "components",
    connectToField: "_id",
    as: "allParts",
    depthField: "level"
  }},
  {$project: {
    name: 1,
    bomList: {
      $map: {
        input: "$allParts",
        as: "part",
        in: {
          name: "$part.name",
          level: "$part.level"
        }
      }
    }
  }}
])
```

---

**Example 5: With restrictSearchWithMatch**
```javascript
// Find only active employees in reporting chain
db.employees.aggregate([
  {$match: {_id: 1}},
  {$graphLookup: {
    from: "employees",
    startWith: "$_id",
    connectFromField: "_id",
    connectToField: "reportsTo",
    as: "activeReports",
    restrictSearchWithMatch: {
      status: "active",
      department: "Engineering"
    }
  }}
])

// Only traverses employees matching the restriction
```

---

**Example 6: Circular Reference Detection**
```javascript
// Detect circular references in categories
db.categories.aggregate([
  {$graphLookup: {
    from: "categories",
    startWith: "$parent",
    connectFromField: "parent",
    connectToField: "_id",
    as: "ancestors"
  }},
  {$project: {
    name: 1,
    hasCircularRef: {
      $in: ["$_id", "$ancestors._id"]  // Check if own ID in ancestors
    }
  }},
  {$match: {hasCircularRef: true}}
])
```

---

**Example 7: Shortest Path (with maxDepth)**
```javascript
// Find connections within 3 hops
db.users.aggregate([
  {$match: {_id: "user1"}},
  {$graphLookup: {
    from: "users",
    startWith: "$connections",
    connectFromField: "connections",
    connectToField: "_id",
    as: "reachable",
    maxDepth: 3,
    depthField: "hops"
  }},
  {$match: {
    "reachable._id": "user2"  // Check if user2 is reachable
  }},
  {$project: {
    connection: {
      $filter: {
        input: "$reachable",
        cond: {$eq: ["$this._id", "user2"]}
      }
    }
  }}
])
```

---

**Performance Considerations:**

**1. Index Requirements:**
```javascript
// CRITICAL: Index on connectToField
db.employees.createIndex({reportsTo: 1})

// Without index, $graphLookup does collection scan at each level
```

**2. Memory Usage:**
```javascript
// Large graphs consume memory
// Use maxDepth to limit recursion
{$graphLookup: {
  // ...
  maxDepth: 5  // Prevent unlimited traversal
}}
```

**3. Query Optimization:**
```javascript
// Use restrictSearchWithMatch to reduce search space
{$graphLookup: {
  from: "employees",
  startWith: "$_id",
  connectFromField: "_id",
  connectToField: "reportsTo",
  as: "reports",
  restrictSearchWithMatch: {
    status: "active",     // Only active employees
    hireDate: {$gte: ISODate("2020-01-01")}
  }
}}
```

**4. Avoid Circular Traversal:**
```javascript
// MongoDB detects and prevents infinite loops
// But still incurs performance cost
// Design schema to avoid circles when possible
```

---

**Comparison with $lookup:**

| Feature | $graphLookup | $lookup |
|---------|--------------|---------|
| Recursion | ✓ | ✗ |
| Single join | ✗ | ✓ (faster) |
| Depth tracking | ✓ | ✗ |
| Max depth limit | ✓ | N/A |
| Performance | Slower | Faster |
| Use Case | Trees/Graphs | Flat relations |

---

**Best Practices:**

1. **Always Index connectToField**
2. **Use maxDepth** to prevent runaway queries
3. **Use restrictSearchWithMatch** to filter early
4. **Consider Alternative Designs:**
   - Flatten hierarchy with path arrays
   - Materialized paths
   - Nested sets
5. **Monitor Query Performance:**
```javascript
db.collection.aggregate([...], {explain: true})
```

---

### 125. How can you optimize an aggregation pipeline?

**1. Use $match Early (Filter First)**

```javascript
// BAD: $match after heavy operations
db.orders.aggregate([
  {$lookup: {
    from: "customers",
    localField: "customerId",
    foreignField: "_id",
    as: "customer"
  }},
  {$unwind: # MongoDB Advanced Interview Questions & Answers

## Architecture & Internals

### 101. What is the role of mongod, mongos, and config servers in a MongoDB cluster?

**mongod** is the primary daemon process for MongoDB that handles data requests, manages data access, and performs background management operations. In a replica set, multiple mongod instances run on different servers.

**mongos** acts as a query router in sharded clusters. It processes queries from applications, determines which shards contain the relevant data, and aggregates results from multiple shards. It's the interface between client applications and the sharded cluster.

**Config servers** store metadata and configuration settings for sharded clusters. They maintain the mapping of chunks to shards, cluster topology, and authentication configuration. MongoDB uses a replica set of config servers (CSRS - Config Server Replica Set) for high availability.

---

### 102. How does MongoDB manage journaling and checkpoints internally?

**Journaling** is a write-ahead logging mechanism that ensures data durability. MongoDB writes all data modifications to the journal before applying them to data files. The journal is a sequential log file stored in the `journal/` directory.

**Write flow:**
1. Write operation received
2. Write to journal (group commits every 100ms by default)
3. Write to in-memory WiredTiger cache
4. Background checkpoint writes to disk

**Checkpoints** are snapshots of data at a consistent state. WiredTiger creates checkpoints every 60 seconds by default or when 2GB of journal data is written. During checkpoint:
- All dirty pages are flushed to disk
- Journal files can be purged
- Provides recovery point

After a clean checkpoint, older journal files are removed.

---

### 103. How does MongoDB write data to disk in WiredTiger?

WiredTiger uses a **multi-version concurrency control (MVCC)** architecture:

1. **Write to Cache**: Data is first written to WiredTiger's internal cache (50% of RAM minus 1GB by default)
2. **Write to Journal**: Simultaneously logged to journal for durability
3. **Background Eviction**: When cache pressure increases, least-recently-used pages are evicted
4. **Checkpoint Process**: Every 60 seconds, dirty pages are flushed to disk in a consistent snapshot
5. **Compression**: Data is compressed before writing to disk (snappy by default)

WiredTiger writes are **copy-on-write**, meaning it never overwrites existing data - it writes new versions and later reclaims space.

---

### 104. What are write-ahead logs (WAL) in MongoDB?

**Write-Ahead Logs** (journal in MongoDB terminology) ensure durability by recording all write operations before they're applied to the main data files.

**Key characteristics:**
- Operations logged sequentially for fast writes
- Group commits batch multiple operations
- Enables crash recovery by replaying journal
- Can be disabled for better performance (at risk of data loss)
- Journal files are binary encoded for efficiency

**Recovery process:**
1. After crash, MongoDB replays journal from last checkpoint
2. Applies all logged operations
3. Restores database to consistent state

---

### 105. Explain the difference between storage compression and index compression in WiredTiger.

**Storage Compression** (Collection Level):
- Compresses document data on disk
- Default: Snappy (balanced speed/compression)
- Options: Snappy, zlib, zstd, or none
- Configured per collection: `{storageEngine: {wiredTiger: {configString: "block_compressor=zstd"}}}`
- Reduces disk I/O and storage costs
- Documents decompressed when read into cache

**Index Compression** (Index Level):
- Compresses index data separately
- Default: Prefix compression
- Reduces index size by storing common prefixes once
- Can use block compression (zlib, zstd)
- Trades CPU for disk space
- Particularly effective for indexes with repeated prefixes

**Key difference**: Storage compression affects documents, index compression affects index structures. Both can be configured independently based on workload characteristics.

---

## Performance Tuning

### 106. How would you identify and fix a performance bottleneck in MongoDB?

**Identification Process:**

1. **Enable Profiling**:
```javascript
db.setProfilingLevel(1, {slowms: 100}) // Log queries >100ms
db.system.profile.find().sort({ts: -1}).limit(5)
```

2. **Check Current Operations**:
```javascript
db.currentOp({active: true, secs_running: {$gte: 3}})
```

3. **Analyze Slow Queries**:
```javascript
db.system.profile.find({millis: {$gt: 100}}).sort({millis: -1})
```

4. **Use explain()**:
```javascript
db.collection.find({...}).explain("executionStats")
```

**Common Bottlenecks & Fixes:**

- **Missing Indexes**: Add appropriate indexes
- **Collection Scans**: Create covering indexes
- **High Memory Usage**: Increase RAM or optimize queries
- **Lock Contention**: Redesign schema or use sharding
- **Network Latency**: Use connection pooling, deploy closer to app
- **Disk I/O**: Use SSDs, enable compression, add RAM

**Monitoring Tools:**
- mongostat, mongotop
- MongoDB Atlas Performance Advisor
- Database Profiler

---

### 107. How do you decide which fields to index?

**Key Considerations:**

1. **Query Patterns**: Index fields used in:
   - WHERE clauses (find, update, delete)
   - Sort operations
   - Join conditions ($lookup)

2. **Selectivity**: Prioritize high-cardinality fields
   - Good: userEmail, userId, orderId
   - Poor: gender, status (few distinct values)

3. **ESR Rule** (Equality, Sort, Range):
```javascript
// Query: Find active users, sort by createdAt, filter by age range
db.users.createIndex({
    status: 1,      // Equality first
    createdAt: -1,  // Sort second
    age: 1          // Range last
})
```

4. **Write vs Read Ratio**:
   - Heavy reads: More indexes acceptable
   - Heavy writes: Minimize indexes (each index slows writes)

5. **Compound Index Efficiency**:
   - Left-to-right prefix rule
   - Index {a: 1, b: 1} supports queries on {a} and {a, b}, not just {b}

**Anti-patterns:**
- Don't index low-cardinality fields alone
- Avoid indexing fields that change frequently
- Don't create redundant indexes

---

### 108. How do you detect index scans vs collection scans?

**Using explain():**

```javascript
db.collection.find({status: "active"}).explain("executionStats")
```

**Index Scan Indicators:**
```javascript
{
  "executionStats": {
    "executionStages": {
      "stage": "IXSCAN",           // Index scan
      "indexName": "status_1",
      "keysExamined": 100,
      "docsExamined": 100          // Efficient if equal
    }
  }
}
```

**Collection Scan Indicators:**
```javascript
{
  "executionStats": {
    "executionStages": {
      "stage": "COLLSCAN",         // Collection scan - BAD!
      "docsExamined": 1000000      // Scanned entire collection
    },
    "totalDocsExamined": 1000000,
    "nReturned": 10                // Only returned 10 - very inefficient
  }
}
```

**Key Metrics:**
- **COLLSCAN**: Full collection scan (slow)
- **IXSCAN**: Index scan (fast)
- **docsExamined/nReturned ratio**: Should be close to 1
- **executionTimeMillis**: Total execution time

**Quick Check:**
```javascript
// If this shows COLLSCAN, you need an index
db.collection.find({field: value}).explain("executionStats").executionStats.executionStages.stage
```

---

### 109. What are the performance implications of $lookup?

**Performance Challenges:**

1. **Left Join Operation**: $lookup performs left outer join, which is expensive
2. **No Index on Foreign Field**: If foreign collection lacks index on join field, causes COLLSCAN
3. **Memory Intensive**: Joins happen in memory, can hit 100MB aggregation limit
4. **Network Overhead**: In sharded clusters, may require cross-shard communication

**Example Impact:**
```javascript
// Without index on orders.userId - VERY SLOW
db.users.aggregate([
  {$lookup: {
    from: "orders",
    localField: "_id",
    foreignField: "userId",  // If no index here, scans all orders for EACH user
    as: "userOrders"
  }}
])
```

**Optimization Strategies:**

1. **Index Foreign Key**:
```javascript
db.orders.createIndex({userId: 1})
```

2. **Limit Results Before $lookup**:
```javascript
db.users.aggregate([
  {$match: {status: "active"}},  // Reduce users first
  {$lookup: {...}}
])
```

3. **Use $project to Reduce Data**:
```javascript
{$project: {_id: 1, name: 1}}  // Fetch only needed fields
```

4. **Consider Embedding** instead of $lookup for frequently accessed data

5. **Pagination**:
```javascript
{$skip: 0}, {$limit: 20}  // Don't lookup entire dataset
```

**When to Avoid:**
- High-frequency queries
- Large collections without proper indexes
- Real-time applications requiring <100ms response

---

### 110. What are "hot" documents and how does MongoDB handle them?

**Hot Documents** are documents accessed/modified extremely frequently, causing:
- Write contention
- Lock conflicts
- Performance degradation
- Uneven load distribution in sharded clusters

**Common Examples:**
- Like counters on viral posts
- Real-time inventory counts
- Session documents
- Global configuration documents

**MongoDB's Handling:**

1. **Document-Level Locking**: WiredTiger uses document-level concurrency, but hot documents still bottleneck

2. **In-Memory Cache**: Frequently accessed docs stay in WiredTiger cache

3. **Write Conflicts**: Multiple concurrent updates cause retries

**Mitigation Strategies:**

1. **Sharding** (distribute hot doc across shards):
```javascript
// Bad: single counter
{_id: "post123", likes: 50000}

// Good: distributed counters
{_id: "post123:shard1", likes: 10000}
{_id: "post123:shard2", likes: 15000}
```

2. **Bucketing Pattern**:
```javascript
// Group counters into time buckets
{
  _id: "post123:2025-11-08:hour14",
  likes: 1500,
  bucket: ISODate("2025-11-08T14:00:00Z")
}
```

3. **Approximation**:
```javascript
// Update every N operations instead of every time
if (Math.random() < 0.1) {  // 10% sampling
  db.posts.updateOne({_id: "post123"}, {$inc: {likes: 10}})
}
```

4. **Client-Side Aggregation**: Aggregate in application, periodic batch updates

5. **Separate Collection**: Move hot fields to dedicated collection

---

## Data Modeling (Real-world Scenarios)

### 111. How would you model user posts and comments (1:N relation)?

**Three Approaches:**

**1. Embedding (Recommended for Moderate Comments)**
```javascript
// User Posts Collection
{
  _id: ObjectId("..."),
  userId: ObjectId("user123"),
  title: "My First Post",
  content: "Post content here",
  createdAt: ISODate("2025-11-08"),
  comments: [
    {
      commentId: ObjectId("comment1"),
      userId: ObjectId("user456"),
      text: "Great post!",
      createdAt: ISODate("2025-11-08T10:30:00Z")
    },
    {
      commentId: ObjectId("comment2"),
      userId: ObjectId("user789"),
      text: "Thanks for sharing",
      createdAt: ISODate("2025-11-08T11:00:00Z")
    }
  ],
  commentCount: 2
}
```

**Pros**: Single query, atomicity, good performance for <100 comments
**Cons**: 16MB document limit, difficult to paginate comments

**2. Referencing (For High-Volume Comments)**
```javascript
// Posts Collection
{
  _id: ObjectId("post123"),
  userId: ObjectId("user123"),
  title: "Viral Post",
  content: "Content here",
  commentCount: 15000
}

// Comments Collection (separate)
{
  _id: ObjectId("comment1"),
  postId: ObjectId("post123"),  // Reference to post
  userId: ObjectId("user456"),
  text: "Great post!",
  createdAt: ISODate("2025-11-08T10:30:00Z")
}

// Index for efficient queries
db.comments.createIndex({postId: 1, createdAt: -1})
```

**Pros**: Unbounded comments, easy pagination, no 16MB limit
**Cons**: Multiple queries, no atomic updates

**3. Hybrid (Best of Both)**
```javascript
// Posts with recent comments embedded
{
  _id: ObjectId("post123"),
  userId: ObjectId("user123"),
  title: "My Post",
  content: "Content",
  commentCount: 500,
  recentComments: [  // Only last 5-10 comments embedded
    {commentId: ObjectId("..."), text: "Latest", createdAt: ISODate("...")}
  ],
  hasMoreComments: true
}

// Full comments in separate collection for pagination
```

**Recommendation**: Start with embedding, migrate to hybrid/referencing when comments > 100 per post.

---

### 112. When would you use $lookup vs embedding?

**Use Embedding When:**

1. **One-to-Few Relationship**: Parent has limited children (<100)
2. **Data Accessed Together**: User profile with addresses
3. **No Independent Queries**: Children only queried with parent
4. **Bounded Growth**: Array won't exceed 16MB
5. **Atomic Updates Required**: Updates must be transactional

**Example:**
```javascript
// User with addresses - perfect for embedding
{
  _id: ObjectId("user123"),
  name: "John Doe",
  addresses: [
    {type: "home", street: "123 Main St", city: "NYC"},
    {type: "work", street: "456 Office Blvd", city: "NYC"}
  ]
}
```

**Use $lookup When:**

1. **One-to-Many/Many-to-Many**: Unbounded relationships
2. **Independent Access**: Children queried separately
3. **Large Child Documents**: Would cause document bloat
4. **Frequent Updates**: Children updated independently
5. **Data Duplication Issues**: Same child belongs to multiple parents

**Example:**
```javascript
// Users and Orders - use $lookup
// Users Collection
{_id: ObjectId("user123"), name: "John"}

// Orders Collection
{_id: ObjectId("order1"), userId: ObjectId("user123"), total: 99.99}

// Query with $lookup
db.users.aggregate([
  {$match: {_id: ObjectId("user123")}},
  {$lookup: {
    from: "orders",
    localField: "_id",
    foreignField: "userId",
    as: "orders"
  }}
])
```

**Performance Comparison:**

| Aspect | Embedding | $lookup |
|--------|-----------|---------|
| Read Speed | Fast (1 query) | Slower (join) |
| Write Speed | Fast (1 write) | Fast (separate docs) |
| Scalability | Limited by 16MB | Unlimited |
| Atomicity | Yes | No (requires transactions) |
| Flexibility | Low | High |

**Hybrid Approach:**
Embed recent/popular items, reference the rest:
```javascript
{
  _id: ObjectId("post123"),
  recentComments: [...],  // Last 10 embedded
  totalComments: 5000     // Rest in separate collection
}
```

---

### 113. How do you handle large arrays in MongoDB?

**Problem**: Arrays growing unbounded can:
- Hit 16MB document limit
- Cause performance issues (index overhead, memory)
- Make updates inefficient

**Solutions:**

**1. Pagination/Slicing** (Keep only recent items):
```javascript
// Keep only last 100 comments
db.posts.updateOne(
  {_id: "post123"},
  {
    $push: {
      comments: {
        $each: [newComment],
        $position: 0,      // Add to beginning
        $slice: 100        // Keep only first 100
      }
    }
  }
)
```

**2. Bucketing Pattern** (Split into time-based buckets):
```javascript
// Instead of single document with huge array
{
  _id: "messages:user123:2025-11",
  userId: "user123",
  month: "2025-11",
  messages: [
    {text: "Hi", timestamp: ISODate("2025-11-01")},
    {text: "Hello", timestamp: ISODate("2025-11-02")}
  ],
  count: 2
}

// New bucket each month
{
  _id: "messages:user123:2025-12",
  month: "2025-12",
  messages: [...],
  count: 45
}
```

**3. Separate Collection** (Reference instead of embed):
```javascript
// Parent
{_id: "order123", totalItems: 5000}

// Children in separate collection
{_id: "item1", orderId: "order123", name: "Product A"}
{_id: "item2", orderId: "order123", name: "Product B"}

// Query
db.orderItems.find({orderId: "order123"}).limit(20)
```

**4. Subset Pattern** (Embed most accessed, reference rest):
```javascript
{
  _id: "product123",
  topReviews: [...],      // 10 highest-rated embedded
  totalReviews: 50000,
  allReviewsRef: true     // Flag indicating more in separate collection
}
```

**5. Outlier Pattern** (Special handling for outliers):
```javascript
// Normal document
{_id: "user123", friends: ["user2", "user3"], friendCount: 2}

// Outlier (celebrity with millions of friends)
{
  _id: "celebrity789",
  friends: [],            // Empty array
  friendCount: 5000000,
  friendsOverflow: true   // Friends stored in separate collection
}
```

**6. Approximation** (Don't store every item):
```javascript
// Instead of tracking every viewer
{
  _id: "video123",
  sampleViewers: [...],   // Sample of 1000 viewers
  totalViews: 10000000    // Just counter
}
```

**Best Practice**: Design schema to prevent unbounded arrays from the start. If array might grow indefinitely, use separate collection.

---

### 114. What are bucket pattern and subset pattern in schema design?

**Bucket Pattern**

Groups related data into time-based or quantity-based buckets to avoid unbounded document growth.

**Use Cases:**
- Time-series data (IoT sensors, logs, metrics)
- Event streams
- High-frequency data points

**Example - IoT Temperature Sensors:**
```javascript
// Bad: Single document per sensor (unbounded)
{
  _id: "sensor123",
  readings: [
    {temp: 22.5, timestamp: ISODate("2025-11-08T10:00:00Z")},
    {temp: 22.6, timestamp: ISODate("2025-11-08T10:01:00Z")},
    // ... millions of readings
  ]
}

// Good: Bucketing by hour
{
  _id: "sensor123:2025-11-08:10",
  sensorId: "sensor123",
  bucket: ISODate("2025-11-08T10:00:00Z"),
  readings: [
    {temp: 22.5, minute: 0},
    {temp: 22.6, minute: 1},
    // ... max 60 readings per hour bucket
  ],
  count: 60,
  avgTemp: 22.8,
  minTemp: 22.3,
  maxTemp: 23.1
}

// Query specific hour
db.sensors.findOne({"_id": "sensor123:2025-11-08:10"})

// Query range
db.sensors.find({
  sensorId: "sensor123",
  bucket: {
    $gte: ISODate("2025-11-08T10:00:00Z"),
    $lt: ISODate("2025-11-08T12:00:00Z")
  }
})
```

**Benefits:**
- Predictable document size
- Easy to archive/delete old buckets
- Efficient range queries
- Pre-aggregated statistics

---

**Subset Pattern**

Embeds frequently accessed subset of data while keeping full dataset in separate collection.

**Use Cases:**
- Product reviews (show top reviews, link to all)
- Social media posts (recent comments embedded)
- User activity logs (recent activities)

**Example - E-commerce Reviews:**
```javascript
// Products Collection
{
  _id: "product123",
  name: "Laptop",
  price: 999,
  
  // Subset: Top 3 reviews embedded
  featuredReviews: [
    {
      reviewId: ObjectId("rev1"),
      rating: 5,
      text: "Amazing product!",
      helpful: 245,
      userId: "user456"
    },
    {
      reviewId: ObjectId("rev2"),
      rating: 5,
      text: "Best laptop ever",
      helpful: 189,
      userId: "user789"
    },
    {
      reviewId: ObjectId("rev3"),
      rating: 4,
      text: "Great value",
      helpful: 156,
      userId: "user321"
    }
  ],
  
  // Metadata
  reviewStats: {
    total: 15847,
    avgRating: 4.3,
    distribution: {5: 8000, 4: 5000, 3: 2000, 2: 500, 1: 347}
  }
}

// Reviews Collection (complete data)
{
  _id: ObjectId("rev1"),
  productId: "product123",
  userId: "user456",
  rating: 5,
  text: "Amazing product!",
  helpful: 245,
  createdAt: ISODate("2025-10-15")
}

// Full review queries
db.reviews.find({productId: "product123"})
  .sort({helpful: -1})
  .skip(20)
  .limit(10)
```

**Benefits:**
- Fast initial page load (embedded subset)
- No 16MB limit (full data separate)
- Easy pagination
- Reduced $lookup operations

**Maintenance:**
```javascript
// Periodic job to update featured reviews
db.products.updateOne(
  {_id: "product123"},
  {$set: {
    featuredReviews: db.reviews.find({productId: "product123"})
      .sort({helpful: -1})
      .limit(3)
      .toArray()
  }}
)
```

---

### 115. How do you design schema for time-series data in MongoDB?

MongoDB has built-in **Time Series Collections** (MongoDB 5.0+) optimized for this use case.

**1. Native Time Series Collections (Recommended):**

```javascript
// Create time series collection
db.createCollection("sensorData", {
  timeseries: {
    timeField: "timestamp",
    metaField: "metadata",
    granularity: "seconds"  // seconds, minutes, or hours
  }
})

// Insert data
db.sensorData.insertMany([
  {
    timestamp: ISODate("2025-11-08T10:00:00Z"),
    metadata: {sensorId: "sensor123", location: "warehouse-A"},
    temperature: 22.5,
    humidity: 45
  },
  {
    timestamp: ISODate("2025-11-08T10:01:00Z"),
    metadata: {sensorId: "sensor123", location: "warehouse-A"},
    temperature: 22.6,
    humidity: 46
  }
])

// Efficient aggregations
db.sensorData.aggregate([
  {$match: {
    timestamp: {$gte: ISODate("2025-11-08T00:00:00Z")},
    "metadata.sensorId": "sensor123"
  }},
  {$group: {
    _id: {$dateTrunc: {date: "$timestamp", unit: "hour"}},
    avgTemp: {$avg: "$temperature"},
    maxTemp: {$max: "$temperature"},
    count: {$sum: 1}
  }}
])
```

**Benefits:**
- Automatic bucketing and compression (90% storage reduction)
- Optimized queries for time ranges
- Efficient aggregations
- Automatic index on timeField

**2. Manual Bucketing Pattern (Pre-5.0 or custom needs):**

```javascript
// Bucket per hour
{
  _id: ObjectId("..."),
  sensorId: "sensor123",
  bucket: ISODate("2025-11-08T10:00:00Z"),
  measurements: [
    {time: 0, temp: 22.5, humidity: 45},   // 10:00:00
    {time: 60, temp: 22.6, humidity: 46},  // 10:01:00
    {time: 120, temp: 22.7, humidity: 46}  // 10:02:00
  ],
  count: 3,
  stats: {
    avgTemp: 22.6,
    minTemp: 22.5,
    maxTemp: 22.7
  }
}

// Indexes
db.sensorData.createIndex({sensorId: 1, bucket: 1})
```

**3. Schema Design Patterns:**

**IoT Sensors:**
```javascript
{
  _id: "sensor123:2025-11-08:10",
  sensorId: "sensor123",
  deviceType: "temperature",
  location: {type: "Point", coordinates: [40.7128, -74.0060]},
  bucket: ISODate("2025-11-08T10:00:00Z"),
  readings: [{timestamp, value, quality}],
  aggregates: {count, sum, avg, min, max, stdDev}
}
```

**Application Logs:**
```javascript
{
  _id: ObjectId("..."),
  appId: "app123",
  bucket: ISODate("2025-11-08T10:00:00Z"),
  logs: [
    {offset: 0, level: "ERROR", message: "Failed to connect", userId: "user456"},
    {offset: 30, level: "INFO", message: "Request completed", userId: "user789"}
  ]
}
```

**Financial Ticks:**
```javascript
{
  _id: "AAPL:2025-11-08:10",
  symbol: "AAPL",
  bucket: ISODate("2025-11-08T10:00:00Z"),
  ticks: [
    {time: 0, price: 150.25, volume: 1000},
    {time: 1, price: 150.26, volume: 500}
  ],
  ohlc: {open: 150.25, high: 150.30, low: 150.20, close: 150.26}
}
```

**4. Query Optimization:**

```javascript
// Index strategy
db.sensorData.createIndex({
  "metadata.sensorId": 1,
  timestamp: 1
})

// Efficient range query
db.sensorData.find({
  "metadata.sensorId": "sensor123",
  timestamp: {
    $gte: ISODate("2025-11-08T00:00:00Z"),
    $lt: ISODate("2025-11-09T00:00:00Z")
  }
}).sort({timestamp: -1}).limit(100)

// Downsampling aggregation
db.sensorData.aggregate([
  {$match: {timestamp: {$gte: ISODate("2025-11-01")}}},
  {$group: {
    _id: {
      $dateTrunc: {date: "$timestamp", unit: "day"}
    },
    avgTemp: {$avg: "$temperature"},
    count: {$sum: 1}
  }},
  {$sort: {_id: 1}}
])
```

**5. Data Retention Strategy:**

```javascript
// TTL index for automatic deletion
db.sensorData.createIndex(
  {timestamp: 1},
  {expireAfterSeconds: 2592000}  // 30 days
)

// Or manual archival
db.sensorData.deleteMany({
  timestamp: {$lt: ISODate("2025-10-08")}
})
```

---

## Transactions & Concurrency

### 116. How are multi-document transactions implemented in MongoDB?

MongoDB implements **ACID transactions** across multiple documents, collections, and databases using a two-phase commit protocol with snapshot isolation.

**Architecture:**

**1. Transaction Lifecycle:**
```javascript
const session = db.getMongo().startSession()
session.startTransaction({
  readConcern: {level: "snapshot"},
  writeConcern: {w: "majority"},
  readPreference: "primary"
})

try {
  const accounts = session.getDatabase("bank").accounts
  
  // Debit account A
  accounts.updateOne(
    {_id: "accountA"},
    {$inc: {balance: -100}},
    {session}
  )
  
  // Credit account B
  accounts.updateOne(
    {_id: "accountB"},
    {$inc: {balance: 100}},
    {session}
  )
  
  // Commit transaction
  session.commitTransaction()
} catch (error) {
  session.abortTransaction()
  throw error
} finally {
  session.endSession()
}
```

**2. Implementation Details:**

**Transaction Coordinator:**
- Each transaction gets unique transaction ID (txnNumber)
- Session tracks transaction state
- Coordinator manages prepare, commit, abort phases

**Write Staging:**
- Writes are staged in memory during transaction
- Not visible to other sessions until commit
- Uses versioned storage (MVCC)

**Two-Phase Commit:**
```
Phase 1: Prepare
- Validate all operations
- Acquire necessary locks
- Write to oplog with "prepare" entry

Phase 2: Commit/Abort
- If all nodes prepared successfully → commit
- Oplog entry marks transaction committed
- Release locks
- Make changes visible
```

**3. Snapshot Isolation:**

```javascript
// Transaction sees consistent snapshot from start time
session.startTransaction()

// Read sees data as of transaction start
db.products.findOne({_id: "product123"}, {session})
// Returns: {_id: "product123", stock: 100}

// Even if another transaction updates stock to 50,
// this transaction still sees 100

db.products.updateOne(
  {_id: "product123", stock: {$gte: 10}},
  {$inc: {stock: -10}},
  {session}
)

session.commitTransaction()
```

**4. Conflict Resolution:**

MongoDB uses **first-write-wins** for conflicts:

```javascript
// Transaction T1
session1.startTransaction()
db.accounts.updateOne({_id: "acc1"}, {$inc: {balance: 100}}, {session: session1})

// Transaction T2 (concurrent)
session2.startTransaction()
db.accounts.updateOne({_id: "acc1"}, {$inc: {balance: 50}}, {session: session2})

// T1 commits first → succeeds
session1.commitTransaction()

// T2 tries to commit → WriteConflict error, must retry
session2.commitTransaction() // Throws error
```

**5. Transaction Limitations:**

- 60-second default timeout
- 16MB oplog entry size limit per transaction
- Cannot read/write to capped collections, system collections
- Performance impact on high-concurrency workloads
- Replica sets: all operations on primary
- Sharded clusters: additional overhead

**6. Replication:**

```javascript
// Transaction replicated as single oplog entry
{
  op: "c",
  ns: "admin.$cmd",
  o: {
    applyOps: [
      {op: "u", ns: "bank.accounts", o: {$inc: {balance: -100}}},
      {op: "u", ns: "bank.accounts", o: {$inc: {balance: 100}}}
    ]
  },
  txnNumber: 1,
  stmtId: 0,
  lsid: {id: UUID("...")},
  prevOpTime: {...}
}
```

---

### 117. What are the limitations of MongoDB transactions?

**1. Performance Limitations:**

**Overhead:**
- Transactions are slower than single-document operations
- WiredTiger maintains transaction state in memory
- Snapshot isolation requires version tracking
- Lock acquisition overhead

**Concurrency:**
- Write conflicts force retries
- Can cause contention on hot documents
- Reduced throughput under high contention

**2. Size Limitations:**

```javascript
// 16MB oplog entry limit
// Transaction with too many operations fails
session.startTransaction()
for (let i = 0; i < 100000; i++) {
  db.collection.insertOne({data: "..."}, {session}) // May exceed 16MB
}
session.commitTransaction() // ERROR: Transaction too large
```

**Workaround:** Batch into smaller transactions

**3. Time Limitations:**

```javascript
// Default 60-second timeout
session.startTransaction({
  maxTimeMS: 60000  // Cannot exceed this
})
// If transaction runs > 60s, automatically aborted
```

**4. Collection Type Restrictions:**

**Cannot Use With:**
- Capped collections
- System collections (system.*)
- config, admin, local databases in sharded clusters

```javascript
session.startTransaction()
db.cappedCollection.insertOne({...}, {session}) // ERROR
```

**5. Sharding Limitations:**

**Cross-Shard Transactions:**
- Higher latency
- More coordinator overhead
- Network failures can cause aborts
- Requires MongoDB 4.2+

**Orphaned Documents:**
- Can see orphaned documents during chunk migration
- Requires careful handling

**6. DDL Operations:**

```javascript
// Cannot perform DDL in transactions
session.startTransaction()
db.createCollection("newCollection", {session}) // ERROR
db.collection.createIndex({field: 1}, {session}) // ERROR
```

**7. Read/Write Concern Restrictions:**

```javascript
// Must use compatible read/write concerns
session.startTransaction({
  readConcern: {level: "snapshot"},     // Required
  writeConcern: {w: "majority"}         // Required for durability
})

// Invalid combinations cause errors
session.startTransaction({
  readConcern: {level: "local"},  // ERROR: must be snapshot
  writeConcern: {w: 1}            // ERROR: should be majority
})
```

**8. Retryability:**

```javascript
// Must implement retry logic
function runTransactionWithRetry(txnFunc, session) {
  while (true) {
    try {
      txnFunc(session)
      session.commitTransaction()
      break
    } catch (error) {
      if (error.hasErrorLabel("TransientTransactionError")) {
        // Retry entire transaction
        continue
      } else if (error.hasErrorLabel("UnknownTransactionCommitResult")) {
        // Retry commit
        session.commitTransaction()
      } else {
        throw error
      }
    }
  }
}
```

**9. Memory Pressure:**

- Transactions held in memory until commit
- Large transactions can cause memory issues
- Can trigger cache pressure and evictions

**10. No Isolation for DDL:**

```javascript
// Other sessions can see schema changes immediately
// Even if transaction uncommitted
session.startTransaction()
db.newCollection.insertOne({...}, {session})
// Other sessions can now see newCollection exists
```

**Best Practices:**
- Keep transactions short (< 1 second ideal)
- Minimize operations per transaction
- Use single-document atomicity when possible
- Implement proper retry logic
- Monitor transaction metrics
- Avoid transactions for high-frequency operations

---

### 118. How does MongoDB maintain ACID properties in a replica set?

**Atomicity:**

**Single Document:**
```javascript
// Always atomic without transactions
db.accounts.updateOne(
  {_id: "acc1"},
  {
    $inc: {balance: 100},
    $push: {transactions: {amount: 100, date: new Date()}}
  }
)
// Both operations succeed or fail together
```

**Multi-Document:**
```javascript
// Requires explicit transaction
session.startTransaction()
db.accounts.updateOne({_id: "acc1"}, {$inc: {balance: -100}}, {session})
db.accounts.updateOne({_id: "acc2"}, {$inc: {balance: 100}}, {session})
session.commitTransaction() // Both or neither
```

**Implementation:**
- WiredTiger transaction log ensures atomicity
- Operations grouped in oplog entry
- Rollback if any operation fails

---

**Consistency:**

**Write Concern Enforcement:**
```javascript
// Ensure consistency across replica set
db.collection.insertOne(
  {data: "important"},
  {writeConcern: {w: "majority", j: true}}
)
// Confirmed by majority before acknowledged
```

**Schema Validation:**
```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      required: ["email", "age"],
      properties: {
        email: {type: "string"},
        age: {type: "number", minimum: 0}
      }
    }
  }
})
// Enforces consistency of data structure
```

**Consistency Model:**
- **Eventual Consistency**: Default for secondary reads
- **Strong Consistency**: readConcern "majority" + writeConcern "majority"

```javascript
db.collection.find({}).readConcern("majority")
// Reads only data acknowledged by majority
```

---

**Isolation:**

**Document-Level Locking (WiredTiger):**
```javascript
// Concurrent reads - no blocking
session1: db.accounts.find({_id: "acc1"})
session2: db.accounts.find({_id: "acc1"}) // No conflict

// Concurrent writes - last write wins
session1: db.accounts.updateOne({_id: "acc1"}, {$inc: {balance: 10}})
session2: db.accounts.updateOne({_id: "acc1"}, {$inc: {balance: 20}})
// Both succeed, final state depends on order
```

**Snapshot Isolation (Transactions):**
```javascript
// Transaction sees consistent snapshot
session.startTransaction({readConcern: {level: "snapshot"}})

// All reads in transaction see data as of transaction start
db.accounts.find({}, {session})

// External changes not visible until commit
session.commitTransaction()
```

**Read Isolation Levels:**
```javascript
// Local: reads latest data (may not be durable)
db.collection.find().readConcern("local")

// Majority: reads only majority-committed data
db.collection.find().readConcern("majority")

// Linearizable: reads with real-time guarantees
db.collection.find().readConcern("linearizable")
```

---

**Durability:**

**Journal (Write-Ahead Log):**
```javascript
// Ensure durability with journal
db.collection.insertOne(
  {data: "critical"},
  {writeConcern: {w: 1, j: true}} // j:true = wait for journal
)
```

**Journal Process:**
1. Write to journal (on-disk log)
2. Group commit every 100ms
3. Flush to data files later
4. Crash recovery replays journal

**Replication for Durability:**
```javascript
// Durability across multiple servers
db.collection.insertOne(
  {data: "important"},
  {writeConcern: {w: "majority"}} // Replicated to majority
)
```

**Write Concern Levels:**
```javascript
// No acknowledgment (fire and forget)
{w: 0}

// Acknowledged by primary only
{w: 1, j: false}

// Primary + journaled
{w: 1, j: true}

// Majority of replica set
{w: "majority"}

// Custom: specific number of nodes
{w: 3}
```

---

**Replica Set Guarantees:**

**Primary Election:**
```javascript
// Ensures only one primary writes
// Prevents split-brain scenarios
// Election uses Raft-like protocol

// Priority settings
rs.reconfig({
  members: [
    {_id: 0, host: "server1:27017", priority: 2}, // Preferred primary
    {_id: 1, host: "server2:27017", priority: 1},
    {_id: 2, host: "server3:27017", priority: 1}
  ]
})
```

**Oplog Replication:**
```javascript
// Oplog entry structure
{
  ts: Timestamp(1699430400, 1),
  t: 1,
  h: NumberLong("123456789"),
  v: 2,
  op: "u",  // operation: i=insert, u=update, d=delete
  ns: "db.collection",
  o: {$set: {balance: 100}},
  o2: {_id: "acc1"}
}

// Secondaries continuously tail oplog
// Apply operations in same order as primary
```

**Rollback Prevention:**
```javascript
// Write concern prevents rollbacks
db.collection.insertOne(
  {data: "critical"},
  {writeConcern: {w: "majority", j: true, wtimeout: 5000}}
)
// Waits for majority acknowledgment
// If timeout, throws error (doesn't rollback)
```

**Failure Scenarios:**

**Primary Crash:**
1. Primary crashes
2. Replica set detects heartbeat failure
3. Election triggered
4. New primary elected
5. Clients reconnect to new primary

**Network Partition:**
```javascript
// Minority partition cannot elect primary
// Majority partition continues operating
// Prevents split-brain

// 3-node set splits 1-2:
// 1 node: becomes secondary (no writes)
// 2 nodes: elect new primary (continues)
```

**Rollback Handling:**
```javascript
// If primary crashes with uncommitted writes
// Rolled back when rejoins as secondary
// Written to rollback files in dbPath/rollback

// View rollback files
ls /data/db/rollback/

// Manually resolve if needed
```

**Causal Consistency:**
```javascript
// Session-based causal consistency
const session = client.startSession({causalConsistency: true})

// Write on primary
db.collection.insertOne({_id: 1}, {session})

// Read from secondary sees write
db.collection.findOne({_id: 1}, {
  session,
  readPreference: "secondary"
}) // Returns document (causally consistent)
```

---

### 119. How does optimistic concurrency control work in MongoDB?

**Optimistic Concurrency Control (OCC)** assumes conflicts are rare and validates at commit time rather than locking preemptively.

**1. Version-Based OCC:**

```javascript
// Document with version field
{
  _id: "product123",
  name: "Laptop",
  stock: 100,
  version: 1
}

// Update with version check
const product = db.products.findOne({_id: "product123"})
const currentVersion = product.version

const result = db.products.updateOne(
  {
    _id: "product123",
    version: currentVersion  // Check version hasn't changed
  },
  {
    $inc: {stock: -10},
    $set: {version: currentVersion + 1}  // Increment version
  }
)

if (result.matchedCount === 0) {
  // Conflict detected - version changed
  // Retry with fresh data
  throw new ConflictError("Document was modified by another operation")
}
```

**Application-Level Retry:**
```javascript
async function updateWithRetry(productId, quantity, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      // Read current state
      const product = await db.products.findOne({_id: productId})
      
      if (product.stock < quantity) {
        throw new Error("Insufficient stock")
      }
      
      // Attempt update with version check
      const result = await db.products.updateOne(
        {_id: productId, version: product.version},
        {
          $inc: {stock: -quantity},
          $set: {
            version: product.version + 1,
            lastModified: new Date()
          }
        }
      )
      
      if (result.matchedCount === 1) {
        return {success: true, newVersion: product.version + 1}
      }
      
      // Conflict - retry
      console.log(`Conflict detected, retry ${attempt + 1}`)
      await sleep(Math.random() * 100) // Exponential backoff
      
    } catch (error) {
      if (attempt === maxRetries - 1) throw error
    }
  }
  
  throw new Error("Max retries exceeded")
}
```

**2. Timestamp-Based OCC:**

```javascript
{
  _id: "order123",
  status: "pending",
  total: 99.99,
  lastModified: ISODate("2025-11-08T10:30:00Z")
}

// Update with timestamp check
const order = db.orders.findOne({_id: "order123"})

db.orders.updateOne(
  {
    _id: "order123",
    lastModified: order.lastModified  // Check timestamp
  },
  {
    $set: {
      status: "processing",
      lastModified: new Date()
    }
  }
)
```

**3. MongoDB's Internal OCC (WiredTiger):**

MongoDB uses OCC internally with **MVCC (Multi-Version Concurrency Control)**:

```javascript
// Transaction T1
session1.startTransaction()
const doc = db.collection.findOne({_id: 1}, {session: session1})
db.collection.updateOne({_id: 1}, {$set: {value: doc.value + 10}}, {session: session1})

// Transaction T2 (concurrent)
session2.startTransaction()
db.collection.updateOne({_id: 1}, {$set: {value: 50}}, {session: session2})
session2.commitTransaction() // Commits first

// T1 tries to commit
session1.commitTransaction() // WriteConflict error
// Must abort and retry
```

**Internal Process:**
1. Each transaction reads snapshot at start time
2. Changes staged in memory (not visible to others)
3. At commit, check if read data was modified
4. If conflict → abort with WriteConflict
5. If no conflict → commit changes

**4. Conditional Updates (Implicit OCC):**

```javascript
// Check condition during update
db.inventory.updateOne(
  {
    _id: "item123",
    quantity: {$gte: 10}  // Implicit version check
  },
  {
    $inc: {quantity: -10}
  }
)

// If quantity changed before update, matchedCount = 0
// No explicit version field needed
```

**5. Compare-and-Swap Pattern:**

```javascript
function compareAndSwap(docId, expectedValue, newValue) {
  const result = db.collection.updateOne(
    {
      _id: docId,
      value: expectedValue  // Expected state
    },
    {
      $set: {value: newValue}
    }
  )
  
  return result.matchedCount === 1 // True if succeeded
}

// Usage
while (!compareAndSwap("counter1", currentValue, currentValue + 1)) {
  currentValue = db.collection.findOne({_id: "counter1"}).value
  // Retry with updated value
}
```

**6. Advantages:**

- **High Concurrency**: No locks held during read phase
- **Better Performance**: No blocking on reads
- **Deadlock-Free**: No lock acquisition order issues
- **Scalable**: Works well with distributed systems

**7. Disadvantages:**

- **Retry Overhead**: High contention causes many retries
- **Wasted Work**: Failed transactions must be redone
- **Application Complexity**: Must implement retry logic
- **Starvation**: Unlucky transactions may retry indefinitely

**8. When to Use:**

**Use OCC When:**
- Conflicts are rare
- Read-heavy workload
- Short transactions
- Distributed environment

**Avoid OCC When:**
- High contention on same documents
- Long-running transactions
- Write-heavy workloads
- Pessimistic locking preferred (use MongoDB transactions with explicit locking patterns)

---

### 120. How does snapshot isolation work in MongoDB?

**Snapshot Isolation** provides each transaction a consistent view of the database as of a specific point in time (the snapshot).

**1. Core Concept:**

```javascript
// Transaction starts and captures snapshot
session.startTransaction({
  readConcern: {level: "snapshot"}
})

// Time: T0 (transaction start)
const account = db.accounts.findOne({_id: "acc1"}, {session})
// Reads: {_id: "acc1", balance: 100}

// Time: T1 (another transaction commits)
// External update: balance → 200

// Time: T2 (still in transaction)
const accountAgain = db.accounts.findOne({_id: "acc1"}, {session})
// Still reads: {_id: "acc1", balance: 100} (snapshot unchanged)

session.commitTransaction()
```

**2. MVCC Implementation:**

**Multi-Version Storage:**
```javascript
// WiredTiger maintains multiple versions of each document

// Version 1 (timestamp: 1000)
{_id: "acc1", balance: 100}

// Version 2 (timestamp: 2000)
{_id: "acc1", balance: 200}

// Version 3 (timestamp: 3000)
{_id: "acc1", balance: 250}

// Transaction with snapshot at timestamp 1500:
// Reads version 1 (balance: 100)

// Transaction with snapshot at timestamp 2500:
// Reads version 2 (balance: 200)
```

**3. Snapshot Timestamp:**

```javascript
session.startTransaction({
  readConcern: {level: "snapshot"}
})

// MongoDB internally assigns snapshot timestamp
// All reads in transaction use this timestamp

// Logical clock: guarantees ordering
snapshot_timestamp = cluster_time_at_transaction_start

// All reads see data ≤ snapshot_timestamp
```

**4. Read Consistency Guarantees:**

**Repeatable Reads:**
```javascript
session.startTransaction({readConcern: {level: "snapshot"}})

// First read
const doc1 = db.collection.findOne({_id: 1}, {session})
// Returns: {_id: 1, value: 10}

// Another transaction updates and commits
// db.collection.updateOne({_id: 1}, {$set: {value: 20}})

// Second read in same transaction
const doc2 = db.collection.findOne({_id: 1}, {session})
// Still returns: {_id: 1, value: 10} (same as first read)

session.commitTransaction()
```

**No Phantom Reads:**
```javascript
session.startTransaction({readConcern: {level: "snapshot"}})

// First query
const count1 = db.products.countDocuments({status: "active"}, {session})
// Returns: 100

// Another transaction inserts new active product
// db.products.insertOne({status: "active", name: "New Product"})

// Second query in same transaction
const count2 = db.products.countDocuments({status: "active"}, {session})
// Still returns: 100 (no phantom reads)

session.commitTransaction()
```

**5. Write Conflict Detection:**

```javascript
// Transaction T1
session1.startTransaction({readConcern: {level: "snapshot"}})
const doc = db.accounts.findOne({_id: "acc1"}, {session: session1})
// Snapshot timestamp: 1000, reads balance: 100

// Transaction T2 (concurrent)
session2.startTransaction({readConcern: {level: "snapshot"}})
db.accounts.updateOne(
  {_id: "acc1"},
  {$set: {balance: 200}},
  {session: session2}
)
session2.commitTransaction() // Commits at timestamp: 2000

// T1 tries to update
db.accounts.updateOne(
  {_id: "acc1"},
  {$set: {balance: 150}}, // Based on stale read (balance: 100)
  {session: session1}
)

session1.commitTransaction()
// ERROR: WriteConflict
// Document modified between read (timestamp 1000) and write attempt
```

**6. Snapshot Isolation Anomalies:**

**Write Skew (Possible):**
```javascript
// Two doctors on-call, at least 1 required

// Transaction T1 (Dr. Alice requests time off)
session1.startTransaction({readConcern: {level: "snapshot"}})
const onCall = db.doctors.countDocuments({status: "on-call"}, {session: session1})
// Reads: 2 doctors on-call

if (onCall > 1) {
  db.doctors.updateOne(
    {name: "Alice"},
    {$set: {status: "off-call"}},
    {session: session1}
  )
}
session1.commitTransaction()

// Transaction T2 (Dr. Bob requests time off, concurrent)
session2.startTransaction({readConcern: {level: "snapshot"}})
const onCall2 = db.doctors.countDocuments({status: "on-call"}, {session: session2})
// Also reads: 2 doctors on-call (snapshot before T1 committed)

if (onCall2 > 1) {
  db.doctors.updateOne(
    {name: "Bob"},
    {$set: {status: "off-call"}},
    {session: session2}
  )
}
session2.commitTransaction()

// Result: 0 doctors on-call! (write skew anomaly)
```

**Prevention:**
```javascript
// Use explicit locking or serializable isolation
db.doctors.updateOne(
  {
    name: "Alice",
    // Check constraint in update
    $expr: {$gt: [{$size: "$colleagues_on_call"}, 1]}
  },
  {$set: {status: "off-call"}},
  {session}
)
```

**7. Performance Characteristics:**

**Benefits:**
- No read locks
- High read concurrency
- Predictable read performance
- No blocking between readers and writers

**Costs:**
- Version storage overhead
- Write conflict retries
- Garbage collection of old versions
- Higher memory usage

**8. Snapshot Cleanup:**

```javascript
// WiredTiger periodically removes old versions

// Version GC policy:
// - Keep versions needed by active transactions
// - Keep versions within checkpoint interval
// - Remove older versions

// Oldest active transaction determines oldest required version
oldest_required = min(all_active_transaction_snapshots)
```

**9. Configuration:**

```javascript
// Transaction with snapshot isolation
session.startTransaction({
  readConcern: {level: "snapshot"},
  writeConcern: {w: "majority"},
  maxTimeMS: 60000  // Snapshot valid for max 60s
})

// Read preference
session.startTransaction({
  readConcern: {level: "snapshot"},
  readPreference: "primary"  // Must read from primary
})
```

**10. Monitoring:**

```javascript
// Check active transactions
db.serverStatus().transactions

// View transaction metrics
{
  currentActive: 5,
  currentInactive: 0,
  currentOpen: 5,
  totalAborted: 120,
  totalCommitted: 9880,
  totalStarted: 10000
}

// Find long-running transactions
db.currentOp({
  active: true,
  secs_running: {$gte: 30},
  $or: [
    {op: "command", "command.commitTransaction": 1},
    {op: "command", "command.abortTransaction": 1}
  ]
})
```

---

## Aggregation Framework Deep Dive

### 121. Explain $facet and $bucket stages with examples.

**$facet Stage:**

**$facet** allows running multiple aggregation pipelines in parallel on the same input documents and returns results in a single document.

**Use Cases:**
- Multiple analytics on same dataset
- Dashboard queries with different metrics
- Pagination with total count

**Example 1: E-commerce Analytics**
```javascript
db.products.aggregate([
  {$match: {category: "electronics"}},
  {$facet: {
    // Facet 1: Price statistics
    "priceStats": [
      {$group: {
        _id: null,
        avgPrice: {$avg: "$price"},
        minPrice: {$min: "$price"},
        maxPrice: {$max: "$price"},
        totalProducts: {$sum: 1}
      }}
    ],
    
    // Facet 2: Top 5 brands by product count
    "topBrands": [
      {$group: {
        _id: "$brand",
        count: {$sum: 1}
      }},
      {$sort: {count: -1}},
      {$limit: 5}
    ],
    
    // Facet 3: Price range distribution
    "priceRanges": [
      {$bucket: {
        groupBy: "$price",
        boundaries: [0, 100, 500, 1000, 5000],
        default: "5000+",
        output: {
          count: {$sum: 1},
          products: {$push: "$name"}
        }
      }}
    ],
    
    // Facet 4: Recent products
    "recentProducts": [
      {$sort: {createdAt: -1}},
      {$limit: 10},
      {$project: {name: 1, price: 1, brand: 1}}
    ]
  }}
])

// Result:
{
  "priceStats": [{
    _id: null,
    avgPrice: 749.99,
    minPrice: 29.99,
    maxPrice: 4999.99,
    totalProducts: 1250
  }],
  "topBrands": [
    {_id: "Samsung", count: 320},
    {_id: "Apple", count: 280},
    {_id: "Sony", count: 210}
  ],
  "priceRanges": [
    {_id: 0, count: 150, products: [...]},
    {_id: 100, count: 450, products: [...]},
    {_id: 500, count: 380, products: [...]}
  ],
  "recentProducts": [...]
}
```

**Example 2: Pagination with Total Count**
```javascript
db.orders.aggregate([
  {$match: {status: "shipped"}},
  {$facet: {
    "metadata": [
      {$count: "total"},
      {$addFields: {
        page: 1,
        pageSize: 20
      }}
    ],
    "data": [
      {$skip: 0},
      {$limit: 20},
      {$sort: {orderDate: -1}}
    ]
  }}
])

// Result:
{
  "metadata": [{total: 5420, page: 1, pageSize: 20}],
  "data": [/* 20 orders */]
}
```

---

**$bucket Stage:**

**$bucket** categorizes documents into groups (buckets) based on a specified expression and boundaries.

**Syntax:**
```javascript
{$bucket: {
  groupBy: <expression>,
  boundaries: [<value1>, <value2>, ...],
  default: <literal>,  // Optional: for values outside boundaries
  output: {           // Optional: output specifications
    <output1>: {<accumulator>},
    <output2>: {<accumulator>}
  }
}}
```

**Example 1: Age Distribution**
```javascript
db.users.aggregate([
  {$bucket: {
    groupBy: "$age",
    boundaries: [0, 18, 25, 35, 50, 65, 100],
    default: "Other",
    output: {
      count: {$sum: 1},
      users: {$push: "$name"},
      avgAge: {$avg: "$age"}
    }
  }}
])

// Result:
[
  {_id: 0, count: 45, users: ["Alice", "Bob",...], avgAge: 12.5},
  {_id: 18, count: 230, users: [...], avgAge: 21.3},
  {_id: 25, count: 450, users: [...], avgAge: 29.8},
  {_id: 35, count: 320, users: [...], avgAge: 42.1},
  {_id: 50, count: 180, users: [...], avgAge: 57.2},
  {_id: 65, count: 75, users: [...], avgAge: 71.5}
]
```

**Example 2: Revenue Buckets**
```javascript
db.orders.aggregate([
  {$bucket: {
    groupBy: "$totalAmount",
    boundaries: [0, 50, 200, 1000, 10000],
    default: "Huge",
    output: {
      count: {$sum: 1},
      totalRevenue: {$sum: "$totalAmount"},
      avgOrder: {$avg: "$totalAmount"},
      orders: {$push: {orderId: "$_id", amount: "$totalAmount"}}
    }
  }}
])

// Result:
[
  {
    _id: 0,           // $0-$50
    count: 1200,
    totalRevenue: 36000,
    avgOrder: 30,
    orders: [...]
  },
  {
    _id: 50,          // $50-$200
    count: 800,
    totalRevenue: 96000,
    avgOrder: 120,
    orders: [...]
  },
  {
    _id: 200,         // $200-$1000
    count: 300,
    totalRevenue: 180000,
    avgOrder: 600,
    orders: [...]
  }
]
```

**$bucketAuto** (Automatic Boundaries):**

```javascript
// MongoDB automatically determines boundaries
db.products.aggregate([
  {$bucketAuto: {
    groupBy: "$price",
    buckets: 5,  // Create 5 equal-sized buckets
    output: {
      count: {$sum: 1},
      avgPrice: {$avg: "$price"},
      products: {$push: "$name"}
    }
  }}
])

// MongoDB calculates boundaries to distribute documents evenly
```

**Example 3: Time-based Bucketing**
```javascript
db.logs.aggregate([
  {$bucket: {
    groupBy: {$hour: "$timestamp"},
    boundaries: [0, 6, 12, 18, 24],
    output: {
      count: {$sum: 1},
      errors: {
        $sum: {$cond: [{$eq: ["$level", "ERROR"]}, 1, 0]}
      }
    }
  }}
])

// Result: Logs grouped by time of day
[
  {_id: 0, count: 450, errors: 12},    // 12 AM - 6 AM
  {_id: 6, count: 1200, errors: 45},   // 6 AM - 12 PM
  {_id: 12, count: 2100, errors: 78},  // 12 PM - 6 PM
  {_id: 18, count: 890, errors: 23}    // 6 PM - 12 AM
]
```

**Combining $facet and $bucket:**
```javascript
db.sales.aggregate([
  {$facet: {
    "byRegion": [
      {$group: {
        _id: "$region",
        totalSales: {$sum: "$amount"}
      }}
    ],
    "byAmount": [
      {$bucket: {
        groupBy: "$amount",
        boundaries: [0, 100, 500, 1000, 5000],
        default: "VIP",
        output: {
          count: {$sum: 1},
          revenue: {$sum: "$amount"}
        }
      }}
    ],
    "byQuarter": [
      {$bucket: {
        groupBy: {$month: "$date"},
        boundaries: [1, 4, 7, 10, 13],
        output: {
          sales: {$sum: "$amount"},
          transactions: {$sum: 1}
        }
      }}
    ]
  }}
])
```

---

### 122. What's the difference between $group and $accumulator operators?

**$group Stage:**

**$group** is a pipeline stage that groups documents by a specified identifier and applies accumulator expressions.

**Syntax:**
```javascript
{$group: {
  _id: <expression>,  // Group key
  <field1>: {<accumulator1>: <expression>},
  <field2>: {<accumulator2>: <expression>}
}}
```

**Example:**
```javascript
db.orders.aggregate([
  {$group: {
    _id: "$customerId",
    totalSpent: {$sum: "$amount"},
    orderCount: {$sum: 1},
    avgOrderValue: {$avg: "$amount"},
    orders: {$push: {orderId: "$_id", amount: "$amount"}}
  }}
])
```

---

**$accumulator Operator:**

**$accumulator** is a custom accumulator operator that allows you to define custom aggregation logic using JavaScript functions (MongoDB 4.4+).

**Syntax:**
```javascript
{$accumulator: {
  init: <code>,                    // Initialize state
  accumulate: <code>,              // Process each document
  accumulateArgs: [<arg1>, ...],  // Arguments to accumulate
  merge: <code>,                   // Merge states (sharding)
  finalize: <code>,               // Final transformation
  lang: "js"
}}
```

**Key Differences:**

| Aspect | $group | $accumulator |
|--------|--------|--------------|
| Type | Pipeline stage | Accumulator operator |
| Built-in | Yes | Custom logic |
| Performance | Optimized (C++) | Slower (JavaScript) |
| Flexibility | Limited to built-in operators | Fully customizable |
| Use Case | Standard aggregations | Complex custom logic |

---

**Built-in Accumulator Operators (used with $group):**

```javascript
// Standard accumulators
{
  $sum: <expression>,
  $avg: <expression>,
  $max: <expression>,
  $min: <expression>,
  $first: <expression>,
  $last: <expression>,
  $push: <expression>,
  $addToSet: <expression>,
  $stdDevPop: <expression>,
  $stdDevSamp: <expression>
}

// Example
db.sales.aggregate([
  {$group: {
    _id: "$product",
    totalRevenue: {$sum: "$amount"},
    avgPrice: {$avg: "$amount"},
    maxSale: {$max: "$amount"},
    uniqueCustomers: {$addToSet: "$customerId"}
  }}
])
```

---

**Custom $accumulator Examples:**

**Example 1: Weighted Average**
```javascript
db.reviews.aggregate([
  {$group: {
    _id: "$productId",
    weightedRating: {
      $accumulator: {
        init: function() {
          return {sum: 0, weightSum: 0}
        },
        accumulate: function(state, rating, helpful) {
          return {
            sum: state.sum + (rating * helpful),
            weightSum: state.weightSum + helpful
          }
        },
        accumulateArgs: ["$rating", "$helpfulVotes"],
        merge: function(state1, state2) {
          return {
            sum: state1.sum + state2.sum,
            weightSum: state1.weightSum + state2.weightSum
          }
        },
        finalize: function(state) {
          return state.weightSum > 0 
            ? state.sum / state.weightSum 
            : 0
        },
        lang: "js"
      }
    }
  }}
])
```

**Example 2: Running Percentile Calculation**
```javascript
db.testScores.aggregate([
  {$group: {
    _id: "$class",
    p95Score: {
      $accumulator: {
        init: function() {
          return []
        },
        accumulate: function(scores, score) {
          scores.push(score)
          return scores
        },
        accumulateArgs: ["$score"],
        merge: function(scores1, scores2) {
          return scores1.concat(scores2)
        },
        finalize: function(scores) {
          scores.sort((a, b) => a - b)
          const index = Math.ceil(scores.length * 0.95) - 1
          return scores[index]
        },
        lang: "js"
      }
    }
  }}
])
```

**Example 3: Custom String Aggregation**
```javascript
db.comments.aggregate([
  {$group: {
    _id: "$postId",
    topWords: {
      $accumulator: {
        init: function() {
          return {}
        },
        accumulate: function(wordCounts, text) {
          const words = text.toLowerCase().split(/\s+/)
          words.forEach(word => {
            if (word.length > 3) {
              wordCounts[word] = (wordCounts[word] || 0) + 1
            }
          })
          return wordCounts
        },
        accumulateArgs: ["$text"],
        merge: function(counts1, counts2) {
          Object.keys(counts2).forEach(word => {
            counts1[word] = (counts1[word] || 0) + counts2[word]
          })
          return counts1
        },
        finalize: function(wordCounts) {
          return Object.entries(wordCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10)
            .map(([word, count]) => ({word, count}))
        },
        lang: "js"
      }
    }
  }}
])
```

**Example 4: Complex Business Logic**
```javascript
// Calculate customer tier based on custom rules
db.orders.aggregate([
  {$group: {
    _id: "$customerId",
    tier: {
      $accumulator: {
        init: function() {
          return {
            totalSpent: 0,
            orderCount: 0,
            returnsCount: 0,
            avgOrderValue: 0
          }
        },
        accumulate: function(state, amount, isReturn) {
          state.orderCount++
          if (isReturn) {
            state.returnsCount++
          } else {
            state.totalSpent += amount
          }
          state.avgOrderValue = state.totalSpent / (state.orderCount - state.returnsCount)
          return state
        },
        accumulateArgs: ["$amount", "$isReturn"],
        merge: function(state1, state2) {
          return {
            totalSpent: state1.totalSpent + state2.totalSpent,
            orderCount: state1.orderCount + state2.orderCount,
            returnsCount: state1.returnsCount + state2.returnsCount,
            avgOrderValue: (state1.totalSpent + state2.totalSpent) / 
                          (state1.orderCount + state2.orderCount - 
                           state1.returnsCount - state2.returnsCount)
          }
        },
        finalize: function(state) {
          const returnRate = state.returnsCount / state.orderCount
          
          if (state.totalSpent > 10000 && returnRate < 0.05) {
            return "platinum"
          } else if (state.totalSpent > 5000 && returnRate < 0.1) {
            return "gold"
          } else if (state.totalSpent > 1000) {
            return "silver"
          } else {
            return "bronze"
          }
        },
        lang: "js"
      }
    }
  }}
])
```

**Performance Considerations:**

1. **$group with built-ins**: Always prefer when possible (10-100x faster)
2. **$accumulator**: Use only for logic that can't be expressed with built-in operators
3. **Memory**: JavaScript accumulators use more memory
4. **Optimization**: Built-in operators are pushed down to storage engine

**When to Use Each:**

**Use $group + built-in accumulators:**
- Standard aggregations (sum, avg, count)
- Simple array operations
- Performance-critical queries
- Production workloads

**Use $accumulator:**
- Complex custom business logic
- Algorithms not supported by built-ins
- Prototyping complex calculations
- When built-ins can't express the logic

---

### 123. How can $merge be used to write aggregation results into another collection?

**$merge** (MongoDB 4.2+) writes aggregation pipeline results to a collection, with options for handling existing documents.

**Basic Syntax:**
```javascript
{$merge: {
  into: <target_collection>,
  on: <identifier_field>,          // Optional
  whenMatched: <action>,            // Optional
  whenNotMatched: <action>          // Optional
}}
```

**Actions:**

**whenMatched:**
- `replace` (default): Replace entire document
- `keepExisting`: Keep existing document, discard new
- `merge`: Merge new fields into existing
- `fail`: Fail if document exists
- `pipeline`: Custom update pipeline

**whenNotMatched:**
- `insert` (default): Insert new document
- `discard`: Discard new document
- `fail`: Fail if document doesn't exist

---

**Example 1: Simple Merge (Replace)**
```javascript
// Aggregate daily sales and merge into summary collection
db.orders.aggregate([
  {$match: {
    orderDate: {
      $gte: ISODate("2025-11-08T00:00:00Z"),
      $lt: ISODate("2025-11-09T00:00:00Z")
    }
  }},
  {$group: {
    _id: {
      product: "$productId",
      date: {$dateToString: {format: "%Y-%m-%d", date: "$orderDate"}}
    },
    totalSales: {$sum: "$amount"},
    quantity: {$sum: "$quantity"},
    orderCount: {$sum: 1}
  }},
  {$merge: {
    into: "dailySalesSummary",
    on: "_id",
    whenMatched: "replace",
    whenNotMatched: "insert"
  }}
])

// Result in dailySalesSummary:
{
  _id: {product: "prod123", date: "2025-11-08"},
  totalSales: 5420.50,
  quantity: 124,
  orderCount: 45
}
```

---

**Example 2: Incremental Updates (Merge)**
```javascript
// Update customer stats incrementally
db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {
    _id: "$customerId",
    newOrders: {$sum: 1},
    newRevenue: {$sum: "$amount"}
  }},
  {$merge: {
    into: "customerStats",
    on: "_id",
    whenMatched: "merge",  // Merge new fields, keep existing
    whenNotMatched: "insert"
  }}
])

// Before:
{_id: "cust123", totalOrders: 10, totalRevenue: 1000}

// After merge:
{
  _id: "cust123",
  totalOrders: 10,           // Existing field kept
  totalRevenue: 1000,        // Existing field kept
  newOrders: 5,              // New field added
  newRevenue: 450            // New field added
}
```

---

**Example 3: Custom Pipeline (Complex Logic)**
```javascript
// Update product inventory with custom logic
db.orderItems.aggregate([
  {$group: {
    _id: "$productId",
    soldQuantity: {$sum: "$quantity"}
  }},
  {$merge: {
    into: "products",
    on: "_id",
    whenMatched: [
      {$set: {
        stock: {$subtract: ["$stock", "$new.soldQuantity"]},
        lastSold: new Date(),
        totalSold: {$add: ["$totalSold", "$new.soldQuantity"]},
        status: {
          $cond: {
            if: {$lte: [{$subtract: ["$stock", "$new.soldQuantity"]}, 10]},
            then: "low_stock",
            else: "in_stock"
          }
        }
      }}
    ],
    whenNotMatched: "discard"
  }}
])

// $new refers to aggregation result
// $ refers to existing document fields
```

---

**Example 4: Materialized View Pattern**
```javascript
// Create/update materialized view for dashboard
db.transactions.aggregate([
  {$match: {timestamp: {$gte: ISODate("2025-11-01")}}},
  {$facet: {
    byCategory: [
      {$group: {
        _id: "$category",
        count: {$sum: 1},
        total: {$sum: "$amount"}
      }}
    ],
    byDay: [
      {$group: {
        _id: {$dateToString: {format: "%Y-%m-%d", date: "$timestamp"}},
        transactions: {$sum: 1},
        revenue: {$sum: "$amount"}
      }},
      {$sort: {_id: 1}}
    ],
    overall: [
      {$group: {
        _id: null,
        totalTransactions: {$sum: 1},
        totalRevenue: {$sum: "$amount"},
        avgTransaction: {$avg: "$amount"}
      }}
    ]
  }},
  {$project: {
    _id: "november_2025_summary",
    timestamp: new Date(),
    byCategory: 1,
    byDay: 1,
    overall: {$arrayElemAt: ["$overall", 0]}
  }},
  {$merge: {
    into: "dashboardCache",
    on: "_id",
    whenMatched: "replace",
    whenNotMatched: "insert"
  }}
])

// Schedule this to run periodically
// Fast dashboard queries from dashboardCache
```

---

**Example 5: Time-Series Rollup**
```javascript
// Rollup hourly metrics to daily
db.hourlyMetrics.aggregate([
  {$match: {
    timestamp: {
      $gte: ISODate("2025-11-08T00:00:00Z"),
      $lt: ISODate("2025-11-09T00:00:00Z")
    }
  }},
  {$group: {
    _id: {
      sensor: "$sensorId",
      date: {$dateToString: {format: "%Y-%m-%d", date: "$timestamp"}}
    },
    avgTemp: {$avg: "$temperature"},
    minTemp: {$min: "$temperature"},
    maxTemp: {$max: "$temperature"},
    readings: {$sum: "$count"}
  }},
  {$merge: {
    into: "dailyMetrics",
    on: "_id",
    whenMatched: "replace",
    whenNotMatched: "insert"
  }}
])
```

---

**Example 6: Upsert with Timestamp**
```javascript
// Track last update time
db.events.aggregate([
  {$group: {
    _id: "$userId",
    lastEvent: {$max: "$timestamp"},
    eventCount: {$sum: 1}
  }},
  {$merge: {
    into: "userActivity",
    on: "_id",
    whenMatched: [
      {$set: {
        lastEvent: "$new.lastEvent",
        eventCount: {$add: ["$eventCount", "$new.eventCount"]},
        updatedAt: new Date()
      }}
    ],
    whenNotMatched: "insert"
  }}
])
```

---

**Example 7: Different Database/Collection**
```javascript
// Merge to different database
db.transactions.aggregate([
  {$group: {
    _id: "$storeId",
    dailyRevenue: {$sum: "$amount"}
  }},
  {$merge: {
    into: {
      db: "analytics",
      coll: "storeMetrics"
    },
    on: "_id",
    whenMatched: "replace",
    whenNotMatched: "insert"
  }}
])
```

---

**Example 8: Conditional Merge**
```javascript
// Only merge if certain conditions met
db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {
    _id: "$customerId",
    lifetimeValue: {$sum: "$amount"}
  }},
  {$match: {lifetimeValue: {$gte: 1000}}},  // Only high-value customers
  {$merge: {
    into: "vipCustomers",
    on: "_id",
    whenMatched: [
      {$set: {
        lifetimeValue: "$new.lifetimeValue",
        tier: {
          $switch: {
            branches: [
              {case: {$gte: ["$new.lifetimeValue", 10000]}, then: "platinum"},
              {case: {$gte: ["$new.lifetimeValue", 5000]}, then: "gold"}
            ],
            default: "silver"
          }
        },
        updatedAt: new Date()
      }}
    ],
    whenNotMatched: "insert"
  }}
])
```

---

**Advantages over $out:**

| Feature | $merge | $out |
|---------|--------|------|
| Update existing docs | ✓ | ✗ (replaces entire collection) |
| Custom update logic | ✓ | ✗ |
| On-demand refresh | ✓ | ✗ |
| Preserve indexes | ✓ | ✗ |
| Atomic | Per-document | Collection-level |
| Sharded output | ✓ | Limited |

---

**Best Practices:**

1. **Use Indexes**: Ensure target collection has index on merge key
```javascript
db.targetCollection.createIndex({_id: 1})
```

2. **Error Handling**: Wrap in try-catch for production
```javascript
try {
  db.collection.aggregate([...pipeline, {$merge: {...}}])
} catch (e) {
  if (e.code === 11000) {
    // Handle duplicate key error
  }
}
```

3. **Monitor Performance**: Check merge operation duration
```javascript
db.currentOp({
  "command.aggregate": {$exists: true},
  "command.pipeline.$merge": {$exists: true}
})
```

4. **Schedule for Off-Peak**: Run heavy merges during low-traffic periods

5. **Test with Small Datasets**: Verify logic before production

---
# MongoDB Advanced Topics Guide

## Aggregation Pipeline Advanced

### 124. What is $graphLookup and when would you use it?

**$graphLookup** performs a recursive search on a collection to traverse graph or tree structures.

**Syntax:**
```javascript
{
  $graphLookup: {
    from: "collection",
    startWith: "$fieldName",
    connectFromField: "fieldName",
    connectToField: "fieldName",
    as: "outputArray",
    maxDepth: number,
    depthField: "depthFieldName",
    restrictSearchWithMatch: { query }
  }
}
```

**Use Cases:**
- **Organizational hierarchies** - Find all employees reporting to a manager (direct and indirect)
- **Social networks** - Find friends of friends
- **Category trees** - Navigate product categories
- **Recommendation systems** - Find connected items

**Example - Employee Hierarchy:**
```javascript
db.employees.aggregate([
  {
    $graphLookup: {
      from: "employees",
      startWith: "$_id",
      connectFromField: "_id",
      connectToField: "managerId",
      as: "subordinates",
      maxDepth: 3,
      depthField: "level"
    }
  }
])
```

**Example - Social Network:**
```javascript
db.users.aggregate([
  { $match: { username: "alice" } },
  {
    $graphLookup: {
      from: "users",
      startWith: "$friends",
      connectFromField: "friends",
      connectToField: "_id",
      as: "network",
      maxDepth: 2,
      restrictSearchWithMatch: { active: true }
    }
  }
])
```

---

### 125. How can you optimize an aggregation pipeline?

**Key Optimization Strategies:**

#### 1. **Stage Ordering**
```javascript
// 2. Use Collection Normally
const db = client.db('myapp')
await db.collection('patients').insertOne({
  name: 'Jane Doe',
  ssn: '987-65-4321',  // Encrypted, queryable
  age: 45,  // Encrypted, range queryable
  medicalRecord: 'Sensitive data...'  // Encrypted, not queryable
})

// 3. Query Encrypted Fields
const patient = await db.collection('patients').findOne({
  ssn: '987-65-4321'  // Equality query on encrypted field
})

const seniors = await db.collection('patients').find({
  age: { $gte: 65 }  // Range query on encrypted field
}).toArray()
```

**Queryable Encryption vs CSFLE:**

| Feature | CSFLE | Queryable Encryption |
|---------|-------|---------------------|
| **Equality Queries** | ✅ (Deterministic) | ✅ (More secure) |
| **Range Queries** | ❌ | ✅ |
| **Frequency Analysis Protection** | ❌ | ✅ |
| **MongoDB Version** | 4.2+ | 7.0+ |
| **Performance** | Faster | Slightly slower |
| **Security** | Good | Better |

**Use Cases:**
- **Healthcare** - Patient records, PHI data
- **Finance** - Credit cards, bank accounts, SSNs
- **PII Protection** - Email, phone, addresses
- **Compliance** - GDPR, HIPAA, PCI-DSS

**Best Practices:**
- Use queryable encryption for fields needing search
- Use random encryption for maximum security (no queries needed)
- Rotate data encryption keys regularly
- Store master keys in proper KMS (AWS, Azure, GCP)
- Implement key rotation policies
- Monitor encryption performance impact

---

### 138. How do you implement IP whitelisting for MongoDB?

**IP Whitelisting restricts access to specific IP addresses or ranges**

#### **1. MongoDB Atlas (Cloud)**

**Via UI:**
1. Navigate to Network Access
2. Add IP Address
3. Enter IP or CIDR range (e.g., 192.168.1.0/24)
4. Add description (optional)
5. Confirm

**Via Atlas CLI:**
```bash
# Add single IP
atlas accessLists create 203.0.113.45 --projectId PROJECT_ID

# Add CIDR block
atlas accessLists create 192.168.1.0/24 --projectId PROJECT_ID

# Add temporary access (auto-expires)
atlas accessLists create 198.51.100.10 --projectId PROJECT_ID --deleteAfter "2025-12-31T23:59:59Z"

# List current whitelist
atlas accessLists list --projectId PROJECT_ID

# Delete entry
atlas accessLists delete 203.0.113.45 --projectId PROJECT_ID
```

**Via Atlas API:**
```bash
curl --user "PUBLIC_KEY:PRIVATE_KEY" \
  --digest \
  --header "Content-Type: application/json" \
  --request POST \
  "https://cloud.mongodb.com/api/atlas/v1.0/groups/PROJECT_ID/accessList" \
  --data '{
    "ipAddress": "203.0.113.45",
    "comment": "Production API server"
  }'
```

---

#### **2. Self-Hosted MongoDB**

**Method 1: bindIp Configuration**
```yaml
# mongod.conf
net:
  port: 27017
  bindIp: 127.0.0.1,192.168.1.10  # Comma-separated IPs
  # bindIpAll: true  # Listen on all interfaces (dangerous!)
```

**Method 2: Firewall Rules (Recommended)**

**Linux (iptables):**
```bash
# Allow specific IP
iptables -A INPUT -p tcp --dport 27017 -s 203.0.113.45 -j ACCEPT

# Allow CIDR range
iptables -A INPUT -p tcp --dport 27017 -s 192.168.1.0/24 -j ACCEPT

# Block all others
iptables -A INPUT -p tcp --dport 27017 -j DROP

# Save rules
iptables-save > /etc/iptables/rules.v4
```

**Linux (ufw):**
```bash
# Enable firewall
ufw enable

# Allow specific IP
ufw allow from 203.0.113.45 to any port 27017

# Allow subnet
ufw allow from 192.168.1.0/24 to any port 27017

# Check status
ufw status numbered

# Delete rule
ufw delete 3
```

**Linux (firewalld):**
```bash
# Create rich rule
firewall-cmd --permanent --add-rich-rule='
  rule family="ipv4"
  source address="203.0.113.45"
  port protocol="tcp" port="27017" accept'

# Add zone for MongoDB
firewall-cmd --permanent --new-zone=mongodb
firewall-cmd --permanent --zone=mongodb --add-source=192.168.1.0/24
firewall-cmd --permanent --zone=mongodb --add-port=27017/tcp

# Reload
firewall-cmd --reload
```

**Windows Firewall:**
```powershell
# Allow specific IP
New-NetFirewallRule -DisplayName "MongoDB from 203.0.113.45" `
  -Direction Inbound `
  -Protocol TCP `
  -LocalPort 27017 `
  -RemoteAddress 203.0.113.45 `
  -Action Allow

# Allow subnet
New-NetFirewallRule -DisplayName "MongoDB from local network" `
  -Direction Inbound `
  -Protocol TCP `
  -LocalPort 27017 `
  -RemoteAddress 192.168.1.0/24 `
  -Action Allow
```

---

#### **3. Cloud Provider Security Groups**

**AWS Security Groups:**
```bash
# Via AWS CLI
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 27017 \
  --cidr 203.0.113.45/32

# Or via Terraform
resource "aws_security_group_rule" "mongodb" {
  type              = "ingress"
  from_port         = 27017
  to_port           = 27017
  protocol          = "tcp"
  cidr_blocks       = ["203.0.113.45/32", "192.168.1.0/24"]
  security_group_id = aws_security_group.mongodb.id
}
```

**Azure Network Security Groups:**
```bash
# Via Azure CLI
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myNSG \
  --name Allow-MongoDB \
  --priority 100 \
  --source-address-prefixes 203.0.113.45 \
  --destination-port-ranges 27017 \
  --protocol Tcp \
  --access Allow
```

**GCP Firewall Rules:**
```bash
# Via gcloud
gcloud compute firewall-rules create allow-mongodb \
  --allow tcp:27017 \
  --source-ranges 203.0.113.45/32,192.168.1.0/24 \
  --target-tags mongodb-server
```

---

#### **4. Application-Level IP Filtering**

**Node.js Middleware:**
```javascript
const allowedIPs = ['203.0.113.45', '192.168.1.10']

function ipWhitelist(req, res, next) {
  const clientIP = req.ip || req.connection.remoteAddress
  
  if (!allowedIPs.includes(clientIP)) {
    return res.status(403).json({ error: 'Access denied' })
  }
  
  next()
}

app.use('/api', ipWhitelist, apiRoutes)
```

---

#### **5. VPN/Bastion Host Approach**

**Production Best Practice:**
```
Client → VPN → Bastion Host → MongoDB

# Only allow MongoDB access from bastion host
iptables -A INPUT -p tcp --dport 27017 -s BASTION_IP -j ACCEPT
iptables -A INPUT -p tcp --dport 27017 -j DROP
```

---

#### **Best Practices**

**Multi-Layer Security:**
```yaml
1. Cloud Security Groups (AWS/Azure/GCP)
2. OS Firewall (iptables/firewalld)
3. MongoDB bindIp configuration
4. VPN for remote access
5. Authentication (SCRAM, x.509, LDAP)
6. TLS/SSL encryption
```

**Dynamic IP Management:**
```python
# Script to update Atlas whitelist with current IP
import requests
import json

def update_atlas_whitelist():
    current_ip = requests.get('https://api.ipify.org').text
    
    # Add to Atlas
    response = requests.post(
        f'https://cloud.mongodb.com/api/atlas/v1.0/groups/{PROJECT_ID}/accessList',
        auth=(PUBLIC_KEY, PRIVATE_KEY),
        json={
            'ipAddress': current_ip,
            'comment': 'Auto-updated',
            'deleteAfterDate': '2025-12-31T23:59:59Z'  # Auto-expire
        }
    )
    
    print(f'Added {current_ip} to whitelist')

# Run on schedule
update_atlas_whitelist()
```

**Documentation:**
```markdown
# IP Whitelist Documentation

## Production IPs
- API Server 1: 203.0.113.45
- API Server 2: 203.0.113.46
- Office Network: 192.168.1.0/24

## Emergency Access
- VPN: 10.0.0.0/8
- Bastion: 198.51.100.10

## Review Schedule
- Monthly review of all IPs
- Remove unused entries
- Update documentation
```

---

### 139. What is audit logging and how do you enable it?

**Audit Logging** tracks database activities for security, compliance, and troubleshooting.

**MongoDB Enterprise Feature** (not available in Community Edition)

#### **Enable Audit Logging**

**Configuration File:**
```yaml
# mongod.conf
auditLog:
  destination: file
  format: JSON
  path: /var/log/mongodb/audit.json
  filter: '{}'  # Log everything (can be filtered)
```

**Command Line:**
```bash
mongod --auditDestination file \
  --auditFormat JSON \
  --auditPath /var/log/mongodb/audit.json \
  --auditFilter '{}'
```

**Start MongoDB with Auditing:**
```bash
sudo systemctl restart mongod
```

---

#### **Audit Log Destinations**

**1. File (JSON or BSON):**
```yaml
auditLog:
  destination: file
  format: JSON  # or BSON
  path: /var/log/mongodb/audit.json
```

**2. Syslog:**
```yaml
auditLog:
  destination: syslog
  format: JSON
```

**3. Console:**
```yaml
auditLog:
  destination: console
  format: JSON
```

---

#### **Audit Filters**

**Log All Operations:**
```yaml
auditLog:
  filter: '{}'
```

**Log Specific Actions:**
```javascript
// Authentication events only
{
  atype: { $in: ['authenticate', 'logout'] }
}

// DDL operations (createCollection, dropCollection, etc.)
{
  atype: { $in: ['createCollection', 'dropCollection', 'createIndex', 'dropIndex'] }
}

// User management
{
  atype: { $in: ['createUser', 'dropUser', 'updateUser', 'grantRolesToUser', 'revokeRolesFromUser'] }
}

// Read/write operations on specific collection
{
  atype: { $in: ['insert', 'update', 'delete', 'find'] },
  'param.ns': 'mydb.sensitive_collection'
}

// Failed authentication attempts
{
  atype: 'authenticate',
  result: 5  // Authorization failed
}

// Administrative commands
{
  atype: 'authCheck',
  'param.command': { $in: ['shutdown', 'serverStatus', 'replSetReconfig'] }
}
```

**Apply Filter:**
```yaml
# mongod.conf
auditLog:
  destination: file
  format: JSON
  path: /var/log/mongodb/audit.json
  filter: '{ "atype": { "$in": ["authenticate", "createUser", "dropUser"] } }'
```

---

#### **Audit Log Format**

**Sample Audit Entry:**
```json
{
  "atype": "authenticate",
  "ts": { "$date": "2025-11-12T10:30:00.000Z" },
  "local": { "ip": "127.0.0.1", "port": 27017 },
  "remote": { "ip": "192.168.1.100", "port": 52345 },
  "users": [{ "user": "app_user", "db": "admin" }],
  "roles": [{ "role": "readWrite", "db": "myapp" }],
  "param": {
    "user": "app_user",
    "db": "admin",
    "mechanism": "SCRAM-SHA-256"
  },
  "result": 0
}
```

**Field Descriptions:**
- `atype`: Action type (authenticate, insert, update, delete, etc.)
- `ts`: Timestamp
- `local`: MongoDB server IP/port
- `remote`: Client IP/port
- `users`: Authenticated user
- `roles`: User roles
- `param`: Action-specific parameters
- `result`: Result code (0 = success, non-zero = failure)

---

#### **Common Audit Scenarios**

**1. Track Failed Logins:**
```yaml
auditLog:
  filter: '{ "atype": "authenticate", "result": { "$ne": 0 } }'
```

**2. Monitor Sensitive Collections:**
```yaml
auditLog:
  filter: '{
    "atype": { "$in": ["insert", "update", "delete", "find"] },
    "$or": [
      { "param.ns": "myapp.users" },
      { "param.ns": "myapp.payments" },
      { "param.ns": "myapp.transactions" }
    ]
  }'
```

**3. Track Administrative Actions:**
```yaml
auditLog:
  filter: '{
    "$or": [
      { "atype": { "$in": ["createUser", "dropUser", "updateUser"] } },
      { "atype": "authCheck", "param.command": "shutdown" },
      { "atype": "authCheck", "param.command": "replSetReconfig" }
    ]
  }'
```

**4. Compliance Logging (HIPAA, PCI-DSS):**
```yaml
# Log all data access
auditLog:
  filter: '{
    "$or": [
      { "atype": { "$in": ["insert", "update", "delete", "find", "findAndModify"] } },
      { "atype": { "$in": ["createUser", "dropUser", "grantRolesToUser"] } },
      { "atype": "authenticate" }
    ]
  }'
```

---

#### **Analyze Audit Logs**

**Using mongosh:**
```javascript
// Read audit log (if in MongoDB collection)
use audit
db.log.find({ atype: 'authenticate', result: { $ne: 0 } })

// Failed login attempts by user
db.log.aggregate([
  { $match: { atype: 'authenticate', result: { $ne: 0 } } },
  { $group: { _id: '$users.user', count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

**Using jq (for JSON files):**
```bash
# Failed authentications
cat /var/log/mongodb/audit.json | jq 'select(.atype == "authenticate" and .result != 0)'

# Most active users
cat /var/log/mongodb/audit.json | jq -r '.users[0].user' | sort | uniq -c | sort -rn

# Operations on specific collection
cat /var/log/mongodb/audit.json | jq 'select(.param.ns == "myapp.users")'
```

**Using ELK Stack:**
```yaml
# Filebeat configuration
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/mongodb/audit.json
    json.keys_under_root: true
    json.add_error_key: true

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "mongodb-audit-%{+yyyy.MM.dd}"
```

---

#### **Rotate Audit Logs**

**Logrotate Configuration:**
```bash
# /etc/logrotate.d/mongodb-audit
/var/log/mongodb/audit.json {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
    create 0640 mongodb mongodb
    postrotate
        /usr/bin/killall -SIGUSR1 mongod
    endscript
}
```

**Manual Rotation:**
```bash
# Rotate log file
mv /var/log/mongodb/audit.json /var/log/mongodb/audit.json.$(date +%Y%m%d)

# Signal MongoDB to reopen log file
kill -SIGUSR1 $(pidof mongod)
```

---

#### **Best Practices**

**Performance Considerations:**
- Audit logging adds I/O overhead
- Use filters to reduce log volume
- Use BSON format for better performance than JSON
- Monitor disk space for audit logs
- Rotate logs regularly

**Security:**
- Restrict access to audit log files
  ```bash
  chmod 600 /var/log/mongodb/audit.json
  chown mongodb:mongodb /var/log/mongodb/audit.json
  ```
- Store logs on separate disk partition
- Forward logs to central SIEM system
- Encrypt audit logs at rest

**Compliance:**
- Define retention policy (90 days, 1 year, 7 years)
- Implement tamper-proof logging
- Regular audit log reviews
- Document audit procedures
- Test log integrity

---

### 140. What are MongoDB's compliance certifications (HIPAA, GDPR, etc.)?

MongoDB Atlas and Enterprise have various compliance certifications:

#### **1. HIPAA (Health Insurance Portability and Accountability Act)**

**Status:** ✅ MongoDB Atlas Enterprise is HIPAA-eligible

**Requirements:**
- Sign Business Associate Agreement (BAA) with MongoDB
- Use MongoDB Atlas M10+ clusters (not shared)
- Enable encryption at rest
- Enable encryption in transit (TLS)
- Implement audit logging
- Use field-level encryption for PHI

**Setup:**
```javascript
// Sign BAA through Atlas
// Atlas Settings → Privacy & Compliance → HIPAA

// Configure encryption
// Cluster → Configuration → Encryption at Rest: Enabled
// Connection: Require TLS

// Enable audit logging (Enterprise)
auditLog:
  destination: file
  format: JSON
  filter: '{ "atype": { "$in": ["authenticate", "insert", "update", "delete"] } }'

// Use CSFLE for PHI
const encryptedFieldsMap = {
  'healthcare.patients': {
    fields: [
      { path: 'ssn', bsonType: 'string', queries: { queryType: 'equality' } },
      { path: 'medicalRecord', bsonType: 'string' }
    ]
  }
}
```

---

#### **2. GDPR (General Data Protection Regulation)**

**Status:** ✅ MongoDB compliant

**Key Features:**
- **Right to Access:** Query user data
- **Right to Erasure:** Delete user data
- **Data Portability:** Export data in standard format
- **Pseudonymization:** Field-level encryption
- **Audit Trails:** Audit logging

**Implementation:**
```javascript
// Right to Access - Export user data
const userData = await db.collection('users').findOne({ email: 'user@example.com' })

// Right to Erasure - Delete user data
await db.collection('users').deleteOne({ email: 'user@example.com' })
await db.collection('orders').deleteMany({ userEmail: 'user@example.com' })
await db.collection('logs').deleteMany({ userId: ObjectId('...') })

// Data Portability - Export to JSON
mongodump --db=myapp --query='{"email":"user@example.com"}' --out=/exports

// Pseudonymization - Encrypt PII
const encryptedEmail = await encryption.encrypt(email, {
  algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic',
  keyId: dataKey
})

// Data residency - Use Atlas regions
// EU customers: Deploy in EU regions only (Frankfurt, Ireland, London)
```

**GDPR Compliance Checklist:**
- ✅ Data residency (deploy in appropriate regions)
- ✅ Encryption at rest and in transit
- ✅ Field-level encryption for sensitive data
- ✅ Audit logging for data access
- ✅ Data retention policies
- ✅ Implement user data export/deletion APIs
- ✅ Privacy policy and consent management

---

#### **3. SOC 2 Type II**

**Status:** ✅ MongoDB Atlas certified

**Controls:**
- Security
- Availability
- Processing Integrity
- Confidentiality
- Privacy

**Audit Report:** Available through Atlas (Contact MongoDB sales)

---

#### **4. ISO 27001**

**Status:** ✅ MongoDB Atlas certified

**Information Security Management System (ISMS)**
- Risk assessment
- Security policies
- Access controls
- Incident management
- Business continuity

---

#### **5. PCI DSS (Payment Card Industry Data Security Standard)**

**Status:** ✅ MongoDB Atlas can be used in PCI DSS environments

**Requirements:**
- Strong access control (authentication, authorization)
- Encryption of cardholder data
- Regular security testing
- Maintain audit trails
- Network segmentation

**Implementation:**
```javascript
// Never store full credit card numbers unencrypted
// Use tokenization or encryption

// Encrypt credit card data
const encryptedCard = await encryption.encrypt(creditCardNumber, {
  algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Random',  // Non-deterministic
  keyId: dataKey
})

await db.collection('payments').insertOne({
  userId: ObjectId('...'),
  cardLast4: '1234',  // Only store last 4 digits in plaintext
  cardToken: 'tok_...', // Payment processor token
  encryptedCard: encryptedCard  // Fully encrypted full number (if needed)
})

// Network isolation
// Use VPC peering or private endpoints
// Firewall rules to restrict access
```

---

#### **6. FedRAMP (Federal Risk and Authorization Management Program)**

**Status:** ✅ MongoDB Atlas for Government (FedRAMP Authorized)

**Levels:**
- Low Impact
- Moderate Impact
- High Impact

**Requirements:**
- US-based data centers only
- Enhanced security controls
- Continuous monitoring
- Incident response procedures

---

#### **7. CSA STAR (Cloud Security Alliance Security, Trust & Assurance Registry)**

**Status:** ✅ MongoDB Atlas Level 2 certified

---

#### **Compliance Summary Table**

| Certification | Atlas Support | Enterprise Support | Key Requirements |
|--------------|---------------|-------------------|------------------|
| **HIPAA** | ✅ (with BAA) | ✅ | Encryption, audit logging, BAA |
| **GDPR** | ✅ | ✅ | Data residency, encryption, right to erasure |
| **SOC 2 Type II** | ✅ | ✅ | Security controls, availability |
| **ISO 27001** | ✅ | ✅ | ISMS, risk management |
| **PCI DSS** | ✅ | ✅ | Cardholder data encryption, access control |
| **FedRAMP** | ✅ (Gov) | ✅ | US data centers, enhanced security |
| **CSA STAR** | ✅ | ✅ | Cloud security controls |

---

#### **Atlas Compliance Features**

**Network Security:**
- VPC Peering
- Private Endpoints (AWS PrivateLink, Azure Private Link)
- IP Whitelisting
- Dedicated clusters (M10+)

**Encryption:**
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.2+)
- Customer-managed keys (AWS KMS, Azure Key Vault, GCP KMS)
- Field-level encryption

**Access Control:**
- RBAC (Role-Based Access Control)
- LDAP integration
- x.509 certificate authentication
- Auditing and logging

**Backup & DR:**
- Continuous backups with point-in-time recovery
- Cross-region snapshots
- Automated backup encryption

**Monitoring:**
- Real-time performance monitoring
- Security alerts
- Audit logs

---

#### **Compliance Best Practices**

**1. Data Classification:**
```javascript
// Tag collections by sensitivity
db.createCollection('users', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      properties: {
        classification: { enum: ['public', 'internal', 'confidential', 'restricted'] }
      }
    }
  }
})
```

**2. Regular Audits:**
```bash
# Schedule regular access reviews
# Review user permissions quarterly
# Audit encryption key rotation
# Test backup/restore procedures
```

**3. Documentation:**
```markdown
# Compliance Documentation

## Data Flow Diagrams
- Where data is stored
- How data moves through systems
- Encryption points

## Access Control Matrix
- Who has access to what data
- Role definitions
- Access review schedule

## Incident Response Plan
- Data breach procedures
- Notification requirements
- Contact information
```

**4. Testing:**
```bash
# Penetration testing
# Vulnerability scanning
# Disaster recovery drills
# Compliance audits
```

---

## Deployment & Cloud

### 141. What's the difference between MongoDB Atlas, Ops Manager, and Enterprise Advanced?

#### **MongoDB Atlas (DBaaS - Database as a Service)**

**Fully managed cloud database**

**Key Features:**
- Automated provisioning and deployment
- Auto-scaling (storage and compute)
- Automated backups with PITR
- Built-in monitoring and alerting
- Global clusters (multi-region)
- Serverless instances (preview)
- Atlas Search (full-text search)
- Atlas Data Federation
- One-click upgrades

**Deployment:**
```bash
# Via Atlas CLI
atlas clusters create myCluster \
  --provider AWS \
  --region US_EAST_1 \
  --tier M10 \
  --members 3 \
  --projectId PROJECT_ID

# Via Terraform
resource "mongodbatlas_cluster" "cluster" {
  project_id = var.project_id
  name       = "production-cluster"
  
  provider_name               = "AWS"
  provider_region_name        = "US_EAST_1"
  provider_instance_size_name = "M10"
  
  replication_specs {
    num_shards = 1
    regions_config {
      region_name     = "US_EAST_1"
      electable_nodes = 3
      priority        = 7
    }
  }
}
```

**Pricing Model:**
- Pay-as-you-go
- Tiered pricing (M0/M2/M5 free tier, M10+) BAD - Filter after expensive operations
db.orders.aggregate([
  { $lookup: { ... } },  // Expensive
  { $unwind: "$items" },
  { $match: { status: "completed" } }  // Should be first
])

// GOOD - Filter early
db.orders.aggregate([
  { $match: { status: "completed" } },  // Reduce documents early
  { $lookup: { ... } },
  { $unwind: "$items" }
])
```

#### 2. **Use Indexes**
```javascript
// Ensure $match stages can use indexes
db.orders.createIndex({ status: 1, createdAt: -1 })

db.orders.aggregate([
  { $match: { status: "completed", createdAt: { $gte: startDate } } },
  // ... rest of pipeline
])
```

#### 3. **Projection Early**
```javascript
// BAD - Carry unnecessary fields
db.users.aggregate([
  { $lookup: { ... } },
  { $project: { name: 1, email: 1 } }
])

// GOOD - Project early to reduce memory
db.users.aggregate([
  { $project: { name: 1, email: 1, friendIds: 1 } },
  { $lookup: { ... } }
])
```

#### 4. **Limit Results**
```javascript
// Add $limit early when possible
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { price: -1 } },
  { $limit: 10 },  // Reduces documents in pipeline
  { $lookup: { ... } }
])
```

#### 5. **Use $facet for Multiple Aggregations**
```javascript
// Instead of running multiple pipelines
db.orders.aggregate([
  {
    $facet: {
      totalRevenue: [
        { $group: { _id: null, total: { $sum: "$amount" } } }
      ],
      topProducts: [
        { $unwind: "$items" },
        { $group: { _id: "$items.productId", count: { $sum: 1 } } },
        { $sort: { count: -1 } },
        { $limit: 5 }
      ]
    }
  }
])
```

#### 6. **Avoid $lookup When Possible**
```javascript
// Consider denormalization for frequently accessed data
// Instead of:
db.orders.aggregate([
  { $lookup: { from: "customers", ... } }
])

// Embed customer data in orders if read-heavy
{
  _id: ObjectId("..."),
  customerId: ObjectId("..."),
  customerName: "John Doe",  // Denormalized
  customerEmail: "john@example.com",  // Denormalized
  items: [...]
}
```

#### 7. **Use allowDiskUse for Large Datasets**
```javascript
db.orders.aggregate(
  [ /* pipeline */ ],
  { allowDiskUse: true }  // For pipelines exceeding 100MB memory
)
```

#### 8. **Optimize $unwind**
```javascript
// Use preserveNullAndEmptyArrays only when needed
{ $unwind: { path: "$items", preserveNullAndEmptyArrays: false } }
```

#### 9. **Use $indexStats to Monitor**
```javascript
db.collection.aggregate([
  { $indexStats: {} }
])
```

---

## Replica Set and Sharding

### 126. How do you force a MongoDB replica set failover?

**Methods to Force Failover:**

#### Method 1: Step Down Primary
```javascript
// Connect to primary
rs.stepDown(60)  // Step down for 60 seconds

// With options
rs.stepDown(120, 60)  // stepDownSecs, secondaryCatchUpPeriodSecs
```

#### Method 2: Using Priority
```javascript
// Set primary priority to 0 (temporarily)
cfg = rs.conf()
cfg.members[0].priority = 0  // Assuming member 0 is primary
rs.reconfig(cfg)

// Restore priority later
cfg.members[0].priority = 1
rs.reconfig(cfg)
```

#### Method 3: Shut Down Primary
```javascript
// On primary server
db.adminCommand({ shutdown: 1 })
// or
mongod --shutdown
```

#### Method 4: Freeze Secondary (Prevent from becoming primary)
```javascript
// Connect to secondary
rs.freeze(120)  // Freeze for 120 seconds
```

**Verification:**
```javascript
rs.status()
rs.isMaster()
```

**Best Practices:**
- Perform during maintenance windows
- Ensure secondaries are caught up (replication lag < 10 seconds)
- Monitor application connections
- Use stepDown for controlled failover
- Document the procedure in runbooks

---

### 127. What is the difference between primaryPreferred and secondaryPreferred read preferences?

**Read Preference Modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| **primary** | Always read from primary | Strong consistency required |
| **primaryPreferred** | Primary first, fallback to secondary | Default for most apps |
| **secondary** | Always read from secondary | Analytics, reports |
| **secondaryPreferred** | Secondary first, fallback to primary | Reduce primary load |
| **nearest** | Lowest network latency | Geo-distributed apps |

#### **primaryPreferred**
```javascript
db.collection.find().readPref("primaryPreferred")

// With tags
db.collection.find().readPref("primaryPreferred", [
  { datacenter: "east" },
  { datacenter: "west" }
])
```

**Behavior:**
1. Reads from primary when available
2. Falls back to secondary if primary unavailable
3. Ensures you read from primary during normal operations
4. Provides availability during failover

**Use When:**
- You want strong consistency by default
- Occasional stale reads during failover are acceptable
- Primary is available most of the time

#### **secondaryPreferred**
```javascript
db.collection.find().readPref("secondaryPreferred")

// With max staleness
db.collection.find().readPref("secondaryPreferred", null, {
  maxStalenessSeconds: 90
})
```

**Behavior:**
1. Reads from secondary when available
2. Falls back to primary if no secondary available
3. Distributes read load to secondaries
4. May return stale data

**Use When:**
- You want to reduce load on primary
- Stale reads are acceptable
- Running analytics or reporting queries
- Have multiple secondaries for load distribution

**Connection String Examples:**
```javascript
// primaryPreferred
mongodb://host1,host2,host3/?readPreference=primaryPreferred

// secondaryPreferred with tags
mongodb://host1,host2,host3/?readPreference=secondaryPreferred&readPreferenceTags=datacenter:east&readPreferenceTags=
```

**Code Examples:**
```javascript
// Node.js Driver
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred',
  readPreferenceTags: [{ region: 'us-east' }]
})

// Python Driver
client = MongoClient(
    uri,
    read_preference=ReadPreference.SECONDARY_PREFERRED,
    readPreferenceTags=[{'region': 'us-east'}]
)
```

---

### 128. How do you rebalance chunks in a sharded cluster?

**Automatic Balancing:**

MongoDB's balancer runs automatically and distributes chunks evenly across shards.

#### Check Balancer Status
```javascript
sh.getBalancerState()  // Returns true if enabled
sh.isBalancerRunning()  // Returns true if currently running
db.adminCommand({ balancerStatus: 1 })
```

#### Enable/Disable Balancer
```javascript
// Enable
sh.startBalancer()

// Disable
sh.stopBalancer()

// Disable temporarily during maintenance window
sh.stopBalancer()
// Perform maintenance
sh.startBalancer()
```

#### Schedule Balancer Window
```javascript
// Only run balancer during off-peak hours
db.settings.updateOne(
  { _id: "balancer" },
  {
    $set: {
      activeWindow: {
        start: "23:00",  // 11 PM
        stop: "06:00"    // 6 AM
      }
    }
  },
  { upsert: true }
)

// Remove window restriction
db.settings.updateOne(
  { _id: "balancer" },
  { $unset: { activeWindow: "" } }
)
```

#### Manual Chunk Operations

**Move Specific Chunk:**
```javascript
sh.moveChunk(
  "mydb.mycollection",
  { userId: 1000 },  // Chunk containing this value
  "shard0001"        // Destination shard
)
```

**Split Chunk:**
```javascript
sh.splitAt("mydb.mycollection", { userId: 5000 })

// Or split at middle
sh.splitFind("mydb.mycollection", { userId: 3000 })
```

#### Monitor Chunk Distribution
```javascript
// View chunk distribution
db.getSiblingDB("config").chunks.aggregate([
  { $group: { _id: "$shard", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])

// View specific collection chunks
sh.status()

// More detailed
use config
db.chunks.find({ ns: "mydb.mycollection" }).count()
```

#### Set Chunk Size
```javascript
// Default is 64MB, can be 1-1024 MB
use config
db.settings.updateOne(
  { _id: "chunksize" },
  { $set: { value: 128 } },  // 128 MB
  { upsert: true }
)
```

**Best Practices:**
- Monitor balancer during peak hours
- Use maintenance windows for large rebalancing
- Adjust chunk size based on data patterns
- Monitor migration impact on performance
- Keep chunks balanced to avoid hotspots

---

### 129. What is a chunk migration and how does it affect performance?

**Chunk Migration Process:**

A chunk migration moves data from one shard to another to maintain balanced distribution.

#### Migration Steps

1. **Start Migration**
   - Balancer identifies unbalanced shards
   - Initiates migration from donor to recipient shard

2. **Initial Clone**
   - Copy chunk data to recipient shard
   - Donor continues serving reads/writes

3. **Sync Changes**
   - Apply changes made during clone
   - Uses oplog to capture modifications

4. **Commit**
   - Update config servers with new chunk location
   - Route queries to new shard

5. **Delete Source**
   - Clean up data on donor shard
   - Range deleter runs in background

#### Performance Impact

**Network Impact:**
```javascript
// Monitor migration progress
db.currentOp({
  $or: [
    { op: "command", "command.moveChunk": { $exists: true } },
    { op: "command", "command._recvChunkStart": { $exists: true } }
  ]
})
```

**CPU and I/O:**
- Increased disk I/O on both shards
- Network bandwidth consumption
- Additional CPU for copying and syncing

**Write Performance:**
- Writes to migrating chunk tracked in session
- Slight latency increase during transfer
- Critical section blocks writes briefly (typically <1 second)

**Read Performance:**
- Reads continue normally during migration
- Some overhead from change tracking

#### Monitoring Migration
```javascript
// Check active migrations
db.currentOp().inprog.filter(op => 
  op.desc && op.desc.includes("migration")
)

// Migration stats
db.serverStatus().sharding

// Changelog
use config
db.changelog.find({ what: "moveChunk.start" }).sort({ time: -1 }).limit(10)
```

#### Tuning Migration Performance

**Throttle Migrations:**
```javascript
// Limit concurrent migrations (default: 1)
db.adminCommand({
  setParameter: 1,
  maxNumActiveTransferMods: 2
})

// Adjust migration chunk size
db.settings.updateOne(
  { _id: "chunksize" },
  { $set: { value: 32 } },  // Smaller chunks = faster migrations
  { upsert: true }
)
```

**Migration Window:**
```javascript
// Only allow migrations during off-peak
db.settings.updateOne(
  { _id: "balancer" },
  {
    $set: {
      activeWindow: { start: "01:00", stop: "05:00" }
    }
  },
  { upsert: true }
)
```

**Best Practices:**
- Schedule migrations during low traffic periods
- Monitor replication lag during migrations
- Use smaller chunk sizes for faster migrations
- Ensure adequate network bandwidth between shards
- Monitor disk space on recipient shard
- Test migrations in staging environment first

---

### 130. How do you handle shard key selection and what are the best practices?

**Shard Key Characteristics:**

Good shard keys have three properties: **Cardinality, Frequency, Rate of Change**

#### 1. **High Cardinality**
```javascript
// GOOD - High cardinality
{ userId: ObjectId("...") }  // Millions of unique values

// BAD - Low cardinality
{ status: "active" }  // Only 2-3 values
{ country: "US" }     // Limited values
```

#### 2. **Low Frequency**
```javascript
// GOOD - Even distribution
{ email: "user@example.com" }  // Unique per user

// BAD - Skewed distribution
{ category: "electronics" }  // 80% of docs in one category
```

#### 3. **Non-Monotonic (Avoid constantly increasing)
```javascript
// BAD - Monotonically increasing (hot shard)
{ _id: ObjectId("...") }  // Always writes to last chunk
{ timestamp: ISODate("...") }  // Always writes to newest chunk

// GOOD - Random distribution
{ userId: ObjectId("..."), timestamp: ISODate("...") }  // Compound key
{ hashedId: "hashed" }  // Hashed shard key
```

#### Shard Key Strategies

**1. Hashed Shard Key**
```javascript
// Even distribution but no range queries
db.collection.createIndex({ userId: "hashed" })
sh.shardCollection("mydb.users", { userId: "hashed" })

// Use when: Need even distribution, no range queries needed
```

**2. Ranged Shard Key**
```javascript
// Good for range queries but risk of hot spots
sh.shardCollection("mydb.orders", { customerId: 1, orderDate: 1 })

// Use when: Range queries important, can manage distribution
```

**3. Compound Shard Key**
```javascript
// Balance distribution and query patterns
sh.shardCollection("mydb.events", { 
  userId: 1,      // High cardinality
  timestamp: 1    // Time-based queries
})

// Use when: Multiple access patterns, need targeted routing
```

**4. Zoned Sharding (Tag-Aware)**
```javascript
// Pin data to specific shards by region/type
sh.addShardTag("shard0000", "US")
sh.addShardTag("shard0001", "EU")

sh.addTagRange(
  "mydb.users",
  { country: "US", userId: MinKey },
  { country: "US", userId: MaxKey },
  "US"
)

// Use when: Geographic requirements, compliance needs
```

#### Examples by Use Case

**Time-Series Data (IoT, Logs):**
```javascript
// Compound key: device + time
sh.shardCollection("iot.readings", {
  deviceId: 1,
  timestamp: 1
})

// Or hashed device with time
sh.shardCollection("iot.readings", {
  deviceId: "hashed",
  timestamp: 1
})
```

**E-commerce:**
```javascript
// Orders: customer + order ID
sh.shardCollection("shop.orders", {
  customerId: 1,
  _id: 1
})

// Products: hashed product ID
sh.shardCollection("shop.products", {
  _id: "hashed"
})
```

**Social Network:**
```javascript
// User posts: hashed user + timestamp
sh.shardCollection("social.posts", {
  userId: "hashed",
  createdAt: 1
})

// Messages: conversation + timestamp
sh.shardCollection("social.messages", {
  conversationId: 1,
  timestamp: 1
})
```

**Multi-Tenant SaaS:**
```javascript
// Tenant isolation
sh.shardCollection("app.data", {
  tenantId: 1,
  _id: 1
})

// With zones for premium tenants
sh.addShardTag("shard0000", "premium")
sh.addTagRange(
  "app.data",
  { tenantId: "premium_tenant_1", _id: MinKey },
  { tenantId: "premium_tenant_1", _id: MaxKey },
  "premium"
)
```

#### Evaluation Checklist

**Before choosing shard key:**
- ✅ Cardinality: Does it have enough unique values?
- ✅ Frequency: Are values evenly distributed?
- ✅ Monotonicity: Avoid always-increasing keys
- ✅ Query patterns: Does it align with common queries?
- ✅ Write patterns: Distributes writes evenly?
- ✅ Read patterns: Enables targeted reads?
- ✅ Future growth: Scales with data volume?

**Testing:**
```javascript
// Check existing distribution
db.collection.aggregate([
  { $group: { _id: "$proposedShardKey", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 10 }
])

// Analyze query patterns
db.setProfilingLevel(2)
// Run typical queries
db.system.profile.find({ ns: "mydb.collection" })
```

**Migration Considerations:**
- Cannot change shard key after sharding (before MongoDB 5.0)
- From 5.0+, can refine shard key by adding suffix fields
- Plan carefully - migration is expensive

---

## Backup, Restore & Monitoring

### 131. What's the difference between mongodump and oplog-based backups?

#### **mongodump**

**Logical Backup Tool:**
```bash
# Basic dump
mongodump --uri="mongodb://localhost:27017" --out=/backup

# Specific database
mongodump --db=myapp --out=/backup

# Specific collection
mongodump --db=myapp --collection=users --out=/backup

# With compression
mongodump --gzip --archive=/backup/myapp.gz

# Exclude collections
mongodump --db=myapp --excludeCollection=logs --out=/backup
```

**Characteristics:**
- Reads data using regular queries
- Creates BSON files for each collection
- Includes indexes
- Can backup specific databases/collections
- No point-in-time recovery
- Causes read load on database
- Slower for large datasets

**Pros:**
- Portable across MongoDB versions
- Human-readable format (with bsondump)
- Selective backup/restore
- Works on any MongoDB deployment

**Cons:**
- Not suitable for point-in-time recovery
- Impacts production performance
- Longer restore time for large datasets
- No transactional consistency across collections

#### **Oplog-Based Backups**

**Continuous Backup:**
```javascript
// Manual oplog backup
mongodump --oplog --out=/backup/base
mongodump --uri="mongodb://localhost:27017/local" --collection=oplog.rs --out=/backup/oplog
```

**Characteristics:**
- Captures base snapshot + oplog changes
- Enables point-in-time recovery (PITR)
- Continuous incremental backups
- Transactionally consistent
- Lower impact on production

**Implementation with MongoDB Ops Manager/Atlas:**
```javascript
// Atlas Continuous Backup
// - Automatic snapshots every 6-24 hours
// - Oplog stored for point-in-time recovery
// - Restore to any point within retention window
```

**Pros:**
- Point-in-time recovery to any second
- Minimal performance impact
- Transactional consistency
- Automated in Atlas/Ops Manager

**Cons:**
- Requires replica set
- More complex setup
- Larger storage requirements
- Requires continuous oplog retention

#### Comparison Table

| Feature | mongodump | Oplog-Based |
|---------|-----------|-------------|
| **Backup Type** | Logical snapshot | Continuous |
| **PITR** | ❌ No | ✅ Yes |
| **Performance Impact** | Medium-High | Low |
| **Storage** | Moderate | Higher |
| **Complexity** | Simple | Complex |
| **Selective Backup** | ✅ Yes | ❌ No |
| **Transactional** | ❌ No | ✅ Yes |
| **Version Portability** | ✅ Yes | Limited |

#### Hybrid Approach
```bash
# Daily mongodump for disaster recovery
mongodump --oplog --gzip --archive=/backup/daily/$(date +%Y%m%d).gz

# Continuous oplog backup for PITR
# Use MongoDB Ops Manager or Cloud Manager

# Or manual oplog tailing
mongodump --host=primary:27017 \
  --db=local --collection=oplog.rs \
  --query='{"ts":{"$gte":Timestamp(1699900800, 1)}}' \
  --out=/backup/oplog/$(date +%Y%m%d_%H%M)
```

---

### 132. How do you restore a specific collection from a dump?

**Using mongorestore:**

#### Basic Collection Restore
```bash
# Restore single collection
mongorestore --db=myapp --collection=users /backup/myapp/users.bson

# With URI
mongorestore --uri="mongodb://localhost:27017" \
  --db=myapp \
  --collection=users \
  /backup/myapp/users.bson
```

#### Restore with Options
```bash
# Drop existing collection first
mongorestore --drop --db=myapp --collection=users /backup/myapp/users.bson

# Restore to different collection name
mongorestore --db=myapp \
  --collection=users_backup \
  /backup/myapp/users.bson

# Restore to different database
mongorestore --db=myapp_new \
  --collection=users \
  /backup/myapp/users.bson

# From gzip archive
mongorestore --gzip \
  --db=myapp \
  --collection=users \
  /backup/myapp/users.bson.gz
```

#### Restore from Archive
```bash
# Extract specific collection from archive
mongorestore --gzip \
  --archive=/backup/myapp.gz \
  --nsInclude="myapp.users"

# Multiple collections
mongorestore --archive=/backup/full.gz \
  --nsInclude="myapp.users" \
  --nsInclude="myapp.orders"
```

#### Selective Restore with Filter
```bash
# Not directly supported, but workaround:

# 1. Export to JSON
bsondump /backup/myapp/users.bson > users.json

# 2. Filter with jq or similar
cat users.json | jq 'select(.status == "active")' > filtered.json

# 3. Import filtered data
mongoimport --db=myapp --collection=users_filtered filtered.json
```

#### Restore Indexes
```bash
# Indexes are restored automatically with --restoreIndexes (default)
mongorestore --db=myapp --collection=users /backup/myapp/users.bson

# Skip index restoration
mongorestore --noIndexRestore --db=myapp --collection=users /backup/myapp/users.bson

# Restore indexes separately
mongorestore --db=myapp /backup/myapp/users.metadata.json
```

#### Production Restore Strategy

**Zero-Downtime Restore:**
```bash
# 1. Restore to temporary collection
mongorestore --db=myapp --collection=users_temp /backup/myapp/users.bson

# 2. Verify data
mongosh --eval 'db.users_temp.countDocuments()'

# 3. Atomic rename (requires some downtime)
mongosh --eval '
  db.users.renameCollection("users_old");
  db.users_temp.renameCollection("users");
'

# 4. Cleanup
mongosh --eval 'db.users_old.drop()'
```

**Parallel Restore:**
```bash
# Faster restore with multiple jobs
mongorestore --numParallelCollections=4 \
  --db=myapp \
  --collection=users \
  /backup/myapp/users.bson
```

#### Restore to Replica Set
```bash
# Connect to primary
mongorestore --host=replicaset/primary:27017,secondary1:27017,secondary2:27017 \
  --db=myapp \
  --collection=users \
  /backup/myapp/users.bson

# With authentication
mongorestore --uri="mongodb://user:pass@primary:27017,secondary:27017/?replicaSet=rs0" \
  --db=myapp \
  --collection=users \
  /backup/myapp/users.bson
```

#### Monitoring Restore Progress
```bash
# Verbose output
mongorestore --verbose --db=myapp --collection=users /backup/myapp/users.bson

# In another terminal, monitor
mongosh --eval 'db.currentOp({"command.restoreIndex": {$exists: true}})'
mongosh --eval 'db.serverStatus().metrics.commands.insert'
```

---

### 133. How do you monitor replication lag?

**Replication Lag** = time delay between primary writes and secondary replication

#### Check Lag via Replica Set Status

```javascript
// Connect to any replica set member
rs.status()

// Look for 'optimeDate' difference
rs.status().members.forEach(member => {
  print(member.name + " - " + member.optimeDate)
})

// Calculate lag
var primary = rs.status().members.find(m => m.stateStr === "PRIMARY")
var secondaries = rs.status().members.filter(m => m.stateStr === "SECONDARY")

secondaries.forEach(sec => {
  var lagMs = primary.optimeDate - sec.optimeDate
  print(sec.name + " lag: " + lagMs + "ms")
})
```

#### Simpler Lag Check
```javascript
// Get replication info
rs.printReplicationInfo()  // Shows oplog details

rs.printSecondaryReplicationInfo()  // Shows lag for each secondary
// Output:
// source: secondary1:27017
//   syncedTo: Thu Nov 12 2025 10:30:45 GMT+0000 (UTC)
//   3 secs (0 hrs) behind the primary
```

#### Programmatic Monitoring

**Using `replSetGetStatus`:**
```javascript
var status = db.adminCommand({ replSetGetStatus: 1 })

status.members.forEach(member => {
  if (member.state === 2) {  // SECONDARY
    var lag = (status.date - member.optimeDate) / 1000  // Convert to seconds
    print(member.name + ": " + lag + " seconds behind")
  }
})
```

**Node.js Example:**
```javascript
const { MongoClient } = require('mongodb')

async function checkReplicationLag() {
  const client = await MongoClient.connect('mongodb://replica-set-uri')
  const admin = client.db().admin()
  
  const status = await admin.command({ replSetGetStatus: 1 })
  const primary = status.members.find(m => m.state === 1)
  
  status.members.forEach(member => {
    if (member.state === 2) {
      const lagMs = primary.optimeDate - member.optimeDate
      console.log(`${member.name}: ${lagMs}ms lag`)
      
      if (lagMs > 10000) {  // Alert if > 10 seconds
        console.error(`HIGH LAG ALERT: ${member.name}`)
      }
    }
  })
  
  client.close()
}

setInterval(checkReplicationLag, 60000)  // Check every minute
```

#### Monitoring with MongoDB Tools

**mongostat:**
```bash
# Show replication lag
mongostat --host=secondary:27017 --discover

# Output includes:
# - repllag: replication lag in seconds
```

**Ops Manager / Cloud Manager:**
- Visual graphs for replication lag
- Automatic alerts when lag exceeds threshold
- Historical lag data

**Atlas Metrics:**
- Replication Lag chart in Metrics tab
- Configurable alerts

#### Set Up Alerts

**MongoDB Alert Example:**
```javascript
// In Atlas or Ops Manager, configure alert:
// Metric: Replication Lag
// Threshold: > 10 seconds
// Notification: Email/Slack/PagerDuty
```

**Custom Monitoring Script:**
```python
from pymongo import MongoClient
import time

def check_lag():
    client = MongoClient('mongodb://replica-set-uri')
    status = client.admin.command('replSetGetStatus')
    
    primary = next(m for m in status['members'] if m['state'] == 1)
    primary_time = primary['optimeDate']
    
    for member in status['members']:
        if member['state'] == 2:  # Secondary
            lag = (primary_time - member['optimeDate']).total_seconds()
            
            if lag > 10:
                send_alert(f"Replication lag on {member['name']}: {lag}s")
    
    client.close()

while True:
    check_lag()
    time.sleep(60)
```

#### Common Causes of Replication Lag

1. **Network Issues** - Check connectivity between nodes
2. **High Write Load** - Scale or optimize writes
3. **Secondary Hardware** - Underpowered secondary
4. **Large Transactions** - Break into smaller operations
5. **Index Builds** - Background index builds on secondaries
6. **Long-Running Operations** - Blocking operations on secondary

**Troubleshooting Steps:**
```javascript
// Check oplog size
db.getReplicationInfo()

// Check current operations on secondary
db.currentOp(true)

// Check network stats
db.serverStatus().network

// Monitor secondary application of oplog
db.serverStatus().metrics.repl
```

---

### 134. What metrics do you track for MongoDB health?

#### **Core Performance Metrics**

**1. Operations Per Second (IOPS)**
```javascript
db.serverStatus().opcounters
// {
//   insert: 1000000,
//   query: 5000000,
//   update: 500000,
//   delete: 100000,
//   getmore: 200000,
//   command: 3000000
// }

// Calculate ops/sec by sampling over time
```

**2. Connection Pool**
```javascript
db.serverStatus().connections
// {
//   current: 250,      // Current connections
//   available: 51688,  // Available connections
//   totalCreated: 5000 // Lifetime connections created
// }

// Alert if current approaches available
```

**3. Memory Usage**
```javascript
db.serverStatus().mem
// {
//   resident: 2048,  // MB in RAM
//   virtual: 4096,   // MB virtual
//   mapped: 0        // Memory-mapped (deprecated)
// }

db.serverStatus().wiredTiger.cache
// {
//   "bytes currently in cache": 1073741824,
//   "maximum bytes configured": 2147483648,
//   "percentage full": 50
// }
```

**4. Disk I/O and Storage**
```javascript
db.serverStatus().wiredTiger.cache['pages read into cache']
db.serverStatus().wiredTiger.cache['pages written from cache']

// Collection statistics
db.collection.stats()
// {
//   size: 1000000,           // Total size in bytes
//   storageSize: 500000,     // Allocated storage
//   totalIndexSize: 200000,  // Index size
//   indexSizes: {...}
// }
```

**5. Query Performance**
```javascript
// Enable profiling
db.setProfilingLevel(1, { slowms: 100 })

// Query slow operations
db.system.profile.find({ millis: { $gt: 100 } }).sort({ ts: -1 })

// Average query time
db.system.profile.aggregate([
  { $group: { _id: "$ns", avgMs: { $avg: "$millis" }, count: { $sum: 1 } } },
  { $sort: { avgMs: -1 } }
])
```

**6. Replication Metrics**
```javascript
rs.status()
// Monitor:
// - Replication lag (optimeDate difference)
// - Member health (state)
// - Heartbeat status

db.serverStatus().repl
// {
//   hosts: [...],
//   setName: "rs0",
//   primary: "host1:27017"
// }
```

**7. Lock Statistics**
```javascript
db.serverStatus().locks
// Shows lock contention by lock type

db.serverStatus().globalLock
// {
//   totalTime: 1000000,
//   currentQueue: { total: 0, readers: 0, writers: 0 },
//   activeClients: { total: 50, readers: 40, writers: 10 }
// }
```

#### **Essential Metrics Dashboard**

**CPU & System:**
- CPU utilization (target: <80%)
- System load average
- Disk I/O wait time
- Network throughput

**MongoDB Specific:**
- Page faults per second
- Cache hit ratio (target: >95%)
- Queue depth (readers/writers)
- Ticket availability (WiredTiger)

**Application Level:**
- Average query latency
- P95/P99 query latency
- Query error rate
- Connection pool exhaustion

**Replication (if applicable):**
- Replication lag (target: <10s)
- Oplog window (target: >24 hours)
- Secondary read preference load

**Sharding (if applicable):**
- Chunk distribution balance
- Migration activity
- Jumbo chunks count

#### **Monitoring Script Example**
```javascript
// Comprehensive health check
function mongoHealthCheck() {
  const status = db.serverStatus()
  const replStatus = rs.status()
  
  return {
    connections: {
      current: status.connections.current,
      available: status.connections.available,
      utilization: (status.connections.current / status.connections.available * 100).toFixed(2) + "%"
    },
    memory: {
      residentMB: status.mem.resident,
      cacheUsage: ((status.wiredTiger.cache["bytes currently in cache"] / 
                    status.wiredTiger.cache["maximum bytes configured"]) * 100).toFixed(2) + "%"
    },
    operations: {
      insertsPerSec: status.opcounters.insert,
      queriesPerSec: status.opcounters.query,
      updatesPerSec: status.opcounters.update
    },
    replication: replStatus.members.map(m => ({
      name: m.name,
      state: m.stateStr,
      health: m.health,
      lag: m.optimeDate ? (Date.now() - m.optimeDate) / 1000 : null
    })),
    locks: {
      queuedReaders: status.globalLock.currentQueue.readers,
      queuedWriters: status.globalLock.currentQueue.writers
    }
  }
}

printjson(mongoHealthCheck())
```

#### **Alert Thresholds (Recommended)**

```yaml
Critical:
  - Replication lag > 60 seconds
  - Connection usage > 90%
  - Cache usage > 95%
  - Disk usage > 85%
  - Primary unavailable

Warning:
  - Replication lag > 10 seconds
  - Connection usage > 75%
  - Cache usage > 80%
  - Slow queries > 1000ms (P95)
  - Queue depth > 100
```

---

### 135. How do you integrate MongoDB with Prometheus / Grafana for monitoring?

#### **Architecture Overview**

```
MongoDB → MongoDB Exporter → Prometheus → Grafana
```

#### **Step 1: Install MongoDB Exporter**

**Docker:**
```bash
docker run -d \
  --name mongodb-exporter \
  -p 9216:9216 \
  percona/mongodb_exporter:0.40 \
  --mongodb.uri=mongodb://monitoring_user:password@mongodb:27017
```

**Binary Installation:**
```bash
# Download
wget https://github.com/percona/mongodb_exporter/releases/download/v0.40.0/mongodb_exporter-0.40.0.linux-amd64.tar.gz
tar xvzf mongodb_exporter-0.40.0.linux-amd64.tar.gz

# Run
./mongodb_exporter --mongodb.uri="mongodb://localhost:27017" \
  --web.listen-address=":9216"
```

**Create Monitoring User:**
```javascript
// In MongoDB
use admin
db.createUser({
  user: "mongodb_exporter",
  pwd: "secure_password",
  roles: [
    { role: "clusterMonitor", db: "admin" },
    { role: "read", db: "local" }
  ]
})
```

#### **Step 2: Configure Prometheus**

**prometheus.yml:**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'mongodb'
    static_configs:
      - targets: ['localhost:9216']
        labels:
          environment: 'production'
          cluster: 'main'
    
    # For multiple MongoDB instances
  - job_name: 'mongodb-replica-set'
    static_configs:
      - targets:
        - 'mongodb-primary:9216'
        - 'mongodb-secondary-1:9216'
        - 'mongodb-secondary-2:9216'
        labels:
          replica_set: 'rs0'

  # Service discovery (Kubernetes)
  - job_name: 'mongodb-k8s'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        regex: mongodb-exporter
        action: keep
```

**Start Prometheus:**
```bash
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

#### **Step 3: Set Up Grafana**

**Install Grafana:**
```bash
docker run -d \
  --name grafana \
  -p 3000:3000 \
  -e "GF_SECURITY_ADMIN_PASSWORD=admin" \
  grafana/grafana
```

**Add Prometheus Data Source:**
1. Login to Grafana (http://localhost:3000)
2. Configuration → Data Sources → Add data source
3. Select Prometheus
4. URL: http://prometheus:9090
5. Save & Test

**Import MongoDB Dashboard:**
1. Dashboards → Import
2. Use dashboard ID: **2583** (MongoDB Exporter Dashboard)
3. Or **7353** (Percona MongoDB Dashboard)
4. Select Prometheus data source
5. Import

#### **Step 4: Key Prometheus Queries**

**Operations Per Second:**
```promql
# Total operations
rate(mongodb_opcounters_total[5m])

# By operation type
rate(mongodb_opcounters_insert_total[5m])
rate(mongodb_opcounters_query_total[5m])
rate(mongodb_opcounters_update_total[5m])
```

**Memory Usage:**
```promql
# Resident memory
mongodb_memory_resident_bytes

# Cache usage percentage
(mongodb_wiredTiger_cache_bytes / mongodb_wiredTiger_cache_maximum_bytes) * 100
```

**Connections:**
```promql
# Current connections
mongodb_connections{state="current"}

# Available connections
mongodb_connections{state="available"}

# Connection usage percentage
(mongodb_connections{state="current"} / mongodb_connections{state="available"}) * 100
```

**Replication Lag:**
```promql
# Lag in seconds
mongodb_replset_member_replication_lag_seconds

# Alert on high lag
mongodb_replset_member_replication_lag_seconds > 10
```

**Query Performance:**
```promql
# Average query time
rate(mongodb_mongod_metrics_query_executor_total[5m])

# Slow queries
increase(mongodb_mongod_slow_queries_total[5m])
```

**Lock Contention:**
```promql
# Queued operations
mongodb_mongod_global_lock_current_queue_readers
mongodb_mongod_global_lock_current_queue_writers

# Active clients
mongodb_mongod_global_lock_active_clients_readers
mongodb_mongod_global_lock_active_clients_writers
```

#### **Step 5: Create Custom Grafana Dashboard**

**Example Panel Queries:**

```json
{
  "panels": [
    {
      "title": "Operations Per Second",
      "targets": [
        {
          "expr": "sum(rate(mongodb_opcounters_total[5m])) by (type)",
          "legendFormat": "{{type}}"
        }
      ]
    },
    {
      "title": "Replication Lag",
      "targets": [
        {
          "expr": "mongodb_replset_member_replication_lag_seconds",
          "legendFormat": "{{member}}"
        }
      ],
      "alert": {
        "conditions": [
          {
            "evaluator": { "params": [10], "type": "gt" },
            "query": { "params": ["A", "5m", "now"] }
          }
        ]
      }
    },
    {
      "title": "Connection Pool Usage",
      "targets": [
        {
          "expr": "(mongodb_connections{state='current'} / mongodb_connections{state='available'}) * 100",
          "legendFormat": "Usage %"
        }
      ]
    }
  ]
}
```

#### **Step 6: Configure Alerts**

**Prometheus Alert Rules (alerts.yml):**
```yaml
groups:
  - name: mongodb_alerts
    interval: 30s
    rules:
      - alert: MongoDBDown
        expr: up{job="mongodb"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "MongoDB instance down"
          description: "MongoDB instance {{ $labels.instance }} is down"
      
      - alert: MongoDBReplicationLag
        expr: mongodb_replset_member_replication_lag_seconds > 10
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "High replication lag"
          description: "Replication lag on {{ $labels.member }} is {{ $value }}s"
      
      - alert: MongoDBConnectionsHigh
        expr: (mongodb_connections{state="current"} / mongodb_connections{state="available"}) > 0.8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Connection pool usage high"
          description: "Connection usage is {{ $value }}%"
      
      - alert: MongoDBCursorTimeout
        expr: increase(mongodb_mongod_metrics_cursor_timed_out_total[5m]) > 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "High cursor timeout rate"
      
      - alert: MongoDBSlowQueries
        expr: increase(mongodb_mongod_slow_queries_total[5m]) > 100
        for: 5m
        labels:
          severity: info
        annotations:
          summary: "High slow query rate"
```

**Grafana Alerting:**
1. Edit panel → Alert tab
2. Create alert rule
3. Configure notification channels (Slack, PagerDuty, Email)

#### **Step 7: Production Best Practices**

**Security:**
```yaml
# Use TLS for MongoDB exporter
mongodb_exporter --mongodb.uri="mongodb://user:pass@host:27017/?ssl=true" \
  --web.listen-address=":9216"

# Enable authentication in Prometheus
basic_auth:
  username: admin
  password: secure_password
```

**High Availability:**
```yaml
# Monitor all replica set members
scrape_configs:
  - job_name: 'mongodb-rs'
    static_configs:
      - targets:
        - 'primary:9216'
        - 'secondary1:9216'
        - 'secondary2:9216'
```

**Retention:**
```yaml
# Prometheus storage retention
storage:
  tsdb:
    retention.time: 30d
    retention.size: 50GB
```

---

## Security & Compliance

### 136. What are MongoDB's authentication mechanisms (SCRAM, x.509, LDAP, Kerberos)?

MongoDB supports multiple authentication mechanisms for different use cases:

#### **1. SCRAM (Salted Challenge Response Authentication Mechanism)**

**Default mechanism** - username/password based

**SCRAM-SHA-256 (Recommended):**
```javascript
// Enable authentication in mongod.conf
security:
  authorization: enabled

// Create admin user
use admin
db.createUser({
  user: "admin",
  pwd: "securePassword123",
  roles: [ { role: "root", db: "admin" } ]
})

// Create application user
use myapp
db.createUser({
  user: "app_user",
  pwd: "appPassword456",
  roles: [
    { role: "readWrite", db: "myapp" },
    { role: "read", db: "analytics" }
  ]
})

// Connect with authentication
mongosh "mongodb://app_user:appPassword456@localhost:27017/myapp?authSource=myapp"
```

**SCRAM-SHA-1 (Legacy):**
```javascript
// Still supported but SHA-256 is preferred
db.createUser({
  user: "legacy_user",
  pwd: "password",
  roles: ["readWrite"],
  mechanisms: ["SCRAM-SHA-1"]  // Explicit mechanism
})
```

**Pros:**
- Simple to implement
- No external dependencies
- Built-in to MongoDB

**Cons:**
- Password management complexity
- No centralized authentication
- Manual user provisioning

---

#### **2. x.509 Certificate Authentication**

**Certificate-based authentication** - no passwords needed

**Setup:**

1. **Generate Certificates:**
```bash
# CA certificate
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt

# Server certificate
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt

# Client certificate
openssl genrsa -out client.key 4096
openssl req -new -key client.key -out client.csr
# CN must match username: CN=app_client,OU=MyOrg,O=MyCompany
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key -set_serial 02 -out client.crt

# Combine for MongoDB
cat client.crt client.key > client.pem
```

2. **Configure MongoDB:**
```yaml
# mongod.conf
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb/server.pem
    CAFile: /etc/ssl/mongodb/ca.crt

security:
  authorization: enabled
  clusterAuthMode: x509
```

3. **Create User:**
```javascript
db.getSiblingDB("$external").createUser({
  user: "CN=app_client,OU=MyOrg,O=MyCompany,L=NYC,ST=NY,C=US",
  roles: [
    { role: "readWrite", db: "myapp" }
  ]
})
```

4. **Connect:**
```bash
mongosh "mongodb://localhost:27017/myapp?authMechanism=MONGODB-X509&tls=true" \
  --tlsCertificateKeyFile /etc/ssl/client.pem \
  --tlsCAFile /etc/ssl/ca.crt
```

**Pros:**
- No password transmission
- Strong cryptographic authentication
- Certificate revocation possible
- Good for service-to-service auth

**Cons:**
- Complex certificate management
- Certificate rotation overhead
- Requires PKI infrastructure

---

#### **3. LDAP Authentication**

**Enterprise feature** - centralized user management

**Configuration:**
```yaml
# mongod.conf
security:
  authorization: enabled
  ldap:
    servers: "ldap.company.com"
    bind:
      method: "simple"
      queryUser: "cn=admin,dc=company,dc=com"
      queryPassword: "ldapPassword"
    userToDNMapping:
      '[
        {
          match: "(.+)",
          substitution: "uid={0},ou=users,dc=company,dc=com"
        }
      ]'
    authz:
      queryTemplate: "ou=groups,dc=company,dc=com??sub?(&(objectClass=groupOfNames)(member=uid={USER},ou=users,dc=company,dc=com))"

setParameter:
  authenticationMechanisms: PLAIN,SCRAM-SHA-256
```

**Map LDAP Groups to Roles:**
```javascript
db.getSiblingDB("admin").createRole({
  role: "CN=MongoDB Admins,OU=Groups,DC=company,DC=com",
  privileges: [],
  roles: [ "root" ]
})

db.getSiblingDB("admin").createRole({
  role: "CN=MongoDB Developers,OU=Groups,DC=company,DC=com",
  privileges: [],
  roles: [
    { role: "readWrite", db: "myapp" }
  ]
})
```

**Connect:**
```bash
mongosh "mongodb://jdoe:ldapPassword@localhost:27017/myapp?authMechanism=PLAIN&authSource=$external"
```

**Pros:**
- Centralized user management
- Single sign-on integration
- Automatic group-based authorization
- No duplicate user databases

**Cons:**
- Requires MongoDB Enterprise
- LDAP infrastructure dependency
- Network latency for auth
- Password sent in plaintext (use TLS!)

---

#### **4. Kerberos Authentication**

**Enterprise feature** - for Windows/Unix environments with Kerberos

**Setup:**

1. **Configure KDC and Create Service Principal:**
```bash
# On KDC server
kadmin.local
addprinc -randkey mongodb/mongodb-server.company.com@COMPANY.COM
ktadd -k /etc/mongodb.keytab mongodb/mongodb-server.company.com@COMPANY.COM
```

2. **Configure MongoDB:**
```yaml
# mongod.conf
security:
  authorization: enabled

setParameter:
  authenticationMechanisms: GSSAPI

# Set environment variable
export KRB5_KTNAME=/etc/mongodb.keytab
```

3. **Create User:**
```javascript
db.getSiblingDB("$external").createUser({
  user: "app_user@COMPANY.COM",
  roles: [
    { role: "readWrite", db: "myapp" }
  ]
})
```

4. **Client Setup:**
```bash
# Get Kerberos ticket
kinit app_user@COMPANY.COM

# Connect
mongosh "mongodb://app_user%40COMPANY.COM@mongodb-server.company.com/myapp?authMechanism=GSSAPI&authSource=$external"
```

**Pros:**
- Strong, ticket-based authentication
- No password transmission
- Integrated with Windows Active Directory
- Mutual authentication

**Cons:**
- Requires MongoDB Enterprise
- Complex Kerberos infrastructure
- Difficult to troubleshoot
- Clock synchronization critical

---

#### **Comparison Table**

| Mechanism | MongoDB Edition | Complexity | Use Case |
|-----------|----------------|------------|----------|
| **SCRAM-SHA-256** | Community | Low | General purpose, small deployments |
| **x.509** | Community | Medium | Service accounts, microservices |
| **LDAP** | Enterprise | Medium | Enterprise with existing LDAP |
| **Kerberos** | Enterprise | High | Windows/AD environments |

---
