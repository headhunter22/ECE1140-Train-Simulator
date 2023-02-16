import csv
import sqlite3

# db to store table
connection = sqlite3.connect('tracklayout.db')
cursor = connection.cursor()

# define the table
tracklayout = '''CREATE TABLE tracklayout (
             line TEXT,
             section TEXT,
             block_number TEXT,
             block_length INTEGER,
             block_grade,
             speed_limit,
             infrastructure TEXT,
             blank,
             elevation INTEGER,
             cum_elevation INTEGER); 
           '''

# create table in db
cursor.execute(tracklayout)

# open file and insert into table
file = open('Track Layout.csv')
content = csv.reader(file)

# query to insert data
insert = "INSERT INTO tracklayout (line, section, block_number, block_length, block_grade, speed_limit, infrastructure, blank, elevation, cum_elevation) VALUES(?,?,?,?,?,?,?,?,?,?)"
cursor.executemany(insert, content)

# commit changes and close
connection.commit()
connection.close()