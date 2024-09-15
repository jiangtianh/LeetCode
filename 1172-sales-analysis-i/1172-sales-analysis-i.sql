# Write your MySQL query statement below

SELECT 
    seller_id
FROM Sales s1
GROUP BY seller_id
HAVING SUM(s1.price) = 
(SELECT
    SUM(price) AS ssum
FROM Sales
GROUP BY seller_id
ORDER BY ssum DESC
LIMIT 1)