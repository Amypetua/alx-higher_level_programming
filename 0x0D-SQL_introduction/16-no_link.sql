#!/usr/bin/env sql

-- A script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server

SELECT `score`, `name` FROM `second_tsble` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
