class Student:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name
        self._grades = {}

    def add_grade(self, subject, grade):
        self._grades[subject] = grade

    def average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

    def display_details(self):
        print(f"Student ID: {self._student_id}")
        print(f"Name: {self._name}")
        print(f"Average Grade: {self.average_grade()}")

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name


class StudentManagementSystem:
    def __init__(self):
        self._students = {}

    def add_student(self, student_id, name):
        if student_id not in self._students:
            self._students[student_id] = Student(student_id, name)
            print(f"Student with ID {student_id} added successfully.")
        else:
            print("Student with this ID already exists.")

    def show_student_details(self, student_id):
        if student_id in self._students:
            self._students[student_id].display_details()
        else:
            print("Student not found.")

    def show_student_average_grade(self, student_id):
        if student_id in self._students:
            student = self._students[student_id]
            print(f"Average grade for {student.name}: {student.average_grade()}")
        else:
            print("Student not found.")

sms = StudentManagementSystem()

sms.add_student(1, "lana")
sms.add_student(2, "dato")

sms.add_student(1, "Another lana")

sms.show_student_details(1)
sms.show_student_details(2)
sms.show_student_details(3)

alice = sms._students[1]
alice.add_grade("Math", 90)
alice.add_grade("Science", 85)

sms.show_student_average_grade(1)
