# Write your MySQL query statement below
SELECT 
    Users.user_id AS buyer_id,
    join_date,
    COUNT(Orders.order_id) AS orders_in_2019
FROM
    Users
    LEFT JOIN Orders ON Users.user_id = Orders.buyer_id AND order_date LIKE '2019-%'

GROUP BY user_id
