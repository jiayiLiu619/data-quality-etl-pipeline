-- Reporting queries for business analysis.

-- Revenue and gross profit by channel
SELECT
    channel,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND(SUM(gross_profit) * 1.0 / NULLIF(SUM(amount), 0), 4) AS gross_margin_rate
FROM transactions
WHERE status = 'Completed'
GROUP BY channel
ORDER BY total_revenue DESC;

-- Average order value by channel
SELECT
    channel,
    ROUND(AVG(amount), 2) AS average_order_value
FROM transactions
WHERE status = 'Completed'
GROUP BY channel
ORDER BY average_order_value DESC;

-- Transaction count and revenue by customer segment
SELECT
    c.segment,
    COUNT(t.transaction_id) AS transaction_count,
    ROUND(SUM(t.amount), 2) AS total_revenue,
    ROUND(SUM(t.gross_profit), 2) AS total_gross_profit
FROM transactions t
JOIN customers c
    ON t.customer_id = c.customer_id
GROUP BY c.segment
ORDER BY total_revenue DESC;

-- Return rate by channel
SELECT
    channel,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END) AS returned_transactions,
    ROUND(
        SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END) * 1.0 / COUNT(*),
        4
    ) AS return_rate
FROM transactions
GROUP BY channel
ORDER BY return_rate DESC;