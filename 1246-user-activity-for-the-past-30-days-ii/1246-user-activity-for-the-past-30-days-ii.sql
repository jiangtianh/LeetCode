# Write your MySQL query statement below
SELECT
    IF(COUNT(*) != 0, ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) AS average_sessions_per_user
FROM
    (SELECT *
    FROM Activity 
    WHERE activity_date > "2019-06-27" AND activity_date <= "2019-07-27") AS sub