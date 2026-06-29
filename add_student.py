import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

name = input("Enter name: ")


try:
    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number. ")

    exit()

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))


connection.commit()
connection.close()

print("Student added successfully.")
