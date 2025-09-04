# 📊 Database Indexes: Complete Guide

This document provides a comprehensive overview of database indexing concepts, types, and implementation strategies.

---

## 🔍 1. What are Database Indexes?

A **database index** is a data structure that improves the speed of data retrieval operations on a database table. Think of it like an index in a book - it provides a quick way to locate specific information without scanning every page.

### Key Benefits
- **Faster query performance** for SELECT operations
- **Efficient sorting** and filtering
- **Quick joins** between tables
- **Unique constraint enforcement**

### Trade-offs
- **Additional storage space** required
- **Slower INSERT/UPDATE/DELETE** operations
- **Maintenance overhead** during data modifications

---

## 🏗️ 2. Index Types

### 🔹 Primary Index

Built automatically on the **primary key** of a table.

**Characteristics:**
- **Unique and non-null** by definition
- **Dense index** (contains entry for every row)
- Can be **sparse** if data is physically sorted by primary key
- Directly identifies record location

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);
-- Primary index created automatically on emp_id
```

---

### 🔹 Secondary Index

Created on **non-primary key columns** to optimize specific queries.

**Characteristics:**
- **Always dense** (entry for every search key value)
- **Allows duplicate values**
- Points to primary key or row identifier
- Multiple secondary indexes per table allowed

```sql
-- Create secondary indexes for optimization
CREATE INDEX idx_department ON employees(department);
CREATE INDEX idx_name ON employees(name);
CREATE INDEX idx_composite ON employees(department, name);
```

---

### 🔹 Clustered Index

Determines the **physical storage order** of data on disk.

**Characteristics:**
- **Only one per table** (data can only be sorted one way physically)
- Often coincides with primary index
- **Excellent for range queries**
- **Slower for random access patterns**

```sql
CREATE CLUSTERED INDEX idx_order_date ON orders(order_date);
-- Data physically sorted by order_date
```

---

### 🔹 Non-Clustered Index

**Logical ordering** that doesn't affect physical data storage.

**Characteristics:**
- **Multiple allowed per table**
- Contains pointers to actual data rows
- **Faster for specific lookups**
- **Additional lookup step** required

---

## 📈 3. Index Density: Sparse vs Dense

### Dense Index
- **One index entry per record** in the data file
- **Direct access** to any record
- **Larger storage requirement**
- **Faster search operations**

### Sparse Index
- **One index entry per data block**
- **Requires data to be sorted** on the indexed column
- **Smaller storage footprint**
- **Additional block scanning** needed

| Aspect | Dense Index | Sparse Index |
|--------|-------------|--------------|
| Entry Count | One per record | One per block |
| Storage Size | Larger | Smaller |
| Search Speed | Faster | Slower |
| Data Requirement | Any order | Must be sorted |
| Primary Index | ✅ Possible | ✅ Possible |
| Secondary Index | ✅ Always | ❌ Never |
| Clustered Index | ✅ Always | ❌ Never |

---

## 🔄 4. Handling Duplicate Values

### Primary Index
- **No duplicates allowed** (enforces uniqueness)
- Each key maps to exactly one record

### Secondary Index with Duplicates
When duplicate values exist in a secondary index:

**Method 1: Pointer Lists**
```
Index Entry: "Manager" → [ptr1, ptr2, ptr3, ptr4]
```

**Method 2: Multiple Index Entries**
```
Index Entries:
"Manager" → ptr1
"Manager" → ptr2
"Manager" → ptr3
"Manager" → ptr4
```

### Clustered Index with Duplicates
- Records with same key value are **stored together physically**
- **Block pointer** points to first block containing the key
- **Block hangers** point to additional blocks with same key

---

## ⚡ 5. Index Structures

### B-Tree Index (Most Common)
- **Balanced tree structure**
- **Logarithmic search time** O(log n)
- **Efficient for range queries**
- **Good for equality and inequality searches**

### Hash Index
- **Constant time lookups** O(1) for equality
- **Not suitable for range queries**
- **Memory-based** typically
- **Perfect for exact match searches**

### Bitmap Index
- **Efficient for low-cardinality data**
- **Excellent for analytical queries**
- **Good for OR/AND operations**
- **High storage for high-cardinality data**

---

## 🎯 6. Index Selection Strategy

### When to Create Indexes

**Good Candidates:**
- Frequently queried columns in WHERE clauses
- Columns used in JOIN conditions
- Columns used in ORDER BY clauses
- Foreign key columns

**Poor Candidates:**
- Frequently updated columns
- Tables with high INSERT/DELETE activity
- Very small tables
- Columns with very few distinct values

### Composite Indexes
```sql
-- Order matters: department first, then name
CREATE INDEX idx_dept_name ON employees(department, name);

-- Efficient for:
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees WHERE department = 'IT' AND name = 'John';

-- Less efficient for:
SELECT * FROM employees WHERE name = 'John';
```

---

## 📊 7. Performance Characteristics

| Operation | Primary Index | Secondary Index | Clustered Index |
|-----------|---------------|-----------------|-----------------|
| Point Query | Excellent | Good | Good |
| Range Query | Good | Fair | Excellent |
| Insert | Fast | Slower | Variable |
| Update | Fast | Slower | Variable |
| Delete | Fast | Slower | Variable |
| Storage | Minimal | Moderate | Minimal |

---

## 🛠️ 8. Index Maintenance

### Automatic Maintenance
- Database automatically updates indexes during DML operations
- **Index fragmentation** can occur over time
- **Statistics** are updated for query optimization

### Manual Maintenance
```sql
-- Rebuild fragmented index
ALTER INDEX idx_department REBUILD;

-- Update statistics
UPDATE STATISTICS employees;

-- Check index usage
SELECT * FROM sys.dm_db_index_usage_stats;
```

---

## 🎓 9. Best Practices

### Design Guidelines
1. **Start with primary key** - automatic primary index
2. **Identify frequent queries** - create secondary indexes accordingly
3. **Consider composite indexes** for multi-column searches
4. **Monitor index usage** - remove unused indexes
5. **Balance read vs write performance**

### Common Patterns
- **Covering indexes** - include all columns needed for a query
- **Partial indexes** - index only subset of rows meeting conditions
- **Expression indexes** - index computed values or functions

### Monitoring
- Track query execution plans
- Monitor index fragmentation levels
- Analyze index usage statistics
- Review slow query logs

---

## 📝 10. Key Terminology

| Term | Definition |
|------|------------|
| **Dense Index** | Contains entry for every record in the data file |
| **Sparse Index** | Contains entry for every data block, not every record |
| **Block Pointer** | First pointer to a data block containing the search key |
| **Block Hanger** | Additional pointers to blocks containing same search key |
| **Selectivity** | Ratio of distinct values to total rows |
| **Cardinality** | Number of distinct values in a column |
| **Index Fragmentation** | Scattered index pages that reduce performance |
| **Covering Index** | Index containing all columns needed for a query |

---

## 🎯 11. Quick Reference

### Index Type Decision Matrix

| Scenario | Recommended Index Type |
|----------|----------------------|
| Primary key column | Primary Index (automatic) |
| Frequent WHERE conditions | Secondary Index |
| Range queries (dates, numbers) | Clustered Index |
| JOIN conditions | Secondary Index on both tables |
| ORDER BY operations | Clustered or Secondary Index |
| Unique constraints | Unique Secondary Index |

### Performance Tips
- **Limit indexes per table** (5-10 maximum for OLTP systems)
- **Drop unused indexes** to improve write performance
- **Use partial indexes** for large tables with skewed data
- **Consider index-only scans** with covering indexes
- **Regular maintenance** prevents performance degradation