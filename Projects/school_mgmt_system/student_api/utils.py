from datetime import datetime

class Student:
    def __init__(self, roll_no, name, email, age):
        self.roll_no = roll_no
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.now()

    def __str__(self):
        return f"<Student: {self.name}>"

