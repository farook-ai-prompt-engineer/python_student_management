import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

try:
    student_id = int(input("Enter ID: "))
    new_age = int(input("New age: "))

except ValueError:
    print("ID and Age must be numbers.")
    exit()

cursor.execute("UPDATE students SET age=? WHERE id=?", (new_age, student_id))

connection.commit()

if cursor.rowcount > 0:
    print("Student updated successfully.")
else:
    print("Student not found.")

connection.close()
