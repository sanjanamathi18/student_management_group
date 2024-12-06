from student_management import Student, Students
import unittest
import json
import os
from unittest.mock import patch


class TestStudents(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_data.json"
        self.students_control = Students(self.file_name)

    def test_add_student(self):
        self.students_control.add_student(Student(1, "Durga", 22, "vg", ["Programming", "swidish"]))
        self.students_control.add_student(Student(2, "Sanjana", 20, "vg", ["math", "physics"]))
        self.assertEqual(self.students_control.student_list[0].name, "Durga")
        self.assertEqual(self.students_control.student_list[1].name, "Sanjana")

    def test_update_student(self):
        self.students_control.add_student(
            Student(3, "Swathi", 24, "vg", ["Programming", "Swedish"])
        )

        self.students_control.update_name(3, "swathi")
        self.assertEqual(self.students_control.student_list[0].name, "swathi")

        self.students_control.update_age(3, 23)
        self.assertEqual(self.students_control.student_list[0].age, 23)

        self.students_control.update_grade(3, "g")
        self.assertEqual(self.students_control.student_list[0].grade, "g")

        self.students_control.update_subjects(3, ["Math", "Science"])
        self.assertEqual(self.students_control.student_list[0].subjects, ["Math", "Science"])

    @patch("student_management.to_print")
    def test_view_students(self, mock_print):
        student_1 = Student(3, "MGR", 23, "bad", ["acting"])
        self.students_control.add_student(student_1)
        self.students_control.view_all_students()
        mock_print.assert_any_call(
            {"id": 3, "name": "MGR", "age": 23, "grade": "bad", "subjects": ["acting"]},
        )

    def test_delete_student(self):
        self.students_control.add_student(Student(4, "Patrik", 23, "C", ["Biology"]))
        self.students_control.add_student(Student(5, "Syeda", 25, "B", ["Math", "English"]))
        self.students_control.delete_student(4)
        self.assertEqual(self.students_control.student_list[0].name, "Syeda")

    def test_save_students(self):
        self.students_control.add_student(Student(6, "Vimal", 23, "C", ["Biology"]))
        self.students_control.save_students_to_file()
        with open(self.file_name, "r") as file:
            data = json.load(file)
            self.assertEqual(data[0]["name"], "Vimal")

    def test_load_studemts(self):
        student_1 = Student(6, "Vimal", 23, "C", ["Biology"])
        student_2 = Student(7, "kamal", 23, "C", ["Maths"])
        student_3 = Student(8, "rajini", 23, "C", ["science"])
        self.students_control.add_student(student_1)
        self.students_control.add_student(student_2)
        self.students_control.add_student(student_3)

        self.students_control.save_students_to_file()
        new_students = Students(self.file_name)
        self.assertEqual(new_students.get_stored_student_data(6).to_dict(), student_1.to_dict())
        self.assertEqual(new_students.get_stored_student_data(7).to_dict(), student_2.to_dict())
        self.assertEqual(new_students.get_stored_student_data(8).to_dict(), student_3.to_dict())

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)


if __name__ == "__main__":
    unittest.main()
