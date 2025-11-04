from django.db import models

'''Create a model representing a company with departments and employees, using ForeignKey relationships'''
class Department(models.Model):
  name = models.CharField(max_length=200)

class Employee(models.Model):
  name = models.CharField(max_length=200)
  department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

''' Create a model for a product and its detailed description using a OneToOneField'''

class Product(models.Model):
  name = models.CharField(max_length=200)

class Description(models.Model):
  product = models.OneToOneField(Product, on_delete=models.CASCADE)
  description = models.TextField()

'''Implement a ManyToManyField to model the relationship between students and courses'''

class Student(models.Model):
  name = models.CharField(max_length=200)

class Course(models.Model):
  name = models.CharField(max_length=200)
  student = models.ManyToManyField(Student, related_name='courses')

'''Optimize queries involving complex relationships using prefetching and select_related'''


employees = Employee.objects.select_related('department')
products = Description.objects.select_related('product')
students = Student.objects.prefetch_related('courses')
courses = Course.objects.prefetch_related('student')