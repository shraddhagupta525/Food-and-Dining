from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseNotFound
# from django.contrib.auth.models import User
# from django.db.models import Q
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from base.models import orders
# from .forms import userForm
#from .models import orders 

def homePage(request):
    order=orders.objects.all()
    print(order)
    return render(request, 'base/home.html')
def trackOrder(request):
    return render(request, 'base/order_track.html')
# temp
def review(request):
    return render(request, 'base/review.html')
def menu(request):
    return render(request, 'base/menu.html')
def recipeSharing(request):
    return render(request, 'base/recipeSharing.html')
def about(request):
    return render(request, 'base/about.html')


