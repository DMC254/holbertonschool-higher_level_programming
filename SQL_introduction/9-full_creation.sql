-- Script creates a table second_table in database hbtn_0c_0
-- Create the table only if it does not exist
CREATE  TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT);

-- Insert the required records
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
