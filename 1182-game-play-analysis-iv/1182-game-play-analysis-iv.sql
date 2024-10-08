# Write your MySQL query statement below


SELECT ROUND(SUM(IF(DATE_ADD(minEventDate.minDate, INTERVAL 1 DAY) = Activity.event_date, 1, 0)) / COUNT(DISTINCT(Activity.player_id)),2) AS fraction
FROM Activity 
JOIN (
    SELECT player_id, MIN(event_date) AS minDate
    FROM Activity 
    GROUP BY player_id
) AS minEventDate
ON Activity.player_id = minEventDate.player_id


