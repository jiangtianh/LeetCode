
SELECT B.player_id, B.device_id
FROM Activity B
WHERE (B.player_id, B.event_date) IN
(SELECT
  A.player_id,
  MIN(A.event_date) AS first_login
FROM
  Activity A
GROUP BY
  A.player_id)