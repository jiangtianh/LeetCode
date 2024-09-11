# Write your MySQL query statement below

SELECT actor_id, director_id 
FROM
    (SELECT COUNT(timestamp) AS c, actor_id, director_id
    FROM ActorDirector
    GROUP BY actor_id, director_id) AS sub
WHERE c >= 3