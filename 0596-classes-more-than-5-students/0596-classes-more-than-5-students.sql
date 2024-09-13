# Write your MySQL query statement below
SELECT 
    class
FROM
    (SELECT
        COUNT(student) AS count,
        class
    FROM 
        Courses
    GROUP BY 
        class) AS sub
WHERE count >= 5