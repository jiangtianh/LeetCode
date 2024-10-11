# Write your MySQL query statement below
SELECT customer_id
FROM
(
    SELECT COUNT(*) AS totalCount
    FROM Product
) AS a,
(
    SELECT customer_id, COUNT(DISTINCT(product_key)) AS cnt
    FROM Customer 
    GROUP BY customer_id
) AS b
WHERE b.cnt = a.totalCount

