# SQL Advanced Topics - Complete Guide

## 1. Stored Procedures and Functions

### Understanding the Difference

**Stored Procedures:**
- Can return multiple result sets
- Can perform DML operations (INSERT, UPDATE, DELETE)
- Cannot be used in SELECT statements
- Can have input/output parameters

**Functions:**
- Return a single value or table
- Generally read-only (some exceptions)
- Can be used in SELECT statements
- Must return a value

---

### Stored Procedures

#### SQL Server Stored Procedures

```sql
-- Basic stored procedure
CREATE PROCEDURE GetCustomerOrders
    @CustomerID INT,
    @StartDate DATE = NULL,
    @EndDate DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Input validation
    IF @CustomerID IS NULL OR @CustomerID <= 0
    BEGIN
        RAISERROR('Invalid Customer ID provided', 16, 1);
        RETURN -1;
    END;
    
    -- Set default dates if not provided
    IF @StartDate IS NULL
        SET @StartDate = DATEADD(YEAR, -1, GETDATE());
    
    IF @EndDate IS NULL
        SET @EndDate = GETDATE();
    
    -- Main query
    SELECT 
        o.order_id,
        o.order_date,
        o.total_amount,
        c.customer_name,
        COUNT(oi.product_id) as item_count
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.customer_id = @CustomerID
        AND o.order_date BETWEEN @StartDate AND @EndDate
    GROUP BY o.order_id, o.order_date, o.total_amount, c.customer_name
    ORDER BY o.order_date DESC;
    
    -- Return success code
    RETURN 0;
END;
GO

-- Execute the procedure
EXEC GetCustomerOrders @CustomerID = 123;
EXEC GetCustomerOrders @CustomerID = 123, @StartDate = '2024-01-01', @EndDate = '2024-12-31';
```

#### Advanced Stored Procedure with Output Parameters

```sql
-- Procedure with multiple output parameters and error handling
CREATE PROCEDURE ProcessCustomerOrder
    @CustomerID INT,
    @ProductID INT,
    @Quantity INT,
    @OrderID INT OUTPUT,
    @TotalAmount DECIMAL(10,2) OUTPUT,
    @ErrorMessage VARCHAR(500) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Initialize output parameters
        SET @OrderID = 0;
        SET @TotalAmount = 0.00;
        SET @ErrorMessage = NULL;
        
        -- Validate customer exists and is active
        IF NOT EXISTS (SELECT 1 FROM customers WHERE customer_id = @CustomerID AND status = 'Active')
        BEGIN
            SET @ErrorMessage = 'Customer not found or inactive';
            ROLLBACK TRANSACTION;
            RETURN -1;
        END;
        
        -- Validate product and get price
        DECLARE @UnitPrice DECIMAL(10,2);
        DECLARE @StockQuantity INT;
        
        SELECT @UnitPrice = unit_price, @StockQuantity = stock_quantity
        FROM products 
        WHERE product_id = @ProductID AND status = 'Active';
        
        IF @UnitPrice IS NULL
        BEGIN
            SET @ErrorMessage = 'Product not found or inactive';
            ROLLBACK TRANSACTION;
            RETURN -2;
        END;
        
        -- Check stock availability
        IF @StockQuantity < @Quantity
        BEGIN
            SET @ErrorMessage = 'Insufficient stock. Available: ' + CAST(@StockQuantity AS VARCHAR(10));
            ROLLBACK TRANSACTION;
            RETURN -3;
        END;
        
        -- Calculate total amount
        SET @TotalAmount = @UnitPrice * @Quantity;
        
        -- Create order
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (@CustomerID, GETDATE(), @TotalAmount, 'Pending');
        
        SET @OrderID = SCOPE_IDENTITY();
        
        -- Add order item
        INSERT INTO order_items (order_id, product_id, quantity, unit_price)
        VALUES (@OrderID, @ProductID, @Quantity, @UnitPrice);
        
        -- Update stock
        UPDATE products 
        SET stock_quantity = stock_quantity - @Quantity
        WHERE product_id = @ProductID;
        
        COMMIT TRANSACTION;
        RETURN 0;
        
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        SET @ErrorMessage = ERROR_MESSAGE();
        RETURN -999;
    END CATCH;
END;
GO

-- Execute with output parameters
DECLARE @NewOrderID INT, @OrderTotal DECIMAL(10,2), @Error VARCHAR(500);
EXEC ProcessCustomerOrder 
    @CustomerID = 123,
    @ProductID = 456,
    @Quantity = 2,
    @OrderID = @NewOrderID OUTPUT,
    @TotalAmount = @OrderTotal OUTPUT,
    @ErrorMessage = @Error OUTPUT;

SELECT @NewOrderID as OrderID, @OrderTotal as Total, @Error as ErrorMsg;
```

#### MySQL Stored Procedures

```sql
-- MySQL stored procedure with cursors and loops
DELIMITER //

CREATE PROCEDURE CalculateCustomerLTV()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_customer_id INT;
    DECLARE v_total_spent DECIMAL(15,2);
    DECLARE v_order_count INT;
    DECLARE v_first_order DATE;
    DECLARE v_last_order DATE;
    DECLARE v_ltv DECIMAL(15,2);
    
    -- Cursor for customers
    DECLARE customer_cursor CURSOR FOR 
        SELECT customer_id FROM customers WHERE status = 'Active';
        
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Create temporary table for results
    DROP TEMPORARY TABLE IF EXISTS customer_ltv_temp;
    CREATE TEMPORARY TABLE customer_ltv_temp (
        customer_id INT,
        total_spent DECIMAL(15,2),
        order_count INT,
        avg_order_value DECIMAL(15,2),
        customer_lifespan_days INT,
        ltv_score DECIMAL(15,2)
    );
    
    OPEN customer_cursor;
    
    customer_loop: LOOP
        FETCH customer_cursor INTO v_customer_id;
        IF done THEN
            LEAVE customer_loop;
        END IF;
        
        -- Calculate customer metrics
        SELECT 
            COALESCE(SUM(total_amount), 0),
            COUNT(order_id),
            MIN(order_date),
            MAX(order_date)
        INTO v_total_spent, v_order_count, v_first_order, v_last_order
        FROM orders 
        WHERE customer_id = v_customer_id;
        
        -- Calculate LTV (simplified formula)
        IF v_order_count > 0 THEN
            SET v_ltv = v_total_spent * 
                       (DATEDIFF(COALESCE(v_last_order, CURDATE()), v_first_order) / 365.0) * 
                       1.5; -- Growth factor
        ELSE
            SET v_ltv = 0;
        END IF;
        
        -- Insert into temporary table
        INSERT INTO customer_ltv_temp VALUES (
            v_customer_id,
            v_total_spent,
            v_order_count,
            CASE WHEN v_order_count > 0 THEN v_total_spent / v_order_count ELSE 0 END,
            DATEDIFF(COALESCE(v_last_order, CURDATE()), v_first_order),
            v_ltv
        );
        
    END LOOP;
    
    CLOSE customer_cursor;
    
    -- Update main customer table with LTV scores
    UPDATE customers c
    INNER JOIN customer_ltv_temp t ON c.customer_id = t.customer_id
    SET c.ltv_score = t.ltv_score,
        c.last_calculated = NOW();
    
    -- Return summary
    SELECT 
        COUNT(*) as customers_processed,
        AVG(ltv_score) as avg_ltv,
        MAX(ltv_score) as max_ltv,
        MIN(ltv_score) as min_ltv
    FROM customer_ltv_temp;
    
END //

DELIMITER ;

-- Execute the procedure
CALL CalculateCustomerLTV();
```

#### PostgreSQL Stored Procedures

```sql
-- PostgreSQL function (serves as stored procedure)
CREATE OR REPLACE FUNCTION process_monthly_sales_report(
    report_month DATE
) RETURNS TABLE (
    category VARCHAR(50),
    total_sales DECIMAL(15,2),
    order_count BIGINT,
    avg_order_value DECIMAL(15,2),
    top_product VARCHAR(100)
) 
LANGUAGE plpgsql
AS $$
DECLARE
    start_date DATE;
    end_date DATE;
BEGIN
    -- Calculate date range
    start_date := DATE_TRUNC('month', report_month);
    end_date := start_date + INTERVAL '1 month' - INTERVAL '1 day';
    
    -- Log the report generation
    INSERT INTO report_log (report_type, generated_date, parameters)
    VALUES ('monthly_sales', NOW(), 'Month: ' || start_date::TEXT);
    
    RETURN QUERY
    WITH category_sales AS (
        SELECT 
            p.category,
            SUM(oi.quantity * oi.unit_price) as cat_total_sales,
            COUNT(DISTINCT o.order_id) as cat_order_count,
            AVG(o.total_amount) as cat_avg_order
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        WHERE o.order_date BETWEEN start_date AND end_date
        GROUP BY p.category
    ),
    top_products AS (
        SELECT DISTINCT ON (p.category)
            p.category,
            p.product_name
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        WHERE o.order_date BETWEEN start_date AND end_date
        ORDER BY p.category, SUM(oi.quantity * oi.unit_price) DESC
    )
    SELECT 
        cs.category,
        cs.cat_total_sales,
        cs.cat_order_count,
        cs.cat_avg_order,
        tp.product_name
    FROM category_sales cs
    LEFT JOIN top_products tp ON cs.category = tp.category
    ORDER BY cs.cat_total_sales DESC;
    
END;
$$;

-- Execute the function
SELECT * FROM process_monthly_sales_report('2024-06-01');
```

---

### Functions

#### SQL Server Functions

```sql
-- Scalar function
CREATE FUNCTION CalculateOrderDiscount(
    @OrderTotal DECIMAL(10,2),
    @CustomerTier VARCHAR(20)
)
RETURNS DECIMAL(5,2)
AS
BEGIN
    DECLARE @DiscountPercent DECIMAL(5,2) = 0.00;
    
    -- Base discount by customer tier
    SELECT @DiscountPercent = 
        CASE @CustomerTier
            WHEN 'PLATINUM' THEN 0.15
            WHEN 'GOLD' THEN 0.10
            WHEN 'SILVER' THEN 0.05
            ELSE 0.00
        END;
    
    -- Additional discount for large orders
    IF @OrderTotal > 1000
        SET @DiscountPercent = @DiscountPercent + 0.02;
    
    IF @OrderTotal > 5000
        SET @DiscountPercent = @DiscountPercent + 0.03;
    
    -- Maximum discount cap
    IF @DiscountPercent > 0.25
        SET @DiscountPercent = 0.25;
    
    RETURN @DiscountPercent;
END;
GO

-- Table-valued function
CREATE FUNCTION GetCustomerOrderHistory(
    @CustomerID INT,
    @MonthsBack INT = 12
)
RETURNS TABLE
AS
RETURN
(
    WITH MonthlyOrders AS (
        SELECT 
            YEAR(order_date) as order_year,
            MONTH(order_date) as order_month,
            COUNT(*) as order_count,
            SUM(total_amount) as monthly_total,
            AVG(total_amount) as avg_order_value
        FROM orders
        WHERE customer_id = @CustomerID
            AND order_date >= DATEADD(MONTH, -@MonthsBack, GETDATE())
        GROUP BY YEAR(order_date), MONTH(order_date)
    )
    SELECT 
        order_year,
        order_month,
        DATENAME(MONTH, DATEFROMPARTS(order_year, order_month, 1)) as month_name,
        order_count,
        monthly_total,
        avg_order_value,
        SUM(monthly_total) OVER (ORDER BY order_year, order_month 
                                ROWS UNBOUNDED PRECEDING) as running_total
    FROM MonthlyOrders
);
GO

-- Using the functions
SELECT 
    order_id,
    total_amount,
    dbo.CalculateOrderDiscount(total_amount, 'GOLD') as discount_rate,
    total_amount * dbo.CalculateOrderDiscount(total_amount, 'GOLD') as discount_amount
FROM orders
WHERE customer_id = 123;

SELECT * FROM dbo.GetCustomerOrderHistory(123, 6);
```

#### MySQL Functions

```sql
-- MySQL function example
DELIMITER //

CREATE FUNCTION FormatCurrency(amount DECIMAL(15,2), currency_code VARCHAR(3))
RETURNS VARCHAR(50)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE formatted_amount VARCHAR(50);
    
    CASE currency_code
        WHEN 'USD' THEN
            SET formatted_amount = CONCAT('$', FORMAT(amount, 2));
        WHEN 'EUR' THEN
            SET formatted_amount = CONCAT('€', FORMAT(amount, 2));
        WHEN 'GBP' THEN
            SET formatted_amount = CONCAT('£', FORMAT(amount, 2));
        ELSE
            SET formatted_amount = CONCAT(currency_code, ' ', FORMAT(amount, 2));
    END CASE;
    
    RETURN formatted_amount;
END //

-- Function with error handling
CREATE FUNCTION SafeDivide(dividend DECIMAL(15,2), divisor DECIMAL(15,2))
RETURNS DECIMAL(15,4)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(15,4);
    
    IF divisor = 0 OR divisor IS NULL THEN
        RETURN NULL;
    END IF;
    
    SET result = dividend / divisor;
    RETURN result;
END //

DELIMITER ;

-- Using MySQL functions
SELECT 
    product_name,
    FormatCurrency(unit_price, 'USD') as formatted_price,
    SafeDivide(total_sold, days_available) as avg_daily_sales
FROM product_summary;
```

---

## 2. Handle NULL Values Effectively

### Understanding NULL Behavior

NULL represents unknown or missing data, and it has special behavior in SQL that differs from other values.

#### NULL Comparison Behavior

```sql
-- Understanding NULL comparisons
SELECT 
    customer_name,
    phone_number,
    -- These conditions will NOT match NULL values
    CASE WHEN phone_number = NULL THEN 'Has Phone' ELSE 'No Phone' END as wrong_way,
    -- Correct way to check for NULL
    CASE WHEN phone_number IS NULL THEN 'No Phone' ELSE 'Has Phone' END as correct_way,
    -- Three-valued logic demonstration
    CASE 
        WHEN phone_number IS NOT NULL THEN 'Has Phone'
        WHEN phone_number IS NULL THEN 'No Phone'
        ELSE 'Unknown State'  -- This will never execute
    END as null_check
FROM customers;

-- NULL in arithmetic operations
SELECT 
    product_name,
    unit_price,
    discount_rate,
    -- Any arithmetic with NULL results in NULL
    unit_price * discount_rate as discounted_price_wrong,
    -- Handle NULL properly
    unit_price * COALESCE(discount_rate, 0) as discounted_price_correct,
    -- Alternative approaches
    CASE 
        WHEN discount_rate IS NULL THEN unit_price
        ELSE unit_price * (1 - discount_rate)
    END as final_price
FROM products;
```

### NULL Handling Functions

#### COALESCE Function

```sql
-- COALESCE returns the first non-NULL value
SELECT 
    customer_id,
    customer_name,
    -- Use first available contact method
    COALESCE(mobile_phone, home_phone, work_phone, 'No Phone') as primary_contact,
    -- Handle missing addresses
    COALESCE(shipping_address, billing_address, 'Address Required') as contact_address,
    -- Default values for calculations
    COALESCE(discount_rate, 0.0) as effective_discount,
    -- Multiple fallbacks
    COALESCE(
        preferred_contact_method, 
        CASE WHEN email IS NOT NULL THEN 'Email' END,
        CASE WHEN mobile_phone IS NOT NULL THEN 'Mobile' END,
        'Mail'
    ) as contact_preference
FROM customers;
```

#### NULLIF Function

```sql
-- NULLIF returns NULL if two values are equal
SELECT 
    product_id,
    product_name,
    stock_quantity,
    reorder_level,
    -- Avoid division by zero
    stock_quantity / NULLIF(reorder_level, 0) as stock_ratio,
    -- Convert empty strings to NULL
    NULLIF(TRIM(description), '') as clean_description,
    -- Handle sentinel values
    NULLIF(last_sold_date, '1900-01-01') as actual_last_sold
FROM products;
```

#### ISNULL / NVL Functions (Database-specific)

```sql
-- SQL Server ISNULL
SELECT 
    customer_name,
    ISNULL(discount_rate, 0.0) as discount,
    ISNULL(credit_limit, 1000.00) as credit_limit
FROM customers;

-- Oracle NVL / NVL2
SELECT 
    customer_name,
    NVL(discount_rate, 0.0) as discount,
    NVL2(last_order_date, 'Active', 'Inactive') as status
FROM customers;

-- PostgreSQL/MySQL use COALESCE or IFNULL (MySQL)
SELECT 
    customer_name,
    IFNULL(discount_rate, 0.0) as discount  -- MySQL
FROM customers;
```

### Advanced NULL Handling Patterns

#### Conditional Aggregation with NULLs

```sql
-- Proper aggregation with NULL values
SELECT 
    department,
    COUNT(*) as total_employees,
    COUNT(salary) as employees_with_salary,  -- Excludes NULLs
    COUNT(*) - COUNT(salary) as employees_without_salary,
    AVG(salary) as avg_salary,  -- Ignores NULLs automatically
    SUM(CASE WHEN salary IS NOT NULL THEN 1 ELSE 0 END) as salary_count_manual,
    -- Conditional aggregation
    AVG(CASE WHEN performance_rating >= 4 THEN salary END) as avg_high_performer_salary,
    COUNT(CASE WHEN phone_number IS NOT NULL THEN 1 END) as employees_with_phone
FROM employees
GROUP BY department;
```

#### NULL-Safe Equality Comparisons

```sql
-- Standard comparison fails with NULLs
SELECT * FROM customers c1
JOIN customer_backup c2 ON c1.customer_id = c2.customer_id
WHERE c1.phone_number = c2.phone_number;  -- Misses records where both are NULL

-- NULL-safe comparison
SELECT * FROM customers c1
JOIN customer_backup c2 ON c1.customer_id = c2.customer_id
WHERE (c1.phone_number = c2.phone_number 
       OR (c1.phone_number IS NULL AND c2.phone_number IS NULL));

-- Using COALESCE for NULL-safe comparison
SELECT * FROM customers c1
JOIN customer_backup c2 ON c1.customer_id = c2.customer_id
WHERE COALESCE(c1.phone_number, '') = COALESCE(c2.phone_number, '');

-- SQL Server: NULL-safe equality operator
SELECT * FROM customers c1
JOIN customer_backup c2 ON c1.customer_id = c2.customer_id
WHERE c1.phone_number <=> c2.phone_number;  -- MySQL syntax

-- Standard SQL approach
SELECT * FROM customers c1
JOIN customer_backup c2 ON c1.customer_id = c2.customer_id
WHERE c1.phone_number IS NOT DISTINCT FROM c2.phone_number;  -- PostgreSQL
```

---

## 3. CASE Statements for Conditional Logic

### Basic CASE Syntax

#### Simple CASE Expression

```sql
-- Simple CASE (equality comparison)
SELECT 
    product_id,
    product_name,
    category,
    CASE category
        WHEN 'Electronics' THEN 'High Tech'
        WHEN 'Books' THEN 'Media'
        WHEN 'Clothing' THEN 'Apparel'
        WHEN 'Food' THEN 'Consumables'
        ELSE 'Other'
    END as category_group,
    unit_price,
    CASE category
        WHEN 'Electronics' THEN unit_price * 0.10  -- 10% markup
        WHEN 'Books' THEN unit_price * 0.05        -- 5% markup
        ELSE unit_price * 0.08                     -- 8% default markup
    END as markup_amount
FROM products;
```

#### Searched CASE Expression

```sql
-- Searched CASE (conditional logic)
SELECT 
    customer_id,
    customer_name,
    total_orders,
    total_spent,
    last_order_date,
    -- Customer segmentation
    CASE 
        WHEN total_spent >= 10000 AND total_orders >= 20 THEN 'VIP'
        WHEN total_spent >= 5000 OR total_orders >= 15 THEN 'Premium'
        WHEN total_spent >= 1000 AND last_order_date >= DATEADD(MONTH, -6, GETDATE()) THEN 'Active'
        WHEN last_order_date < DATEADD(YEAR, -1, GETDATE()) THEN 'Inactive'
        ELSE 'Standard'
    END as customer_segment,
    -- Discount eligibility
    CASE 
        WHEN total_spent >= 10000 THEN 0.15
        WHEN total_spent >= 5000 THEN 0.10
        WHEN total_spent >= 1000 THEN 0.05
        ELSE 0.00
    END as discount_rate,
    -- Risk assessment
    CASE 
        WHEN total_orders = 0 THEN 'No History'
        WHEN total_spent / total_orders < 50 THEN 'Low Value'
        WHEN total_spent / total_orders > 500 THEN 'High Value'
        ELSE 'Medium Value'
    END as value_assessment
FROM customer_summary;
```

### Advanced CASE Applications

#### Conditional Aggregation

```sql
-- Using CASE for conditional counting and summing
SELECT 
    department,
    COUNT(*) as total_employees,
    -- Conditional counting
    COUNT(CASE WHEN salary >= 50000 THEN 1 END) as high_earners,
    COUNT(CASE WHEN salary < 30000 THEN 1 END) as low_earners,
    -- Conditional summing
    SUM(CASE WHEN performance_rating >= 4 THEN salary ELSE 0 END) as high_performer_payroll,
    SUM(CASE WHEN hire_date >= '2024-01-01' THEN 1 ELSE 0 END) as new_hires_2024,
    -- Conditional averaging
    AVG(CASE WHEN years_experience > 5 THEN salary END) as avg_experienced_salary,
    -- Complex conditions
    SUM(CASE 
        WHEN performance_rating >= 4 AND years_experience > 3 THEN bonus_amount 
        ELSE 0 
    END) as performance_bonus_total
FROM employees
GROUP BY department;
```

#### Dynamic Sorting with CASE

```sql
-- Dynamic ORDER BY using CASE
DECLARE @SortColumn VARCHAR(20) = 'total_spent';  -- Parameter
DECLARE @SortDirection VARCHAR(4) = 'DESC';       -- Parameter

SELECT 
    customer_id,
    customer_name,
    total_orders,
    total_spent,
    last_order_date
FROM customer_summary
ORDER BY 
    CASE 
        WHEN @SortColumn = 'name' AND @SortDirection = 'ASC' THEN customer_name 
    END ASC,
    CASE 
        WHEN @SortColumn = 'name' AND @SortDirection = 'DESC' THEN customer_name 
    END DESC,
    CASE 
        WHEN @SortColumn = 'orders' AND @SortDirection = 'ASC' THEN total_orders 
    END ASC,
    CASE 
        WHEN @SortColumn = 'orders' AND @SortDirection = 'DESC' THEN total_orders 
    END DESC,
    CASE 
        WHEN @SortColumn = 'total_spent' AND @SortDirection = 'ASC' THEN total_spent 
    END ASC,
    CASE 
        WHEN @SortColumn = 'total_spent' AND @SortDirection = 'DESC' THEN total_spent 
    END DESC;
```

#### Conditional Updates

```sql
-- Bulk updates with conditional logic
UPDATE products 
SET 
    unit_price = CASE 
        WHEN category = 'Electronics' AND stock_quantity > 100 THEN unit_price * 0.95  -- 5% discount
        WHEN category = 'Books' AND DATEDIFF(DAY, created_date, GETDATE()) > 365 THEN unit_price * 0.80  -- Old books
        WHEN stock_quantity < 10 THEN unit_price * 1.10  -- Low stock premium
        ELSE unit_price
    END,
    status = CASE 
        WHEN stock_quantity = 0 THEN 'Out of Stock'
        WHEN stock_quantity < reorder_level THEN 'Low Stock'
        ELSE 'In Stock'
    END,
    last_updated = GETDATE()
WHERE category IN ('Electronics', 'Books') OR stock_quantity < reorder_level;
```

### Nested CASE Statements

```sql
-- Complex nested CASE logic
SELECT 
    order_id,
    customer_id,
    order_date,
    total_amount,
    urgency_level,
    -- Complex shipping logic
    CASE 
        WHEN urgency_level = 'URGENT' THEN
            CASE 
                WHEN total_amount > 1000 THEN 'Express - Free'
                WHEN total_amount > 500 THEN 'Express - $15'
                ELSE 'Express - $25'
            END
        WHEN urgency_level = 'NORMAL' THEN
            CASE 
                WHEN total_amount > 2000 THEN 'Priority - Free'
                WHEN total_amount > 100 THEN 'Standard - $8'
                ELSE 'Standard - $12'
            END
        ELSE
            CASE 
                WHEN total_amount > 500 THEN 'Economy - Free'
                ELSE 'Economy - $5'
            END
    END as shipping_option,
    -- Estimated delivery
    CASE 
        WHEN urgency_level = 'URGENT' THEN DATEADD(DAY, 1, order_date)
        WHEN urgency_level = 'NORMAL' THEN 
            CASE 
                WHEN DATEPART(WEEKDAY, order_date) IN (1, 7) THEN DATEADD(DAY, 4, order_date)  -- Weekend
                ELSE DATEADD(DAY, 3, order_date)  -- Weekday
            END
        ELSE DATEADD(DAY, 7, order_date)
    END as estimated_delivery
FROM orders;
```

---

## 4. Pivot and Unpivot Operations

### PIVOT Operations

PIVOT transforms rows into columns, useful for creating crosstab reports and summary views.

#### Basic PIVOT Example

```sql
-- Sample data structure
CREATE TABLE sales_data (
    sales_rep VARCHAR(50),
    quarter VARCHAR(10),
    sales_amount DECIMAL(10,2)
);

INSERT INTO sales_data VALUES
('John Smith', 'Q1', 150000),
('John Smith', 'Q2', 175000),
('John Smith', 'Q3', 160000),
('John Smith', 'Q4', 180000),
('Jane Doe', 'Q1', 140000),
('Jane Doe', 'Q2', 165000),
('Jane Doe', 'Q3', 170000),
('Jane Doe', 'Q4', 190000);

-- PIVOT operation (SQL Server)
SELECT 
    sales_rep,
    ISNULL([Q1], 0) as Q1_Sales,
    ISNULL([Q2], 0) as Q2_Sales,
    ISNULL([Q3], 0) as Q3_Sales,
    ISNULL([Q4], 0) as Q4_Sales,
    ISNULL([Q1], 0) + ISNULL([Q2], 0) + ISNULL([Q3], 0) + ISNULL([Q4], 0) as Total_Sales
FROM (
    SELECT sales_rep, quarter, sales_amount
    FROM sales_data
) as source_data
PIVOT (
    SUM(sales_amount)
    FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) as pivot_table
ORDER BY sales_rep;
```

#### Dynamic PIVOT

```sql
-- Dynamic PIVOT for unknown number of quarters
DECLARE @columns NVARCHAR(MAX) = '';
DECLARE @sql NVARCHAR(MAX) = '';

-- Build column list dynamically
SELECT @columns = COALESCE(@columns + ', ', '') + '[' + quarter + ']'
FROM (SELECT DISTINCT quarter FROM sales_data) as quarters
ORDER BY quarter;

-- Build dynamic SQL
SET @sql = '
SELECT sales_rep, ' + @columns + '
FROM (
    SELECT sales_rep, quarter, sales_amount
    FROM sales_data
) as source_data
PIVOT (
    SUM(sales_amount)
    FOR quarter IN (' + @columns + ')
) as pivot_table
ORDER BY sales_rep';

EXEC sp_executesql @sql;
```

#### PIVOT with Multiple Aggregates

```sql
-- PIVOT with multiple metrics
WITH sales_metrics AS (
    SELECT 
        sales_rep,
        quarter,
        sales_amount,
        order_count,
        -- Create metric indicators
        'Sales_' + quarter as sales_quarter,
        'Orders_' + quarter as orders_quarter
    FROM sales_summary
)
SELECT *
FROM (
    SELECT sales_rep, sales_quarter, sales_amount FROM sales_metrics
    UNION ALL
    SELECT sales_rep