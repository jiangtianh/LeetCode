SELECT
    customer_id, name
FROM 
    Customers
    JOIN Orders USING(customer_id)
    JOIN Product Using(product_id)
WHERE YEAR(order_date) = 2020
GROUP BY customer_id
HAVING 
    SUM(
        IF(MONTH(order_date) = 6, quantity, 0) * price
    ) >= 100 
    AND
    SUM(
        IF(Month(order_date) = 7, quantity, 0) * price
    ) >= 100
