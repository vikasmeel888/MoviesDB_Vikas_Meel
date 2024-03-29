# -*- coding: utf-8 -*-
"""Vikas_Meel_MoviesDB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r6ajIYwIPNorfLzLCYw2vb47oY5C-t9j

Importing SQLite3 Module and Connecting to the Database and Creating a Database
"""

import sqlite3
connection = sqlite3.connect("movies.db")

"""Creating a cursor to execute queries and Creating a Table"""

cursor = connection.cursor()
cursor.execute(" CREATE TABLE movies (name TEXT, actor TEXT, actress TEXT, director TEXT, year INTEGER)")

"""Inserting Values into the Movies Table"""

cursor.execute("INSERT INTO movies VALUES('Roohi','Rajkummar Rao','Janhvi Kapoor','Hardik Mehta',2021)")
cursor.execute("INSERT INTO movies VALUES('Stree', 'Rajkummar Rao','Shradhdha Kapoor','Amar Kaushik',2018)")
cursor.execute("INSERT INTO movies VALUES('3-idiots','Aamir Khan','Kareena Kapoor','Rajkumar Hirani',2009)")
cursor.execute("INSERT INTO movies VALUES('Andhadhun','Ayushmann Khurrana','Radhika Apte','Sriram Raghavan',2018)")
cursor.execute("INSERT INTO movies VALUES('Dream Girl','Ayushmann Khurrana','Nushrratt Bharuccha','Raaj Shaandilyaa',2019)")

"""Reading Data from the Database and Simple SELECT statement to query all rows from the Movies table"""

rows = cursor.execute("SELECT * FROM movies").fetchall()
for i in rows:
  name,actor,actress,director,year = i
  print(name+"\t"+actor+"\t"+actress+"\t"+director+"\t"+str(year))

"""Query with parameter like actor name to select movies based on the actor's name."""

actor_rows = cursor.execute("SELECT * FROM movies WHERE actor='Rajkummar Rao'").fetchall()
for i in actor_rows:
  name,actor,actress,director,year = i
  print(name+"\t"+actor+"\t"+actress+"\t"+director+"\t"+str(year))