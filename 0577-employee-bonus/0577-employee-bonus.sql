# Write your MySQL query statement below

SELECT 
    name, 
    bonus
FROM (
SELECT 
    Employee.empId, 
    Employee.name,
    Bonus.bonus
FROM 
    Employee
    LEFT JOIN Bonus ON Bonus.empId = Employee.empId
) AS sub
WHERE bonus IS NULL or bonus < 1000