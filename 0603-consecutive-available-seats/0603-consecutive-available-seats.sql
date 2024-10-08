# Write your MySQL query statement below
SELECT 
    DISTINCT a.seat_id
FROM
    cinema a 
        JOIN cinema b ON abs(a.seat_id - b.seat_id) = 1
            AND a.free = TRUE and b.free = TRUE
ORDER BY a.seat_id