from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from base.models import orders, tables 
# from .models import orders
from .forms import userForm
#from .models import orders 

@login_required(login_url='login')
def homePage(request):
    order=orders.objects.all()
    return render(request, 'base/home.html')


@login_required(login_url='login')
def trackOrder(request):
    if request.method=='POST':
        if request.POST['orderId'] != '':
            orderId=request.POST['orderId']
            order=orders.objects.filter(Q(id__icontains=orderId))
            print(order)
            print("ebhdbf")
            if order.count()==0:
                messages=['Invalid order id']
                context={'messages': messages}
            else:
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
@login_required(login_url='login')
def review(request):
    return render(request, 'base/review.html')

@login_required(login_url='login')
def menu(request):
    return render(request, 'base/menu.html')

@login_required(login_url='login')
def recipeSharing(request):
    return render(request, 'base/recipeSharing.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')

@login_required(login_url='login')
def cart(request):
    return render(request, 'base/cart.html')



def loginPage(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('home')
    else:
        logout(request)

    if request.method=='POST':
        email=request.POST['email'].lower()
        password=request.POST['password1']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Email Id or password.")
            return redirect('login')
    else: 
        context={'page':page}
        return render(request, 'base/login.html', context)
    
    
    
def register(request):
    form = userForm()
    
    if request.method == 'POST': 
        email = request.POST.get('email', '').lower()  
        password1 = request.POST.get('password1', '') 
        password2 = request.POST.get('password2', '') 

        
        if not email:
            messages.error(request, "Please fill in the email.")
            return render(request, 'base/register.html', {'form': form})
    
            
        elif not password1:
            messages.error(request, "Please fill in the password.")
            return render(request, 'base/register.html', {'form': form})
        
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'base/register.html', {'form': form})
        
        elif len(password1) < 6:
            messages.error(request, "Password length must be at least 6 characters.")
            return render(request, 'base/register.html', {'form': form})
        
        elif len(password1) > 15:
            messages.error(request, "Password length must not exceed 15 characters.")
            return render(request, 'base/register.html', {'form': form})
        
        else: 
            form = userForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.email = email
                user.password=password1
                form.save()
                messages.success(request, "Registration successful!")
                return redirect('login')  

            else:
                messages.error(request, "An error occurred during registration.")
            return render(request, 'base/register.html', {'form': form})
        
    else:
        form = userForm()
        
        return render(request, 'base/register.html', {'form': form})
    
    
def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    
    


