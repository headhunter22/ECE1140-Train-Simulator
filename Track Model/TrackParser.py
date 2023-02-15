import csv
import sqlite3

# db to store table
connection = sqlite3.connect('blueline.db')
cursor = connection.cursor()

# define the table
blueLine = '''CREATE TABLE blueline (
             line TEXT NOT NULL,
             section TEXT NOT NULL,
             block_number INTEGER NOT NULL,
             block_length INTEGER NOT NULL,
             block_grade,
             speed_limit,
             infrastructure TEXT,
             blank,
             elevation INTEGER NOT NULL,
             cum_elevation INTEGER NOT NULL); 
           '''

# create table in db
cursor.execute(blueLine)

# open file and insert into table
file = open('Track Layout.csv')
content = csv.reader(file)

# query to insert data
insert = "INSERT INTO blueline (line, section, block_number, block_length, block_grade, speed_limit, infrastructure, blank, elevation, cum_elevation) VALUES(?,?,?,?,?,?,?,?,?,?)"
cursor.executemany(insert, content)

# commit changes and close
connection.commit()
connection.close()