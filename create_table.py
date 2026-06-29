import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS   STUDENTS (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT,
               age INTEGER
               )
               """)


connection.commit()
connection.close()

print("Table created successfully")
