while True:

    print("\n==== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        exec(open("add_student.py").read())

    elif choice == "2":
        exec(open("view_students.py").read())

    elif choice == "3":
        exec(open("update_student.py").read())

    elif choice == "4":
        exec(open("delete_student.py").read())

    elif choice == "5":
        exec(open("search_student.py").read())

    elif choice == "6":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
