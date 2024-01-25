from Students import *

students = load_students_data()

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Assign grades")
    print("4. Send email")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        remove_student(students)
    elif choice == '3':
        assign_grades(students)
    elif choice == '4':
        send_email(students)
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again!")