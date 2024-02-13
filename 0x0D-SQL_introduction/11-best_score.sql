-- Lists all records in descending score of second_table with score >= 10 in my MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
