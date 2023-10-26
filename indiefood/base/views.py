from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseNotFound
# from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from base.models import orders, tables 
# from .models import orders
# from .forms import userForm
#from .models import orders 

def homePage(request):
    order=orders.objects.all()
    return render(request, 'base/home.html')
def trackOrder(request):
    if request.method=='POST':
        if request.POST['orderId'] != '':
            orderId=request.POST['orderId']
            order=orders.objects.filter(Q(id__icontains=orderId))
            context={'orders': order}
            return render(request, 'base/order_track.html', context)
        else:
            try:
                name=request.POST['name']
                phone=request.POST['phone']
                email=request.POST['email']
                noofpersons=request.POST['noofpersons']
                tabletype=request.POST['tabletype']
                date=request.POST['date']
                table=tables(name=name, phone_number=phone, email=email, noofperson=noofpersons, tableType=tabletype, Time=date)
                table.save()
                messages=['table booked']
                context={'messages': messages}
                # context_dict = get_context_dict(context)
                return render(request, 'base/order_track.html', context)
            except:
                messages=['Error occured, try again']
                context={'messages': messages}
                return render(request, 'base/order_track.html', context)


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


