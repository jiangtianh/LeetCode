# Write your MySQL query statement below

SELECT 
    reportee_id AS employee_id, reportee_name AS name, COUNT(employee_id) AS reports_count, ROUND(AVG(age)) AS average_age
FROM
(SELECT 
    a.age, a.employee_id, b.name AS reportee_name, b.employee_id AS reportee_id
FROM
    Employees a
        LEFT JOIN Employees b ON a.reports_to = b.employee_id) AS sub
WHERE reportee_id IS NOT NULL
GROUP BY reportee_id
ORDER BY employee_id