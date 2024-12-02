from student_management import Student, Students
import unittest
import json



class TestStudents(unittest.TestCase):

    def setUp(self):

        self.test_file = "test_data.json"

        self.students_control = Students()

        self.students_control.file_path = self.test_file

        with open(self.test_file, "w") as file:
            json.dump([], file)

       
    def test_add_student(self):
        student1 = Student(1, "Durga", 22, "vg", ["Programming", "swidish"])
        student2 = Student(2, "Sanjana", 20, "vg", ["math", "physics"])
        
        self.students_control.add_student(student1)
        self.students_control.add_student(student2)
        
        self.assertEqual(len(self.students_control.student_list), 2)
        self.assertEqual(self.students_control.student_list[0].name, "Durga")
        self.assertEqual(self.students_control.student_list[1].name, "Sanjana")

    def test_save_students(self):
        student3 = Student(3, "Chama", 21, "A", ["Physics", "Chemistry"])
        student4 = Student(4, "Abdel", 33, "A", ["Science", "Biologi"])

        # Add student and save to file
        self.students_control.add_student(student3)
        self.students_control.add_student(student4)
        self.students_control.save_students_to_file()

        with open(self.test_file, "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "Chama")

    def test_load_students(self):
        # Load the students from the file 
        students_data = [
            {"id": 3, "name": "Chama", "age": 21, "grade": "A", "subjects": ["Physics", "Chemistry"]},
            {"id": 4, "name": "Abdel", "age": 33, "grade": "A", "subjects": ["Science", "Biology"]}
        ]
         
        with open(self.test_file, "w") as file:
            json.dump(students_data, file)
        
        # Load the students 
        new_control = Students()
        new_control.file_path = self.test_file
        new_control.load_students_from_file()
          
        # Verify if the data is loaded successfully 
        self.assertEqual(len(new_control.student_list), 2)
        self.assertEqual(new_control.student_list[0].name, "Chama")
        self.assertEqual(new_control.student_list[1].name, "Abdel")
        
    def test_delete_student(self):
        student4 = Student(4, "Patrik", 23, "C", ["Biology"])
        student5 = Student(5, "Seyda", 25, "B", ["Math", "English"])
        
        # Add students
        self.students_control.add_student(student4)
        self.students_control.add_student(student5)

        # Delete a student
        self.students_control.delete_student(4)

        # Verify deletion
        self.assertEqual(len(self.students_control.student_list), 1)
        self.assertEqual(self.students_control.student_list[0].id, 5)

    def tearDown(self):
        try:
            with open(self.test_file, "w") as file:
                json.dump[[], file] 
        except Exception as e:
            print(f"Error cleaning up test file: {e}")


if __name__ == "__main__":
    unittest.main()
