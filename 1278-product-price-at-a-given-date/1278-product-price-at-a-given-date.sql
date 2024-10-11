# Write your MySQL query statement below

SELECT a.product_id, IFNULL(Products.new_price, 10) AS price

FROM (
    (
        SELECT DISTINCT(product_id) AS product_id
        FROM Products 
    ) a LEFT JOIN
    (
        SELECT product_id, MAX(change_date) as maxDate
        FROM Products 
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) b
    ON a.product_id = b.product_id
    LEFT JOIN 
        Products 
    ON Products.product_id = b.product_id AND Products.change_date = b.maxDate
) 
