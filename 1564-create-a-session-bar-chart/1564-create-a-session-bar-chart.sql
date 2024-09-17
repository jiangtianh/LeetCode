# Write your MySQL query statement below
SELECT 
    "[0-5>" AS bin, SUM(CASE WHEN duration <= 5 * 60 THEN 1 ELSE 0 END) AS total
FROM sessions
UNION
SELECT 
    "[5-10>" AS bin, SUM(CASE WHEN 5 * 60 < duration AND duration <= 10 * 60 THEN 1 ELSE 0 END) AS total
FROM sessions
UNION
SELECT 
    "[10-15>" AS bin, SUM(CASE WHEN 10 * 60 < duration AND duration <= 15 * 60 THEN 1 ELSE 0 END) AS total
FROM sessions
UNION
SELECT 
    "15 or more" AS bin, SUM(CASE WHEN 15 * 60 < duration THEN 1 ELSE 0 END) AS total
FROM sessions
