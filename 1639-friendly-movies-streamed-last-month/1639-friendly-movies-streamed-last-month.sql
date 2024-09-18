# Write your MySQL query statement below
SELECT DISTINCT c.title
FROM TVProgram t
JOIN Content c 
ON t.content_id = c.content_id
WHERE program_date BETWEEN "2020-06-01" AND "2020-06-30" AND Kids_content = "Y" AND content_type = "Movies"