-- Data quality checks for cleaned SQLite tables.

-- Check missing customer IDs
SELECT COUNT(*) AS missing_customer_id
FROM customers
WHERE customer_id IS NULL OR TRIM(customer_id) = '';

-- Check duplicate customer IDs
SELECT customer_id, COUNT(*) AS record_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Check invalid customer segments
SELECT *
FROM customers
WHERE segment NOT IN ('New', 'Returning', 'High Value');

-- Check transactions linked to unknown customers
SELECT t.*
FROM transactions t
LEFT JOIN customers c
    ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Check negative transaction values
SELECT *
FROM transactions
WHERE amount < 0 OR cost < 0;

-- Check invalid transaction statuses
SELECT *
FROM transactions
WHERE status NOT IN ('Completed', 'Returned', 'Cancelled');