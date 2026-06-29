import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

name = input("Enter name: ").strip()

if name == "":
    print("Name cannot be empty.")
    exit()

try:
    age = int(input("Enter age: "))

    if age <= 0:
        print("Age must be greater than 0.")
        exit()

except ValueError:
    print("Age must be a number.")
    exit()

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))

connection.commit()
connection.close()

print("Student added successfully.")
