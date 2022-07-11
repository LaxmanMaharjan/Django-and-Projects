from datetime import datetime

class College:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}:{self.location}"

class Student:
    def __init__(self, roll_no, name, email, age, college):
        self.roll_no = roll_no
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.now()
        self.college = college

    def __str__(self):
        return f"<Student: {self.name}>"

    def __repr__(self) -> str:
        return f"<Student: {self.name}:{self.age}>"

