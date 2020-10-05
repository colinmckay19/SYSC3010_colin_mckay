#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

temperature = 15
date = '2020-10-04'
time = '12:00:00'
zone = 'garage'

for i in range(10):
    temperature += 1
    #execute insert statement
    cursor.execute('''insert into temps values (?, ?, ?, ?)''', (date, time, zone, temperature));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature']);


cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID integer PRIMARY KEY, type text, zone text);''')
cursor.execute('''insert into sensors values (1, "door", "kitchen");''')
cursor.execute('''insert into sensors values (2, "temperature", "kitchen");''')
cursor.execute('''insert into sensors values (3, "door", "garage");''')
cursor.execute('''insert into sensors values (4, "motion", "garage");''')
cursor.execute('''insert into sensors values (5, "temperature", "garage");''')
dbconnect.commit();

cursor.execute('''SELECT * FROM sensors WHERE zone="kitchen"''');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

cursor.execute('''SELECT * FROM sensors WHERE type="door"''');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

#close the connection
dbconnect.close();

