
from grade_calculator import calculate_grade, calculate_average
from file_handler import load_students, save_students


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = []

    for i in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = calculate_grade(marks)

    student = {
        "name": name,
        "marks": marks,
        "average": round(average, 2),
        "grade": grade
    }

    students = load_students()
    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")
    print("Average:", round(average, 2))
    print("Grade:", grade)


def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])


def show_statistics():
    students = load_students()

    if not students:
        print("\nNo records available for statistics.")
        return

    averages = [student["average"] for student in students]

    print("\n========== CLASS STATISTICS ==========")
    print("Total students:", len(students))
    print("Class average:", round(sum(averages) / len(averages), 2))
    print("Highest average:", max(averages))
    print("Lowest average:", min(averages))
