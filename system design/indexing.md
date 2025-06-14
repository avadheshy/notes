# 📊 Database Indexes: Primary, Secondary, Clustered — with Sparse/Dense Indexing and Duplicates Handling

This document covers:

- Different types of indexes: **Primary**, **Secondary**, and **Clustered**
- How **search** is performed
- **Sparse vs Dense indexing**
- **Advantages & disadvantages**
- How **duplicate values** are handled

---

## 🧩 1. Index Types Overview

### 🔹 Primary Index

- Built automatically on the **primary key**.
- **Unique** and **non-null** by definition.
- Used to directly access rows.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

### 🔹 Secondary Index

- Created on **non-primary key columns**.
- Can contain **duplicate values**.
- Uses row ID or primary key to locate data.

```sql
CREATE INDEX idx_email ON users(email);
```

---

### 🔹 Clustered Index

- Dictates the **physical order** of records on disk.
- Only one per table.
- Often coincides with the primary index.

```sql
CREATE CLUSTERED INDEX idx_order_date ON orders(order_date);
```

---

## 🔍 2. Sparse vs Dense Indexing in Primary Indexing

| Feature            | Dense Index                      | Sparse Index                          |
|--------------------|----------------------------------|----------------------------------------|
| Definition         | Index contains **every key**     | Index contains **some keys** only     |
| Usage in Primary   | ✅ Required                      | ❌ Not applicable                      |
| Pointer Type       | Points to **every row**          | Points to **block/first row**         |
| Storage            | More storage                     | Less storage                          |
| Access Time        | Faster (no scanning)             | Slower (requires block scanning)      |

> 🔐 **Primary indexes are always dense** — because they enforce uniqueness and must point to every record.

---

## ✅ 3. Advantages and Disadvantages

### 🔷 Dense Index

**Advantages:**
- Faster lookups
- Direct row access (no scanning)

**Disadvantages:**
- Larger index size
- More maintenance on insert/delete

---

### 🔷 Sparse Index

**Advantages:**
- Smaller in size
- Less overhead during updates

**Disadvantages:**
- Slower access (block scan needed)
- Only works when data is **sorted on index column**

---

## 🔁 4. Handling of Duplicate Values

### 🔹 Clustered Index

- If duplicates exist, rows are sorted **by the index column** and then by the **row ID** (or internal pointer).
- Only allowed when **not on the primary key**.

**Example:**
```sql
CREATE TABLE sales (
    sale_id INT,
    sale_date DATE
);
-- Assuming no primary key, you can have:
CREATE CLUSTERED INDEX idx_sale_date ON sales(sale_date);
```

> ✅ **Duplicates are stored together** in index order.

---

### 🔹 Secondary Index

- **Duplicates are allowed**.
- All matching entries in the index point to the **corresponding rows**.

**Example:**
```sql
SELECT * FROM users WHERE city = 'Delhi';
```

- If 1,000 users are from Delhi, the secondary index will have 1,000 entries pointing to those rows.

---

## 📘 5. Summary Table

| Feature                | Primary Index | Secondary Index | Clustered Index |
|------------------------|---------------|------------------|------------------|
| Unique Required        | ✅ Yes        | ❌ No            | ❌ No (unless on PK) |
| Can Be Sparse          | ❌ No         | ✅ Yes           | ❌ No            |
| Can Be Dense           | ✅ Yes        | ✅ Yes           | ✅ Yes           |
| Allows Duplicates      | ❌ No         | ✅ Yes           | ✅ Yes (on non-PK) |
| Affects Data Ordering  | ❌ No         | ❌ No            | ✅ Yes           |
| Fast for Range Queries | ❌ No         | ❌ No            | ✅ Yes           |

---

## 🧠 6. Best Practices

- Use **Primary Index** for enforcing uniqueness and fast access by ID.
- Use **Secondary Indexes** for non-unique columns like `email`, `status`, etc.
- Use **Clustered Index** for range queries or sorting.

---

# 📚 Indexing Concepts in Databases

This document covers key concepts around **Primary Index**, **Clustered Index**, and **Secondary Index**, including their behavior in **sparse/dense indexing** and how **duplicate values** are handled.

---

## 🔹 1. Primary Index

- A **Primary Index** is usually built on the **primary key** of a table.
- It is typically a **dense index**, meaning it contains an index entry for **every search key** (i.e., every row).
- However, **primary indexes can be sparse** when:
  - Data is stored in sorted order on the search key.
  - The index stores only the **first search key of each block**.

### 🔸 Dense vs Sparse in Primary Index

| Index Type | Description |
|------------|-------------|
| Dense Index | Contains **every search key** with a pointer to the corresponding record. |
| Sparse Index | Contains **only the first search key of each data block**, pointing to that block. |

---

## 🔹 2. Clustered Index

- A **Clustered Index** defines the **physical ordering** of data on disk.
- If the clustered index is on a **primary key**, then there are **no duplicate values**.
- If the clustered index is on a **non-primary key** (i.e., non-unique column), then **duplicate values** can exist.

### 🔸 Duplicate Handling in Clustered Index

- The index contains **pointers to the block** that contains the key.
- If the key appears in **multiple blocks**:
  - The **first pointer** is called the **Block Pointer**.
  - The **subsequent pointers** are called **Block Hangers**.

> 🔹 Block Pointer → points to the **first block** containing the key  
> 🔹 Block Hangers → point to **other blocks** containing the same key

---

## 🔹 3. Secondary Index

- A **Secondary Index** is built on **non-primary key** columns.
- It is **always a dense index** because:
  - It must include an entry for **every search key value**, even if the same value appears multiple times.

### 🔸 Duplicate Handling in Secondary Index

- For **unique values**:  
  The index stores a direct pointer to the **primary key** or **row ID**.

- For **duplicate values**:
  - The index contains a pointer to a **table (or list)** of **record pointers**.
  - This table stores all **primary key pointers** (or row IDs) for rows matching that duplicate value.

---

## 📘 Summary

| Index Type       | Can Be Sparse | Always Dense | Handles Duplicates | Notes |
|------------------|---------------|--------------|---------------------|-------|
| Primary Index    | ✅ Yes         | ✅ Yes        | ❌ No                | Can be sparse if data is sorted |
| Clustered Index  | ❌ No          | ✅ Yes        | ✅ Yes               | Sorts data physically |
| Secondary Index  | ❌ No          | ✅ Yes        | ✅ Yes               | Uses pointer table for duplicates |

---

## 🧠 Key Terms

- **Dense Index**: One index entry per search key (i.e., per row).
- **Sparse Index**: One index entry per block; contains only some keys.
- **Block Pointer**: First pointer to a data block containing the key.
- **Block Hanger**: Additional pointers to blocks containing the same key.
- **Pointer Table**: Structure used in secondary indexes to handle duplicates.

