# Write your MySQL query statement below
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND id = t.total THEN id
        WHEN MOD(id, 2) != 0 AND id != t.total THEN id + 1
        ELSE id - 1
    END) AS id,
    student
FROM Seat,
    (
        SELECT COUNT(*) AS total
        FROM Seat
    ) AS t
ORDER BY id;
