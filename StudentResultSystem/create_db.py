import sqlite3

conn = sqlite3.connect("students.db")

conn.execute("""

CREATE TABLE students(

name TEXT,
roll TEXT PRIMARY KEY,
subject1 INTEGER,
subject2 INTEGER,
subject3 INTEGER,
total INTEGER,
percentage REAL,
grade TEXT

)

""")

conn.close()

print("Database created successfully")