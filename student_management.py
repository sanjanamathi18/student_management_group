import json


class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def print_student(self):
        print(
            f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)}"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects,
        }


class Students:
    def __init__(self, file_name):
        self.student_list = []
        self.file_name = file_name
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

    def update_name(self, id, name):
        for student in self.student_list:
            if student.id == id:
                student.name = name
                print(f"Student ID {id}'s name updated to {name}.")
                self.save_students_to_file()
                return
        print(f"Student with ID {id} not found.")

    def update_age(self, id, age):
        for student in self.student_list:
            if student.id == id:
                student.age = age
                print(f"Student ID {id}'s age updated to {age}.")
                self.save_students_to_file()
                return
        print(f"Student with ID {id} not found.")

    def update_grade(self, id, grade):
        for student in self.student_list:
            if student.id == id:
                student.grade = grade
                print(f"Student ID {id}'s grade updated to {grade}.")
                self.save_students_to_file()
                return
        print(f"Student with ID {id} not found.")

    def update_subjects(self, id, subjects):
        for student in self.student_list:
            if student.id == id:
                student.subjects = subjects
                print(f"Student ID {id}'s subjects updated to {', '.join(subjects)}.")
                self.save_students_to_file()
                return
        print(f"Student with ID {id} not found.")

    def delete_student(self, student_id: int):
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                print(f"Student with ID {student_id} deleted.")
                return
        print(f"Student with ID {student_id} not exist.")

    def save_students_to_file(self):
        with open(self.file_name, mode="w", encoding="utf-8") as file:
            student_data = []
            for student in self.student_list:
                student_data.append(student.to_dict())
            json.dump(student_data, file, indent=4)

    def load_students_from_file(self):
        try:
            with open(self.file_name, mode="r", encoding="utf-8") as outfile:
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

            print("Students loaded from the file.")

        except Exception as e:
            print(f"Error loading students: {e}")

    def field_to_update(self, id):
        print("ID", "Name", "Age", "Grade", "Subjects")
        while True:
            try:
                feild = input("Enter field to update: (type 'exit' to stop)")
                if not feild:
                    print("Feild cannot be empty.")
                    continue
                else:
                    if feild == "id":
                        print("ID cannot be updated")
                        return
                    elif feild == "name":
                        value = self.get_name()
                        self.update_name(id, value)
                    elif feild == "age":
                        value = self.get_age()
                        self.update_age(id, value)
                    elif feild == "grade":
                        value = self.get_grade()
                        self.update_grade(id, value)
                    elif feild == "subjects":
                        value = self.get_subjects()
                        self.update_subjects(id, value)
                    elif feild == "exit":
                        return
            
                    else:
                        print("Invalid field. Please choose: Name, Age, Grade, Subjects")
                
            except ValueError as e:
                print(f"Error: {e}. Please try again.")


    def get_student_data(self):
        id = self.get_id()
        name = self.get_name()
        age = self.get_age()
        grade = self.get_grade()
        subjects = self.get_subjects()
        return Student(id, name, age, grade, subjects)

    def get_id(self) -> int:
        while True:
            try:
                id = int(input("Enter student ID: "))
                if any(student.id == id for student in self.student_list):
                    print("ID exists.")
                else:
                    return id

            except ValueError:
                print("Enter valid value.")

    def get_name(self) -> str:
        while True:
            try:
                name = input("Enter student name: ")
                if not name:
                    print("Name cannot be empty.")
                    continue
                return name
            except ValueError:
                print("Enter valid value.")

    def get_age(self):
        while True:
            try:
                age = int(input("Enter student age: "))
                if age <= 10:
                    print("Age should be greater than 10.")
                    continue
                return age
            except ValueError:
                print("Enter valid value.")

    def get_grade(self):
        while True:
            try:
                grade = input("Enter student grade: ")
                if not grade:
                    print("Grade cannot be empty.")
                    continue
                return grade
            except ValueError:
                print("Enter valid value.")

    def get_subjects(self):
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


FILE_NAME = "student_data.json"


def options():
    students_manager = Students(FILE_NAME)
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
                student_data = students_manager.get_student_data()
                if student_data:
                    students_manager.add_student(student_data)

            elif option == 2:
                students_manager.view_all_students()

            elif option == 3:
                try:
                    student_id = int(input("Enter student ID: "))
                    students_manager.field_to_update(student_id)
                except ValueError:
                    print("Invalid input. ID must be number.")

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


if __name__ == "__main__":
    options()
