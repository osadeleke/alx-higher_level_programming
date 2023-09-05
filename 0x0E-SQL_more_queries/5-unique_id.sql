-- creates a table unique id
CREATE TABLE IF NOT EXISTS `unique_id` (
	id int NOT NULL DEFAULT 1 UNIQUE,
	name varchar(256)
