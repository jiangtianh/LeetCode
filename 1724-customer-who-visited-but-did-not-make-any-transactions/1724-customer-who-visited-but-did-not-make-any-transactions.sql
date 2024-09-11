# Write your MySQL query statement below
SELECT customer_id, COUNT(visit_id) as count_no_trans
FROM 
(   SELECT Visits.visit_id, customer_id, transaction_id
    FROM Visits
    LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
) AS sub
WHERE transaction_id IS NULL
GROUP BY customer_id