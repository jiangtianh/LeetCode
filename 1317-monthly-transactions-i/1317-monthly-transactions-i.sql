# Write your MySQL query statement below

SELECT 
    sub.month, 
    sub.country, 
    count(*) AS trans_count, 
    SUM(IF(sub.state = 'approved', 1, 0)) AS approved_count, 
    SUM(sub.amount) AS trans_total_amount, 
    SUM(IF(sub.state = 'approved', sub.amount, 0)) AS approved_total_amount
FROM (
    SELECT 
        id, 
        country, 
        state, 
        amount, 
        CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')) AS month
    FROM Transactions
) AS sub
GROUP BY sub.country, sub.month
