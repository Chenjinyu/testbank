# Basic SQL Concepts - Query Examples and Explanations

## 1. Select All Employees with Salary > $50,000

### Query:
```sql
SELECT * 
FROM employees 
WHERE salary > 50000;
```

### Explanation:
- `SELECT *` retrieves all columns from the table
- `FROM employees` specifies the table name
- `WHERE salary > 50000` filters records where salary is greater than $50,000
- The semicolon (`;`) terminates the SQL statement

### Alternative with specific columns:
```sql
SELECT employee_id, first_name, last_name, salary 
FROM employees 
WHERE salary > 50000;
```

---

## 2. Find the Second Highest Salary in an Employee Table

### Method 1 - Using LIMIT and OFFSET:
```sql
SELECT DISTINCT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;
```

### Method 2 - Using Subquery:
```sql
SELECT MAX(salary) 
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### Method 3 - Using ROW_NUMBER() Window Function:
```sql
SELECT salary 
FROM (
    SELECT salary, 
           ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked_salaries 
WHERE rn = 2;
```

### Explanation:
- **Method 1**: Orders salaries in descending order, uses `DISTINCT` to avoid duplicates, then skips the first record and takes the next one
- **Method 2**: Finds the maximum salary that's less than the overall maximum salary
- **Method 3**: Uses window functions to rank salaries and select the second-ranked one
- `DISTINCT` is important to handle cases where multiple employees have the same highest salary

---

## 3. Count the Number of Orders Per Customer

### Query:
```sql
SELECT customer_id, COUNT(*) as order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;
```

### With Customer Names (using JOIN):
```sql
SELECT c.customer_id, c.customer_name, COUNT(o.order_id) as order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY order_count DESC;
```

### Explanation:
- `COUNT(*)` counts all rows for each group
- `GROUP BY customer_id` groups records by customer
- `ORDER BY order_count DESC` sorts results by count in descending order
- `LEFT JOIN` ensures all customers are shown, even those with zero orders
- `COUNT(o.order_id)` counts only non-NULL order IDs (useful with LEFT JOIN)

---

## 4. Show Employees Hired in the Last 30 Days

### Query:
```sql
SELECT employee_id, first_name, last_name, hire_date
FROM employees
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
```

### Alternative for different databases:
```sql
-- PostgreSQL
SELECT employee_id, first_name, last_name, hire_date
FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '30 days';

-- SQL Server
SELECT employee_id, first_name, last_name, hire_date
FROM employees
WHERE hire_date >= DATEADD(DAY, -30, GETDATE());

-- Oracle
SELECT employee_id, first_name, last_name, hire_date
FROM employees
WHERE hire_date >= SYSDATE - 30;
```

### Explanation:
- `CURDATE()` returns the current date
- `DATE_SUB()` subtracts a specified time interval from a date
- `INTERVAL 30 DAY` specifies a 30-day period
- Different databases have different date functions and syntax
- The condition filters records where hire_date is within the last 30 days

---

## 5. Find Duplicate Records in a Table

### Method 1 - Show duplicate values and their count:
```sql
SELECT email, COUNT(*) as duplicate_count
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;
```

### Method 2 - Show all duplicate records with details:
```sql
SELECT e1.*
FROM employees e1
INNER JOIN (
    SELECT email, COUNT(*) 
    FROM employees 
    GROUP BY email 
    HAVING COUNT(*) > 1
) e2 ON e1.email = e2.email
ORDER BY e1.email;
```

### Method 3 - Using Window Functions:
```sql
SELECT employee_id, first_name, last_name, email
FROM (
    SELECT employee_id, first_name, last_name, email,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY employee_id) as rn
    FROM employees
) ranked_employees
WHERE rn > 1;
```

### Method 4 - Multiple columns for duplicates:
```sql
SELECT first_name, last_name, email, COUNT(*) as duplicate_count
FROM employees
GROUP BY first_name, last_name, email
HAVING COUNT(*) > 1;
```

### Explanation:
- **Method 1**: Groups by the column you want to check for duplicates and shows only groups with more than one record
- **Method 2**: Uses a subquery to identify duplicate values, then joins back to show all records with those values
- **Method 3**: Uses `ROW_NUMBER()` with `PARTITION BY` to number rows within each group of duplicates
- **Method 4**: Checks for duplicates across multiple columns
- `HAVING` clause filters groups (used with GROUP BY), while `WHERE` filters individual records

## Key SQL Concepts Summary

### Basic Clauses:
- **SELECT**: Specifies which columns to retrieve
- **FROM**: Specifies the source table
- **WHERE**: Filters rows based on conditions
- **GROUP BY**: Groups rows that have the same values
- **HAVING**: Filters groups (used with GROUP BY)
- **ORDER BY**: Sorts the result set

### Important Functions:
- **COUNT()**: Counts rows or non-NULL values
- **MAX(), MIN()**: Find maximum and minimum values
- **DISTINCT**: Returns unique values only
- **Date Functions**: Handle date calculations (vary by database)

### Advanced Features:
- **Window Functions**: Perform calculations across related rows
- **Subqueries**: Nested queries for complex operations
- **JOINs**: Combine data from multiple tables
- **LIMIT/OFFSET**: Control result set size and pagination

These queries demonstrate fundamental SQL operations that are essential for database querying and data analysis.