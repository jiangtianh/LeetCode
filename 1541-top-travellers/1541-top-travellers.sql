# Write your MySQL query statement below

SELECT 
    name,
    IF (distance IS NULL, 0, SUM(distance)) AS travelled_distance

FROM (
    SELECT 
        Users.id,
        Users.name, 
        Rides.distance
    FROM 
        Rides
        RIGHT JOIN Users ON Users.id = Rides.user_id
    ) AS sub

GROUP BY id
ORDER BY travelled_distance DESC, name ASC
