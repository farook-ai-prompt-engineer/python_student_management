import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

try:
    student_id = int(input("Enter ID: "))

except ValueError:
    print("ID must be a number.")
    exit()

cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

connection.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully.")
else:
    print("Student not found.")

connection.close()
