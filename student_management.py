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
            "subjects": self.subjects
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

    def update_student():
        pass

    def delete_student(self, student_id: int):
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                print(f"Student with {student_id} deleted.")
                return
            else:
                print(f"Student with ID {student_id} not exist.")


    def save_students_to_file():
        pass

    def load_students_from_file(self):
        pass


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
            option = int(input(">"))
            if option == 1:
                print("You chose to Add student.\nEnter student details.")
                student_data = get_input(students_manager.student_list)  # Get input and validate ID
                if student_data:
                    students_manager.add_student(student_data)

            elif option == 2:
                students_manager.view_all_students()

            elif option == 3:
                student_id = int(input())
                students_manager.update_student(student_id)

            elif option == 4:
                try:
                    student_id = int(input("Enter ID of the student to delete: "))
                    students_manager.delete_student(student_id)
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
