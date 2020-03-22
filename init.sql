CREATE DATABASE MyTData;

CREATE TABLE IF NOT EXISTS SensorData (
	id SERIAL,
        ts TIMESTAMP,	
	temp integer, 
	pressure integer,
        PRIMARY KEY (id)	
);
