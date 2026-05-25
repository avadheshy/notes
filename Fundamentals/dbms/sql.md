# SQL Complete Reference — Questions & Answers

---

## Table of Contents

1. [Basic Queries](#1-basic-queries)
2. [Intermediate Queries](#2-intermediate-queries)
3. [Advanced Queries & Window Functions](#3-advanced-queries--window-functions)
4. [SQL Commands & Clauses](#4-sql-commands--clauses)
5. [Joins](#5-joins)
6. [Indexing & Performance](#6-indexing--performance)
7. [Transactions & Concurrency](#7-transactions--concurrency)
8. [Database Design & Normalization](#8-database-design--normalization)
9. [Stored Objects — Views, Procedures, Triggers](#9-stored-objects--views-procedures-triggers)
10. [Advanced & Practical Scenarios](#10-advanced--practical-scenarios)

---

## 1. Basic Queries

---

### Q1. Fetch the second-highest salary from an `Employee` table.

**Method 1 — Subquery (most portable):**
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

**Method 2 — `LIMIT` with `OFFSET`:**
```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

**Method 3 — `ROW_NUMBER()` window function:**
```sql
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM Employee
) ranked
WHERE rn = 2;
```

---

### Q2. Get duplicate records from a table.

**Method 1 — `GROUP BY` + `HAVING`:**
```sql
SELECT column1, column2, COUNT(*)
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```

**Method 2 — Show all duplicate rows with full details:**
```sql
SELECT e.*
FROM Employee e
INNER JOIN (
    SELECT name, email
    FROM Employee
    GROUP BY name, email
    HAVING COUNT(*) > 1
) dups ON e.name = dups.name AND e.email = dups.email;
```

---

### Q3. Find employees who earn more than their managers.

```sql
SELECT e.*
FROM Employee e
JOIN Employee m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

---

### Q4. Retrieve the top N records from a table.

```sql
SELECT *
FROM table_name
ORDER BY column_name DESC
LIMIT N;
```

> Replace `N` with the desired count. Use `FETCH NEXT N ROWS ONLY` in SQL Server.

---

### Q5. Count the number of employees in each department.

```sql
SELECT department_id, COUNT(*) AS num_employees
FROM Employee
GROUP BY department_id;
```

---

### Q6. Find the department with the highest number of employees.

```sql
SELECT department_id, COUNT(*) AS num_employees
FROM Employee
GROUP BY department_id
ORDER BY num_employees DESC
LIMIT 1;
```

---

### Q7. Retrieve employees who have the same salary.

**Method 1 — `EXISTS` correlated subquery:**
```sql
SELECT *
FROM Employee e1
WHERE EXISTS (
    SELECT 1 FROM Employee e2
    WHERE e1.salary = e2.salary AND e1.id != e2.id
);
```

**Method 2 — Self-join:**
```sql
SELECT DISTINCT e1.*
FROM Employee e1
JOIN Employee e2 ON e1.salary = e2.salary AND e1.id != e2.id;
```

---

### Q8. List all employees whose name starts with 'A'.

```sql
SELECT *
FROM Employee
WHERE name LIKE 'A%';
```

---

### Q9. Get the last record from a table.

```sql
SELECT *
FROM table_name
ORDER BY id DESC
LIMIT 1;
```

---

### Q10. Get employees who joined in the last 6 months.

```sql
SELECT *
FROM Employee
WHERE join_date >= CURRENT_DATE - INTERVAL 6 MONTH;
```

> SQL Server equivalent: `WHERE join_date >= DATEADD(MONTH, -6, GETDATE())`

---

## 2. Intermediate Queries

---

### Q11. Find the Nth highest salary.

**Method 1 — Correlated subquery:**
```sql
SELECT DISTINCT salary
FROM Employee e1
WHERE (N - 1) = (
    SELECT COUNT(DISTINCT salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary
);
```

**Method 2 — `DENSE_RANK()`:**
```sql
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) ranked
WHERE rnk = N;
```

**Method 3 — `LIMIT` + `OFFSET`:**
```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET N-1;
```

---

### Q12. Remove duplicate rows without using `DISTINCT`.

**Method 1 — Delete using `ROW_NUMBER()`:**
```sql
DELETE FROM Employee
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (
            PARTITION BY name, email ORDER BY id
        ) AS rn
        FROM Employee
    ) t
    WHERE rn > 1
);
```

**Method 2 — Using `MIN(id)` with `NOT IN`:**
```sql
DELETE FROM table_name
WHERE id NOT IN (
    SELECT MIN(id)
    FROM table_name
    GROUP BY column1, column2
);
```

**Method 3 — Create a clean copy:**
```sql
CREATE TABLE employees_clean AS
SELECT DISTINCT * FROM Employee;

DROP TABLE Employee;
ALTER TABLE employees_clean RENAME TO Employee;
```

---

### Q13. Find missing numbers in a sequence of IDs.

```sql
SELECT t1.id + 1 AS missing_id
FROM table_name t1
LEFT JOIN table_name t2 ON t1.id + 1 = t2.id
WHERE t2.id IS NULL;
```

---

### Q14. Display first name and last name in a single column.

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM Employee;
```

---

### Q15. Get the cumulative sum of salaries.

```sql
SELECT id, name, salary,
       SUM(salary) OVER (ORDER BY id) AS cumulative_salary
FROM Employee;
```

---

### Q16. Swap the values of two columns without a third variable.

```sql
UPDATE Employee
SET column1 = column1 + column2,
    column2 = column1 - column2,
    column1 = column1 - column2;
```

---

### Q17. Fetch employees whose names contain only vowels.

```sql
SELECT *
FROM Employee
WHERE name REGEXP '^[AEIOUaeiou]+$';
```

---

### Q18. Transpose rows into columns (pivot).

```sql
SELECT
    MAX(CASE WHEN month = 'Jan' THEN sales END) AS Jan,
    MAX(CASE WHEN month = 'Feb' THEN sales END) AS Feb,
    MAX(CASE WHEN month = 'Mar' THEN sales END) AS Mar
FROM sales_data;
```

> For dynamic pivoting, use database-specific dynamic SQL (e.g., `PIVOT` in SQL Server).

---

### Q19. Find employees with the highest salary in each department.

**Method 1 — Correlated subquery:**
```sql
SELECT *
FROM Employee e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE department_id = e.department_id
);
```

**Method 2 — `ROW_NUMBER()` window function:**
```sql
SELECT department_id, name, salary
FROM (
    SELECT department_id, name, salary,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rn
    FROM Employee
) ranked
WHERE rn = 1;
```

---

### Q20. Find customers who made multiple purchases on the same day.

```sql
SELECT customer_id, order_date
FROM Orders
GROUP BY customer_id, order_date
HAVING COUNT(*) > 1;
```

---

### Q21. Update one table using data from another table.

**Method 1 — `UPDATE` with `FROM` (PostgreSQL / SQL Server):**
```sql
UPDATE employees e
SET salary = s.new_salary
FROM salary_updates s
WHERE e.id = s.employee_id;
```

**Method 2 — Correlated subquery:**
```sql
UPDATE employees
SET salary = (
    SELECT new_salary FROM salary_updates s WHERE s.employee_id = employees.id
)
WHERE EXISTS (
    SELECT 1 FROM salary_updates s WHERE s.employee_id = employees.id
);
```

**Method 3 — `JOIN` syntax (MySQL):**
```sql
UPDATE employees e
INNER JOIN salary_updates s ON e.id = s.employee_id
SET e.salary = s.new_salary;
```

---

### Q22. Find employees who never submitted a report.

**Method 1 — `LEFT JOIN` + `IS NULL`:**
```sql
SELECT e.id, e.name
FROM employees e
LEFT JOIN reports r ON e.id = r.employee_id
WHERE r.employee_id IS NULL;
```

**Method 2 — `NOT EXISTS`:**
```sql
SELECT e.id, e.name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 FROM reports r WHERE r.employee_id = e.id
);
```

**Method 3 — `NOT IN` (watch for NULLs):**
```sql
SELECT e.id, e.name
FROM employees e
WHERE e.id NOT IN (
    SELECT employee_id FROM reports WHERE employee_id IS NOT NULL
);
```

---

### Q23. Filter NULL values.

```sql
-- Exclude NULLs
SELECT * FROM employees WHERE phone_number IS NOT NULL;

-- Include only NULLs
SELECT * FROM employees WHERE phone_number IS NULL;

-- Replace NULLs with a default using COALESCE
SELECT name, COALESCE(phone_number, 'No Phone') AS contact
FROM employees;
```

---

### Q24. Implement pagination.

**Method 1 — `LIMIT` / `OFFSET` (MySQL / PostgreSQL):**
```sql
SELECT * FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;  -- Page 3, 10 rows per page
```

**Method 2 — `OFFSET`/`FETCH` (SQL Server):**
```sql
SELECT * FROM employees
ORDER BY id
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY;
```

**Method 3 — `ROW_NUMBER()` (universal):**
```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM employees
) t
WHERE rn BETWEEN 21 AND 30;
```

**Method 4 — Cursor-based (best for large datasets):**
```sql
SELECT * FROM employees
WHERE id > @last_id
ORDER BY id
LIMIT 10;
```

---

## 3. Advanced Queries & Window Functions

---

### Q25. Get the moving average of sales for the last 3 months.

```sql
SELECT month,
       AVG(sales) OVER (
           ORDER BY month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS moving_avg
FROM sales_data;
```

---

### Q26. Rank employees by salary within each department.

```sql
SELECT *, RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM Employee;
```

---

### Q27. Find employees who have more than one manager.

```sql
SELECT employee_id
FROM EmployeeManagers
GROUP BY employee_id
HAVING COUNT(manager_id) > 1;
```

---

### Q28. Retrieve the most frequent order date.

```sql
SELECT order_date
FROM Orders
GROUP BY order_date
ORDER BY COUNT(*) DESC
LIMIT 1;
```

---

### Q29. Compare two tables and find mismatched records.

```sql
SELECT * FROM table1
EXCEPT
SELECT * FROM table2

UNION

SELECT * FROM table2
EXCEPT
SELECT * FROM table1;
```

---

### Q30. Calculate the difference between consecutive rows.

```sql
SELECT id, value,
       value - LAG(value) OVER (ORDER BY id) AS diff
FROM data_table;
```

---

### Q31. Delete every alternate row from a table.

```sql
DELETE FROM Employee
WHERE id % 2 = 0;
```

---

### Q32. Get the first purchase date for each customer.

```sql
SELECT customer_id, MIN(order_date) AS first_purchase
FROM Orders
GROUP BY customer_id;
```

---

### Q33. Get the running total of sales per month.

```sql
SELECT month,
       SUM(sales) OVER (ORDER BY month) AS running_total
FROM sales_data;
```

---

### Q34. Assign a global salary rank to all employees.

```sql
SELECT *, RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM Employee;
```

---

### Q35. Find the percentage contribution of each employee's salary to the total.

```sql
SELECT name, salary,
       ROUND(100.0 * salary / SUM(salary) OVER (), 2) AS percentage
FROM Employee;
```

---

### Q36. Get `LEAD()` and `LAG()` salaries for each employee.

```sql
SELECT name, salary,
       LAG(salary)  OVER (ORDER BY salary) AS previous_salary,
       LEAD(salary) OVER (ORDER BY salary) AS next_salary
FROM Employee;
```

---

### Q37. Get the difference between two consecutive transactions.

```sql
SELECT id, transaction_amount,
       transaction_amount - LAG(transaction_amount) OVER (ORDER BY transaction_date) AS difference
FROM Transactions;
```

---

## 4. SQL Commands & Clauses

---

### Q38. What is the difference between `WHERE` and `HAVING`?

`WHERE` filters **individual rows before** grouping. `HAVING` filters **groups after** aggregation.

```sql
-- WHERE filters rows first
SELECT department, COUNT(*) AS emp_count
FROM employees
WHERE salary > 50000
GROUP BY department;

-- HAVING filters groups after aggregation
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

-- Combined
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE hire_date > '2020-01-01'
GROUP BY department
HAVING AVG(salary) > 60000;
```

---

### Q39. What is the difference between `UNION` and `UNION ALL`?

```sql
-- UNION: removes duplicates (slower — requires deduplication)
SELECT name FROM employees_2023
UNION
SELECT name FROM employees_2024;

-- UNION ALL: keeps duplicates (faster — no dedup step)
SELECT name FROM employees_2023
UNION ALL
SELECT name FROM employees_2024;
```

> **Prefer `UNION ALL`** when you know the result sets are already distinct or duplicates are acceptable.

---

### Q40. What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?

```sql
-- DELETE: removes specific rows, can be rolled back, fires triggers
DELETE FROM employees WHERE department_id = 5;

-- TRUNCATE: removes all rows, minimal logging, resets identity column
TRUNCATE TABLE employees;

-- DROP: removes the entire table structure and data permanently
DROP TABLE employees;
```

| Operation | Speed  | Rollback | Triggers | WHERE Clause | Identity Reset |
|-----------|--------|----------|----------|--------------|----------------|
| DELETE    | Slow   | Yes      | Yes      | Yes          | No             |
| TRUNCATE  | Fast   | Limited  | No       | No           | Yes            |
| DROP      | Fast   | DDL only | No       | No           | N/A            |

---

### Q41. What is the difference between `EXISTS` and `IN`?

```sql
-- EXISTS: short-circuits on first match; better for large subquery results
SELECT * FROM employees e
WHERE EXISTS (
    SELECT 1 FROM departments d
    WHERE d.id = e.department_id AND d.active = 1
);

-- IN: better for small, static lists; careful with NULLs in subquery
SELECT * FROM employees
WHERE department_id IN (1, 2, 3);
```

> **Rule of thumb:** Use `EXISTS` for large datasets and correlated lookups; use `IN` for small, known value lists.

---

### Q42. What is the difference between `GROUP BY` and `ORDER BY`?

```sql
-- GROUP BY: collapses rows into groups for aggregation
SELECT department_id, COUNT(*), AVG(salary)
FROM employees
GROUP BY department_id;

-- ORDER BY: sorts the final result set
SELECT * FROM employees
ORDER BY salary DESC, name ASC;

-- Combined
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY avg_salary DESC;
```

---

### Q43. How do aggregate functions handle `NULL` values?

```sql
SELECT
    COUNT(*)           AS total_rows,          -- Counts ALL rows including NULLs
    COUNT(commission)  AS non_null_count,       -- Skips NULLs
    AVG(commission)    AS avg_non_null,         -- Averages only non-NULLs
    SUM(commission)    AS sum_non_null          -- Sums only non-NULLs
FROM employees;

-- Treat NULLs as zero
SELECT AVG(COALESCE(commission, 0)) AS avg_with_zeros
FROM employees;
```

---

### Q44. What is the difference between `PRIMARY KEY` and `UNIQUE`?

```sql
-- PRIMARY KEY: enforces uniqueness + NOT NULL; only one per table
CREATE TABLE employees (
    id    INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE   -- UNIQUE allows one NULL; multiple per table
);

-- Composite PRIMARY KEY
CREATE TABLE order_items (
    order_id   INT,
    product_id INT,
    PRIMARY KEY (order_id, product_id)
);
```

| Property   | PRIMARY KEY          | UNIQUE                     |
|------------|----------------------|----------------------------|
| NULL       | Not allowed          | One NULL allowed           |
| Per table  | Only one             | Multiple allowed           |
| Purpose    | Row identity         | Business uniqueness        |

---

### Q45. Subqueries and Correlated Subqueries — what's the difference?

```sql
-- Regular subquery: runs ONCE, result reused for all rows
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery: runs FOR EACH ROW of the outer query
SELECT e1.name, e1.salary, e1.department_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

---

### Q46. What are Common Table Expressions (CTEs)?

```sql
-- Simple CTE
WITH high_earners AS (
    SELECT name, salary, department_id
    FROM employees
    WHERE salary > 100000
)
SELECT he.name, d.department_name
FROM high_earners he
JOIN departments d ON he.department_id = d.id;

-- Multiple CTEs
WITH
dept_stats AS (
    SELECT department_id, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
),
high_paying AS (
    SELECT * FROM dept_stats WHERE avg_salary > 80000
)
SELECT d.department_name, hp.emp_count, hp.avg_salary
FROM high_paying hp
JOIN departments d ON hp.department_id = d.id;

-- Recursive CTE (org hierarchy)
WITH RECURSIVE emp_hierarchy AS (
    SELECT id, name, manager_id, 0 AS level
    FROM employees WHERE manager_id IS NULL        -- anchor
    UNION ALL
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    JOIN emp_hierarchy h ON e.manager_id = h.id   -- recursive step
)
SELECT * FROM emp_hierarchy ORDER BY level, name;
```

---

## 5. Joins

---

### Q47. Explain all types of SQL JOINs with examples.

```sql
-- INNER JOIN: only matching rows from both tables
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- LEFT JOIN: all rows from left + matching from right (NULLs where no match)
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- RIGHT JOIN: all rows from right + matching from left
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;

-- FULL OUTER JOIN: all rows from both tables
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;

-- CROSS JOIN: Cartesian product (every row × every row)
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;

-- SELF JOIN: join a table to itself (e.g., employee-manager)
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

**Performance order (fastest → slowest):**
`INNER JOIN` → `LEFT/RIGHT JOIN` → `FULL OUTER JOIN` → `CROSS JOIN`

---

## 6. Indexing & Performance

---

### Q48. What is an index and when should you use one?

Indexes are data structures that speed up data retrieval by creating a lookup shortcut.

```sql
-- Single-column index
CREATE INDEX idx_salary ON employees(salary);

-- Composite index
CREATE INDEX idx_dept_salary ON employees(department_id, salary);

-- Unique index
CREATE UNIQUE INDEX idx_email ON employees(email);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_emp ON employees(salary) WHERE status = 'ACTIVE';

-- Functional index
CREATE INDEX idx_upper_name ON employees(UPPER(name));
```

**Use indexes on columns that appear frequently in:** `WHERE`, `JOIN ON`, `ORDER BY`, foreign keys.

---

### Q49. Clustered vs Non-Clustered Index — what's the difference?

```sql
-- Clustered: physically reorders rows on disk; only ONE per table
CREATE CLUSTERED INDEX idx_emp_id ON employees(id);       -- SQL Server

-- Non-Clustered: separate structure pointing to rows; multiple allowed
CREATE NONCLUSTERED INDEX idx_emp_name ON employees(name);
```

| Type           | Data Storage           | Per Table | Lookup Speed |
|----------------|------------------------|-----------|--------------|
| Clustered      | Rows ordered by index  | Only 1    | Direct       |
| Non-Clustered  | Separate index pages   | Multiple  | Extra lookup |

---

### Q50. How do indexes affect DML performance?

Every `INSERT`, `UPDATE`, or `DELETE` must also update all associated indexes, making writes slower. For bulk loads, it's often best to drop indexes, load, then recreate them.

```sql
-- Drop before bulk insert
DROP INDEX idx_salary ON employees;
-- ... bulk insert ...
-- Recreate after
CREATE INDEX idx_salary ON employees(salary);
```

---

### Q51. How do you analyze and optimize a slow query?

```sql
-- Use EXPLAIN / EXPLAIN ANALYZE
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.salary > 50000;

-- Avoid functions on indexed columns in WHERE
-- BAD:
WHERE YEAR(hire_date) = 2023
-- GOOD:
WHERE hire_date >= '2023-01-01' AND hire_date < '2024-01-01'

-- Use covering indexes to avoid table lookups
CREATE INDEX idx_covering ON employees(department_id, salary, name);

-- Force index (when necessary)
SELECT * FROM employees USE INDEX (idx_salary) WHERE salary > 50000;

-- Update statistics
ANALYZE employees;
```

---

## 7. Transactions & Concurrency

---

### Q52. What are ACID properties?

```sql
-- ATOMICITY: All-or-nothing
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;   -- Both succeed, or ROLLBACK makes both disappear

-- CONSISTENCY: Constraints always maintained (CHECK, FK, etc.)

-- ISOLATION: Concurrent transactions don't interfere
-- Controlled via isolation levels

-- DURABILITY: Committed data survives crashes (WAL / redo logs)
```

---

### Q53. What are Transaction Isolation Levels?

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;  -- Allows dirty reads
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;    -- Prevents dirty reads
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;   -- Prevents dirty + non-repeatable reads
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;      -- Prevents all anomalies (strictest)
```

| Level            | Dirty Read | Non-Repeatable Read | Phantom Read |
|------------------|-----------|---------------------|--------------|
| READ UNCOMMITTED | Yes        | Yes                 | Yes          |
| READ COMMITTED   | No         | Yes                 | Yes          |
| REPEATABLE READ  | No         | No                  | Yes          |
| SERIALIZABLE     | No         | No                  | No           |

---

### Q54. How do you prevent deadlocks?

```sql
-- Strategy 1: Always acquire locks in a consistent order
BEGIN TRANSACTION;
    SELECT * FROM accounts WHERE id = 1 FOR UPDATE;  -- lower ID first
    SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
COMMIT;

-- Strategy 2: Keep transactions short
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Strategy 3: Use appropriate isolation levels
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Strategy 4: Implement retry logic in application code
```

---

### Q55. Pessimistic vs Optimistic locking — what's the difference?

```sql
-- Pessimistic: lock the row before reading; others must wait
BEGIN TRANSACTION;
    SELECT * FROM products WHERE id = 1 FOR UPDATE;
    UPDATE products SET quantity = quantity - 1 WHERE id = 1;
COMMIT;

-- Optimistic: no lock; check version before saving
-- (requires a `version` column)
SELECT id, name, price, version FROM products WHERE id = 1;
-- ... user edits in app ...
UPDATE products
SET price = 150, version = version + 1
WHERE id = 1 AND version = @original_version;
-- If 0 rows affected → another user already updated it
```

---

## 8. Database Design & Normalization

---

### Q56. What are the normal forms? (1NF → 3NF)

**1NF — Atomic values, no repeating groups:**
```sql
-- Violates 1NF (multiple phones in one column)
CREATE TABLE employees_bad (id INT, phones VARCHAR(200));

-- 1NF compliant
CREATE TABLE employee_phones (
    employee_id INT,
    phone       VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
```

**2NF — No partial dependency on a composite key:**
```sql
-- Violates 2NF (product_name depends only on product_id, not order_id)
CREATE TABLE order_items_bad (
    order_id INT, product_id INT, product_name VARCHAR(100),
    PRIMARY KEY (order_id, product_id)
);

-- 2NF compliant: move product_name to a products table
CREATE TABLE products   (id INT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2));
CREATE TABLE order_items(order_id INT, product_id INT, quantity INT,
    PRIMARY KEY (order_id, product_id));
```

**3NF — No transitive dependency:**
```sql
-- Violates 3NF (department_name depends on department_id, not employee id)
CREATE TABLE employees_bad (
    id INT PRIMARY KEY, name VARCHAR(100),
    department_id INT, department_name VARCHAR(100)
);

-- 3NF compliant
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE employees   (id INT PRIMARY KEY, name VARCHAR(100),
    department_id INT, FOREIGN KEY (department_id) REFERENCES departments(id));
```

---

### Q57. What is Denormalization and when is it used?

Denormalization intentionally introduces redundancy to improve **read performance**, often used in reporting or data warehouse scenarios.

```sql
-- Denormalized orders table (avoids joins at query time)
CREATE TABLE orders_denormalized (
    id              INT PRIMARY KEY,
    customer_id     INT,
    customer_name   VARCHAR(100),  -- duplicated from customers
    order_date      DATE,
    total_amount    DECIMAL(10,2), -- pre-calculated
    item_count      INT            -- pre-calculated
);
```

---

### Q58. What are Foreign Keys and Referential Integrity?

```sql
CREATE TABLE employees (
    id            INT PRIMARY KEY,
    name          VARCHAR(100),
    department_id INT,
    CONSTRAINT fk_emp_dept
        FOREIGN KEY (department_id) REFERENCES departments(id)
        ON DELETE SET NULL     -- set to NULL if department is deleted
        ON UPDATE CASCADE      -- propagate department ID changes
);

-- Find orphaned records (broken referential integrity)
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id
WHERE d.id IS NULL AND e.department_id IS NOT NULL;
```

---

### Q59. What is the difference between a VIEW and a TABLE?

```sql
-- VIEW: virtual table; no data stored; always reflects current data
CREATE VIEW active_employees AS
SELECT id, name, email, hire_date
FROM employees
WHERE status = 'ACTIVE';

-- Use like a table
SELECT * FROM active_employees;
```

| Aspect       | VIEW                     | TABLE                    |
|--------------|--------------------------|--------------------------|
| Storage      | No physical storage      | Data physically stored   |
| Performance  | Recalculated each query  | Direct data access       |
| Real-time    | Always current           | Data as of last DML      |
| Indexes      | Not directly indexable   | Fully indexable          |

---

### Q60. What are Materialized Views?

```sql
-- Create (PostgreSQL)
CREATE MATERIALIZED VIEW dept_stats AS
SELECT d.department_name, COUNT(e.id) AS emp_count, AVG(e.salary) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.department_name;

-- Refresh manually
REFRESH MATERIALIZED VIEW dept_stats;

-- Non-blocking refresh
REFRESH MATERIALIZED VIEW CONCURRENTLY dept_stats;
```

> Materialized views store the query result physically, so reads are fast but data can become stale until refreshed.

---

## 9. Stored Objects — Views, Procedures, Triggers

---

### Q61. What are Stored Procedures and what are their pros/cons?

```sql
-- Basic stored procedure (SQL Server)
CREATE PROCEDURE GetEmployeesByDept
    @DeptId    INT,
    @MinSalary DECIMAL(10,2) = 0
AS
BEGIN
    SELECT id, name, salary
    FROM employees
    WHERE department_id = @DeptId AND salary >= @MinSalary
    ORDER BY salary DESC;
END;

EXEC GetEmployeesByDept @DeptId = 1, @MinSalary = 50000;

-- With OUTPUT parameters
CREATE PROCEDURE GetDeptStats
    @DeptId      INT,
    @EmpCount    INT OUTPUT,
    @AvgSalary   DECIMAL(10,2) OUTPUT
AS
BEGIN
    SELECT @EmpCount = COUNT(*), @AvgSalary = AVG(salary)
    FROM employees WHERE department_id = @DeptId;
END;
```

**Pros:** Pre-compiled (fast), centralized logic, parameterized (secure), reduced network round-trips.
**Cons:** DB-specific (not portable), harder to version-control, tight coupling to schema.

---

### Q62. What are Triggers and when are they used?

```sql
-- AFTER INSERT trigger (audit logging)
CREATE TRIGGER tr_emp_insert
ON employees
AFTER INSERT
AS
BEGIN
    INSERT INTO audit_log (table_name, operation, record_id, changed_by, change_date)
    SELECT 'employees', 'INSERT', i.id, SYSTEM_USER, GETDATE()
    FROM inserted i;
END;

-- AFTER UPDATE trigger
CREATE TRIGGER tr_emp_update
ON employees
AFTER UPDATE
AS
BEGIN
    INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, changed_by)
    SELECT 'employees', 'UPDATE', i.id,
           CONCAT('salary:', d.salary),
           CONCAT('salary:', i.salary),
           SYSTEM_USER
    FROM inserted i JOIN deleted d ON i.id = d.id;
END;

-- BEFORE INSERT trigger (MySQL) — validation + defaults
DELIMITER //
CREATE TRIGGER tr_emp_before_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Salary cannot be negative';
    END IF;
    IF NEW.hire_date IS NULL THEN
        SET NEW.hire_date = CURDATE();
    END IF;
END;
//
DELIMITER ;
```

---

### Q63. What is the difference between Triggers and Stored Procedures?

| Aspect         | Triggers                        | Stored Procedures              |
|----------------|---------------------------------|--------------------------------|
| Execution      | Automatic on DML events         | Manual / explicit call         |
| Parameters     | None                            | Supported                      |
| Return values  | Cannot return values            | Can return values              |
| Transactions   | Part of triggering transaction  | Can manage own transactions    |
| Use cases      | Auditing, validation, cascades  | Business logic, complex ops    |

---

## 10. Advanced & Practical Scenarios

---

### Q64. Implement Soft Delete.

```sql
-- Add soft-delete columns
ALTER TABLE products ADD is_deleted BIT DEFAULT 0;
ALTER TABLE products ADD deleted_at DATETIME2;
ALTER TABLE products ADD deleted_by VARCHAR(100);

-- Soft delete procedure
CREATE PROCEDURE sp_SoftDelete
    @ProductId INT, @DeletedBy VARCHAR(100)
AS
BEGIN
    UPDATE products
    SET is_deleted = 1, deleted_at = GETDATE(), deleted_by = @DeletedBy, is_active = 0
    WHERE id = @ProductId;
END;

-- View to hide deleted records
CREATE VIEW active_products AS
SELECT * FROM products WHERE is_deleted = 0;

-- Restore a soft-deleted record
UPDATE products
SET is_deleted = 0, deleted_at = NULL, deleted_by = NULL, is_active = 1
WHERE id = @ProductId;
```

---

### Q65. Implement Audit Logging.

```sql
CREATE TABLE audit_log (
    id          BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name  VARCHAR(100)  NOT NULL,
    operation   VARCHAR(10)   NOT NULL,   -- INSERT / UPDATE / DELETE
    record_id   VARCHAR(50),
    old_values  NVARCHAR(MAX),            -- JSON
    new_values  NVARCHAR(MAX),            -- JSON
    changed_by  VARCHAR(100)  NOT NULL,
    changed_at  DATETIME2     DEFAULT GETDATE()
);

-- Query audit history for a record
SELECT table_name, operation, record_id, changed_by, changed_at,
       JSON_VALUE(old_values, '$.name') AS old_name,
       JSON_VALUE(new_values, '$.name') AS new_name
FROM audit_log
WHERE table_name = 'products' AND record_id = '123'
ORDER BY changed_at DESC;
```

---

### Q66. What is the Outbox Pattern for microservices consistency?

```sql
CREATE TABLE outbox_events (
    id           BIGINT IDENTITY(1,1) PRIMARY KEY,
    aggregate_id VARCHAR(100)   NOT NULL,
    event_type   VARCHAR(100)   NOT NULL,
    event_data   NVARCHAR(MAX)  NOT NULL,  -- JSON payload
    created_at   DATETIME2      DEFAULT GETDATE(),
    processed_at DATETIME2,
    retry_count  INT            DEFAULT 0,
    status       VARCHAR(20)    DEFAULT 'PENDING'  -- PENDING / PROCESSED / FAILED
);
```

The application writes to the `outbox_events` table **in the same transaction** as the business data change. A separate process picks up pending events and publishes them to the message broker, guaranteeing at-least-once delivery without distributed transactions.

---

### Q67. What is Schema Migration and how is it versioned?

```sql
-- Track applied migrations
CREATE TABLE schema_migrations (
    version      VARCHAR(50)  PRIMARY KEY,
    description  VARCHAR(255),
    applied_at   DATETIME2    DEFAULT GETDATE(),
    applied_by   VARCHAR(100) DEFAULT SYSTEM_USER
);

-- Example migration script
BEGIN TRANSACTION;
IF NOT EXISTS (SELECT 1 FROM schema_migrations WHERE version = '20240101_001')
BEGIN
    ALTER TABLE orders ADD loyalty_points INT DEFAULT 0;

    CREATE INDEX idx_orders_loyalty ON orders(loyalty_points);

    INSERT INTO schema_migrations (version, description)
    VALUES ('20240101_001', 'Add loyalty_points column to orders');
END
COMMIT;

-- Rollback script
BEGIN TRANSACTION;
    ALTER TABLE orders DROP COLUMN loyalty_points;
    DELETE FROM schema_migrations WHERE version = '20240101_001';
COMMIT;
```

---

---

## 11. DBMS Fundamentals

---

### Q68. What is DBMS and how is it different from a File System?

A **DBMS** is software that manages, stores, and retrieves structured data. It acts as a bridge between the database and client applications.

Key advantages over a file system:

| Aspect | File System | DBMS |
|---|---|---|
| Redundancy | High (data duplicated across files) | Controlled via normalization |
| Integrity | Manual enforcement | Constraints (PK, FK, CHECK) |
| Concurrency | No built-in control | Locking & isolation levels |
| Security | OS-level only | Role-based access (DCL) |
| Query | No standard language | SQL with optimizer |
| Relationships | Not supported | Foreign keys, joins |

---

### Q69. What are the SQL sub-languages? (DDL / DML / DCL / TCL / DQL)

This is a very common interview question. Know all five with examples.

**DDL — Data Definition Language** *(defines structure)*
```sql
CREATE TABLE employees (...);
ALTER TABLE employees ADD column_name datatype;
DROP TABLE employees;
TRUNCATE TABLE employees;   -- DDL, not DML (cannot be rolled back in MySQL)
RENAME TABLE old_name TO new_name;
```

**DML — Data Manipulation Language** *(manipulates data)*
```sql
INSERT INTO employees (name, salary) VALUES ('Alice', 90000);
UPDATE employees SET salary = 95000 WHERE id = 1;
DELETE FROM employees WHERE id = 1;
MERGE INTO target USING source ON (condition) ...;  -- UPSERT
```

**DCL — Data Control Language** *(manages permissions)*
```sql
GRANT SELECT, INSERT ON employees TO analyst_role;
REVOKE INSERT ON employees FROM analyst_role;
```

**TCL — Transaction Control Language** *(manages transactions)*
```sql
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 500 WHERE id = 1;
    SAVEPOINT after_debit;          -- partial rollback point
    UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;

-- Rollback to savepoint (not full rollback)
ROLLBACK TO SAVEPOINT after_debit;
```

**DQL — Data Query Language** *(retrieves data)*
```sql
SELECT name, salary FROM employees WHERE department_id = 3;
```

> **Key distinction asked in interviews:** `TRUNCATE` is **DDL** (not DML), so it cannot be rolled back in most databases and does not fire row-level triggers.

---

### Q70. What are the three types of table cloning?

```sql
-- 1. Simple Clone — copies structure AND data
CREATE TABLE employees_copy AS
SELECT * FROM employees;
-- Result: new table with data but NO constraints, indexes, or keys

-- 2. Shallow Clone — copies structure ONLY (no data, no constraints)
CREATE TABLE employees_shell LIKE employees;  -- MySQL only
-- Result: empty table with column definitions only

-- 3. Deep Clone — copies structure WITH constraints AND data
CREATE TABLE employees_full LIKE employees;   -- Step 1: structure + constraints
INSERT INTO employees_full SELECT * FROM employees;  -- Step 2: copy data
-- Result: full replica including indexes and constraints
```

| Clone Type | Data | Constraints / Indexes |
|---|---|---|
| Simple | ✅ Yes | ❌ No |
| Shallow | ❌ No | ❌ No |
| Deep | ✅ Yes | ✅ Yes |

*End of SQL Complete Reference*