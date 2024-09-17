# Write your MySQL query statement below
SELECT q.id, q.year, IFNULL(npv, 0) AS npv
FROM Queries q
LEFT JOIN NPV n
ON n.id = q.id AND q.year = n.year