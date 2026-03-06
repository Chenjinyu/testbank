# SQL Performance Optimization - Complete Guide


## Key Sections Covered (Conclusion First):
1. Clustered vs Non-Clustered Indexes
- Detailed explanations with visual representations
- Physical vs logical ordering concepts
- Performance comparisons with examples
- When to use each type with practical guidelines

2. Composite Indexes
- Leftmost prefix rule explanation
- Column ordering strategies for optimal performance
- Advanced techniques (including columns, filtered indexes)
- Multiple index vs single composite index strategies

3. Query Execution Plan Analysis
- Reading and interpreting execution plans
- Database-specific tools and commands
- Common problems (table scans, parameter sniffing, implicit conversions)
- Practical optimization techniques

4. Slow Query Optimization
- Common bottlenecks identification
- WHERE clause optimization techniques
- JOIN performance improvements
- Subquery vs JOIN performance comparisons
- Advanced optimization techniques and hints

5. Partitioning Strategies
- Range, hash, and list partitioning examples
- Sub-partitioning for complex scenarios
- Automated partition management
- Best practices and monitoring techniques

Practical Features:
- Real-world examples with actual SQL code
- Performance comparisons showing before/after scenarios
- Database-specific implementations (SQL Server, PostgreSQL, MySQL, Oracle)
- Monitoring queries to track performance improvements

### Best practices checklist for ongoing optimization
The guide is structured as a complete reference that covers both theoretical concepts and practical implementation details. Each section builds upon previous knowledge and provides copy-ready SQL examples that you can use in production environments.

This comprehensive resource serves as both a learning guide and a practical reference for database performance optimization across different database systems.

## 1. Clustered vs Non-Clustered Indexes

### Understanding Index Fundamentals

An **index** is a data structure that improves query performance by creating shortcuts to data, similar to an index in a book that helps you quickly find specific topics.

### Clustered Indexes

A **clustered index** determines the physical storage order of data in the table. Think of it as a dictionary where words are stored alphabetically - the actual data pages are arranged according to the clustered index key.

#### Key Characteristics:
- **Physical ordering**: Data rows are stored in the order of the clustered index
- **One per table**: A table can have only one clustered index
- **Leaf level contains actual data**: The bottom level of the index contains the actual table rows
- **Primary key default**: Primary keys automatically create clustered indexes

#### Example - Clustered Index:
```sql
-- Create table with clustered index on primary key
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,  -- Automatically creates clustered index
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE
);

-- Create explicit clustered index
CREATE CLUSTERED INDEX IX_employees_hire_date 
ON employees (hire_date);
```

#### Visual Representation:
```
Clustered Index Structure (Employee ID):
Level 2: [1-100] [101-200] [201-300] [301-400]
Level 1: [1-25] [26-50] [51-75] [76-100] ...
Level 0: [Actual Data Rows stored physically in ID order]
```

### Non-Clustered Indexes

A **non-clustered index** is a separate structure that points to the actual data rows. Like a library catalog that references where books are located - the catalog is separate from the books themselves.

#### Key Characteristics:
- **Logical ordering**: Index keys are ordered, but data rows remain in physical storage order
- **Multiple per table**: A table can have many non-clustered indexes (up to 999 in SQL Server)
- **Leaf level contains pointers**: Bottom level contains row identifiers or clustered index keys
- **Additional storage**: Requires extra storage space

#### Example - Non-Clustered Index:
```sql
-- Create non-clustered indexes for frequent queries
CREATE NONCLUSTERED INDEX IX_employees_department 
ON employees (department);

CREATE NONCLUSTERED INDEX IX_employees_last_name 
ON employees (last_name);

CREATE NONCLUSTERED INDEX IX_employees_hire_date 
ON employees (hire_date);
```

#### Visual Representation:
```
Non-Clustered Index Structure (Department):
Level 1: [Engineering] [Finance] [HR] [Marketing]
Level 0: [Pointers to actual rows in clustered index order]

Data Storage (remains in clustered index order):
Employee_ID: 1, 5, 12, 25, 30, 45, 67, 89...
```

### Performance Comparison

#### Clustered Index Performance:
```sql
-- Range queries are very efficient
SELECT * FROM employees 
WHERE employee_id BETWEEN 100 AND 200;
-- Fast: Data is physically stored in order

-- Single row lookups
SELECT * FROM employees 
WHERE employee_id = 150;
-- Fastest: Direct access to data
```

#### Non-Clustered Index Performance:
```sql
-- Covered queries (all columns in index)
CREATE NONCLUSTERED INDEX IX_employees_dept_name 
ON employees (department) 
INCLUDE (first_name, last_name);

SELECT first_name, last_name 
FROM employees 
WHERE department = 'Engineering';
-- Fast: All data available in index

-- Non-covered queries require key lookup
SELECT * FROM employees 
WHERE department = 'Engineering';
-- Slower: Index seek + key lookup to get other columns
```

### When to Use Each Type

#### Use Clustered Index When:
- ✅ Frequent range queries on the column
- ✅ Ordering queries (ORDER BY) are common
- ✅ Column has unique or mostly unique values
- ✅ Data is frequently accessed sequentially

```sql
-- Good clustered index candidates
CREATE CLUSTERED INDEX IX_orders_date ON orders (order_date);     -- Range queries
CREATE CLUSTERED INDEX IX_customers_id ON customers (customer_id); -- Primary key
```

#### Use Non-Clustered Index When:
- ✅ Multiple columns need indexing
- ✅ Selective WHERE clauses
- ✅ Supporting specific query patterns
- ✅ Foreign key relationships

```sql
-- Good non-clustered index candidates
CREATE NONCLUSTERED INDEX IX_orders_customer ON orders (customer_id);  -- FK lookups
CREATE NONCLUSTERED INDEX IX_products_category ON products (category);   -- Filtering
```

---

## 2. Composite Indexes (Multi-Column Indexes)

### What are Composite Indexes?

A **composite index** includes multiple columns in a single index structure. The order of columns in the index is crucial for performance.

### Column Order Importance

The order of columns in a composite index follows the **leftmost prefix rule** - queries can use the index effectively only if they reference columns starting from the leftmost column in the index.

#### Example Setup:
```sql
CREATE TABLE customer_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(20),
    total_amount DECIMAL(10,2),
    sales_rep_id INT
);

-- Create composite index
CREATE INDEX IX_orders_composite 
ON customer_orders (customer_id, order_date, status);
```

### Index Usage Examples

#### Queries That Can Use the Index:
```sql
-- ✅ Uses entire index (best performance)
SELECT * FROM customer_orders 
WHERE customer_id = 123 
  AND order_date = '2024-01-15' 
  AND status = 'Shipped';

-- ✅ Uses customer_id + order_date portion
SELECT * FROM customer_orders 
WHERE customer_id = 123 
  AND order_date BETWEEN '2024-01-01' AND '2024-01-31';

-- ✅ Uses only customer_id portion
SELECT * FROM customer_orders 
WHERE customer_id = 123;

-- ✅ Uses customer_id + order_date, ignores status
SELECT * FROM customer_orders 
WHERE customer_id = 123 
  AND order_date > '2024-01-01' 
  AND total_amount > 1000;  -- This condition won't use index
```

#### Queries That Cannot Use the Index Effectively:
```sql
-- ❌ Skips first column (customer_id)
SELECT * FROM customer_orders 
WHERE order_date = '2024-01-15' 
  AND status = 'Shipped';

-- ❌ Starts with second column only
SELECT * FROM customer_orders 
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';

-- ❌ Uses only third column
SELECT * FROM customer_orders 
WHERE status = 'Pending';
```

### Designing Effective Composite Indexes

#### Design Strategy:
1. **Most selective column first** (narrows down results most)
2. **Equality conditions before range conditions**
3. **Most frequently queried columns first**

#### Example Analysis:
```sql
-- Query pattern analysis
-- Query 1: WHERE customer_id = ? AND order_date BETWEEN ? AND ?
-- Query 2: WHERE customer_id = ? AND status = ?
-- Query 3: WHERE customer_id = ?

-- Optimal index design:
CREATE INDEX IX_orders_optimized 
ON customer_orders (customer_id, order_date, status);

-- Why this order?
-- 1. customer_id: Used in all queries (highest frequency)
-- 2. order_date: Used in range queries (put before equality on status)
-- 3. status: Used in equality conditions
```

### Advanced Composite Index Techniques

#### Including Columns (SQL Server/PostgreSQL):
```sql
-- Include frequently selected columns
CREATE NONCLUSTERED INDEX IX_orders_covering
ON customer_orders (customer_id, order_date)
INCLUDE (total_amount, status, sales_rep_id);

-- Benefits:
-- 1. Avoids key lookups
-- 2. Creates covering index
-- 3. Better performance for SELECT queries
```

#### Filtered Indexes:
```sql
-- Index only active orders
CREATE NONCLUSTERED INDEX IX_orders_active
ON customer_orders (customer_id, order_date)
WHERE status IN ('Pending', 'Processing', 'Shipped');

-- Benefits:
-- 1. Smaller index size
-- 2. Faster maintenance
-- 3. Better selectivity
```

### Multiple Index Strategy

Sometimes multiple targeted indexes perform better than one composite index:

```sql
-- Instead of one large composite index:
CREATE INDEX IX_orders_all_columns 
ON customer_orders (customer_id, order_date, status, sales_rep_id);

-- Consider multiple smaller indexes:
CREATE INDEX IX_orders_customer_date ON customer_orders (customer_id, order_date);
CREATE INDEX IX_orders_status ON customer_orders (status);
CREATE INDEX IX_orders_sales_rep ON customer_orders (sales_rep_id);

-- Database optimizer can combine indexes when beneficial
```

---

## 3. Query Execution Plan Analysis

### Understanding Execution Plans

An **execution plan** shows how the database engine executes your query, including which indexes are used, join methods, and resource costs.

### Reading Execution Plans

#### SQL Server Execution Plan:
```sql
-- Enable execution plan display
SET SHOWPLAN_ALL ON;
-- OR
SET STATISTICS IO ON;

-- Analyze this query
SELECT c.customer_name, COUNT(o.order_id) as order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.registration_date >= '2024-01-01'
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;

-- View graphical execution plan (SQL Server Management Studio)
-- Ctrl + M to include actual execution plan
```

#### Key Execution Plan Components:

1. **Scan vs Seek Operations:**
```sql
-- Index Seek (Good - selective)
SELECT * FROM employees WHERE employee_id = 123;
-- Shows: Index Seek on IX_employees_id

-- Table Scan (Bad - reads entire table)
SELECT * FROM employees WHERE UPPER(last_name) = 'SMITH';
-- Shows: Table Scan on employees

-- Index Scan (Better than table scan, but not ideal)
SELECT * FROM employees WHERE salary > 50000;
-- Shows: Index Scan on IX_employees_salary
```

2. **Join Operations:**
```sql
-- Nested Loop Join (good for small result sets)
-- Hash Join (good for large result sets with no indexes)
-- Merge Join (good for large sorted result sets)

EXPLAIN (FORMAT=JSON)  -- PostgreSQL
SELECT c.customer_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

3. **Cost Analysis:**
```sql
-- PostgreSQL execution plan with costs
EXPLAIN (ANALYZE, BUFFERS) 
SELECT product_name, SUM(quantity * unit_price) as revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date >= '2024-01-01'
GROUP BY p.product_id, product_name
ORDER BY revenue DESC
LIMIT 10;
```

### Common Execution Plan Problems

#### Problem 1: Table Scans
```sql
-- Problem query
SELECT * FROM orders WHERE YEAR(order_date) = 2024;

-- Solution: Remove function from WHERE clause
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';

-- Add appropriate index
CREATE INDEX IX_orders_date ON orders (order_date);
```

#### Problem 2: Parameter Sniffing
```sql
-- Problematic stored procedure
CREATE PROCEDURE GetOrdersByStatus(@Status VARCHAR(20))
AS
BEGIN
    SELECT * FROM orders WHERE status = @Status;
    -- Plan optimized for first parameter value
END;

-- Solutions:
-- Option 1: Use local variables
CREATE PROCEDURE GetOrdersByStatus(@Status VARCHAR(20))
AS
BEGIN
    DECLARE @LocalStatus VARCHAR(20) = @Status;
    SELECT * FROM orders WHERE status = @LocalStatus;
END;

-- Option 2: Use OPTION(RECOMPILE)
CREATE PROCEDURE GetOrdersByStatus(@Status VARCHAR(20))
AS
BEGIN
    SELECT * FROM orders WHERE status = @Status
    OPTION(RECOMPILE);
END;
```

#### Problem 3: Implicit Conversions
```sql
-- Problem: Data type mismatch
CREATE TABLE test_table (
    id VARCHAR(10),
    name VARCHAR(50)
);

-- This causes implicit conversion (bad)
SELECT * FROM test_table WHERE id = 123;

-- Solution: Use proper data types
SELECT * FROM test_table WHERE id = '123';
```

### Execution Plan Tools

#### Database-Specific Tools:
```sql
-- SQL Server
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- Use SQL Server Management Studio graphical plans

-- PostgreSQL
EXPLAIN (ANALYZE, BUFFERS, VERBOSE) 
SELECT * FROM your_query;

-- MySQL
EXPLAIN FORMAT=JSON 
SELECT * FROM your_query;

-- Oracle
EXPLAIN PLAN FOR
SELECT * FROM your_query;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

---

## 4. Optimize Slow Queries

### Common Performance Bottlenecks

#### Bottleneck 1: Missing Indexes

**Problem:**
```sql
-- Slow query without index
SELECT customer_name, email 
FROM customers 
WHERE city = 'New York' 
  AND registration_date > '2024-01-01';

-- Execution plan shows Table Scan
```

**Solution:**
```sql
-- Create composite index
CREATE INDEX IX_customers_city_regdate 
ON customers (city, registration_date)
INCLUDE (customer_name, email);

-- Now the query uses Index Seek + Key Lookup or Covering Index
```

#### Bottleneck 2: Poor WHERE Clause Design

**Problems and Solutions:**
```sql
-- ❌ Problem: Function in WHERE clause
SELECT * FROM orders 
WHERE YEAR(order_date) = 2024;

-- ✅ Solution: Range condition
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';

-- ❌ Problem: Leading wildcards
SELECT * FROM customers 
WHERE customer_name LIKE '%Smith%';

-- ✅ Solution: Trailing wildcards when possible
SELECT * FROM customers 
WHERE customer_name LIKE 'Smith%';

-- ❌ Problem: OR conditions
SELECT * FROM products 
WHERE category = 'Electronics' 
   OR category = 'Computers';

-- ✅ Solution: IN clause
SELECT * FROM products 
WHERE category IN ('Electronics', 'Computers');
```

#### Bottleneck 3: Inefficient JOINs

**Problem:**
```sql
-- Cartesian product risk
SELECT c.customer_name, o.order_date, p.product_name
FROM customers c, orders o, order_items oi, products p
WHERE c.customer_id = o.customer_id
  AND o.order_id = oi.order_id
  AND oi.product_id = p.product_id;
```

**Solution:**
```sql
-- Explicit JOIN syntax with proper conditions
SELECT c.customer_name, o.order_date, p.product_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE c.status = 'Active'  -- Additional filtering
ORDER BY o.order_date DESC;

-- Ensure proper indexes exist
CREATE INDEX IX_orders_customer ON orders (customer_id);
CREATE INDEX IX_order_items_order ON order_items (order_id);
CREATE INDEX IX_order_items_product ON order_items (product_id);
```

#### Bottleneck 4: Subquery vs JOIN Performance

**Slow Subquery:**
```sql
-- Often slower for large datasets
SELECT customer_name 
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.customer_id = c.customer_id 
      AND o.order_date > '2024-01-01'
);
```

**Optimized JOIN:**
```sql
-- Usually faster with proper indexes
SELECT DISTINCT c.customer_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date > '2024-01-01';
```

### Query Optimization Techniques

#### Technique 1: Query Rewriting
```sql
-- Instead of this expensive query:
SELECT * FROM products p
WHERE p.product_id IN (
    SELECT oi.product_id 
    FROM order_items oi 
    JOIN orders o ON oi.order_id = o.order_id
    WHERE o.order_date > '2024-01-01'
);

-- Use this more efficient approach:
SELECT DISTINCT p.*
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
INNER JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date > '2024-01-01';
```

#### Technique 2: Limiting Result Sets
```sql
-- Add LIMIT/TOP clauses when appropriate
SELECT TOP 100 customer_name, total_spent
FROM customer_summary
ORDER BY total_spent DESC;

-- Use pagination for large result sets
SELECT customer_name, order_date
FROM customer_orders
ORDER BY order_date DESC
OFFSET 1000 ROWS FETCH NEXT 100 ROWS ONLY;  -- SQL Server
-- LIMIT 100 OFFSET 1000;  -- MySQL/PostgreSQL
```

#### Technique 3: Avoiding SELECT *
```sql
-- ❌ Avoid: Selecting unnecessary columns
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- ✅ Better: Select only needed columns
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```

### Advanced Optimization Techniques

#### Using Hints (Use Sparingly):
```sql
-- SQL Server hints
SELECT /*+ INDEX(orders IX_orders_date) */ 
       order_id, customer_id
FROM orders 
WHERE order_date > '2024-01-01';

-- Force specific join type
SELECT c.customer_name, o.order_total
FROM customers c
INNER HASH JOIN orders o ON c.customer_id = o.customer_id;
```

#### Query Caching:
```sql
-- Enable query cache (MySQL)
SET GLOBAL query_cache_type = ON;
SET GLOBAL query_cache_size = 268435456; -- 256MB

-- Use consistent parameter formatting for better cache hits
SELECT * FROM products WHERE price = 19.99;  -- Cached
SELECT * FROM products WHERE price = 19.990; -- Different cache entry
```

---

## 5. Partitioning Strategies for Large Tables

### What is Table Partitioning?

**Table partitioning** divides a large table into smaller, more manageable pieces called partitions, while maintaining the appearance of a single table to applications.

### Types of Partitioning

#### Horizontal Partitioning (Most Common)

**Range Partitioning:**
```sql
-- SQL Server range partitioning by date
CREATE PARTITION FUNCTION pf_orders_by_year (DATE)
AS RANGE RIGHT FOR VALUES 
('2022-01-01', '2023-01-01', '2024-01-01', '2025-01-01');

CREATE PARTITION SCHEME ps_orders_by_year
AS PARTITION pf_orders_by_year
TO (fg_2021, fg_2022, fg_2023, fg_2024, fg_2025);

CREATE TABLE orders_partitioned (
    order_id INT IDENTITY(1,1),
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
) ON ps_orders_by_year (order_date);
```

**Hash Partitioning:**
```sql
-- PostgreSQL hash partitioning
CREATE TABLE orders_hash_partitioned (
    order_id SERIAL,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
) PARTITION BY HASH (customer_id);

-- Create hash partitions
CREATE TABLE orders_hash_p1 PARTITION OF orders_hash_partitioned
FOR VALUES WITH (modulus 4, remainder 0);

CREATE TABLE orders_hash_p2 PARTITION OF orders_hash_partitioned
FOR VALUES WITH (modulus 4, remainder 1);

CREATE TABLE orders_hash_p3 PARTITION OF orders_hash_partitioned
FOR VALUES WITH (modulus 4, remainder 2);

CREATE TABLE orders_hash_p4 PARTITION OF orders_hash_partitioned
FOR VALUES WITH (modulus 4, remainder 3);
```

**List Partitioning:**
```sql
-- PostgreSQL list partitioning by region
CREATE TABLE sales_by_region (
    sale_id SERIAL,
    product_id INT,
    sale_date DATE,
    region VARCHAR(20),
    amount DECIMAL(10,2)
) PARTITION BY LIST (region);

CREATE TABLE sales_north PARTITION OF sales_by_region
FOR VALUES IN ('North', 'Northeast', 'Northwest');

CREATE TABLE sales_south PARTITION OF sales_by_region
FOR VALUES IN ('South', 'Southeast', 'Southwest');

CREATE TABLE sales_east PARTITION OF sales_by_region
FOR VALUES IN ('East');

CREATE TABLE sales_west PARTITION OF sales_by_region
FOR VALUES IN ('West');
```

### Benefits of Partitioning

#### Performance Benefits:
```sql
-- Partition elimination in action
SELECT COUNT(*) FROM orders_partitioned 
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
-- Only scans 2024 partition, ignores others

-- Parallel processing
SELECT region, SUM(amount) 
FROM sales_by_region 
GROUP BY region;
-- Each partition can be processed in parallel
```

#### Maintenance Benefits:
```sql
-- Faster index rebuilds (per partition)
ALTER INDEX IX_orders_customer_id ON orders_2024 REBUILD;

-- Easy data archival
-- Move old partition to archive storage
ALTER TABLE orders_partitioned 
SWITCH PARTITION 1 TO archive_orders;

-- Efficient data purging
DROP TABLE orders_2020;  -- Instant deletion vs DELETE statement
```

### Advanced Partitioning Strategies

#### Sub-partitioning (Composite Partitioning):
```sql
-- PostgreSQL: Partition by date, then sub-partition by hash
CREATE TABLE orders_composite (
    order_id SERIAL,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2024 PARTITION OF orders_composite
FOR VALUES FROM ('2024-01-01') TO ('2025-01-01')
PARTITION BY HASH (customer_id);

CREATE TABLE orders_2024_h1 PARTITION OF orders_2024
FOR VALUES WITH (modulus 4, remainder 0);

CREATE TABLE orders_2024_h2 PARTITION OF orders_2024
FOR VALUES WITH (modulus 4, remainder 1);
-- ... additional sub-partitions
```

#### Automated Partition Management:
```sql
-- SQL Server: Automated partition management
CREATE PROCEDURE manage_order_partitions
AS
BEGIN
    DECLARE @next_boundary DATE = DATEADD(MONTH, 1, GETDATE());
    
    -- Add new partition for next month
    ALTER PARTITION SCHEME ps_orders_by_month
    NEXT USED [new_filegroup];
    
    ALTER PARTITION FUNCTION pf_orders_by_month()
    SPLIT RANGE (@next_boundary);
    
    -- Archive old partitions (older than 2 years)
    DECLARE @old_boundary DATE = DATEADD(YEAR, -2, GETDATE());
    
    -- Switch out old partition
    ALTER TABLE orders_partitioned
    SWITCH PARTITION 1 TO archive_orders;
    
    -- Merge the empty partition
    ALTER PARTITION FUNCTION pf_orders_by_month()
    MERGE RANGE (@old_boundary);
END;
```

### Partitioning Best Practices

#### Choosing Partition Keys:
```sql
-- ✅ Good partition key: Date columns for time-series data
CREATE TABLE transactions (
    transaction_id BIGINT,
    transaction_date DATE,  -- Good partition key
    customer_id INT,
    amount DECIMAL(10,2)
) PARTITION BY RANGE (transaction_date);

-- ✅ Good partition key: High-cardinality, evenly distributed
CREATE TABLE user_activity (
    user_id BIGINT,         -- Good for hash partitioning
    activity_date DATE,
    activity_type VARCHAR(50),
    details TEXT
) PARTITION BY HASH (user_id);

-- ❌ Poor partition key: Low cardinality
CREATE TABLE orders (
    order_id INT,
    status VARCHAR(20),     -- Only few distinct values
    order_date DATE
) PARTITION BY LIST (status);  -- Creates uneven partitions
```

#### Partition Sizing Guidelines:
```sql
-- Optimal partition sizes
-- Small partitions: 10GB - 50GB (better for maintenance)
-- Large partitions: 50GB - 100GB (better for query performance)
-- Very large partitions: > 100GB (consider sub-partitioning)

-- Monitor partition sizes
SELECT 
    SCHEMA_NAME(o.schema_id) AS schema_name,
    OBJECT_NAME(p.object_id) AS table_name,
    p.partition_number,
    p.rows AS row_count,
    au.total_pages * 8 / 1024 AS size_mb
FROM sys.partitions p
JOIN sys.allocation_units au ON p.partition_id = au.container_id
JOIN sys.objects o ON p.object_id = o.object_id
WHERE o.type = 'U'  -- User tables only
ORDER BY size_mb DESC;
```

### Partitioning Considerations

#### Query Patterns:
```sql
-- Ensure queries can benefit from partition elimination
-- ✅ Good: Uses partition key in WHERE clause
SELECT * FROM orders_partitioned 
WHERE order_date = '2024-06-15';

-- ❌ Poor: No partition elimination
SELECT * FROM orders_partitioned 
WHERE customer_id = 12345;

-- Solution: Include partition key when possible
SELECT * FROM orders_partitioned 
WHERE customer_id = 12345 
  AND order_date >= '2024-01-01';
```

#### Index Strategy for Partitioned Tables:
```sql
-- Local indexes (recommended)
CREATE INDEX IX_orders_customer 
ON orders_partitioned (customer_id)
ON ps_orders_by_year (order_date);  -- Same partition scheme

-- Global indexes (SQL Server)
CREATE INDEX IX_orders_global_customer 
ON orders_partitioned (customer_id);
-- Creates index across all partitions
```

### Monitoring Partitioned Tables

#### Performance Monitoring:
```sql
-- Check partition elimination
SET STATISTICS IO ON;
SELECT COUNT(*) FROM orders_partitioned 
WHERE order_date = '2024-01-15';
-- Should show IO only for relevant partition

-- Monitor partition sizes and growth
SELECT 
    t.name AS table_name,
    p.partition_number,
    f.name AS partition_function,
    r.boundary_value,
    p.rows,
    CAST(SUM(au.used_pages * 8) / 1024.0 AS DECIMAL(10,2)) AS size_mb
FROM sys.tables t
JOIN sys.partitions p ON t.object_id = p.object_id
JOIN sys.allocation_units au ON p.partition_id = au.container_id
LEFT JOIN sys.partition_schemes ps ON t.object_id = ps.object_id
LEFT JOIN sys.partition_functions f ON ps.function_id = f.function_id
LEFT JOIN sys.partition_range_values r ON f.function_id = r.function_id 
    AND r.boundary_id = p.partition_number
WHERE t.name = 'orders_partitioned'
GROUP BY t.name, p.partition_number, f.name, r.boundary_value, p.rows
ORDER BY p.partition_number;
```

## Performance Optimization Checklist

### Database Design:
- ✅ Proper normalization balanced with performance needs
- ✅ Appropriate data types and sizes
- ✅ Primary keys on all tables
- ✅ Foreign key constraints for data integrity

### Indexing Strategy:
- ✅ Indexes on frequently queried columns
- ✅ Composite indexes for multi-column queries
- ✅ Covering indexes to avoid key lookups
- ✅ Regular index maintenance and statistics updates

### Query Optimization:
- ✅ Analyze execution plans regularly
- ✅ Avoid functions in WHERE clauses
- ✅ Use appropriate JOIN types
- ✅ Limit result sets when possible

### Hardware and Configuration:
- ✅ Sufficient memory for buffer pools
- ✅ Fast storage (SSDs) for high-performance databases
- ✅ Proper tempdb configuration
- ✅ Regular maintenance plans

### Monitoring and Maintenance:
- ✅ Regular performance monitoring
- ✅ Index fragmentation checks
- ✅ Statistics updates
- ✅ Query performance baselines

This comprehensive guide provides the foundation for understanding and implementing effective SQL performance optimization strategies across different database systems.