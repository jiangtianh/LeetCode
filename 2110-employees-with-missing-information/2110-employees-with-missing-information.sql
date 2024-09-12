# Write your MySQL query statement below


SELECT
    sub.employee_id
FROM
    (
        SELECT
            *
        FROM Employees LEFT JOIN Salaries USING(employee_id)

        UNION

        SELECT
            *
        FROM Employees RIGHT JOIN Salaries USING(employee_id)
    ) as sub
WHERE 
    sub.name IS NULL OR sub.salary IS NULL
ORDER BY employee_id