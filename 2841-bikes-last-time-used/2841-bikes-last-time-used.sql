# Write your MySQL query statement below
SELECT 
    bike_number,
    MAX(end_time) as end_time
FROM Bikes
GROUP BY bike_number
ORDER BY end_time DESC