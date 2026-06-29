import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

name = input("Enter studetn name: ")


cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + name + "%",))

students = cursor.fetchall()


if students:
    print("ID\tNAME\tAGE")
    print("------------------")

for student in students:
    print(student[0], "\t", student[1], "\t", student[2])

else:
    print("No student found. ")

connection.close()
