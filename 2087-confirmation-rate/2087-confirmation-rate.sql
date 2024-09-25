SELECT 

    s.user_id, 
    ROUND(
        IFNULL(confirmedCount, 0) / IFNULL(totalCount, 1), 2
    ) AS confirmation_rate
FROM
Signups s LEFT JOIN 
    (SELECT
        user_id, COUNT(*) AS totalCount
    FROM Confirmations
    GROUP BY user_id) a
    LEFT JOIN 
    (SELECT
        user_id, COUNT(*) AS confirmedCount
    FROM Confirmations
    WHERE action = 'confirmed'
    GROUP BY user_id) b
    ON a.user_id = b.user_id 
ON s.user_id = a.user_id
