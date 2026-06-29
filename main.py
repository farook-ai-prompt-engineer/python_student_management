print("==== STUDENT MANAGEMENT SYSTEM =====")

print("1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Delete Student")
print("5. Search Student")
print("6. Exit")


choice = input("Enter choice: ")


if choice == "1":
    import add_student

elif choice == "2":
    import view_students

elif choice == "3":
    import update_student

elif choice == "4":
    import delete_student

elif choice == "5":
    exec(open("search_student.py").read())

elif choice == "6":
    print("Thank you")

else:
    print("invalid choice")
