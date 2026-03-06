Great question! Let me break down `DATE_SUB` and `INTERVAL` in MySQL:

## DATE_SUB Function
`DATE_SUB(date, INTERVAL value unit)` subtracts a time interval from a date.

## INTERVAL Syntax
The `INTERVAL` keyword specifies what time period to subtract.

## Time Unit Options

### Days
```sql
DATE_SUB(CURDATE(), INTERVAL 1 DAY)        -- Yesterday
DATE_SUB(CURDATE(), INTERVAL 7 DAY)        -- 1 week ago
DATE_SUB(CURDATE(), INTERVAL 30 DAY)       -- 30 days ago
```

### Weeks
```sql
DATE_SUB(CURDATE(), INTERVAL 1 WEEK)       -- 1 week ago
DATE_SUB(CURDATE(), INTERVAL 4 WEEK)       -- 4 weeks ago
```

### Months
```sql
DATE_SUB(CURDATE(), INTERVAL 1 MONTH)      -- 1 month ago
DATE_SUB(CURDATE(), INTERVAL 6 MONTH)      -- 6 months ago
DATE_SUB(CURDATE(), INTERVAL 12 MONTH)     -- 1 year ago
```

### Years
```sql
DATE_SUB(CURDATE(), INTERVAL 1 YEAR)       -- 1 year ago
DATE_SUB(CURDATE(), INTERVAL 5 YEAR)       -- 5 years ago
```

### Hours/Minutes/Seconds
```sql
DATE_SUB(NOW(), INTERVAL 1 HOUR)           -- 1 hour ago
DATE_SUB(NOW(), INTERVAL 30 MINUTE)        -- 30 minutes ago
DATE_SUB(NOW(), INTERVAL 45 SECOND)        -- 45 seconds ago
```

### Combined Intervals
```sql
DATE_SUB(NOW(), INTERVAL '1:30' HOUR_MINUTE)     -- 1 hour 30 minutes ago
DATE_SUB(CURDATE(), INTERVAL '2-6' YEAR_MONTH)   -- 2 years 6 months ago
DATE_SUB(NOW(), INTERVAL '1 2:30:45' DAY_SECOND) -- 1 day, 2 hours, 30 min, 45 sec ago
```

## Practical Examples

### Find records from last 3 months
```sql
SELECT * FROM orders 
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH);
```

### Get users who registered in the last week
```sql
SELECT * FROM users 
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 1 WEEK);
```

### Archive old data (older than 2 years)
```sql
DELETE FROM logs 
WHERE created_date < DATE_SUB(CURDATE(), INTERVAL 2 YEAR);
```

### Business hours calculation
```sql
SELECT * FROM appointments 
WHERE scheduled_time BETWEEN 
    DATE_SUB(NOW(), INTERVAL 8 HOUR) 
    AND NOW();
```

## DATE_ADD (Opposite Function)
```sql
DATE_ADD(CURDATE(), INTERVAL 30 DAY)       -- 30 days from now
DATE_ADD(NOW(), INTERVAL 2 HOUR)           -- 2 hours from now
```

## Alternative Syntax (MySQL specific)
```sql
CURDATE() - INTERVAL 90 DAY                -- Same as DATE_SUB
CURDATE() + INTERVAL 30 DAY                -- Same as DATE_ADD
```

The `INTERVAL` keyword is what makes MySQL's date arithmetic so readable and flexible!