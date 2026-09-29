import csv
import os

FILE_NAME = "students.csv"
SUBJECTS = ["Mathematics", "Physics", "Python", "English", "EVS"]


def load_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    return students


def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["roll_no", "name", "course"] + SUBJECTS
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def find_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student

    return None


def calculate_result(student):
    marks = []

    for subject in SUBJECTS:
        marks.append(float(student.get(subject, 0)))

    total = sum(marks)
    percentage = total / len(SUBJECTS)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    status = "PASS" if percentage >= 40 else "FAIL"

    return total, percentage, grade, status


def add_student(students):
    print("\n--- ADD STUDENT ---")

    roll_no = input("Enter Roll Number: ").strip()

    if find_student(students, roll_no):
        print("A student with this roll number already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course
    }

    for subject in SUBJECTS:
        student[subject] = "0"

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students(students):
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"Roll No: {student['roll_no']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']}"
        )


def search_student(students):
    print("\n--- SEARCH STUDENT ---")

    keyword = input("Enter Roll Number or Name: ").strip().lower()
    found = False

    for student in students:
        if (
            keyword == student["roll_no"].lower()
            or keyword in student["name"].lower()
        ):
            print("\nStudent Found")
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            found = True

    if not found:
        print("Student not found.")


def update_student(students):
    print("\n--- UPDATE STUDENT ---")

    roll_no = input("Enter Roll Number: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print("Leave blank if you don't want to change a field.")

    name = input(f"Enter new name ({student['name']}): ").strip()
    course = input(f"Enter new course ({student['course']}): ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    save_students(students)

    print("Student details updated successfully!")


def delete_student(students):
    print("\n--- DELETE STUDENT ---")

    roll_no = input("Enter Roll Number: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print(f"Student: {student['name']}")

    confirm = input("Are you sure you want to delete? (y/n): ").lower()

    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def enter_marks(students):
    print("\n--- ENTER / UPDATE MARKS ---")

    roll_no = input("Enter Roll Number: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print(f"\nEntering marks for {student['name']}")

    for subject in SUBJECTS:

        while True:
            try:
                marks = float(input(f"{subject} (0-100): "))

                if 0 <= marks <= 100:
                    student[subject] = str(marks)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    save_students(students)

    print("Marks saved successfully!")


def view_result(students):
    print("\n--- STUDENT RESULT ---")

    roll_no = input("Enter Roll Number: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    total, percentage, grade, status = calculate_result(student)

    print("\n========================================")
    print("              MARKSHEET")
    print("========================================")
    print("Name       :", student["name"])
    print("Roll Number:", student["roll_no"])
    print("Course     :", student["course"])
    print("----------------------------------------")

    for subject in SUBJECTS:
        print(f"{subject:<15}: {student[subject]}")

    print("----------------------------------------")
    print(f"Total      : {total:.2f}/500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Status     : {status}")
    print("========================================")


def class_statistics(students):
    print("\n--- CLASS STATISTICS ---")

    if not students:
        print("No student records found.")
        return

    percentages = []

    for student in students:
        total, percentage, grade, status = calculate_result(student)
        percentages.append(percentage)

    average = sum(percentages) / len(percentages)

    highest = max(percentages)
    lowest = min(percentages)

    print("Number of Students :", len(students))
    print(f"Class Average      : {average:.2f}%")
    print(f"Highest Percentage : {highest:.2f}%")
    print(f"Lowest Percentage  : {lowest:.2f}%")

    passed = sum(1 for p in percentages if p >= 40)
    failed = len(students) - passed

    print("Passed Students    :", passed)
    print("Failed Students    :", failed)


def student_ranking(students):
    print("\n--- STUDENT RANKING ---")

    if not students:
        print("No student records found.")
        return

    ranking = []

    for student in students:
        total, percentage, grade, status = calculate_result(student)

        ranking.append(
            (
                student["name"],
                student["roll_no"],
                percentage
            )
        )

    ranking.sort(key=lambda x: x[2], reverse=True)

    print("\nRank | Roll No | Name | Percentage")
    print("----------------------------------------")

    for rank, student in enumerate(ranking, start=1):
        print(
            f"{rank:<5}| "
            f"{student[1]:<8}| "
            f"{student[0]:<15}| "
            f"{student[2]:.2f}%"
        )


def subject_analysis(students):
    print("\n--- SUBJECT ANALYSIS ---")

    if not students:
        print("No student records found.")
        return

    for subject in SUBJECTS:

        marks = [
            float(student[subject])
            for student in students
        ]

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"\n{subject}")
        print(f"Average : {average:.2f}")
        print(f"Highest : {highest:.2f}")
        print(f"Lowest  : {lowest:.2f}")


def main():
    students = load_students()

    while True:

        print("\n")
        print("========================================")
        print("   STUDENT RESULT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Enter / Update Marks")
        print("7. View Student Result")
        print("8. Class Statistics")
        print("9. Student Ranking")
        print("10. Subject Analysis")
        print("11. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            enter_marks(students)

        elif choice == "7":
            view_result(students)

        elif choice == "8":
            class_statistics(students)

        elif choice == "9":
            student_ranking(students)

        elif choice == "10":
            subject_analysis(students)

        elif choice == "11":
            print("\nThank you for using Student Result Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()