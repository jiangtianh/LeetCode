# Write your MySQL query statement below

SELECT g.customer_id, name
FROM (
    SELECT 
        o.customer_id, SUM(o.quantity * p.price) AS total_spent,
        CASE 
            WHEN o.order_date BETWEEN "2020-06-01" AND "2020-06-30" THEN "June"
            WHEN o.order_date BETWEEN "2020-07-01" AND "2020-07-31" THEN "July"
        END AS order_month
    FROM Orders o
    JOIN Product p
    ON o.product_id = p.product_id
    WHERE o.order_date BETWEEN "2020-06-01" AND "2020-07-31"
    GROUP BY customer_id, order_month
) AS g 
JOIN Customers c ON g.customer_id = c.customer_id
GROUP BY g.customer_id
HAVING SUM(IF(g.order_month = 'June', total_spent, 0)) >= 100
   AND SUM(IF(g.order_month = 'July', total_spent, 0)) >= 100;