### MongoDB Interview Questions and Answers (3 Years Experience)

---

#### 1. **What is MongoDB? What are its key features?**

**Answer**: MongoDB is a NoSQL, document-oriented database. It stores data in BSON format (Binary JSON) and provides features like schema-less design, horizontal scaling, high performance, replication, and sharding.

---

#### 2. **Compare MongoDB with relational databases like MySQL.**

**Answer**:

* MongoDB is schema-less, while MySQL uses a strict schema.
* MongoDB stores data as documents, MySQL stores data as rows in tables.
* MongoDB is horizontally scalable, MySQL is typically vertically scalable.
* MongoDB is more suitable for hierarchical and unstructured data.

---

#### 3. **What is a document and a collection in MongoDB?**

**Answer**: A document is a record in MongoDB, stored in BSON format. A collection is a group of related documents, equivalent to a table in relational databases.

---

#### 4. **What are the data types supported by MongoDB?**

**Answer**: String, Integer, Boolean, Double, Min/Max keys, Arrays, Timestamp, Object, Null, Symbol, Date, Binary Data, ObjectId, Regular Expression, JavaScript.

---

#### 5. **What is the difference between `findOne()` and `find()`?**

**Answer**:

* `findOne()` returns a single document.
* `find()` returns a cursor to all matching documents.

---

#### 6. **How is MongoDB schema-less?**

**Answer**: Collections in MongoDB do not enforce document structure, so each document can have a different set of fields.

---

#### 7. **What is BSON? How is it different from JSON?**

**Answer**: BSON (Binary JSON) extends JSON with additional data types (e.g., Date, ObjectId) and is stored in a binary format to improve efficiency.

---

#### 8. **How do you insert, update, and delete a document in MongoDB?**

**Answer**:

```javascript
// Insert
 db.collection.insertOne({ name: "John", age: 30 });

// Update
 db.collection.updateOne({ name: "John" }, { $set: { age: 31 } });

// Delete
 db.collection.deleteOne({ name: "John" });
```

---

#### 9. **Difference between `updateOne`, `updateMany`, `replaceOne`?**

**Answer**:

* `updateOne`: Updates the first matching document.
* `updateMany`: Updates all matching documents.
* `replaceOne`: Replaces the entire document.

---

#### 10. **How can you query documents with multiple conditions?**

**Answer**:

```javascript
 db.collection.find({ age: { $gt: 25 }, city: "Delhi" });
```

---

#### 11. **How do you perform a projection in MongoDB?**

**Answer**:

```javascript
 db.collection.find({}, { name: 1, age: 1 });
```

---

#### 12. **What is the aggregation framework?**

**Answer**: It's a powerful tool for data transformation and analysis. It processes documents through a pipeline of stages like `$match`, `$group`, `$project`, etc.

---

#### 13. **Common aggregation stages?**

**Answer**:

* `$match`: Filter documents.
* `$group`: Group by fields.
* `$project`: Shape the output.
* `$sort`: Sort results.
* `$lookup`: Perform joins.

---

#### 14. **How to perform join operation?**

**Answer**:

```javascript
 db.orders.aggregate([
   { $lookup: {
     from: "customers",
     localField: "cust_id",
     foreignField: "_id",
     as: "customer_info"
   }}
 ]);
```

---

#### 15. **Index types in MongoDB?**

**Answer**:

* Single field index
* Compound index
* Multikey index
* Geospatial index
* Text index
* Hashed index

---

#### 16. **How does indexing improve performance?**

**Answer**: Indexes allow MongoDB to efficiently query documents without scanning the entire collection, reducing time complexity.

---

#### 17. **What is a compound index?**

**Answer**: An index on multiple fields. For example: `{ name: 1, age: -1 }`. Useful for queries using both fields.

---

#### 18. **How to view indexes on a collection?**

**Answer**:

```javascript
 db.collection.getIndexes();
```

---

#### 19. **What is `explain()` used for?**

**Answer**: To analyze the execution plan of a query. It shows index usage, number of documents scanned, etc.

---

#### 20. **Effect of large indexes on writes?**

**Answer**: Large indexes can slow down write operations as indexes need to be updated with every insert/update.

---

#### 21. **Embedded vs Referenced Documents?**

**Answer**:

* Embedded: Store related data in the same document (better read performance).
* Referenced: Store in separate documents and link via ObjectId (better normalization, flexibility).

---

#### 22. **Modeling one-to-many relationships?**

**Answer**: Use embedded documents for small sub-documents or references if sub-documents grow large or are shared.

---

#### 23. **Schema design best practices?**

**Answer**:

* Embed when you read data together.
* Reference for large or independent data.
* Avoid deep nesting.
* Use indexes wisely.
* Pre-calculate if needed.

---

#### 24. **Does MongoDB support transactions?**

**Answer**: Yes, since version 4.0, MongoDB supports multi-document ACID transactions.

---

#### 25. **Write concern vs Read concern?**

**Answer**:

* Write concern: Level of acknowledgment requested during writes (e.g., `w: 1`, `w: majority`).
* Read concern: Guarantees level of consistency for reads (e.g., `local`, `majority`).

---

#### 26. **What is a replica set?**

**Answer**: A group of MongoDB servers (nodes) that maintain the same data set for redundancy and high availability.

---

#### 27. **Primary vs Secondary in replica set?**

**Answer**:

* Primary: Accepts write operations.
* Secondary: Replicates data from primary and handles reads if enabled.

---

#### 28. **Failover in replica set?**

**Answer**: If the primary node fails, the replica set automatically elects a new primary from secondaries.

---

#### 29. **What is sharding?**

**Answer**: Distributing data across multiple servers to handle large datasets and high throughput operations.

---

#### 30. **Components of a sharded cluster?**

**Answer**:

* Shard: A MongoDB server or replica set storing data.
* Mongos: Query router.
* Config server: Stores metadata and cluster config.

---

#### 31. **Handling time-series data in MongoDB?**

**Answer**: Use time-series collections (since MongoDB 5.0) or indexed `timestamp` fields with TTL or capped collections.

---

#### 32. **Diagnosing slow queries?**

**Answer**: Use `explain()`, check index usage, use `mongotop`, `mongostat`, and monitor logs.

---

#### 33. **How to migrate a large collection?**

**Answer**: Use `mongoexport`/`mongoimport`, `mongodump`/`mongorestore`, or a script with pagination/batch processing.

---

#### 34. **Backup and restore in MongoDB?**

**Answer**:

* Backup: `mongodump`
* Restore: `mongorestore`
* Atlas users can use automated backups.

---

#### 35. **Monitoring MongoDB?**

**Answer**: Tools like `mongostat`, `mongotop`, MongoDB Atlas, Ops Manager, or Prometheus + Grafana.

---

#### 36. **What is a TTL index?**

**Answer**: Automatically removes documents after a specified period. Useful for session data, logs.

---

#### 37. **What are capped collections?**

**Answer**: Fixed-size collections that maintain insertion order and automatically overwrite oldest documents when full.

---

#### 38. **How does MongoDB handle concurrency?**

**Answer**: MongoDB uses readers-writer locks at the database and collection level. WiredTiger supports document-level concurrency.

---

#### 39. **How to implement audit logging?**

**Answer**: Use change streams, application-level logging, or MongoDB Ops Manager.

---

#### 40. **ACID compliance in MongoDB?**

**Answer**: Since v4.0, MongoDB supports ACID transactions for replica sets; v4.2 extended this to sharded clusters.

---
# query
### MongoDB Interview Questions and Answers (3 Years Experience)

...\[Previous content remains unchanged]...

---

### MongoDB Query Examples (Easy / Medium / Hard)

#### 🟢 Easy Level

```javascript
// 1. Find all users in the 'users' collection
 db.users.find();

// 2. Find users with age greater than 25
 db.users.find({ age: { $gt: 25 } });

// 3. Find users from Delhi and project only name and city
 db.users.find({ city: "Delhi" }, { name: 1, city: 1 });

// 4. Insert a document
 db.users.insertOne({ name: "Avadhesh", age: 28, city: "Lucknow" });
```

---

#### 🟡 Medium Level

```javascript
// 5. Find users with age > 25 and city = 'Delhi', sorted by age
 db.users.find({ age: { $gt: 25 }, city: "Delhi" }).sort({ age: -1 });

// 6. Count documents in the collection
 db.users.countDocuments();

// 7. Group users by city and count them
 db.users.aggregate([
   { $group: { _id: "$city", count: { $sum: 1 } } }
 ]);

// 8. Update multiple users
 db.users.updateMany({ city: "Delhi" }, { $set: { verified: true } });
```

---

#### 🔴 Hard Level

```javascript
// 9. Use $lookup to join 'orders' with 'users'
 db.orders.aggregate([
   { $lookup: {
     from: "users",
     localField: "user_id",
     foreignField: "_id",
     as: "user_details"
   }},
   { $unwind: "$user_details" },
   { $project: { order_id: 1, amount: 1, user_name: "$user_details.name" } }
 ]);

// 10. Use $facet for multiple aggregations in a single query
 db.products.aggregate([
   {
     $facet: {
       "TopCategories": [
         { $group: { _id: "$category", total: { $sum: 1 } } },
         { $sort: { total: -1 } }
       ],
       "AvgPrice": [
         { $group: { _id: null, avgPrice: { $avg: "$price" } } }
       ]
     }
   }
 ]);

// 11. Full-text search on 'description'
 db.articles.createIndex({ description: "text" });
 db.articles.find({ $text: { $search: "\"mongodb indexing\"" } });

// 12. Find documents with nested field condition
 db.orders.find({ "shipping.address.city": "Delhi" });
```

---

### MongoDB Cheat Sheet (Commands & Operators)

#### 🔍 Basic Operations

```javascript
show dbs                          // Show all databases
db                                // Show current database
use acme                          // Create or switch to DB
db.dropDatabase()                 // Drop current DB
show collections                  // Show collections in DB
db.createCollection('posts')     // Create collection
```

#### 📥 Insert Documents

```javascript
// Insert One
 db.posts.insert({...});

// Insert Many
 db.posts.insertMany([...]);
```

#### 🔎 Find Documents

```javascript
db.posts.find()                        // All documents
db.posts.find().pretty()              // Formatted

// Conditional
 db.posts.find({ category: 'News' });

// Sort
 db.posts.find().sort({ title: 1 });   // Ascending
 db.posts.find().sort({ title: -1 });  // Descending

// Count
 db.posts.find().count();
 db.posts.find({ category: 'News' }).count();

// Limit
 db.posts.find().limit(2);

// Chaining
 db.posts.find().limit(2).sort({ title: 1 });

// Find One
 db.posts.findOne({ category: 'News' });

// Find Specific Fields
 db.posts.find({ title: 'Post One' }, { title: 1, author: 1 });
```

#### 🔄 Update Documents

```javascript
// Update with upsert
 db.posts.update({ title: 'Post Two' }, { title: 'Post Two', body: '...', date: Date() }, { upsert: true });

// Update specific field
 db.posts.update({ title: 'Post Two' }, { $set: { body: '...', category: 'Technology' } });

// Increment field
 db.posts.update({ title: 'Post Two' }, { $inc: { likes: 5 } });

// Rename field
 db.posts.update({ title: 'Post Two' }, { $rename: { likes: 'views' } });

// Sub-document
 db.posts.update({ title: 'Post One' }, {
   $set: {
     comments: [
       { body: 'Comment One', user: 'Mary Williams', date: Date() },
       { body: 'Comment Two', user: 'Harry White', date: Date() }
     ]
   }
 });

// UpdateOne with $set, $unset
 db.posts.updateOne({ title: "Post One" }, { $set: { body: "Updated..." }, $unset: { category: "" } });

// UpdateMany
 db.posts.updateMany({ category: "News" }, { $set: { category: "Updated News" } });
```

#### ❌ Delete Documents

```javascript
// Remove
 db.posts.remove({ title: 'Post Four' });

// DeleteOne
 db.posts.deleteOne({ title: 'Post Four' });

// DeleteMany
 db.posts.deleteMany({ category: 'Entertainment' });
```

#### 📚 Array and Element Operators

```javascript
// Match element in array
 db.posts.find({ comments: { $elemMatch: { user: 'Mary Williams' } } });
```

#### 🧠 Indexes & Search

```javascript
// Add text index
 db.posts.createIndex({ title: 'text' });

// Text search
 db.posts.find({ $text: { $search: '"Post O"' } });

// View indexes
 db.posts.getIndexes();

// Drop index
 db.posts.dropIndex({ title: 1 });
```

#### 🔢 Comparison Operators

```javascript
// Not equal
 db.posts.find({ category: { $ne: "News" } });

// In / Not In
 db.posts.find({ category: { $in: ["News", "Technology"] } });
 db.posts.find({ category: { $nin: ["News", "Technology"] } });

// Greater/Less
 db.posts.find({ views: { $gt: 2 } });
 db.posts.find({ views: { $gte: 7 } });
 db.posts.find({ views: { $lt: 7 } });
 db.posts.find({ views: { $lte: 7 } });
```

#### 🔗 Logical Operators

```javascript
// AND
 db.posts.find({ $and: [ { category: "News" }, { "user.name": "John Doe" } ] });

// OR
 db.posts.find({ $or: [ { category: "News" }, { category: "Technology" } ] });

// NOR
 db.posts.find({ $nor: [ { category: "News" }, { category: "Technology" } ] });

// NOT
 db.posts.find({ $and: [ { views: { $not: { $lte: 100 } } }, { title: { $not: /^Post/ } } ] });
```

---
