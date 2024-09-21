# Write your MySQL query statement below
SELECT
    machine_id, ROUND(AVG(time), 3) AS processing_time
FROM
(
    SELECT
        a.machine_id, a.process_id, b.timestamp - a.timestamp AS time
    FROM Activity a, Activity b 
    WHERE 
        a.machine_id = b.machine_id AND
        a.process_id = b.process_id AND
        a.activity_type = 'start' AND
        b.activity_type = 'end'
) AS sub
GROUP BY machine_id