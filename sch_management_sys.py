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
SUBJECTS_FILE = "subjects.json"
RESULTS_FILE = "results.json"


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
subjects_db = check_and_load_file(SUBJECTS_FILE)
results_db = check_and_load_file(RESULTS_FILE)


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

                                if not subjects_db:

                                    print("No subjects available.")

                                else:
                                    for subject in subjects_db:

                                        print(f"ID: {subject['id']}")
                                        print(f"Subject: {subject['name']}")
                                        print(f"Teacher: {subject['teacher']}")
                                        print("--------------------------------")
                        elif student_choice == 3:
                                print("\n========== RESULTS ==========")

                                student_results = []

                                # Find results belonging to the logged-in student
                                for result in results_db:

                                    if result["student_id"] == student["id"]:

                                        student_results.append(result)

                                # Check if student has any results
                                if not student_results:

                                    print("No results available.")

                                else:

                                    for result in student_results:

                                        # Find the subject
                                        for subject in subjects_db:

                                            if subject["id"] == result["subject_id"]:

                                                print(f"Subject: {subject['name']}")
                                                print(f"Teacher: {subject['teacher']}")
                                                print(f"Score: {result['score']}")
                                                print("--------------------------------")
                                                break

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

        teacher_id = int(input("Enter Teacher ID: "))
        password = input("Enter Password: ").strip()

        # Check if teacher exists
        teacher_found = False

        for teacher in teachers_db:

            if teacher["id"] == teacher_id:

                teacher_found = True

                # Check password
                if teacher["password"] == password:

                    print(f"\nWelcome back, {teacher['name']}!")

                    # ==========================
                    # TEACHER MENU
                    # ==========================

                    while True:

                        print("""
    ========================================
                TEACHER MENU
    ========================================

    1. View Profile
    2. Create Subject
    3. View Subjects
    4. View Students
    5. Enter Results
    6. Logout

    ========================================
    """)

                        teacher_choice = int(input("Select an option: "))

                        # VIEW PROFILE
                        if teacher_choice == 1:

                            print("\n========== TEACHER PROFILE ==========")

                            print(f"ID: {teacher['id']}")
                            print(f"Name: {teacher['name']}")
                            print(f"Age: {teacher['age']}")
                            print(f"Email: {teacher['email']}")

                        # CREATE SUBJECT
                        elif teacher_choice == 2:

                            print("\n========== CREATE SUBJECT ==========")

                            subject_name = input("Enter Subject Name: ").strip()

                            if not subject_name:

                                print("\nSubject name is required.")

                            else:

                                # Create subject ID
                                subject_id = len(subjects_db) + 1

                                subject = {
                                    "id": subject_id,
                                    "name": subject_name,
                                    "teacher": teacher["name"]
                                }

                                # Add subject to database
                                subjects_db.append(subject)

                                # Save subjects to JSON
                                check_and_write_file(
                                    SUBJECTS_FILE,
                                    json.dumps(subjects_db, indent=4)
                                )

                                print("\nSubject created successfully!")
                                print(f"Subject: {subject_name}")
                                print(f"Teacher: {teacher['name']}")
                                print(f"Subject ID: {subject_id}")

                        # VIEW SUBJECTS
                        elif teacher_choice == 3:

                            print("\n========== SUBJECTS ==========")

                            if not subjects_db:

                                print("No subjects available.")

                            else:

                                for subject in subjects_db:

                                    print(f"ID: {subject['id']}")
                                    print(f"Subject: {subject['name']}")
                                    print(f"Teacher: {subject['teacher']}")
                                    print("--------------------------------")

                        # VIEW STUDENTS
                        elif teacher_choice == 4:

                            print("\n========== STUDENTS ==========")

                            if not students_db:

                                print("No students registered.")

                            else:

                                for student in students_db:

                                    print(f"ID: {student['id']}")
                                    print(f"Name: {student['name']}")
                                    print(f"Class: {student['class']}")
                                    print(f"Email: {student['email']}")
                                    print("--------------------------------")

                        # ENTER RESULTS
                        elif teacher_choice == 5:

                            print("\n========== ENTER RESULTS ==========")

                            # Display students
                            if not students_db:

                                print("No students registered.")

                            else:

                                print("\nStudents:")

                                for student in students_db:

                                    print(f"ID: {student['id']} | Name: {student['name']}")

                                student_id = int(input("\nEnter Student ID: "))

                                # Find student
                                student_found = False

                                for student in students_db:

                                    if student["id"] == student_id:

                                        student_found = True
                                        selected_student = student
                                        break

                                if not student_found:

                                    print("\nStudent not found.")

                                else:

                                    # Display subjects
                                    if not subjects_db:

                                        print("\nNo subjects available.")

                                    else:

                                        print("\nSubjects:")

                                        for subject in subjects_db:

                                            print(
                                                f"ID: {subject['id']} | "
                                                f"Subject: {subject['name']}"
                                            )

                                        subject_id = int(input("\nEnter Subject ID: "))

                                        # Find subject
                                        subject_found = False

                                        for subject in subjects_db:

                                            if subject["id"] == subject_id:

                                                subject_found = True
                                                selected_subject = subject
                                                break

                                        if not subject_found:

                                            print("\nSubject not found.")

                                        else:

                                            score = int(input("Enter Score: "))

                                            # Check score
                                            if score < 0 or score > 100:

                                                print("\nScore must be between 0 and 100.")

                                            else:

                                                result_id = len(results_db) + 1

                                                result = {
                                                    "id": result_id,
                                                    "student_id": selected_student["id"],
                                                    "subject_id": selected_subject["id"],
                                                    "score": score
                                                }

                                                # Add result to database
                                                results_db.append(result)

                                                # Save results to JSON
                                                check_and_write_file(
                                                    RESULTS_FILE,
                                                    json.dumps(results_db, indent=4)
                                                )

                                                print("\nResult entered successfully!")
                                                print(f"Student: {selected_student['name']}")
                                                print(f"Subject: {selected_subject['name']}")
                                                print(f"Score: {score}")

                        # LOGOUT
                        elif teacher_choice == 6:

                            print("\nLogging out...")
                            break

                        else:

                            print("\nInvalid option. Please try again.")

                else:

                    print("\nIncorrect password.")

                break

    if not teacher_found:

        print("\nTeacher not found.")

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