# SQL Coding Questions and Answers

## Basic SQL Coding Questions

1. **Write an SQL query to fetch the second-highest salary from an `Employee` table.**
```sql
SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

2. **Write an SQL query to get the duplicate records from a table.**
```sql
SELECT column1, column2, COUNT(*) 
FROM table_name 
GROUP BY column1, column2 
HAVING COUNT(*) > 1;
```

3. **Write a query to find the employees who earn more than their managers.**
```sql
SELECT e.*
FROM Employee e
JOIN Employee m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

4. **Write an SQL query to retrieve the top `N` records from a table.**
```sql
SELECT * 
FROM table_name 
ORDER BY column_name DESC 
LIMIT N;
```

5. **Write an SQL query to count the number of employees in each department.**
```sql
SELECT department_id, COUNT(*) AS num_employees 
FROM Employee 
GROUP BY department_id;
```

6. **Write a query to find the department with the highest number of employees.**
```sql
SELECT department_id, COUNT(*) AS num_employees 
FROM Employee 
GROUP BY department_id 
ORDER BY num_employees DESC 
LIMIT 1;
```

7. **Write a query to retrieve employees who have the same salary.**
```sql
SELECT *
FROM Employee e1
WHERE EXISTS (
    SELECT 1 FROM Employee e2
    WHERE e1.salary = e2.salary AND e1.id != e2.id
);
```

8. **Write an SQL query to list all employees whose name starts with 'A'.**
```sql
SELECT * 
FROM Employee 
WHERE name LIKE 'A%';
```

9. **Write an SQL query to get the last record from a table.**
```sql
SELECT * 
FROM table_name 
ORDER BY id DESC 
LIMIT 1;
```

10. **Write a query to get employees who joined in the last 6 months.**
```sql
SELECT * 
FROM Employee 
WHERE join_date >= CURRENT_DATE - INTERVAL 6 MONTH;
```

---

## Intermediate SQL Coding Questions

11. **Write an SQL query to find the `Nth` highest salary from a table.**
```sql
SELECT DISTINCT salary 
FROM Employee e1 
WHERE N - 1 = (
    SELECT COUNT(DISTINCT salary) 
    FROM Employee e2 
    WHERE e2.salary > e1.salary
);
```

12. **Write a query to remove duplicate rows from a table without using `DISTINCT`.**
```sql
DELETE FROM table_name
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM table_name 
    GROUP BY column1, column2
);
```

13. **Write a query to find missing numbers in a sequence of IDs.**
```sql
SELECT t1.id + 1 AS missing_id
FROM table_name t1
LEFT JOIN table_name t2 ON t1.id + 1 = t2.id
WHERE t2.id IS NULL;
```

14. **Write an SQL query to display the first and last name in a single column.**
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name 
FROM Employee;
```

15. **Write an SQL query to get the cumulative sum of salaries for each employee.**
```sql
SELECT id, name, salary,
       SUM(salary) OVER (ORDER BY id) AS cumulative_salary
FROM Employee;
```

16. **Write an SQL query to swap the values of two columns without using a third variable.**
```sql
UPDATE Employee
SET column1 = column1 + column2,
    column2 = column1 - column2,
    column1 = column1 - column2;
```

17. **Write a query to fetch employees whose names contain only vowels.**
```sql
SELECT * 
FROM Employee 
WHERE name REGEXP '^[AEIOUaeiou]+$';
```

18. **Write an SQL query to transpose rows into columns.**
```sql
SELECT
    MAX(CASE WHEN month = 'Jan' THEN sales END) AS Jan,
    MAX(CASE WHEN month = 'Feb' THEN sales END) AS Feb
FROM sales_data;
```

19. **Write an SQL query to find the employees with the highest salary in each department.**
```sql
SELECT * 
FROM Employee e 
WHERE salary = (
    SELECT MAX(salary) 
    FROM Employee 
    WHERE department_id = e.department_id
);
```

20. **Write a query to find customers who made multiple purchases on the same day.**
```sql
SELECT customer_id, order_date
FROM Orders
GROUP BY customer_id, order_date
HAVING COUNT(*) > 1;
```

---

## Advanced SQL Coding Questions

21. **Write a query to get the moving average of sales for the last 3 months.**
```sql
SELECT month, AVG(sales) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales_data;
```

22. **Write an SQL query to rank employees by salary in each department.**
```sql
SELECT *, RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
FROM Employee;
```

23. **Write an SQL query to find employees who have more than one manager.**
```sql
SELECT employee_id 
FROM EmployeeManagers 
GROUP BY employee_id 
HAVING COUNT(manager_id) > 1;
```

24. **Write a query to retrieve the most frequent order date from an `Orders` table.**
```sql
SELECT order_date 
FROM Orders 
GROUP BY order_date 
ORDER BY COUNT(*) DESC 
LIMIT 1;
```

25. **Write an SQL query to compare two tables and find mismatched records.**
```sql
SELECT * FROM table1
EXCEPT
SELECT * FROM table2
UNION
SELECT * FROM table2
EXCEPT
SELECT * FROM table1;
```

26. **Write an SQL query to calculate the difference between consecutive rows.**
```sql
SELECT id, value,
       value - LAG(value) OVER (ORDER BY id) AS diff
FROM data_table;
```

27. **Write a query to pivot table data dynamically.**
> Note: Requires dynamic SQL – DBMS specific (e.g., MySQL, SQL Server).

28. **Write a query to delete every alternate row from a table.**
```sql
DELETE FROM Employee
WHERE id % 2 = 0;
```

29. **Write an SQL query to get the first purchase date for each customer.**
```sql
SELECT customer_id, MIN(order_date) AS first_purchase
FROM Orders
GROUP BY customer_id;
```

30. **Write an SQL query to get the running total of sales per month.**
```sql
SELECT month, SUM(sales) OVER (ORDER BY month) AS running_total
FROM sales_data;
```

---

## Window Functions & Analytical Queries

31. **Write an SQL query to assign a rank to employees based on their salaries.**
```sql
SELECT *, RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM Employee;
```

32. **Write an SQL query to find the percentage contribution of each employee’s salary to the total salary.**
```sql
SELECT name, salary, 
       ROUND(100.0 * salary / SUM(salary) OVER (), 2) AS percentage
FROM Employee;
```

33. **Write a query to find the cumulative sum of sales using a window function.**
```sql
SELECT id, sale_amount, 
       SUM(sale_amount) OVER (ORDER BY sale_date) AS cumulative_sum
FROM Sales;
```

34. **Write an SQL query to get the difference between two consecutive transactions.**
```sql
SELECT id, transaction_amount, 
       transaction_amount - LAG(transaction_amount) OVER (ORDER BY transaction_date) AS difference
FROM Transactions;
```

35. **Write an SQL query to find the `LEAD()` and `LAG()` salary for each employee.**
```sql
SELECT name, salary,
       LAG(salary) OVER (ORDER BY salary) AS previous_salary,
       LEAD(salary) OVER (ORDER BY salary) AS next_salary
FROM Employee;
```

