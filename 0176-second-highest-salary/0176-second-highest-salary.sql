# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN COUNT(*) = 1 THEN NULL
        ELSE (
            SELECT MAX(salary) AS SecondHighestSalary
            FROM Employee
            WHERE salary != (SELECT MAX(salary) FROM Employee)
        )
    END AS SecondHighestSalary
FROM Employee;