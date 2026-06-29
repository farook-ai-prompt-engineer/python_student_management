import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

student_id = int(input("Enter ID: "))
new_age = int(input("New age: "))

cursor.execute("UPDATE students SET age=? WHERE id=?", (new_age, student_id))

connection.commit()
connection.close()

print("Updated")
