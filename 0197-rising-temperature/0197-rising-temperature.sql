# Write your MySQL query statement below
SELECT id as Id
FROM 
(
    SELECT a.id, a.temperature AS atemp, b.temperature AS btemp
    FROM Weather a
        LEFT JOIN Weather b ON DATEDIFF(a.recordDate, b.recordDate) = 1
) AS sub
WHERE atemp > btemp