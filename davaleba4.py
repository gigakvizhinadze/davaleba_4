class Student:

    university = "Example University"


    def __init__(self, name, grade, age):
        self.name = name
        self._grade = grade
        self.age = age


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self._grade}"


    @property
    def is_passing(self):
        return self._grade > 60


    def increase_grade(self, amount):
        self._grade += amount
        return self._grade > 60


student1 = Student("giorgi", 60, 20)


print(f"{student1.name}'s grade: {student1._grade}")


result = student1.increase_grade(5)


print(f"{student1.name}'s new ugrade: {student1._grade}")


print(f"{student1.name} is passing: {result}")
