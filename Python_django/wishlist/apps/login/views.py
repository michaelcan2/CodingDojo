# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import User, Course

# Create your views here.
def index(request) :
   
    return render(request, 'login/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        password = bcrypt.hashpw("request.POST['password']".encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    print request.POST
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['current_user'] =  User.objects.filter(email=request.POST['email'])[0].id
        return redirect('/success')

def success(request):
    if "current_user" not in request.session:
        return redirect('/')
    joined=User.objects.get(id=request.session['current_user'])
    creator=User.objects.get(id=request.session['current_user'])
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'courses': Course.objects.all().exclude(students=joined.id),
        'users' : User.objects.all().exclude(courses=creator.id)
    }
    return render(request, 'login/success.html', context)

def add(request):
    return render(request, 'login/add.html')

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def wish(request,id):
    current_course = Course.objects.get(id=id)
    context = {
        "course":Course.objects.get(id=id),
        "enrolled_students":User.objects.all().filter(courses=current_course)
    }
    return render(request, "login/wishing.html", context)

def new(request):
    if request.method== 'POST':
        errors = Course.objects.Course_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/add')
        name_inputed=request.POST['course_name']
        creator=User.objects.get(id=request.session['current_user'])
        Course.objects.create(name=name_inputed,course_creator=creator)
    return redirect('/success')

def join (request, id):
    name = User.objects.get(id=request.session["current_user"])
    course = Course.objects.get(id=id)
    name.courses.add(course)
    return redirect("/success")

def drop(request,id):
    name=User.objects.get(id=request.session["current_user"])
    wish = Course.objects.get(id=id)
    name.courses.remove(wish)
    return redirect("/success")