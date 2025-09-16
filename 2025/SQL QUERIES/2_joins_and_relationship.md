# SQL Joins and Relationships - Complete Guide

## Table Structure Overview

Before diving into joins, let's establish our sample table structure:

```sql
-- Sample tables for demonstration
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    employee_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## 1. Different Types of JOINs

### INNER JOIN
Returns only records that have matching values in both tables.

```sql
-- Get customers and their orders
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_name, o.order_date;
```

**Explanation:**
- Returns only customers who have placed orders
- Excludes customers with no orders and orders with invalid customer_ids
- Most restrictive join type

---

### LEFT JOIN (LEFT OUTER JOIN)
Returns all records from the left table and matching records from the right table.

```sql
-- Get all customers and their orders (including customers with no orders)
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_name, o.order_date;
```

**Explanation:**
- Returns all customers, even those who haven't placed any orders
- For customers with no orders, order columns will show NULL values
- Most commonly used join type

---

### RIGHT JOIN (RIGHT OUTER JOIN)
Returns all records from the right table and matching records from the left table.

```sql
-- Get all orders and their customer information (including orphaned orders)
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.order_date;
```

**Explanation:**
- Returns all orders, even those with invalid customer_ids
- For orders without valid customers, customer columns will show NULL values
- Less commonly used than LEFT JOIN

---

### FULL OUTER JOIN
Returns all records when there's a match in either table.

```sql
-- Get all customers and all orders (including unmatched records from both sides)
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_name, o.order_date;
```

**Note:** MySQL doesn't support FULL OUTER JOIN directly. Use UNION instead:

```sql
-- MySQL alternative for FULL OUTER JOIN
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
UNION
SELECT c.customer_name, c.email, o.order_id, o.order_date, o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;
```

**Explanation:**
- Returns all customers and all orders
- Shows unmatched records from both tables
- Most comprehensive but least commonly used

---

## 2. Find Employees Who Don't Have Any Orders

```sql
-- Method 1: Using LEFT JOIN with NULL check
SELECT e.employee_id, e.employee_name, e.department
FROM employees e
LEFT JOIN orders o ON e.employee_id = o.employee_id
WHERE o.employee_id IS NULL;
```

```sql
-- Method 2: Using NOT EXISTS
SELECT e.employee_id, e.employee_name, e.department
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.employee_id = e.employee_id
);
```

```sql
-- Method 3: Using NOT IN (be careful with NULLs)
SELECT e.employee_id, e.employee_name, e.department
FROM employees e
WHERE e.employee_id NOT IN (
    SELECT DISTINCT o.employee_id 
    FROM orders o 
    WHERE o.employee_id IS NOT NULL
);
```

**Explanation:**
- **Method 1**: LEFT JOIN brings all employees, NULL check filters those without orders
- **Method 2**: NOT EXISTS is often more efficient for large datasets
- **Method 3**: NOT IN requires handling NULL values explicitly
- LEFT JOIN with NULL check is the most intuitive and commonly used approach

---

## 3. Get Customer Information with Total Order Amount

```sql
-- Basic version: Customers with orders only
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    c.city,
    SUM(o.total_amount) as total_order_amount,
    COUNT(o.order_id) as total_orders
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.email, c.city
ORDER BY total_order_amount DESC;
```

```sql
-- Include all customers (even those with no orders)
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    c.city,
    COALESCE(SUM(o.total_amount), 0) as total_order_amount,
    COUNT(o.order_id) as total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.email, c.city
ORDER BY total_order_amount DESC;
```

```sql
-- More detailed version with order statistics
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    c.city,
    COALESCE(SUM(o.total_amount), 0) as total_order_amount,
    COUNT(o.order_id) as total_orders,
    COALESCE(AVG(o.total_amount), 0) as average_order_value,
    COALESCE(MAX(o.total_amount), 0) as largest_order,
    MAX(o.order_date) as last_order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.email, c.city
ORDER BY total_order_amount DESC;
```

**Explanation:**
- `SUM(o.total_amount)` calculates total spending per customer
- `GROUP BY` groups results by customer
- `COALESCE()` replaces NULL values with 0 for customers with no orders
- `COUNT(o.order_id)` counts actual orders (NULL-safe)
- LEFT JOIN ensures all customers are included

---

## 4. Find Products That Have Never Been Ordered

```sql
-- Method 1: Using LEFT JOIN with NULL check
SELECT p.product_id, p.product_name, p.category, p.unit_price
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;
```

```sql
-- Method 2: Using NOT EXISTS
SELECT p.product_id, p.product_name, p.category, p.unit_price
FROM products p
WHERE NOT EXISTS (
    SELECT 1 
    FROM order_items oi 
    WHERE oi.product_id = p.product_id
);
```

```sql
-- Method 3: Using NOT IN
SELECT p.product_id, p.product_name, p.category, p.unit_price
FROM products p
WHERE p.product_id NOT IN (
    SELECT DISTINCT oi.product_id 
    FROM order_items oi 
    WHERE oi.product_id IS NOT NULL
);
```

```sql
-- With additional information about product categories
SELECT 
    p.category,
    COUNT(*) as unordered_products_count,
    GROUP_CONCAT(p.product_name ORDER BY p.product_name) as unordered_products
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL
GROUP BY p.category
ORDER BY unordered_products_count DESC;
```

**Explanation:**
- Similar logic to finding employees without orders
- LEFT JOIN with NULL check is most readable
- Last query groups unordered products by category for better analysis
- `GROUP_CONCAT()` creates a comma-separated list of products (MySQL specific)

---

## 5. Join Three or More Tables

### Basic Multi-Table Join
```sql
-- Get complete order information with customer and product details
SELECT 
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) as line_total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC, o.order_id, p.product_name;
```

### Advanced Multi-Table Analysis
```sql
-- Customer purchase analysis with product categories
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    p.category,
    SUM(oi.quantity * oi.unit_price) as category_total,
    SUM(oi.quantity) as total_items_purchased,
    COUNT(DISTINCT o.order_id) as orders_in_category,
    AVG(oi.unit_price) as avg_price_paid
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name, c.city, p.category
HAVING category_total > 100  -- Only show significant purchases
ORDER BY c.customer_name, category_total DESC;
```

### Complete Sales Report with Employee Information
```sql
-- Comprehensive sales report including employee who processed the order
SELECT 
    e.employee_name as sales_rep,
    e.department,
    c.customer_name,
    c.city as customer_city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) as line_total,
    o.total_amount as order_total
FROM employees e
INNER JOIN orders o ON e.employee_id = o.employee_id
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 90 DAY)  -- Last 90 days
ORDER BY o.order_date DESC, o.order_id, oi.order_item_id;
```

### Monthly Sales Summary with Multiple Joins
```sql
-- Monthly sales summary across all tables
SELECT 
    YEAR(o.order_date) as sales_year,
    MONTH(o.order_date) as sales_month,
    MONTHNAME(o.order_date) as month_name,
    COUNT(DISTINCT c.customer_id) as unique_customers,
    COUNT(DISTINCT o.order_id) as total_orders,
    COUNT(DISTINCT p.product_id) as unique_products_sold,
    SUM(oi.quantity) as total_items_sold,
    SUM(oi.quantity * oi.unit_price) as total_revenue,
    AVG(o.total_amount) as avg_order_value
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
GROUP BY YEAR(o.order_date), MONTH(o.order_date), MONTHNAME(o.order_date)
ORDER BY sales_year DESC, sales_month DESC;
```

**Explanation:**
- **Basic Multi-Table Join**: Connects all four main tables to show complete order details
- **Advanced Analysis**: Groups data by customer and product category for purchasing patterns
- **Sales Report**: Includes employee information for tracking sales performance
- **Monthly Summary**: Aggregates data across time periods for business intelligence

---

## Join Types Comparison Summary

| Join Type | Description | Use Case |
|-----------|-------------|----------|
| **INNER JOIN** | Only matching records from both tables | When you need data that exists in both tables |
| **LEFT JOIN** | All records from left table + matching from right | When you want all records from the primary table |
| **RIGHT JOIN** | All records from right table + matching from left | Less common, usually LEFT JOIN is preferred |
| **FULL OUTER JOIN** | All records from both tables | When you need complete data from both tables |

## Best Practices for Joins

1. **Always use table aliases** for better readability
2. **Use appropriate join types** based on your data requirements
3. **Include proper WHERE clauses** to filter results
4. **Use indexes** on join columns for better performance
5. **Be careful with NULL values** in join conditions
6. **Group and aggregate appropriately** when summarizing data
7. **Consider using EXISTS/NOT EXISTS** for better performance with large datasets

## Performance Tips

- **Index join columns** for faster execution
- **Use INNER JOINs** when possible (fastest)
- **Limit result sets** with WHERE clauses before joining
- **Avoid SELECT *** in production queries
- **Use EXPLAIN** to analyze query execution plans
- **Consider denormalization** for frequently accessed data

This comprehensive guide covers all major join operations and provides practical examples for real-world database scenarios.