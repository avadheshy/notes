# Normalization vs Denormalization

## 🔹 What is Normalization?

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller related tables and defining relationships between them using keys.

### ✅ Objectives:

* Eliminate redundant data
* Ensure data dependencies make sense
* Improve data integrity

### 📦 Example (Before Normalization):

| OrderID | CustomerName | Product  | ProductPrice |
| ------- | ------------ | -------- | ------------ |
| 1       | Alice        | Keyboard | 100          |
| 2       | Bob          | Mouse    | 50           |
| 3       | Alice        | Mouse    | 50           |

### 📦 After Normalization (2NF or higher):

**Customers Table:**

| CustomerID | CustomerName |
| ---------- | ------------ |
| 1          | Alice        |
| 2          | Bob          |

**Products Table:**

| ProductID | ProductName | ProductPrice |
| --------- | ----------- | ------------ |
| 1         | Keyboard    | 100          |
| 2         | Mouse       | 50           |

**Orders Table:**

| OrderID | CustomerID | ProductID |
| ------- | ---------- | --------- |
| 1       | 1          | 1         |
| 2       | 2          | 2         |
| 3       | 1          | 2         |

---

## 🔹 What is Denormalization?

Denormalization is the process of combining normalized tables into larger tables to improve read performance. It introduces some redundancy to avoid complex joins and reduce query execution time.

### ✅ Objectives:

* Improve read performance
* Simplify queries

### 📦 Example:

Denormalized version of the above data:

| OrderID | CustomerName | ProductName | ProductPrice |
| ------- | ------------ | ----------- | ------------ |
| 1       | Alice        | Keyboard    | 100          |
| 2       | Bob          | Mouse       | 50           |
| 3       | Alice        | Mouse       | 50           |

Here, customer and product information is repeated to avoid joins.

### 🔧 Methods to Denormalize Data:

* **Table Merging**: Combine two or more related tables into one.
* **Precomputed Columns**: Store derived or aggregated values (e.g., total\_price).
* **Redundant Columns**: Store frequently joined values directly in the main table.
* **Materialized Views**: Use precomputed views that store the result of complex joins.

---

## 🔸 Key Differences

| Feature            | Normalization                | Denormalization                     |
| ------------------ | ---------------------------- | ----------------------------------- |
| Redundancy         | Eliminates redundancy        | Introduces redundancy               |
| Query Complexity   | More complex (joins needed)  | Simpler queries                     |
| Update Anomalies   | Prevented                    | Possible                            |
| Storage Efficiency | More efficient               | May use more storage                |
| Use Case           | OLTP (Transactional systems) | OLAP (Reporting/Analytical systems) |

---

## 🧩 What Are Normal Forms?

Normal Forms are rules that define the level of normalization in a database schema. Each form builds upon the previous one:

### 🔸 1NF (First Normal Form):

* All attributes must have atomic (indivisible) values
* Each record must be unique

### 🔸 2NF (Second Normal Form):

* Must be in 1NF
* No partial dependency on any candidate key

### 🔸 3NF (Third Normal Form):

* Must be in 2NF
* No transitive dependency (non-key fields must depend only on the primary key)

### 🔸 BCNF (Boyce-Codd Normal Form):

* Stronger version of 3NF
* Every determinant must be a candidate key

### 🔸 4NF and 5NF:

* Address multi-valued dependencies and join dependencies
* Rarely used in practice but ensure very high normalization

---

## 🧾 Data Consistency vs Data Integrity

### 🔹 Data Consistency:

Refers to the correctness and uniformity of data across different parts of the database or system. If a value is updated in one place, it should reflect everywhere consistently.

**Example**: If a user's email is updated in the `users` table, it should also be updated in the `orders` or `messages` table if stored there.

### 🔹 Data Integrity:

Refers to the accuracy and trustworthiness of data throughout its lifecycle. It's maintained by constraints, rules, and validations.

**Types of Data Integrity:**

* **Entity Integrity**: Each row must have a unique primary key.
* **Referential Integrity**: Foreign keys must correctly reference primary keys.
* **Domain Integrity**: Columns must have valid values (e.g., age must be a positive integer).

---

## 🧠 Conclusion:

* **Normalization** = Data integrity & reduced redundancy
* **Denormalization** = Better read performance with redundancy
* **Consistency** ensures changes are reflected uniformly across the system
* **Integrity** ensures accuracy and validity of the data
* Choose based on use-case: OLTP (normalize), OLAP (denormalize)



# SQL Joins Explained with Examples

Joins in SQL are used to combine rows from two or more tables based on a related column. They allow you to retrieve connected data from multiple tables in a relational database.

---

## 🔸 1. INNER JOIN

Returns only the rows with matching values in both tables.

### 🧾 Example:

**Customers Table**

| id | name    |
| -- | ------- |
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |

**Orders Table**

| order\_id | customer\_id |
| --------- | ------------ |
| 101       | 1            |
| 102       | 2            |

```sql
SELECT customers.name, orders.order_id
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
```

**Result:**

| name  | order\_id |
| ----- | --------- |
| Alice | 101       |
| Bob   | 102       |

---

## 🔸 2. LEFT JOIN (LEFT OUTER JOIN)

Returns all rows from the left table and the matched rows from the right table. Unmatched rows in the right table return `NULL`.

```sql
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
```

**Result:**

| name    | order\_id |
| ------- | --------- |
| Alice   | 101       |
| Bob     | 102       |
| Charlie | NULL      |

---

## 🔸 3. RIGHT JOIN (RIGHT OUTER JOIN)

Returns all rows from the right table and the matched rows from the left table. Unmatched rows in the left table return `NULL`.

```sql
SELECT customers.name, orders.order_id
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;
```

**Result:**

| name  | order\_id |
| ----- | --------- |
| Alice | 101       |
| Bob   | 102       |

---

## 🔸 4. FULL JOIN (FULL OUTER JOIN)

Returns all rows when there is a match in one of the tables. Unmatched rows from both tables return `NULL`.

```sql
SELECT customers.name, orders.order_id
FROM customers
FULL OUTER JOIN orders ON customers.id = orders.customer_id;
```

**Result:**

| name    | order\_id |
| ------- | --------- |
| Alice   | 101       |
| Bob     | 102       |
| Charlie | NULL      |

---

## 🔸 5. CROSS JOIN

Returns the Cartesian product of both tables – every row in the first table is joined with every row in the second.

```sql
SELECT customers.name, products.product_name
FROM customers
CROSS JOIN products;
```

**Customers Table:** 3 rows
**Products Table:** 2 rows

➡️ Result will have `3 × 2 = 6` rows.

---

## 🔸 6. SELF JOIN

A table is joined with itself to find relationships within the same table.

### 🧾 Example:

**Employees Table**

| id | name    | manager\_id |
| -- | ------- | ----------- |
| 1  | Alice   | NULL        |
| 2  | Bob     | 1           |
| 3  | Charlie | 1           |

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

**Result:**

| employee | manager |
| -------- | ------- |
| Bob      | Alice   |
| Charlie  | Alice   |

---

## 🧠 Summary Table

| Join Type  | Returns                                                         |
| ---------- | --------------------------------------------------------------- |
| INNER JOIN | Only matched rows from both tables                              |
| LEFT JOIN  | All rows from left + matched rows from right (NULL if no match) |
| RIGHT JOIN | All rows from right + matched rows from left (NULL if no match) |
| FULL JOIN  | All rows from both tables (NULLs where no match)                |
| CROSS JOIN | Every combination of rows from both tables                      |
| SELF JOIN  | Matches rows within the same table                              |

---

Use joins wisely to maintain performance and return exactly the data you need!
