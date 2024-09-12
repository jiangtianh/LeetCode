# Write your MySQL query statement below

SELECT 
    name, 
    IF (travelled_distance IS NOT NULL, travelled_distance, 0) as travelled_distance
FROM Users LEFT JOIN 
    (
        SELECT 
            user_id,
            SUM(distance) as travelled_distance
        FROM    
            Rides
        GROUP BY 
            user_id
    ) AS sub ON Users.id = user_id
ORDER BY 
    travelled_distance DESC, name ASC