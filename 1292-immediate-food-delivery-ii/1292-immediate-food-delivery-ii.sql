# Write your MySQL query statement below

SELECT ROUND(SUM(IF(Delivery.order_date = Delivery.customer_pref_delivery_date, 1, 0)) / COUNT(*) * 100, 2) AS immediate_percentage 
FROM Delivery JOIN (
    SELECT
        customer_id, MIN(order_date) AS earliestOrder
    FROM Delivery
    GROUP BY customer_id
) AS sub 
ON sub.customer_id = Delivery.customer_id AND sub.earliestOrder = Delivery.order_date
