# Write your MySQL query statement below
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE
(Sales.product_id, year) IN 
(
    SELECT
        a.product_id, MIN(year) AS minYear
    FROM Sales a
    GROUP BY a.product_id
)
