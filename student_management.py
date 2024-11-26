import json
from typing import List


# this class stores individual student data
class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def print_student(self):  # to print the details of the student
        print(
            f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)}"
        )

    def dic(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects,
        }


# this manages students data (multiple students)
class Students:
    # student_list,add_students,view_all_students,update_student,delete_student,save_to_file,load_from_file
    def __init__(self):
        self.student_list = []  # here im storing instance of 'class Student'
        self.load_students_from_file()

    def add_student(self, student_data: Student):
        self.student_list.append(student_data)
        print(f"Student {student_data.name} added successfully.")

    def view_all_students(self):
        if not self.student_list:
            print("No students available.")
        else:
            for student in self.student_list:
                student.print_student()

    def update_student(self, student_id: int):
        for student in self.student_list:
            if student.id == student_id:
                print(f"\nUpdating details for Student ID {student_id}.")
                print("Press Enter to skip and keep the current value.\n")

                student.name = self.update_name(student.name)
                student.age = self.update_age(student.age)
                student.grade = self.update_grade(student.grade)
                student.subjects = self.update_subjects(student.subjects)

                print(f"\nStudent ID {student_id} updated successfully!")
                return

        print(f"Student with ID {student_id} not found.\n")

    def update_name(self, current_name):
        print(f"Current Name: {current_name} \n(or Press Enter to keep)")
        new_name = input(" New name:  ")
        return new_name if new_name else current_name

    def update_age(self, current_age):
        try:
            print(f"Current Age: {current_age} \n(or Press Enter to keep)")
            new_age = int(input("Enter new age: "))
            return new_age if new_age else current_age
        except ValueError:
            print("Invalid input for age.")

    def update_grade(self, current_grade):
        print(f"Current Grade: {current_grade} \n(or Press Enter to keep)")
        new_grade = input("New grade: ")
        return new_grade if new_grade else current_grade

    def update_subjects(self, current_subjects):
        print(f"Current Subjects: {', '.join(current_subjects)}")
        choice = input("Do you want to update subjects? (yes/no):")
        if choice.lower() == "yes":
            print("Deleting current subjects.")
            return self.get_new_subjects()
        return current_subjects

    # def get_new_subjects(self):
    #     subjects = []
    #     try:
    #         num_of_subjects = int(input("How many subjects to add?  "))
    #         if num_of_subjects > 0:
    #             for _ in range(num_of_subjects):
    #                 subject = input("Enter subject: ")
    #                 subjects.append(subject)
    #         else:
    #             print("Invalid input. No subjects updated.")
    #     except ValueError:
    #         print("Invalid input. No subjects updated.")
    #     return subjects
    def get_new_subjects(self):
        new_list = []
        while True:
            try:
                num_of_subjects = int(input("How many subjects to add?  "))
                if num_of_subjects > 0:
                    break
                else:
                    print("Count cannot be negative.")
            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}. ")
        n = 1
        while n <= num_of_subjects:
            sub = input(f"Enter subject {n}: ")
            if not sub:
                print("Subject cannot  be empty.")
                continue
            else:
                new_list.append(sub)
                n += 1
        return new_list

    def delete_student(self, student_id: int):
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)

                return
            else:
                print(f"Student with ID {student_id} not exist")

    def save_students_to_file(self):
        with open("student_data.json", mode="w", encoding="utf-8") as file:
            json.dump(
                [student.dic() for student in self.student_list],
                file,
                indent=4,
            )

    def load_students_from_file(self):
        try:
            with open("student_data.json", mode="r", encoding="utf-8") as outfile:
                data = json.load(outfile)
                self.student_list = [
                    Student(
                        student["id"],
                        student["name"],
                        student["age"],
                        student["grade"],
                        student["subjects"],
                    )
                    for student in data
                ]

            print(
                "Students loaded from the file."
            )  # we should write Try except in case of we don't find the data.

        except Exception as e:
            print(f"Error loading students: {e}")


# getting user input and validating - done but needs more conditons for validation
def get_input(student_list: List[Student]):
    try:
        subjects = []
        student_id = int(input("Enter student id: "))
        for student in student_list:
            if student.id == student_id:  # check condition for unique id
                print(f"Student ID {student_id} already exists.")
                return
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        num_of_subjects = int(input("Enter how many subjects: "))
        for n in range(0, num_of_subjects):
            n = input("Enter subject: ")
            subjects.append(n)
        return Student(student_id, name, age, grade, subjects)

    except ValueError:
        print("Enter valid data.")


# user options to perform desired operation. - done
def options():
    students_manager = Students()
    while True:
        print("""Choose a function from below options list:
                1. Add student
                2. View all students
                3. Update a student's information
                4. Delete a student
                5. Save and exit\n""")
        try:
            option = int(input("> "))
            if option == 1:
                print("Enter student details.")
                student_data = get_input(students_manager.student_list)  # Get input and validate ID
                if student_data:
                    students_manager.add_student(student_data)

            elif option == 2:
                students_manager.view_all_students()

            elif option == 3:
                print("Enter student ID to update ")
                try:
                    student_id = int(input("> "))
                    students_manager.update_student(student_id)
                except ValueError:
                    print("Invalid input. Id must be number")

            elif option == 4:
                try:
                    student_id = int(input("Enter ID of the student to delete: "))
                    students_manager.delete_student(student_id)
                    print(f"Student with ID {student_id} deleted.")
                except ValueError:
                    print("Invalid input. ID must be number.")

            elif option == 5:
                students_manager.save_students_to_file()
                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Enter only integers.")


options()
