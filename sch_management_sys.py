"""
Creating Student Management System called SharrySMS

What it does is simple:

A school management system that allows students to view their
profiles, subjects, and results, while teachers can manage
subjects, view students, and enter results.
"""

import os
import json


APP_NAME = "SharrySMS"
STUDENTS_FILE = "students.json"
TEACHERS_FILE = "teachers.json"


print("======================================================================================")
print(f"Welcome to {APP_NAME}")
print("Student Management System")
print("======================================================================================")


# CHECK AND LOAD FILE

def check_and_load_file(filename):

    if not os.path.isfile(filename):

        print(f"{filename} does not exist. Creating now...")

        with open(filename, "w") as f:
            f.write("[]")

    with open(filename, "r") as f:

        return json.load(f)


# CHECK AND WRITE FILE

def check_and_write_file(filename, data):

    if not os.path.isfile(filename):

        print(f"{filename} does not exist. Creating now...")

        with open(filename, "w") as f:
            f.write("[]")

    with open(filename, "w") as f:

        f.write(data)


# LOAD DATA

students_db = check_and_load_file(STUDENTS_FILE)
teachers_db = check_and_load_file(TEACHERS_FILE)


# NEW OR RETURNING USER

print("""
========================================
        WELCOME TO SHARRYSMS
========================================

1. Returning User
2. New User
3. Exit

========================================
""")

user_status = input("Select an option: ").strip()


# ==========================================================
# RETURNING USER
# ==========================================================

if user_status == "1":

    print("""
========================================
             LOGIN AS
========================================

1. Student
2. Teacher
3. Back

========================================
""")

    user_type = input("Select an option: ").strip()
    # RETURNING STUDENT
    if user_type == "1":
        print("\n========== STUDENT LOGIN ==========")
        student_name = input("Enter Student Name: ").strip()
        password = input("Enter Password: ").strip()
        # Check if student exists

        student_found = False

        for student in students_db:

            if student["name"].lower() == student_name.lower():
                student_found = True

                # Check password

                if student["password"] == password:
                    print(f"\nWelcome back, {student['name']}!")

                    # student menu
                    while True:
                        print("""
            STUDENT MENU
1. View Profile
2. View Subjects
3. View Results
4. Logout
""")
                        student_choice = int(input("Select an option: "))
                        if student_choice == 1:
                            print("\n========== STUDENT PROFILE ==========")
                            print(f"ID: {student['id']}")
                            print(f"Name: {student['name']}")
                            print(f"Age: {student['age']}")
                            print(f"Class: {student['class']}")
                            print(f"Email: {student['email']}")

                        elif student_choice == 2:
                            print("\n========== SUBJECTS ==========")
                            print("Subjects will be displayed here.")

                        elif student_choice == 3:

                            print("\n========== RESULTS ==========")
                            print("Results will be displayed here.")

                        elif student_choice == 4:

                            print("\nLogging out...")
                            break
                else:
                    print("\nIncorrect password.")
                break
        if not student_found:
            print("\nStudent not found.")

    # RETURNING TEACHER
    elif user_type == "2":
        print("\n========== TEACHER LOGIN ==========")
        teacher_name = input("Enter Teacher Name: ").strip()
        password = input("Enter Password: ").strip()

        # Check if teacher exists
        teacher_found = False
        for teacher in teachers_db:
            if teacher["name"].lower() == teacher_name.lower():
                teacher_found = True

                # Check password

                if teacher["password"] == password:
                    print(f"\nWelcome back, {teacher['name']}!")
                else:
                    print("\nIncorrect password.")
                break

        if not teacher_found:
            print("\nTeacher not found.")

    elif user_type == "3":
        print("\nReturning to main menu...")
    else:
        print("\nInvalid option.")

# NEW USER

elif user_status == "2":
    print("""
========================================
            REGISTER AS
========================================

1. Student
2. Teacher
3. Back

========================================
""")

    user_type = input("Select an option: ").strip()

    # NEW STUDENT
    if user_type == "1":
        print("\n========== STUDENT REGISTRATION ==========")
        print(f"Welcome to {APP_NAME} School Management System.")

        name = input("Enter Full Name: ").strip()
        age = input("Enter Age: ").strip()
        student_class = input("Enter Class: ").strip()
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()

        # Check required information

        if not name or not password:
            print("\nName and password are required.")
        else:
            # Check if student already exists

            student_exists = False
            for student in students_db:
                if student["name"].lower() == name.lower():
                    student_exists = True
                    break

            if student_exists:
                print("\nA student with this name already exists.")
            else:
                # Create new student
                student_id = len(students_db) + 1
                student = {
                    "id": student_id,
                    "name": name,
                    "age": age,
                    "class": student_class,
                    "email": email,
                    "password": password
                }

                # Add student to database
                students_db.append(student)

                # Save students to JSON file

                check_and_write_file(
                    STUDENTS_FILE,
                    json.dumps(students_db, indent=4)
                )
                print("\nAccount created successfully!")
                print(f"Welcome to {APP_NAME}, {name}!")

    # NEW TEACHER

    elif user_type == "2":
        print("\n========== TEACHER REGISTRATION ==========")
        print(f"Welcome to {APP_NAME} School Management System.")
        
        name = input("Enter Full Name: ").strip()
        age = input("Enter Age: ").strip()
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()


        # Check required information

        if not name or not password:
            print("\nName and password are required.")

        else:
            # Check if teacher already exists

            teacher_exists = False
            for teacher in teachers_db:
                if teacher["name"].lower() == name.lower():
                    teacher_exists = True
                    break

            if teacher_exists:
                print("\nA teacher with this name already exists.")
            else:
                # Create new teacher
                teacher_id = len(teachers_db) + 1
                teacher = {
                    "id": teacher_id,
                    "name": name,
                    "age": age,
                    "email": email,
                    "password": password
                }

                # Add teacher to database
                teachers_db.append(teacher)

                # Save teacher to JSON file

                check_and_write_file(
                    TEACHERS_FILE,
                    json.dumps(teachers_db, indent=4)
                )
                print("\nAccount created successfully!")
                print(f"Welcome to {APP_NAME}, {name}!")
    elif user_type == "3":
        print("\nReturning to main menu...")
    else:
        print("\nInvalid option.")

# EXIT
elif user_status == "3":
    print(f"\nThank you for using {APP_NAME}.")

# INVALID OPTION
else:
    print("\nInvalid option. Please restart the application.")