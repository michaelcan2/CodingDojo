# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, data):
        errors = []
        if len(data['first_name']) < 2 or any(char.isdigit() for char in data['first_name']) :
            errors.append("Invalid First Name")
        if len(data['last_name']) < 2 or any(char.isdigit() for char in data['last_name']) :
            errors.append("Invalid Last Name")    
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")
        #departure = datetime.datetime.strptime(data[""],"%Y-%M-%D")  
        #id departure < datetime.datetme.now():
        # errors.append("Must leave in the Future")
        return errors
    def login_validator(self, data):
        errors = []   
        print self.filter(email=data['email'])      
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")      
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        if self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        if  bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
            errors.append(" bad password")  
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class CourseManager(models.Manager):
    def Course_validator(self, data):
        errors = []
        if len(data['course_name']) < 2 or any(char.isdigit() for char in data['course_name']) :
            errors.append("Invalid Course Name")
        if len(data['course_description']) < 2 :
            errors.append("Invalid Description")      
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=500)
    course_creator = models.ForeignKey(User,related_name='created_course')
    students = models.ManyToManyField(User,related_name='courses')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Pokes(models.Model):
    poker = models.ForeignKey(User,related_name="who_pokeing")
    pokee = models.ForeignKey(User,related_name="got_poked")
    # count=models.IntegerField(default+=1)

    
    # to find the person who is being poked, grouped by pokee.count

   
    




