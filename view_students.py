import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("ID\tNAME\tAGE")
print("-----------------------")

for student in students:
    print(student[0], "\t", student[1], "\t", student[2])


connection.close()
