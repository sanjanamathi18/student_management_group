from student_management import Student, Students
import unittest


class TestStudents(unittest.TestCase):
    
    def test_add_student(self):
        students_control = Students()
        stud1 = Student(3, "sanjana", None, "vg+", ["math", "english"])
        stud2 = Student(2, "Divya", 24, "vg", ["math", "computers"])
        stud3 = Student(4, "chama", 22, "vg", ["math", "physics"])

        students_control.add_student(stud1) 
        students_control.add_student(stud2)
        students_control.add_student(stud3)

        self.assertEqual(len(students_control.student_list), 3)


    def test_delete_student(self):
        students_control = Students()
        stud1 = Student(3, "sanjana", None, "vg+", ["math", "english"])
        stud2 = Student(2, "Divya", 24, "vg", ["math", "computers"])
        stud3 = Student(4, "chama", 22, "vg", ["math", "physics"])

        students_control.add_student(stud1) 
        students_control.add_student(stud2)
        students_control.add_student(stud3)
        

        students_control.delete_student(4)

        self.assertEqual(len(students_control.student_list), 2) # W check if two students left.

if __name__ == "__main__":
    unittest.main()
