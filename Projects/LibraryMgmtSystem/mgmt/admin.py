from django.contrib import admin
from mgmt.models import Book, Student, IssuedBook

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','genre','author']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','roll_no']

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ['book','borrower','issued_date','expiry_date']
