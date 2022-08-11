-- create table with constraint on a column and
-- another column
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
);
