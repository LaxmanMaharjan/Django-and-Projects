from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    roll_no = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


def expiry_date():
    return datetime.today().date() + timedelta(days = 14)

class IssuedBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='issued_book')
    borrower = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='issued_student')
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default = expiry_date)

    def __str__(self):
        return self.book.name

class Fine(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fined_student')
    issue = models.OneToOneField(IssuedBook, on_delete=models.CASCADE, related_name='issued_fine')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student}=>{self.issue.book}=>{self.amount}"
