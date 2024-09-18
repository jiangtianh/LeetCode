# Write your MySQL query statement below
SELECT product_name, sale_date, COUNT(*) AS total
FROM
(
    SELECT REPLACE(LOWER(product_name), " ", "") AS product_name, CONCAT(YEAR(sale_date), '-', LPAD(MONTH(sale_date), 2, '0')) AS sale_date
    FROM Sales
) AS sub
GROUP BY product_name, sale_date
ORDER BY product_name, sale_date