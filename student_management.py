class Student:
    student_list = []

    # "students = [{"id":1,"name":"sanjana","age":30,"grade":"Vg","subject":["math","english"]},
    # {"id":1,"name":"sanjana","age":30,"grade":"Vg","subject":["math","english"]}]"

    def add_student(cls, id, name, age, grade, subject):
        one_student = {}
        for stud in cls.student_list:
            if stud["id"] == id:
                print("ID exists")
                return

        one_student = {
            "id": id,
            "name": name,
            "age": age,
            "grade": grade,
            "subject": subject,
        }
        cls.student_list.append(one_student)

        print(cls.student_list)

    def view_students():
        for student in Student.student_lsit:
            pass

    def update_student():
        pass

    def delete_student():
        pass

    def save_students_to_file(cls):
        with open("student_data.txt", "w") as outfile:
            for student in cls.student_list:
                outfile.write(f"{student}\n")

    def load_students_from_file():
        pass


student = Student()


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
    while True:
        try:
            option = int(
                input("""Choose a function from below options list:
                            1. Add student
                            2. View all students
                            3. Update a student's information
                            4. Delete a student
                            5. Save and exit\n""")
            )
            if option == 1:
                print("You chose to Add student.\nEnter student details.")
                get_input()
            elif option == 2:
                Student.view_students()
            elif option == 3:
                Student.update_student()
            elif option == 4:
                Student.delete_student()
            elif option == 5:
                Student.save_students_to_file()
            else:
                print("Invalid option.")

        except ValueError:
            print("Enter only integers.")


options()
