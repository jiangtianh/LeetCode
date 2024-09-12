SELECT 
    customer_number
FROM 
    (
        SELECT 
            customer_number,
            COUNT(order_number) AS c
        FROM Orders
        GROUP BY customer_number
    ) AS sub
ORDER BY 
    c DESC
LIMIT 1