import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

student_id = int(input("Enter ID: "))

cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

connection.commit()
connection.close()

print("Deleted")
