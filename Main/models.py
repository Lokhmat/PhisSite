from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class form(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    grade = models.IntegerField()
    pro = models.IntegerField()
    link = models.CharField(max_length=30)


class foruser(models.Model):
    login = models.CharField(max_length=100)
    zadachi = models.CharField(max_length=300)
    teachers = models.CharField(max_length=300)
    olimps = models.CharField(max_length=300)

   # def __str__(self):
    # return self.title


class zadachi(models.Model):
    difficulti = models.CharField(max_length=45)
    text = models.CharField(max_length=20000)
    theme = models.CharField(max_length=45)
    tags = models.CharField(max_length=200)
    name = models.CharField(max_length=45)
    answer = models.CharField(max_length=150)


class courses(models.Model):
    teacher = models.IntegerField()
    students = models.CharField(max_length=100000)
    name = models.CharField(max_length=30)
    Theme = models.CharField(max_length=30)
    other = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    done_tasks = models.CharField(max_length=10000)
    ava = models.CharField(max_length=100000)
# class Course(models.Model):
