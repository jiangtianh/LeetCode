# Write your MySQL query statement below

SELECT 
    product_name,
    unit
FROM Products
JOIN 
(
    SELECT 
        product_id,
        SUM(unit) AS unit
    FROM Orders 
    WHERE order_date BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY product_id
) AS sub 
ON sub.product_id = Products.product_id
WHERE unit >= 100