# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import bcrypt
from .models import User, Course, Pokes

# Create your views here.
def index(request) :
   
    return render(request, 'login/index.html')
   
def register(request) :
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        # if the errors [] has a length the for loop will go through all those errors and the display the messages.
        for error in errors:
            messages.error(request, error)
            # ^^^messages take in a ^request, post what the ^error is.
        return redirect('/')
    else:
        password = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password)
        user.save()
        request.session['current_user'] = User.objects.filter(email=request.POST['email'])[0].id
        # ^^^^ first time your se = to 'current_user'
        return redirect('/success')

def login(request) :
    errors = User.objects.login_validator(request.POST)
    print request.POST
    # this shows your the entire post tht you submitted in your login page
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
    context = {
        'user' : User.objects.get(id=request.session['current_user']),
        'courses': Course.objects.all().exclude(students=joined.id),
        "enrolled_students":User.objects.all().exclude(id=request.session["current_user"]),
        'pokes': Pokes.objects.all()
        # *******************
        # were giving the name courses the value of the course model database so you can pass it to the template so that the html can use.
        # ***********
    }
    return render(request, 'login/success.html', context)

def logout(request):
    del request.session["current_user"]
    return redirect('/')

def course(request,id):
    current_course = Course.objects.get(id=id)
    context = {
        "course":Course.objects.get(id=id),
        "enrolled_students":User.objects.all().exclude(id=request.session["current_user"])
    }
    return render(request, "login/course.html", context)

def join (request, id):
    name = User.objects.get(id=request.session["current_user"])
    course = Course.objects.get(id=id)
    # ^^above .courses is the courses in quotes in students in the Course models
    # pulling the user and course models t
    name.courses.add(course)
    return redirect("/success")

def poke (request,id):
    # ^^this is the id of the current user to keep track of the current user
    #  creator=User.objects.get(id=request.session['current_user'])
    # self.bttn_clicks +=1
    # self.bttn['text'] = "you poked" + str(self.bttn_clicks)
    userpoker = User.objects.get(id=request.session["current_user"])
    pokee = User.objects.get(id=id)
    Pokes.objects.create(poker=userpoker,pokee=pokee)
    # you first make the relationship in models then you assign wether there the current
    # user or an id 
    # /////^^^pokes.objects.create it will add to the database??
    # user.beenpoked
    # the current user.
#     Pokes_exisiting=(poker=userpoker,pokee=pokee)

#     context={


#     }
# #       if Pokes_exisiting = len() > 0:
#         new_poke
#     else Pokes.count:
#    save.(Pokes_existing)
    # context={
    #     poeple_who_have_poked_me=.count()
    # }
    # ^^both can be poked and receieve pokes many times.
    # ^^^your creating the a new poker and pokee in to your database then you can display this information 
    # into your database.
    # when its a many to many you add to the table
    # but for foreignkeys this is its own table so we need to create an instance of data to the table.
    # everytime the userpoer pokes it adds an instance to the database.
    
    return redirect("/success")