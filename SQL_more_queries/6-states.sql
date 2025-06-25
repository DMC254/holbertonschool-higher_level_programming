-- Script creates a database hbtn_0_usa and a table inside the database states
CREATE DATABASE IF NOT EXISTS hbtn_0_usa;
USE hbtn_0_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
