# Write your MySQL query statement below

SELECT Department, e1.name as Employee, salary AS Salary
FROM Employee e1
JOIN (
    SELECT MAX(salary) AS highest, Department.name AS Department, Department.id
    FROM Employee JOIN Department ON Department.id = Employee.departmentId
    GROUP BY departmentId
) AS e2 ON e1.departmentId = e2.id
WHERE e1.salary = highest

