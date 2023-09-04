-- list all records of table.
SELECT `score`, `name`
FROM second_table
WHEN name IS NOT NULL
ORDER BY `score` DESC;
