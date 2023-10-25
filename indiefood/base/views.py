from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseNotFound
# from django.contrib.auth.models import User
# from django.db.models import Q
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from base.models import Courses, files ,Syllabus
# from .forms import userForm
#from .models import orders 

def homePage(request):
    return render(request, 'base/home.html')


