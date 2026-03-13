# Student Management System
# Internship Task 2 - SyntecxHub
# Developed by: Ayesha Khanam
# This program allows users to manage student records using a CLI interface.
import json
import os


class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.students = [Student(**student) for student in data]
            except:
                self.students = []

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print("\nStudent ID already exists.")
                return
        self.students.append(student)
        self.save_to_file()
        print("\nStudent added successfully.")

    def view_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print(f"\nTotal Students: {len(self.students)}")
        print("\n{:<15} {:<20} {:<10} {:<10}".format("Student ID", "Name", "Age", "Grade"))
        print("-" * 60)

        for student in self.students:
            print("{:<15} {:<20} {:<10} {:<10}".format(
                student.student_id, student.name, student.age, student.grade
            ))

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                return student

        print("\nStudent not found.")
        return None

    def update_student(self, student_id):
        student = self.search_student(student_id)

        if student:
            new_name = input(f"New Name [{student.name}]: ").strip()
            new_age = input(f"New Age [{student.age}]: ").strip()
            new_grade = input(f"New Grade [{student.grade}]: ").strip()

            if new_name:
                student.name = new_name

            if new_age.isdigit():
                student.age = int(new_age)

            if new_grade:
                student.grade = new_grade

            self.save_to_file()
            print("\nStudent updated successfully.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").strip().lower()

                if confirm == "y":
                    self.students.remove(student)
                    self.save_to_file()
                    print("\nStudent deleted successfully.")
                else:
                    print("\nDeletion cancelled.")

                return

        print("\nStudent not found.")


def is_valid_name(name):
    return name.replace(" ", "").isalpha()


def main():
    manager = StudentManager()

    print("\nWelcome to the Student Management System")
    print("This program allows you to manage student records.\n")

    while True:
        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            student_id = input("Enter Student ID (or press Enter for auto ID): ").strip()

            if student_id == "":
                student_id = str(len(manager.students) + 1)
                print(f"Generated Student ID: {student_id}")

            name = input("Enter Student Name: ").strip()
            if not is_valid_name(name):
                print("Invalid name.")
                input("\nPress Enter to continue...")
                continue

            age_input = input("Enter Age: ").strip()
            if not age_input.isdigit():
                print("Invalid age.")
                input("\nPress Enter to continue...")
                continue

            age = int(age_input)
            grade = input("Enter Grade: ").strip()

            student = Student(student_id, name, age, grade)
            manager.add_student(student)

            input("\nPress Enter to continue...")

        elif choice == "2":
            manager.view_students()
            input("\nPress Enter to continue...")

        elif choice == "3":
            student_id = input("Enter Student ID to search: ").strip()
            manager.search_student(student_id)
            input("\nPress Enter to continue...")

        elif choice == "4":
            student_id = input("Enter Student ID to update: ").strip()
            manager.update_student(student_id)
            input("\nPress Enter to continue...")

        elif choice == "5":
            student_id = input("Enter Student ID to delete: ").strip()
            manager.delete_student(student_id)
            input("\nPress Enter to continue...")

        elif choice == "6":
            print("\nExiting program.")
            break

        else:
            print("\nInvalid choice.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()