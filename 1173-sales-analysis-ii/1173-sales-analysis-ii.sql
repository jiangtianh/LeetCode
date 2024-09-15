# Write your MySQL query statement below


SELECT DISTINCT(buyer_id)
FROM Sales s JOIN Product p ON s.Product_id = p.Product_id and p.product_name = 'S8' AND s.buyer_id NOT IN (
    SELECT
        buyer_id
    FROM Sales s JOIN Product p ON s.Product_id = p.Product_id AND p.product_name = 'Iphone'
)