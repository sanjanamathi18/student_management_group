import json


# this class stores individual student data
class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects


# this manages students data (multiple students)
class Students:
    def __init__(self):
        self.student_list = []  # here im storing instance of 'class Student'
        self.load_students_from_file()

    # "students = [{"id":1,"name":"sanjana","age":30,"grade":"Vg","subject":["math","english"]},
    # {"id":1,"name":"sanjana","age":30,"grade":"Vg","subject":["math","english"]}]"

    def add_student(self):
        student_data = self.get_input()
        if student_data:
            self.student_list.append(student_data)

    def view_students():
        for student in Student.student_lsit:
            pass

    def update_student():
        pass

    def delete_student():
        pass

    def save_students_to_file():
        pass

    def load_students_from_file():
        pass


student = Students()


def get_input():
    try:
        subject = []
        id = int(input("Enter student id: "))  # check condition for unique id
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        num_of_subjects = int(input("Enter how many subjects: "))
        for n in range(0, num_of_subjects):
            n = input("Enter subject: ")
            subject.append(n)

        student.add_student(id, name, age, grade, subject)

    except ValueError:
        print("Enter valid data.")


def options():
    students = Students()
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
                student_data = get_input(students.student_list)
                if student_data:
                    students.add_student(student_data)

            elif option == 2:
                student.view_students()
            elif option == 3:
                student.update_student()
            elif option == 4:
                student.delete_student()
            elif option == 5:
                student.save_students_to_file()
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Enter only integers.")


options()
