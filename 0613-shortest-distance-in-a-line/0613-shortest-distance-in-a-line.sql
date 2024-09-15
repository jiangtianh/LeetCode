# Write your MySQL query statement below
SELECT
    MIN(ABS(a.x - b.x)) AS shortest
FROM
    Point a
        JOIN Point b ON a.x != b.x