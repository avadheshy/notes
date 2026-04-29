# Complete SQL Guide - Queries, Design, and Advanced Concepts

## 1. SQL Query & Joins

### 1. WHERE vs HAVING

**WHERE** filters rows before grouping, while **HAVING** filters groups after grouping.

```sql
-- WHERE: Filters individual rows
SELECT department, COUNT(*) as emp_count
FROM employees
WHERE salary > 50000  -- Filter rows first
GROUP BY department;

-- HAVING: Filters groups after aggregation
SELECT department, COUNT(*) as emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;  -- Filter groups after counting

-- Combined usage
SELECT department, AVG(salary) as avg_salary
FROM employees
WHERE hire_date > '2020-01-01'  -- Filter rows first
GROUP BY department
HAVING AVG(salary) > 60000;     -- Filter groups after aggregation
```

### 2. Types of Joins

#### INNER JOIN
Returns only matching records from both tables.

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

#### LEFT JOIN (LEFT OUTER JOIN)
Returns all records from left table and matching records from right table.

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
-- Includes employees without departments (NULL department_name)
```

#### RIGHT JOIN (RIGHT OUTER JOIN)
Returns all records from right table and matching records from left table.

```sql
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
-- Includes departments without employees (NULL employee names)
```

#### FULL OUTER JOIN
Returns all records when there's a match in either table.

```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;
-- Includes all employees and all departments
```

#### CROSS JOIN
Returns Cartesian product of both tables.

```sql
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;
-- Every employee paired with every department
```

#### Performance Comparison
1. **INNER JOIN** - Fastest (smallest result set)
2. **LEFT/RIGHT JOIN** - Moderate performance
3. **FULL OUTER JOIN** - Slower (larger result set)
4. **CROSS JOIN** - Slowest (largest result set)

### 3. UNION vs UNION ALL

```sql
-- UNION: Removes duplicates (slower)
SELECT name FROM employees_2021
UNION
SELECT name FROM employees_2022;

-- UNION ALL: Keeps duplicates (faster)
SELECT name FROM employees_2021
UNION ALL
SELECT name FROM employees_2022;
```

**UNION ALL is faster** because it doesn't need to check for and remove duplicates.

### Finding Second Highest Salary

```sql
-- Method 1: Using LIMIT and OFFSET
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Method 2: Using subquery
SELECT MAX(salary) as second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 3: Using ROW_NUMBER()
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 2;
```

### 4. Finding Nth Highest Salary

```sql
-- Generic solution for Nth highest salary
SELECT DISTINCT salary
FROM employees e1
WHERE (
    SELECT COUNT(DISTINCT salary)
    FROM employees e2
    WHERE e2.salary > e1.salary
) = N-1;  -- Replace N with desired position

-- Using DENSE_RANK() for 3rd highest
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
) ranked
WHERE rank = 3;

-- Using LIMIT/OFFSET for 3rd highest
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
```

### 5. Highest Salary in Each Department

```sql
-- Method 1: Using window functions
SELECT department_id, name, salary
FROM (
    SELECT department_id, name, salary,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 1;

-- Method 2: Using correlated subquery
SELECT e1.department_id, e1.name, e1.salary
FROM employees e1
WHERE e1.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

### 6. Employees Who Never Submitted a Report

```sql
-- Using LEFT JOIN
SELECT e.id, e.name
FROM employees e
LEFT JOIN reports r ON e.id = r.employee_id
WHERE r.employee_id IS NULL;

-- Using NOT EXISTS
SELECT e.id, e.name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 FROM reports r WHERE r.employee_id = e.id
);

-- Using NOT IN (careful with NULLs)
SELECT e.id, e.name
FROM employees e
WHERE e.id NOT IN (
    SELECT employee_id FROM reports WHERE employee_id IS NOT NULL
);
```

### 7. Removing Duplicates from a Table

```sql
-- Method 1: Using ROW_NUMBER()
DELETE FROM employees
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (
            PARTITION BY name, email ORDER BY id
        ) as rn
        FROM employees
    ) t
    WHERE rn > 1
);

-- Method 2: Create new table without duplicates
CREATE TABLE employees_clean AS
SELECT DISTINCT * FROM employees;

DROP TABLE employees;
ALTER TABLE employees_clean RENAME TO employees;

-- Method 3: Using temporary table
CREATE TABLE temp_employees AS
SELECT MIN(id) as id, name, email, salary
FROM employees
GROUP BY name, email, salary;

TRUNCATE TABLE employees;
INSERT INTO employees SELECT * FROM temp_employees;
DROP TABLE temp_employees;
```

### 8. Finding Duplicate Rows

```sql
-- Find duplicate records
SELECT name, email, COUNT(*) as duplicate_count
FROM employees
GROUP BY name, email
HAVING COUNT(*) > 1;

-- Show all duplicate rows with details
SELECT e.*
FROM employees e
INNER JOIN (
    SELECT name, email
    FROM employees
    GROUP BY name, email
    HAVING COUNT(*) > 1
) duplicates ON e.name = duplicates.name AND e.email = duplicates.email;
```

### 9. Updating One Table Using Another

```sql
-- Standard UPDATE with JOIN
UPDATE employees e
SET salary = s.new_salary
FROM salary_updates s
WHERE e.id = s.employee_id;

-- Using correlated subquery
UPDATE employees
SET salary = (
    SELECT new_salary
    FROM salary_updates s
    WHERE s.employee_id = employees.id
)
WHERE EXISTS (
    SELECT 1 FROM salary_updates s WHERE s.employee_id = employees.id
);

-- MySQL syntax
UPDATE employees e
INNER JOIN salary_updates s ON e.id = s.employee_id
SET e.salary = s.new_salary;
```

### 10. Filtering NULL Values

```sql
-- Include only non-NULL values
SELECT * FROM employees WHERE phone_number IS NOT NULL;

-- Include only NULL values
SELECT * FROM employees WHERE phone_number IS NULL;

-- Using COALESCE to handle NULLs
SELECT name, COALESCE(phone_number, 'No Phone') as contact
FROM employees;

-- Filtering with functions
SELECT * FROM employees 
WHERE ISNULL(phone_number, '') != '';  -- SQL Server
```

###  11. EXISTS vs IN

```sql
-- EXISTS: Better for large datasets, stops at first match
SELECT * FROM employees e
WHERE EXISTS (
    SELECT 1 FROM departments d 
    WHERE d.id = e.department_id AND d.active = 1
);

-- IN: Better for small, static lists
SELECT * FROM employees
WHERE department_id IN (1, 2, 3, 4);

-- IN with subquery (careful with NULLs)
SELECT * FROM employees
WHERE department_id IN (
    SELECT id FROM departments WHERE active = 1
);
```

**Performance**: EXISTS is generally faster for large datasets because it can short-circuit.

### 12. GROUP BY vs ORDER BY

```sql
-- GROUP BY: Groups rows by specified columns for aggregation
SELECT department_id, COUNT(*), AVG(salary)
FROM employees
GROUP BY department_id;

-- ORDER BY: Sorts the result set
SELECT * FROM employees
ORDER BY salary DESC, name ASC;

-- Combined usage
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
ORDER BY avg_salary DESC;
```

### 13. Aggregate Functions with NULLs

```sql
-- NULL values are ignored by aggregate functions
SELECT 
    COUNT(*) as total_rows,           -- Counts all rows including NULLs
    COUNT(commission) as non_null_comm, -- Counts only non-NULL commissions
    AVG(commission) as avg_commission,  -- Averages only non-NULL values
    SUM(commission) as total_commission -- Sums only non-NULL values
FROM employees;

-- Handling NULLs explicitly
SELECT 
    AVG(COALESCE(commission, 0)) as avg_with_zeros,
    COUNT(CASE WHEN commission IS NOT NULL THEN 1 END) as non_null_count
FROM employees;
```

### 14. Implementing Pagination

```sql
-- Standard LIMIT/OFFSET (PostgreSQL, MySQL)
SELECT * FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;  -- Page 3, 10 records per page

-- SQL Server using OFFSET/FETCH
SELECT * FROM employees
ORDER BY id
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY;

-- ROW_NUMBER() approach (works on all databases)
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY id) as rn
    FROM employees
) t
WHERE rn BETWEEN 21 AND 30;

-- Cursor-based pagination (better performance for large datasets)
SELECT * FROM employees
WHERE id > @last_id  -- Last ID from previous page
ORDER BY id
LIMIT 10;
```

## 2. SQL Commands & Clauses

### 15. DELETE vs TRUNCATE vs DROP

```sql
-- DELETE: Removes specific rows, can be rolled back, fires triggers
DELETE FROM employees WHERE department_id = 5;
DELETE FROM employees;  -- Removes all rows but keeps table structure

-- TRUNCATE: Removes all rows, faster, minimal logging, resets identity
TRUNCATE TABLE employees;  -- Cannot be rolled back in some databases

-- DROP: Removes entire table structure and data
DROP TABLE employees;  -- Table no longer exists
```

| Operation | Speed | Rollback | Triggers | Where Clause | Identity Reset |
|-----------|-------|----------|----------|--------------|----------------|
| DELETE    | Slow  | Yes      | Yes      | Yes          | No             |
| TRUNCATE  | Fast  | Limited  | No       | No           | Yes            |
| DROP      | Fast  | DDL*     | No       | No           | N/A            |

### 16. PRIMARY KEY vs UNIQUE

```sql
-- PRIMARY KEY: Unique + NOT NULL, only one per table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) UNIQUE
);

-- UNIQUE: Allows one NULL value, multiple unique constraints allowed
ALTER TABLE employees ADD CONSTRAINT uk_ssn UNIQUE (ssn);

-- Composite PRIMARY KEY
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
```

### CHECK Constraints

```sql
-- Column-level CHECK constraint
CREATE TABLE employees (
    id INT PRIMARY KEY,
    salary DECIMAL(10,2) CHECK (salary > 0),
    age INT CHECK (age >= 18 AND age <= 65),
    email VARCHAR(100) CHECK (email LIKE '%@%')
);

-- Table-level CHECK constraint
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    discount_price DECIMAL(10,2),
    CONSTRAINT chk_price CHECK (price > 0),
    CONSTRAINT chk_discount CHECK (discount_price <= price)
);

-- Adding CHECK constraint to existing table
ALTER TABLE employees 
ADD CONSTRAINT chk_salary_range 
CHECK (salary BETWEEN 30000 AND 200000);

-- Dropping CHECK constraint
ALTER TABLE employees DROP CONSTRAINT chk_salary_range;
```

### Adding/Removing Columns

```sql
-- Add single column
ALTER TABLE employees ADD COLUMN middle_name VARCHAR(50);

-- Add multiple columns
ALTER TABLE employees 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN updated_at TIMESTAMP;

-- Add column with constraints
ALTER TABLE employees 
ADD COLUMN status VARCHAR(20) DEFAULT 'ACTIVE' 
CHECK (status IN ('ACTIVE', 'INACTIVE', 'TERMINATED'));

-- Drop column
ALTER TABLE employees DROP COLUMN middle_name;

-- Modify column (varies by database)
-- PostgreSQL
ALTER TABLE employees ALTER COLUMN salary TYPE DECIMAL(12,2);

-- MySQL
ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12,2);

-- SQL Server
ALTER TABLE employees ALTER COLUMN salary DECIMAL(12,2);
```

### Subqueries and Correlated Subqueries

```sql
-- Regular subquery (executed once)
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery (executed for each row)
SELECT e1.name, e1.salary, e1.department_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);

-- EXISTS with correlated subquery
SELECT d.name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e WHERE e.department_id = d.id
);

-- Subquery in SELECT clause
SELECT 
    name,
    salary,
    (SELECT AVG(salary) FROM employees) as company_avg,
    salary - (SELECT AVG(salary) FROM employees) as difference
FROM employees;
```

### Common Table Expressions (CTEs)

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
    SELECT department_id, COUNT(*) as emp_count, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
),
high_paying_depts AS (
    SELECT * FROM dept_stats WHERE avg_salary > 80000
)
SELECT d.department_name, hpd.emp_count, hpd.avg_salary
FROM high_paying_depts hpd
JOIN departments d ON hpd.department_id = d.id;

-- Recursive CTE (for hierarchical data)
WITH RECURSIVE employee_hierarchy AS (
    -- Anchor: Find top-level managers
    SELECT id, name, manager_id, 0 as level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive: Find subordinates
    SELECT e.id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy ORDER BY level, name;
```

### VIEW vs TABLE

```sql
-- Creating a VIEW
CREATE VIEW employee_summary AS
SELECT 
    e.name,
    e.salary,
    d.department_name,
    CASE WHEN e.salary > 80000 THEN 'High' ELSE 'Standard' END as salary_grade
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Using the VIEW
SELECT * FROM employee_summary WHERE salary_grade = 'High';

-- Updating through VIEW (if updatable)
UPDATE employee_summary SET salary = 85000 WHERE name = 'John Doe';
```

| Aspect | VIEW | TABLE |
|--------|------|-------|
| Storage | No data stored | Data physically stored |
| Performance | Query executed each time | Direct data access |
| Real-time | Always current | May be outdated |
| Updates | Limited updatability | Full update capability |
| Indexes | Cannot be indexed directly | Can be indexed |

### Materialized Views

```sql
-- Creating a materialized view (PostgreSQL)
CREATE MATERIALIZED VIEW dept_employee_stats AS
SELECT 
    d.department_name,
    COUNT(e.id) as employee_count,
    AVG(e.salary) as avg_salary,
    MAX(e.salary) as max_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.department_name;

-- Refreshing materialized view
REFRESH MATERIALIZED VIEW dept_employee_stats;

-- Concurrent refresh (PostgreSQL)
REFRESH MATERIALIZED VIEW CONCURRENTLY dept_employee_stats;
```

## 3. Indexing & Performance

### What is Indexing?

Indexes are data structures that improve query performance by creating shortcuts to data.

```sql
-- Creating indexes
CREATE INDEX idx_employee_salary ON employees(salary);
CREATE INDEX idx_employee_dept_salary ON employees(department_id, salary);
CREATE UNIQUE INDEX idx_employee_email ON employees(email);

-- Composite index
CREATE INDEX idx_employee_lookup ON employees(department_id, hire_date, salary);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_employees ON employees(salary) WHERE status = 'ACTIVE';

-- Functional index
CREATE INDEX idx_employee_upper_name ON employees(UPPER(name));
```

**When to use indexes:**
- Columns frequently used in WHERE clauses
- Columns used in JOINs
- Columns used in ORDER BY
- Foreign key columns

### Clustered vs Non-Clustered Index

```sql
-- Clustered Index (SQL Server) - physically orders data
CREATE CLUSTERED INDEX idx_employee_id ON employees(id);

-- Non-Clustered Index - points to data locations
CREATE NONCLUSTERED INDEX idx_employee_name ON employees(name);
```

| Type | Data Storage | Per Table | Key Lookup |
|------|-------------|-----------|------------|
| Clustered | Data pages ordered by index | Only 1 | Direct |
| Non-Clustered | Separate index structure | Multiple | Additional lookup |

### Index Impact on DML Operations

```sql
-- Indexes slow down INSERT/UPDATE/DELETE
-- Each index must be maintained when data changes

-- Before adding indexes - measure performance
INSERT INTO employees (name, salary, department_id) 
VALUES ('New Employee', 50000, 1);

-- After adding indexes - slower INSERTs but faster SELECTs
-- Consider dropping indexes for bulk operations
DROP INDEX idx_employee_salary;
-- Bulk insert operations
-- Recreate index
CREATE INDEX idx_employee_salary ON employees(salary);
```

### Query Optimization

```sql
-- Use EXPLAIN to analyze queries
EXPLAIN SELECT * FROM employees WHERE salary > 50000;

-- Optimize with proper indexing
CREATE INDEX idx_salary ON employees(salary);

-- Use covering indexes
CREATE INDEX idx_covering ON employees(department_id, salary, name);
SELECT name FROM employees WHERE department_id = 1 ORDER BY salary;

-- Avoid functions in WHERE clauses
-- Bad: WHERE YEAR(hire_date) = 2023
-- Good: WHERE hire_date >= '2023-01-01' AND hire_date < '2024-01-01'

-- Use LIMIT for large result sets
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;

-- Optimize JOINs
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.id  -- Ensure both columns are indexed
WHERE e.salary > 50000;  -- Filter early
```

### Database Optimizer

The query optimizer chooses the best execution plan:

```sql
-- View execution plan
EXPLAIN (ANALYZE, BUFFERS) 
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.salary > 50000;

-- Update table statistics for better optimization
ANALYZE employees;
ANALYZE departments;

-- Force index usage (when necessary)
SELECT * FROM employees USE INDEX (idx_salary) WHERE salary > 50000;
```

### EXPLAIN PLAN Analysis

```sql
-- PostgreSQL EXPLAIN
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT * FROM employees WHERE salary > 50000;

-- Key metrics to look for:
-- 1. Seq Scan vs Index Scan
-- 2. Cost estimates
-- 3. Actual vs estimated rows
-- 4. Buffer usage
-- 5. Execution time
```

## 4. Transactions & Concurrency

### ACID Properties

```sql
-- ATOMICITY: All or nothing
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- Either both succeed or both fail
COMMIT;

-- CONSISTENCY: Database rules maintained
-- CHECK constraints, foreign keys ensure consistency

-- ISOLATION: Concurrent transactions don't interfere
-- Controlled by isolation levels

-- DURABILITY: Committed changes persist
-- Handled by database engine (WAL, etc.)
```

### Transaction Management

```sql
-- Basic transaction
BEGIN TRANSACTION;
INSERT INTO orders (customer_id, total) VALUES (1, 100.00);
INSERT INTO order_items (order_id, product_id, quantity) VALUES (LAST_INSERT_ID(), 1, 2);
COMMIT;

-- Transaction with error handling
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE inventory SET quantity = quantity - 5 WHERE product_id = 1;
    INSERT INTO sales (product_id, quantity) VALUES (1, 5);
    COMMIT;
END TRY
BEGIN CATCH
    ROLLBACK;
    THROW;
END CATCH;

-- Savepoints
BEGIN TRANSACTION;
INSERT INTO audit_log (action) VALUES ('Start process');
SAVEPOINT sp1;
UPDATE products SET price = price * 1.1;
SAVEPOINT sp2;
DELETE FROM products WHERE discontinued = 1;
-- If error occurs, can rollback to sp2 or sp1
ROLLBACK TO sp2;
COMMIT;
```

### Isolation Levels

```sql
-- READ UNCOMMITTED: Lowest isolation, allows dirty reads
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

-- READ COMMITTED: Prevents dirty reads
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- REPEATABLE READ: Prevents dirty and non-repeatable reads
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- SERIALIZABLE: Highest isolation, prevents all phenomena
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### Concurrency Issues

```sql
-- Dirty Read: Reading uncommitted data
-- Transaction 1:
BEGIN TRANSACTION;
UPDATE products SET price = 200 WHERE id = 1;
-- Transaction 2 reads price = 200 (uncommitted)
ROLLBACK;  -- Price returns to original value

-- Non-repeatable Read: Same query returns different results
-- Transaction 1:
BEGIN TRANSACTION;
SELECT price FROM products WHERE id = 1;  -- Returns 100
-- Transaction 2 updates price to 150 and commits
SELECT price FROM products WHERE id = 1;  -- Returns 150
COMMIT;

-- Phantom Read: New rows appear in result set
-- Transaction 1:
BEGIN TRANSACTION;
SELECT COUNT(*) FROM products WHERE category = 'Electronics';  -- Returns 5
-- Transaction 2 inserts new Electronics product and commits
SELECT COUNT(*) FROM products WHERE category = 'Electronics';  -- Returns 6
COMMIT;
```

### Preventing Deadlocks

```sql
-- Deadlock prevention strategies:

-- 1. Consistent locking order
-- Always acquire locks in same order (e.g., by primary key)
BEGIN TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;  -- Lock account 1 first
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;  -- Then account 2
-- Perform operations
COMMIT;

-- 2. Use shorter transactions
BEGIN TRANSACTION;
-- Minimize time between BEGIN and COMMIT
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 3. Use appropriate isolation levels
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 4. Implement retry logic in application
-- DEADLOCK_RETRY:
-- BEGIN TRANSACTION;
-- ... operations ...
-- ON DEADLOCK: ROLLBACK; wait random time; GOTO DEADLOCK_RETRY;
```

### Locking Strategies

```sql
-- Pessimistic Locking: Lock before reading
BEGIN TRANSACTION;
SELECT * FROM products WHERE id = 1 FOR UPDATE;  -- Exclusive lock
-- Other transactions wait
UPDATE products SET quantity = quantity - 1 WHERE id = 1;
COMMIT;

-- Optimistic Locking: Check version before update
-- Add version column to table
SELECT id, name, price, version FROM products WHERE id = 1;
-- Application logic: user modifies data
UPDATE products 
SET name = 'New Name', price = 150, version = version + 1 
WHERE id = 1 AND version = @original_version;
-- Check if @@ROWCOUNT = 1, if not, record was modified by another user
```

## 5. Database Design & Integrity

### Normalization

#### First Normal Form (1NF)
- Eliminate repeating groups
- Each cell contains atomic values

```sql
-- Violates 1NF (multiple phones in one column)
CREATE TABLE employees_bad (
    id INT,
    name VARCHAR(100),
    phones VARCHAR(200)  -- "123-456-7890, 098-765-4321"
);

-- 1NF compliant
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employee_phones (
    employee_id INT,
    phone VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
```

#### Second Normal Form (2NF)
- Must be in 1NF
- No partial dependencies on composite primary key

```sql
-- Violates 2NF
CREATE TABLE order_items_bad (
    order_id INT,
    product_id INT,
    quantity INT,
    product_name VARCHAR(100),  -- Depends only on product_id
    product_price DECIMAL(10,2), -- Depends only on product_id
    PRIMARY KEY (order_id, product_id)
);

-- 2NF compliant
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

#### Third Normal Form (3NF)
- Must be in 2NF
- No transitive dependencies

```sql
-- Violates 3NF
CREATE TABLE employees_bad (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    department_name VARCHAR(100),  -- Transitively dependent on department_id
    department_location VARCHAR(100)  -- Transitively dependent on department_id
);

-- 3NF compliant
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

### Denormalization

Used for performance optimization, introducing controlled redundancy:

```sql
-- Normalized (3NF)
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2)
);

-- Denormalized for performance
CREATE TABLE orders_denormalized (
    id INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),  -- Denormalized from customers table
    order_date DATE,
    total_amount DECIMAL(10,2),  -- Calculated field
    item_count INT               -- Calculated field
);
```

### Foreign Keys and Referential Integrity

```sql
-- Basic foreign key
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Foreign key with actions
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
        ON DELETE SET NULL        -- Set to NULL when department deleted
        ON UPDATE CASCADE        -- Update when department ID changes
);

-- Composite foreign key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    line_number INT,
    quantity INT,
    FOREIGN KEY (order_id, line_number) REFERENCES order_lines(order_id, line_number)
);
```

### ER Model Components

```sql
-- Entity: Real-world object
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Attributes: Properties of entities
-- Simple: name, email
-- Composite: address (street, city, state, zip)
-- Derived: age (calculated from birth_date)

CREATE TABLE customers_detailed (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    street VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip VARCHAR(10),
    -- Derived attribute (calculated)
    age AS (YEAR(CURRENT_DATE) - YEAR(birth_date))
);

-- Relationships: Associations between entities
-- One-to-Many
CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Many-to-Many (using junction table)
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE courses (id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### Surrogate Keys

```sql
-- Natural key (business meaningful)
CREATE TABLE products (
    sku VARCHAR(20) PRIMARY KEY,  -- Natural key
    name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Surrogate key (system generated)
CREATE TABLE products (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- Surrogate key
    sku VARCHAR(20) UNIQUE,            -- Natural key as unique constraint
    name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Benefits of surrogate keys:
-- 1. Immutable
-- 2. No business logic
-- 3. Better performance (integers)
-- 4. Easier foreign key relationships
```

### Composite Keys

```sql
-- Composite primary key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)
);

-- Composite unique key
CREATE TABLE employee_skills (
    id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    skill_id INT,
    proficiency_level INT,
    UNIQUE (employee_id, skill_id),  -- Composite unique constraint
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);
```

### Schema vs Instance

```sql
-- Schema: Structure/definition of database
CREATE SCHEMA hr;

CREATE TABLE hr.employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Instance: Actual data at a point in time
INSERT INTO hr.employees VALUES 
(1, 'John Doe', 75000),
(2, 'Jane Smith', 82000);

-- Schema remains same, instance changes with DML operations
```

### Referential Integrity

```sql
-- Referential integrity ensures foreign key values exist in referenced table
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    CONSTRAINT fk_emp_dept 
        FOREIGN KEY (department_id) REFERENCES departments(id)
        ON DELETE RESTRICT  -- Prevents deletion if referenced
        ON UPDATE CASCADE   -- Updates cascade to dependent records
);

-- Checking referential integrity
-- Find orphaned records
SELECT e.* 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.id 
WHERE d.id IS NULL AND e.department_id IS NOT NULL;

-- Enable/disable referential integrity checks
ALTER TABLE employees NOCHECK CONSTRAINT fk_emp_dept;  -- Disable
ALTER TABLE employees CHECK CONSTRAINT fk_emp_dept;     -- Enable
```

## 6. Stored Objects (Views, Procedures, Triggers)

### Views in SQL

```sql
-- Simple view
CREATE VIEW active_employees AS
SELECT id, name, email, hire_date
FROM employees
WHERE status = 'ACTIVE';

-- Complex view with joins and calculations
CREATE VIEW employee_details AS
SELECT 
    e.id,
    e.name,
    e.salary,
    d.department_name,
    e.salary * 12 as annual_salary,
    CASE 
        WHEN e.salary > 100000 THEN 'Senior'
        WHEN e.salary > 50000 THEN 'Mid-level'
        ELSE 'Junior'
    END as level
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.status = 'ACTIVE';

-- Updatable view
CREATE VIEW manager_employees AS
SELECT id, name, salary, department_id
FROM employees
WHERE position = 'Manager'
WITH CHECK OPTION;  -- Ensures updates maintain view conditions

-- Update through view
UPDATE manager_employees SET salary = 95000 WHERE id = 1;

-- View with security
CREATE VIEW public_employee_info AS
SELECT id, name, department_id, hire_date
FROM employees;
-- Doesn't expose salary information
```

### Materialized Views

```sql
-- Create materialized view (PostgreSQL)
CREATE MATERIALIZED VIEW sales_summary AS
SELECT 
    DATE_TRUNC('month', order_date) as month,
    SUM(total_amount) as total_sales,
    COUNT(*) as order_count,
    AVG(total_amount) as avg_order_value
FROM orders
WHERE order_date >= '2023-01-01'
GROUP BY DATE_TRUNC('month', order_date);

-- Create indexes on materialized view
CREATE INDEX idx_sales_summary_month ON sales_summary(month);

-- Refresh strategies
REFRESH MATERIALIZED VIEW sales_summary;  -- Full refresh
REFRESH MATERIALIZED VIEW CONCURRENTLY sales_summary;  -- Non-blocking

-- Automatic refresh (using triggers or scheduled jobs)
CREATE OR REPLACE FUNCTION refresh_sales_summary()
RETURNS TRIGGER AS $
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY sales_summary;
    RETURN NULL;
END;
$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_refresh_sales
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_sales_summary();
```

### Stored Procedures

```sql
-- Basic stored procedure (SQL Server)
CREATE PROCEDURE GetEmployeesByDepartment
    @DepartmentId INT,
    @MinSalary DECIMAL(10,2) = 0
AS
BEGIN
    SELECT id, name, salary, hire_date
    FROM employees
    WHERE department_id = @DepartmentId
    AND salary >= @MinSalary
    ORDER BY salary DESC;
END;

-- Execute procedure
EXEC GetEmployeesByDepartment @DepartmentId = 1, @MinSalary = 50000;

-- Procedure with output parameters
CREATE PROCEDURE GetDepartmentStats
    @DepartmentId INT,
    @EmployeeCount INT OUTPUT,
    @AverageSalary DECIMAL(10,2) OUTPUT
AS
BEGIN
    SELECT 
        @EmployeeCount = COUNT(*),
        @AverageSalary = AVG(salary)
    FROM employees
    WHERE department_id = @DepartmentId;
END;

-- Execute with output parameters
DECLARE @Count INT, @AvgSal DECIMAL(10,2);
EXEC GetDepartmentStats 1, @Count OUTPUT, @AvgSal OUTPUT;
SELECT @Count as EmployeeCount, @AvgSal as AverageSalary;

-- Complex procedure with error handling
CREATE PROCEDURE TransferEmployee
    @EmployeeId INT,
    @NewDepartmentId INT,
    @EffectiveDate DATE
AS
BEGIN
    BEGIN TRANSACTION;
    BEGIN TRY
        -- Validate employee exists
        IF NOT EXISTS (SELECT 1 FROM employees WHERE id = @EmployeeId)
            THROW 50001, 'Employee not found', 1;
        
        -- Validate department exists
        IF NOT EXISTS (SELECT 1 FROM departments WHERE id = @NewDepartmentId)
            THROW 50002, 'Department not found', 1;
        
        -- Insert transfer record
        INSERT INTO employee_transfers (employee_id, old_department_id, new_department_id, transfer_date)
        SELECT @EmployeeId, department_id, @NewDepartmentId, @EffectiveDate
        FROM employees WHERE id = @EmployeeId;
        
        -- Update employee department
        UPDATE employees 
        SET department_id = @NewDepartmentId, updated_at = GETDATE()
        WHERE id = @EmployeeId;
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
```

### Triggers

```sql
-- AFTER INSERT trigger
CREATE TRIGGER tr_employee_audit_insert
ON employees
AFTER INSERT
AS
BEGIN
    INSERT INTO audit_log (table_name, operation, record_id, changed_by, change_date)
    SELECT 'employees', 'INSERT', i.id, SYSTEM_USER, GETDATE()
    FROM inserted i;
END;

-- AFTER UPDATE trigger
CREATE TRIGGER tr_employee_audit_update
ON employees
AFTER UPDATE
AS
BEGIN
    INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, changed_by, change_date)
    SELECT 
        'employees', 
        'UPDATE', 
        i.id,
        CONCAT('salary:', d.salary, '; dept:', d.department_id),
        CONCAT('salary:', i.salary, '; dept:', i.department_id),
        SYSTEM_USER, 
        GETDATE()
    FROM inserted i
    JOIN deleted d ON i.id = d.id;
END;

-- BEFORE INSERT trigger (MySQL)
DELIMITER //
CREATE TRIGGER tr_employee_before_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    -- Auto-generate employee code
    SET NEW.employee_code = CONCAT('EMP', LPAD(NEW.id, 6, '0'));
    
    -- Set default values
    IF NEW.hire_date IS NULL THEN
        SET NEW.hire_date = CURDATE();
    END IF;
    
    -- Validation
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Salary cannot be negative';
    END IF;
END;
//
DELIMITER ;

-- INSTEAD OF trigger (for views)
CREATE TRIGGER tr_employee_view_insert
ON employee_summary_view
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO employees (name, salary, department_id)
    SELECT name, salary, department_id
    FROM inserted;
    
    -- Additional logic for related tables
    INSERT INTO employee_status (employee_id, status, status_date)
    SELECT 
        (SELECT id FROM employees WHERE name = i.name), 
        'ACTIVE', 
        GETDATE()
    FROM inserted i;
END;
```

### Triggers vs Procedures

| Aspect | Triggers | Stored Procedures |
|--------|----------|-------------------|
| Execution | Automatic (on DML events) | Manual (called explicitly) |
| Parameters | No parameters | Can have parameters |
| Return Values | Cannot return values | Can return values |
| Transactions | Part of triggering transaction | Can control own transactions |
| Use Cases | Auditing, validation, auto-updates | Business logic, complex operations |

### Pros and Cons of Stored Procedures

**Pros:**
- Better performance (compiled, cached)
- Centralized business logic
- Enhanced security (parameterized)
- Reduced network traffic
- Transaction control

**Cons:**
- Database-specific (less portable)
- Harder to version control
- Limited debugging tools
- Can create tight coupling
- Scalability challenges

```sql
-- Example showing benefits
-- Without stored procedure (multiple round trips)
-- 1. SELECT to check balance
-- 2. INSERT transaction record
-- 3. UPDATE balance
-- 4. INSERT audit log

-- With stored procedure (single call)
CREATE PROCEDURE ProcessPayment
    @AccountId INT,
    @Amount DECIMAL(10,2),
    @Description VARCHAR(100)
AS
BEGIN
    BEGIN TRANSACTION;
    -- All operations in single atomic unit
    -- Reduced network traffic
    -- Centralized validation logic
    COMMIT;
END;
```

## 7. Advanced & Practical Scenarios

### E-commerce Database Design

```sql
-- Core entities
CREATE TABLE customers (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE(),
    is_active BIT DEFAULT 1
);

CREATE TABLE addresses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    type VARCHAR(20) CHECK (type IN ('billing', 'shipping')) NOT NULL,
    street_address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    is_default BIT DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE categories (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    parent_id INT,
    description TEXT,
    is_active BIT DEFAULT 1,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);

CREATE TABLE products (
    id INT IDENTITY(1,1) PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    cost DECIMAL(10,2) CHECK (cost >= 0),
    weight DECIMAL(8,2),
    dimensions VARCHAR(50),
    is_active BIT DEFAULT 1,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE inventory (
    id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT NOT NULL,
    warehouse_location VARCHAR(100),
    quantity_available INT NOT NULL DEFAULT 0,
    quantity_reserved INT NOT NULL DEFAULT 0,
    reorder_point INT DEFAULT 10,
    max_stock_level INT,
    last_restocked DATETIME2,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE orders (
    id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    order_number VARCHAR(50) UNIQUE NOT NULL,
    status VARCHAR(20) CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')) DEFAULT 'pending',
    order_date DATETIME2 DEFAULT GETDATE(),
    shipped_date DATETIME2,
    delivered_date DATETIME2,
    subtotal DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    shipping_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    discount_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    total_amount DECIMAL(10,2) NOT NULL,
    billing_address_id INT,
    shipping_address_id INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20) DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (billing_address_id) REFERENCES addresses(id),
    FOREIGN KEY (shipping_address_id) REFERENCES addresses(id)
);

CREATE TABLE order_items (
    id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    total_price AS (quantity * unit_price) PERSISTED,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Shopping cart for session management
CREATE TABLE cart_items (
    id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    session_id VARCHAR(255),
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    added_at DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Reviews and ratings
CREATE TABLE product_reviews (
    id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(255),
    review_text TEXT,
    is_verified_purchase BIT DEFAULT 0,
    created_at DATETIME2 DEFAULT GETDATE(),
    is_approved BIT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    UNIQUE (product_id, customer_id)  -- One review per customer per product
);

-- Coupons and promotions
CREATE TABLE coupons (
    id INT IDENTITY(1,1) PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255),
    discount_type VARCHAR(20) CHECK (discount_type IN ('percentage', 'fixed_amount')),
    discount_value DECIMAL(10,2),
    min_order_amount DECIMAL(10,2) DEFAULT 0,
    max_discount_amount DECIMAL(10,2),
    start_date DATETIME2,
    end_date DATETIME2,
    usage_limit INT,
    used_count INT DEFAULT 0,
    is_active BIT DEFAULT 1
);
```

### Schema Migrations

```sql
-- Migration versioning table
CREATE TABLE schema_migrations (
    version VARCHAR(50) PRIMARY KEY,
    description VARCHAR(255),
    applied_at DATETIME2 DEFAULT GETDATE(),
    applied_by VARCHAR(100) DEFAULT SYSTEM_USER
);

-- Migration script example
-- Migration: 20231201_001_add_customer_loyalty_program.sql
BEGIN TRANSACTION;

-- Check if migration already applied
IF NOT EXISTS (SELECT 1 FROM schema_migrations WHERE version = '20231201_001')
BEGIN
    -- Add loyalty program tables
    CREATE TABLE loyalty_programs (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        points_per_dollar DECIMAL(5,2) DEFAULT 1.0,
        redemption_rate DECIMAL(5,2) DEFAULT 0.01,
        is_active BIT DEFAULT 1
    );
    
    CREATE TABLE customer_loyalty (
        customer_id INT PRIMARY KEY,
        program_id INT NOT NULL,
        points_balance INT DEFAULT 0,
        points_lifetime INT DEFAULT 0,
        tier_level VARCHAR(20) DEFAULT 'Bronze',
        joined_date DATETIME2 DEFAULT GETDATE(),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (program_id) REFERENCES loyalty_programs(id)
    );
    
    -- Add new column to existing table
    ALTER TABLE orders ADD loyalty_points_earned INT DEFAULT 0;
    ALTER TABLE orders ADD loyalty_points_redeemed INT DEFAULT 0;
    
    -- Create indexes
    CREATE INDEX idx_customer_loyalty_points ON customer_loyalty(points_balance);
    CREATE INDEX idx_orders_loyalty_points ON orders(loyalty_points_earned);
    
    -- Insert default loyalty program
    INSERT INTO loyalty_programs (name, points_per_dollar, redemption_rate)
    VALUES ('Standard Program', 1.0, 0.01);
    
    -- Record migration
    INSERT INTO schema_migrations (version, description)
    VALUES ('20231201_001', 'Add customer loyalty program tables and columns');
    
    PRINT 'Migration 20231201_001 applied successfully';
END
ELSE
BEGIN
    PRINT 'Migration 20231201_001 already applied, skipping';
END

COMMIT TRANSACTION;

-- Rollback script (separate file)
-- Rollback: 20231201_001_rollback_add_customer_loyalty_program.sql
BEGIN TRANSACTION;

-- Remove added columns
ALTER TABLE orders DROP COLUMN loyalty_points_earned;
ALTER TABLE orders DROP COLUMN loyalty_points_redeemed;

-- Drop tables (in reverse order due to foreign keys)
DROP TABLE customer_loyalty;
DROP TABLE loyalty_programs;

-- Remove migration record
DELETE FROM schema_migrations WHERE version = '20231201_001';

COMMIT TRANSACTION;
```

### Database Backup and Restore

```sql
-- Full database backup (SQL Server)
BACKUP DATABASE ECommerceDB 
TO DISK = 'C:\Backups\ECommerceDB_Full_20231201.bak'
WITH FORMAT, COMPRESSION, CHECKSUM;

-- Differential backup
BACKUP DATABASE ECommerceDB 
TO DISK = 'C:\Backups\ECommerceDB_Diff_20231201.bak'
WITH DIFFERENTIAL, COMPRESSION, CHECKSUM;

-- Transaction log backup
BACKUP LOG ECommerceDB 
TO DISK = 'C:\Backups\ECommerceDB_Log_20231201.trn';

-- Automated backup script
CREATE PROCEDURE sp_BackupDatabase
    @DatabaseName NVARCHAR(128),
    @BackupPath NVARCHAR(500),
    @BackupType VARCHAR(20) = 'FULL'  -- FULL, DIFF, LOG
AS
BEGIN
    DECLARE @FileName NVARCHAR(500);
    DECLARE @Timestamp VARCHAR(20) = FORMAT(GETDATE(), 'yyyyMMdd_HHmmss');
    
    SET @FileName = @BackupPath + @DatabaseName + '_' + @BackupType + '_' + @Timestamp + 
                   CASE @BackupType 
                       WHEN 'LOG' THEN '.trn' 
                       ELSE '.bak' 
                   END;
    
    IF @BackupType = 'FULL'
        BACKUP DATABASE @DatabaseName TO DISK = @FileName WITH COMPRESSION, CHECKSUM;
    ELSE IF @BackupType = 'DIFF'
        BACKUP DATABASE @DatabaseName TO DISK = @FileName WITH DIFFERENTIAL, COMPRESSION, CHECKSUM;
    ELSE IF @BackupType = 'LOG'
        BACKUP LOG @DatabaseName TO DISK = @FileName;
        
    PRINT 'Backup completed: ' + @FileName;
END;

-- Restore database
RESTORE DATABASE ECommerceDB_Test 
FROM DISK = 'C:\Backups\ECommerceDB_Full_20231201.bak'
WITH MOVE 'ECommerceDB' TO 'C:\Data\ECommerceDB_Test.mdf',
     MOVE 'ECommerceDB_Log' TO 'C:\Data\ECommerceDB_Test.ldf',
     REPLACE;
```

### Audit Logging and Change Tracking

```sql
-- Audit table design
CREATE TABLE audit_log (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    operation VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
    record_id VARCHAR(50),
    old_values NVARCHAR(MAX),  -- JSON format
    new_values NVARCHAR(MAX),  -- JSON format
    changed_by VARCHAR(100) NOT NULL,
    changed_at DATETIME2 DEFAULT GETDATE(),
    ip_address VARCHAR(45),
    user_agent VARCHAR(500),
    session_id VARCHAR(100)
);

-- Generic audit trigger
CREATE TRIGGER tr_audit_products
ON products
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @operation VARCHAR(10);
    
    IF EXISTS (SELECT * FROM inserted) AND EXISTS (SELECT * FROM deleted)
        SET @operation = 'UPDATE';
    ELSE IF EXISTS (SELECT * FROM inserted)
        SET @operation = 'INSERT';
    ELSE
        SET @operation = 'DELETE';
    
    -- For INSERT operations
    IF @operation = 'INSERT'
    BEGIN
        INSERT INTO audit_log (table_name, operation, record_id, new_values, changed_by)
        SELECT 
            'products',
            'INSERT',
            CAST(i.id AS VARCHAR(50)),
            (SELECT i.* FOR JSON PATH, WITHOUT_ARRAY_WRAPPER),
            SYSTEM_USER
        FROM inserted i;
    END
    
    -- For UPDATE operations
    IF @operation = 'UPDATE'
    BEGIN
        INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, changed_by)
        SELECT 
            'products',
            'UPDATE',
            CAST(i.id AS VARCHAR(50)),
            (SELECT d.* FOR JSON PATH, WITHOUT_ARRAY_WRAPPER),
            (SELECT i.* FOR JSON PATH, WITHOUT_ARRAY_WRAPPER),
            SYSTEM_USER
        FROM inserted i
        JOIN deleted d ON i.id = d.id;
    END
    
    -- For DELETE operations
    IF @operation = 'DELETE'
    BEGIN
        INSERT INTO audit_log (table_name, operation, record_id, old_values, changed_by)
        SELECT 
            'products',
            'DELETE',
            CAST(d.id AS VARCHAR(50)),
            (SELECT d.* FOR JSON PATH, WITHOUT_ARRAY_WRAPPER),
            SYSTEM_USER
        FROM deleted d;
    END
END;

-- Query audit history
SELECT 
    table_name,
    operation,
    record_id,
    changed_by,
    changed_at,
    JSON_VALUE(old_values, '$.name') as old_name,
    JSON_VALUE(new_values, '$.name') as new_name
FROM audit_log
WHERE table_name = 'products' 
    AND record_id = '123'
ORDER BY changed_at DESC;
```

### Soft Delete Implementation

```sql
-- Add soft delete columns to tables
ALTER TABLE products ADD is_deleted BIT DEFAULT 0;
ALTER TABLE products ADD deleted_at DATETIME2;
ALTER TABLE products ADD deleted_by VARCHAR(100);

-- Soft delete procedure
CREATE PROCEDURE sp_SoftDeleteProduct
    @ProductId INT,
    @DeletedBy VARCHAR(100)
AS
BEGIN
    UPDATE products
    SET is_deleted = 1,
        deleted_at = GETDATE(),
        deleted_by = @DeletedBy,
        is_active = 0
    WHERE id = @ProductId;
    
    -- Audit the soft delete
    INSERT INTO audit_log (table_name, operation, record_id, changed_by)
    VALUES ('products', 'SOFT_DELETE', @ProductId, @DeletedBy);
END;

-- Views to hide soft-deleted records
CREATE VIEW active_products AS
SELECT * FROM products WHERE is_deleted = 0;

-- Restore soft-deleted record
CREATE PROCEDURE sp_RestoreProduct
    @ProductId INT,
    @RestoredBy VARCHAR(100)
AS
BEGIN
    UPDATE products
    SET is_deleted = 0,
        deleted_at = NULL,
        deleted_by = NULL,
        is_active = 1
    WHERE id = @ProductId;
    
    INSERT INTO audit_log (table_name, operation, record_id, changed_by)
    VALUES ('products', 'RESTORE', @ProductId, @RestoredBy);
END;

-- Permanent delete (after retention period)
CREATE PROCEDURE sp_PermanentDeleteOldRecords
    @TableName VARCHAR(100),
    @RetentionDays INT = 2555  -- 7 years default
AS
BEGIN
    DECLARE @SQL NVARCHAR(MAX);
    DECLARE @CutoffDate DATETIME2 = DATEADD(DAY, -@RetentionDays, GETDATE());
    
    SET @SQL = 'DELETE FROM ' + QUOTENAME(@TableName) + 
               ' WHERE is_deleted = 1 AND deleted_at < @CutoffDate';
    
    EXEC sp_executesql @SQL, N'@CutoffDate DATETIME2', @CutoffDate;
END;
```

### Data Consistency Across Microservices

```sql
-- Outbox pattern for eventual consistency
CREATE TABLE outbox_events (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    aggregate_id VARCHAR(100) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    event_data NVARCHAR(MAX) NOT NULL,  -- JSON payload
    created_at DATETIME2 DEFAULT GETDATE(),
    processed_at DATETIME2,
    retry_count INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'PENDING'  -- PENDING, PROCESSED, FAILED
);

-- Saga pattern for distributed transactions
CREATE TABLE saga_orchestrator (
    id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    saga_type VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'STARTED',  -- STARTED, COMPLETED, FAILED, COMPENSATING
    current_step INT DEFAULT 1,
    context_data NVARCHAR(MAX),  -- JSON with saga state
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE saga_steps (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    saga_id UNIQUEIDENTIFIER NOT NULL,
    step_number INT NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    operation VARCHAR(100) NOT NULL,
    compensation_operation VARCHAR(100),
    request_data NVARCHAR(MAX),
    response_data NVARCHAR(MAX),
    status VARCHAR(20) DEFAULT 'PENDING',
    executed_at DATETIME2,
    compensated_at DATETIME2,
    FOREIGN KEY (saga_id) REFERENCES saga_orchestrator(id)
);

-- Example: Order processing saga
CREATE PROCEDURE sp_StartOrderSaga
    @OrderId INT,
    @CustomerId INT,
    @TotalAmount DECIMAL(10,2)
AS
BEGIN
    DECLARE @SagaId UNIQUEIDENTIFIER = NEWID();
    DECLARE @ContextData NVARCHAR(MAX) = JSON_OBJECT(
        'orderId', @OrderId,
        'customerId', @CustomerId,
        'totalAmount', @TotalAmount
    );
    
    BEGIN TRANSACTION;
    
    -- Create saga orchestrator record
    INSERT INTO saga_orchestrator (id, saga_type, context_data)
    VALUES (@SagaId, 'OrderProcessing', @ContextData);
    
    -- Define saga steps
    INSERT INTO saga_steps (saga_id, step_number, service_name, operation, compensation_operation, request_data)
    VALUES 
    (@SagaId, 1, 'PaymentService', 'ProcessPayment', 'RefundPayment', 
     JSON_OBJECT('customerId', @CustomerId, 'amount', @TotalAmount)),
    (@SagaId, 2, 'InventoryService', 'ReserveItems', 'ReleaseItems',
     JSON_OBJECT('orderId', @OrderId)),
    (@SagaId, 3, 'ShippingService', 'CreateShipment', 'CancelShipment',
     JSON_OBJECT('orderId', @OrderId)),
    (@SagaId, 4, 'OrderService', 'ConfirmOrder', 'CancelOrder',
     JSON_OBJECT('orderId', @OrderId));
    
    COMMIT TRANSACTION;
    
    SELECT @SagaId as SagaId;
END;

-- Compensation handling
CREATE PROCEDURE sp_CompensateSaga
    @SagaId UNIQUEIDENTIFIER
AS
BEGIN
    -- Mark saga as compensating
    UPDATE saga_orchestrator 
    SET status = 'COMPENSATING', updated_at = GETDATE()
    WHERE id = @SagaId;
    
    -- Execute compensation operations in reverse order
    DECLARE step_cursor CURSOR FOR
    SELECT step_number, service_name, compensation_operation, request_data
    FROM saga_steps
    WHERE saga_id = @SagaId AND status = 'COMPLETED'
    ORDER BY step_number DESC;
    
    -- Process each compensation step
    -- (Implementation would involve calling external services)
END;

-- Event sourcing pattern
CREATE TABLE event_store (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    stream_id VARCHAR(100) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    event_data NVARCHAR(MAX) NOT NULL,
    metadata NVARCHAR(MAX),
    version INT NOT NULL,
    timestamp DATETIME2 DEFAULT GETDATE(),
    INDEX idx_stream_version (stream_id, version)
);

-- Projections for read models
CREATE TABLE order_projection (
    order_id INT PRIMARY KEY,
    customer_id INT,
    status VARCHAR(50),
    total_amount DECIMAL(10,2),
    created_at DATETIME2,
    last_updated DATETIME2
);

-- Event replay for projections
CREATE PROCEDURE sp_RebuildOrderProjection
    @OrderId INT
AS
BEGIN
    DELETE FROM order_projection WHERE order_id = @OrderId;
    
    DECLARE event_cursor CURSOR FOR
    SELECT event_type, event_data, timestamp
    FROM event_store
    WHERE stream_id = 'order-' + CAST(@OrderId AS VARCHAR(10))
    ORDER BY version;
    
    -- Process each event to rebuild projection
    -- (Implementation specific to event types)
END;
```

This comprehensive SQL guide covers all the essential concepts from basic queries to advanced database design patterns. Each section includes practical examples and real-world scenarios that you'll encounter in production environments. The examples demonstrate best practices for performance, security, and maintainability while showing how different SQL concepts work together to create robust database