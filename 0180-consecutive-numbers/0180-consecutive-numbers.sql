# Write your MySQL query statement below

SELECT DISTINCT l.num AS ConsecutiveNums
FROM Logs l
JOIN Logs lPrev ON lPrev.id = l.id-1 AND l.num = lPrev.num
JOIN Logs lNext ON lNext.id = l.id+1 AND l.num = lNext.num