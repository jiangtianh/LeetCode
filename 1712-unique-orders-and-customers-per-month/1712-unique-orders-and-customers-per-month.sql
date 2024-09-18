# Write your MySQL query statement below
SELECT
    month, COUNT(DISTINCT order_id) AS order_count, COUNT(DISTINCT customer_id) AS customer_count
FROM 
(
    SELECT
        CONCAT(YEAR(order_date), "-", LPAD(MONTH(order_date), 2, "0")) AS month, 
        customer_id,
        order_id,
        invoice
    FROM Orders
    WHERE invoice > 20
) AS sub
GROUP BY month
