create table NA_Temp (
	state VARCHAR(50),
	Year INT,
	Month VARCHAR(50),
	Avg_Max_Temp NUMERIC,
	Avg_Min_Temp NUMERIC
);

\copy NA_Temp FROM '/Users/saulsantana/Desktop/Fall-2021/CS-233/Book1.csv' DELIMITER ',' CSV HEADER;  


-----------------------------------------------------------------------------------------------------------
--Skewed tempertatures in the relationship of the average max and min temperatures:

--Relation of AVG Maximun temperature that is above 80 for distincts states:
SELECT DISTINCT state, Year, Avg_Max_Temp
FROM NA_Temp 
WHERE Avg_Max_Temp >= 80
GROUP BY state, Avg_Max_Temp, Year
ORDER BY Year DESC;

--Exporting Data
\copy (SELECT DISTINCT state, Year, Avg_Max_Temp FROM NA_Temp WHERE Avg_Max_Temp >= 80 GROUP BY state, Avg_Max_Temp, Year ORDER BY Year DESC) To '/Users/saulsantana/Desktop/Fall-2021/CS-233/Above80.csv' DELIMITER ',' CSV HEADER;  


--Relation of AVG Minimun temperature that is below 40 for distincts states:
SELECT DISTINCT state, Year, Avg_Min_Temp
FROM NA_Temp 
WHERE Avg_Min_Temp <= 40
GROUP BY state, Avg_Min_Temp, Year
ORDER BY Year DESC;

--Exporting Data
\copy (SELECT DISTINCT state, Year, Avg_Min_Temp FROM NA_Temp WHERE Avg_Min_Temp <= 40 GROUP BY state, Avg_Min_Temp, Year ORDER BY Year DESC) TO '/Users/saulsantana/Desktop/Fall-2021/CS-233/Below40.csv' DELIMITER ',' CSV HEADER;  


--Casescenario in which the temperature could be considered Super Hot or Super Cold:
SELECT state, Year, Avg_Max_Temp, Avg_Min_Temp,
CASE
    WHEN Avg_Max_Temp >= 90 THEN 'Super Hot'
    WHEN Avg_Min_Temp <= 35 THEN 'Super Cold'
    WHEN Avg_Min_Temp > 35 AND Avg_Max_Temp < 90 THEN 'Considerable Weather'
    ELSE 'Abnormal Conditions'
END AS Casescenario_Temp
FROM NA_Temp
GROUP BY state, Year, Avg_Min_Temp, Avg_Max_Temp
ORDER BY Year DESC;

--Exporting Data
\copy (SELECT state, Year, Avg_Max_Temp, Avg_Min_Temp, CASE WHEN Avg_Max_Temp >= 90 THEN 'Super Hot' WHEN Avg_Min_Temp <= 35 THEN 'Super Cold' WHEN Avg_Min_Temp > 35 AND Avg_Max_Temp < 90 THEN 'Considerable Weather' ELSE 'Abnormal Conditions' END AS Casescenario_Temp FROM NA_Temp GROUP BY state, Year, Avg_Min_Temp, Avg_Max_Temp ORDER BY Year DESC) TO '/Users/saulsantana/Desktop/Fall-2021/CS-233/Cases.csv' DELIMITER ',' CSV HEADER;  
