import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

name = input("Enter name: ")
age = int(input("Enter age: "))

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))


connection.commit()
connection.close()
