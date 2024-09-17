# Write your MySQL query statement below


SELECT a.employee_id, b.team_size
FROM Employee a JOIN 
(SELECT team_id, COUNT(employee_id) AS team_size
FROM Employee 
GROUP BY team_id) as b 
ON a.team_id = b.team_id