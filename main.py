
print("Python pogram has started!")
from student import add_student, view_students, show_statistics


def main():
    """Main menu of the Student Grade Management System."""

    while True:
        print("\n===================================")
        print("   STUDENT GRADE MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Show Statistics")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
        main()