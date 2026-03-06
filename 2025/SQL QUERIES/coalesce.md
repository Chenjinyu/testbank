The COALESCE function is quite versatile! Here are various examples beyond just replacing with 0:

## Replace with Default Text
```sql
SELECT 
    COALESCE(middle_name, 'N/A') as middle_name,
    COALESCE(description, 'No description available') as description
FROM users;
```

## Replace with Another Column's Value
```sql
SELECT 
    COALESCE(preferred_name, first_name) as display_name,
    COALESCE(work_email, personal_email) as contact_email
FROM employees;
```

## Chain Multiple Fallbacks
```sql
SELECT 
    COALESCE(mobile_phone, work_phone, home_phone, 'No phone') as phone,
    COALESCE(priority_1, priority_2, priority_3, 'Low') as task_priority
FROM contacts;
```

## Replace with Current Date/Time
```sql
SELECT 
    COALESCE(last_login, CURRENT_TIMESTAMP) as effective_login,
    COALESCE(end_date, '9999-12-31') as contract_end
FROM user_sessions;
```

## Replace with Calculated Values
```sql
SELECT 
    COALESCE(discount_rate, 0.05) * price as discounted_price,
    COALESCE(custom_tax_rate, default_tax_rate, 0.08) as tax_rate
FROM products;
```

## Replace with System Values
```sql
SELECT 
    COALESCE(created_by, USER()) as creator,
    COALESCE(status, 'PENDING') as order_status,
    COALESCE(category, 'UNCATEGORIZED') as item_category
FROM orders;
```

## Complex Concatenation with Fallbacks
```sql
SELECT 
    COALESCE(
        CONCAT(first_name, ' ', last_name),
        email,
        username,
        'Anonymous User'
    ) as display_identity
FROM users;
```

## Handle Different Data Types
```sql
SELECT 
    COALESCE(score, -1) as numeric_score,
    COALESCE(is_active, FALSE) as boolean_status,
    COALESCE(tags, '[]') as json_tags
FROM assessments;
```

## Use in WHERE Clauses
```sql
SELECT * FROM products 
WHERE COALESCE(sale_price, regular_price) < 100;

SELECT * FROM users 
WHERE COALESCE(status, 'active') = 'active';
```

## Use in ORDER BY
```sql
SELECT * FROM employees 
ORDER BY COALESCE(last_name, first_name);

SELECT * FROM products 
ORDER BY COALESCE(sort_order, 999), name;
```

The key benefit of COALESCE is that it returns the first non-NULL value from left to right, making it perfect for implementing fallback logic and handling missing data gracefully.