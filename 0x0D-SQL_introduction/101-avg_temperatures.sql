#!/usr/bin/env sql

-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT `city`, AVG(`temperature`) AS `avg_temp` 
FROM `temperatures`
GROUP BY `city` 
ORDER BY `avg_temp` DESC;
