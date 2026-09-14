import json


# ==========================================
# JSON FILE FUNCTIONS
# ==========================================

def load_data(filename):
    """
    Read data from a JSON file.
    """

    with open(filename, "r") as file:
        data = json.load(file)

    return data


def save_data(filename, data):
    """
    Save Python data into a JSON file.
    """

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ==========================================
# LOAD DATA
# ==========================================

students = load_data("students.json")
teachers = load_data("teachers.json")
subjects = load_data("subjects.json")


# ==========================================
# STUDENT FUNCTIONS
# ==========================================

def view_student_profile(student_id):

    student = students[student_id]

    print("\n========== STUDENT PROFILE ==========")

    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Class      : {student['class']}")
    print(f"Email      : {student['email']}")


def view_student_subjects():

    print("\n========== SUBJECTS ==========")

    if not subjects:
        print("No subjects available.")
        return

    count = 1

    for code, name in subjects.items():

        print(f"{count}. {name} ({code})")

        count += 1


def view_student_results(student_id):

    results = students[student_id]["results"]

    print("\n========== RESULTS ==========")

    if not results:
        print("No results found.")
        return

    for subject, score in results.items():

        print(f"{subject}: {score}")


def student_menu(student_id):

    while True:

        print("\n========== STUDENT MENU ==========")

        print("1. View Profile")
        print("2. View Subjects")
        print("3. View Results")
        print("4. Logout")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":

            view_student_profile(student_id)

        elif choice == "2":

            view_student_subjects()

        elif choice == "3":

            view_student_results(student_id)

        elif choice == "4":

            print("\nLogging out...")
            break

        else:

            print("\nInvalid option!")


def student_login():

    print("\n========== STUDENT LOGIN ==========")

    student_id = input("Enter Student ID: ").strip().upper()

    password = input("Enter Password: ").strip()

    if student_id in students:

        if students[student_id]["password"] == password:

            print(f"\nWelcome, {students[student_id]['name']}!")

            student_menu(student_id)

        else:

            print("\nIncorrect password!")

    else:

        print("\nStudent ID not found!")


# ==========================================
# TEACHER FUNCTIONS
# ==========================================

def view_teacher_profile(teacher_id):

    teacher = teachers[teacher_id]

    print("\n========== TEACHER PROFILE ==========")

    print(f"Teacher ID : {teacher_id}")
    print(f"Name       : {teacher['name']}")
    print(f"Age        : {teacher['age']}")
    print(f"Email      : {teacher['email']}")
    print(f"Subject    : {teacher['subject']}")


def create_subject():

    print("\n========== CREATE SUBJECT ==========")

    name = input("Enter subject name: ").strip()

    code = input("Enter subject code: ").strip().upper()

    if name == "" or code == "":

        print("\nSubject name and code cannot be empty.")

        return

    if code in subjects:

        print("\nThis subject code already exists.")

        return

    subjects[code] = name

    save_data("subjects.json", subjects)

    print("\nSubject created successfully!")


def view_teacher_subjects():

    print("\n========== SUBJECTS ==========")

    if not subjects:

        print("No subjects registered.")

        return

    print(f"{'Code':<10} {'Subject'}")

    print("-" * 30)

    for code, name in subjects.items():

        print(f"{code:<10} {name}")


def view_students():

    print("\n========== STUDENTS ==========")

    if not students:

        print("No students registered.")

        return

    print(f"{'ID':<10} {'Name':<20} {'Class'}")

    print("-" * 45)

    for student_id, student in students.items():

        print(
            f"{student_id:<10}"
            f"{student['name']:<20}"
            f"{student['class']}"
        )


def enter_results():

    print("\n========== ENTER RESULTS ==========")

    student_id = input("Enter student ID: ").strip().upper()

    if student_id not in students:

        print("\nStudent ID not found.")

        return

    subject_input = input("Enter subject or subject code: ").strip()

    valid_subject = None

    for code, name in subjects.items():

        if subject_input.lower() == code.lower():

            valid_subject = name

            break

        elif subject_input.lower() == name.lower():

            valid_subject = name

            break

    if valid_subject is None:

        print("\nSubject does not exist.")

        return

    score_input = input("Enter score (0-100): ").strip()

    try:

        score = float(score_input)

        if score < 0 or score > 100:

            print("\nScore must be between 0 and 100.")

            return

        if score.is_integer():

            score = int(score)

        students[student_id]["results"][valid_subject] = score

        save_data("students.json", students)

        print("\nResult entered successfully!")

    except ValueError:

        print("\nPlease enter a valid number.")


def teacher_menu(teacher_id):

    while True:

        print("\n========== TEACHER MENU ==========")

        print("1. View Profile")
        print("2. Create Subject")
        print("3. View Subjects")
        print("4. View Students")
        print("5. Enter Results")
        print("6. Logout")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":

            view_teacher_profile(teacher_id)

        elif choice == "2":

            create_subject()

        elif choice == "3":

            view_teacher_subjects()

        elif choice == "4":

            view_students()

        elif choice == "5":

            enter_results()

        elif choice == "6":

            print("\nLogging out...")

            break

        else:

            print("\nInvalid option!")


def teacher_login():

    print("\n========== TEACHER LOGIN ==========")

    teacher_id = input("Enter Teacher ID: ").strip().upper()

    password = input("Enter Password: ").strip()

    if teacher_id in teachers:

        if teachers[teacher_id]["password"] == password:

            print(f"\nWelcome, {teachers[teacher_id]['name']}!")

            teacher_menu(teacher_id)

        else:

            print("\nIncorrect password!")

    else:

        print("\nTeacher ID not found!")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n========================================")
        print("       SCHOOL MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Student")
        print("2. Teacher")
        print("3. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":

            student_login()

        elif choice == "2":

            teacher_login()

        elif choice == "3":

            print("\nExiting program. Goodbye!")

            break

        else:

            print("\nInvalid choice!")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":

    main()