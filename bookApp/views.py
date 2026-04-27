from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
@login_required
def homePage(req):
    data = ProfileModel.objects.filter(user=req.user)
    context = {
        'data':data
    }
    return render(req, 'pages/home.html', context)

def registerPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm-password')

        user_exist =UserModel.objects.filter(username=username).exists()
        email_exist =UserModel.objects.filter(email=email).exists()

        if user_exist and email_exist:
            messages.error(req, 'User already exist')
            return redirect('register')
        else:
            if password == confirm_password:
                user =UserModel.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                ProfileModel.objects.create(
                    user =user
                )
                messages.success(req, 'User created successfully')
                return redirect('login')
            else:
                 messages.error(req, 'Password does not match')
                 return redirect('register')


    return render(req, 'account/register.html')

       
def loginPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, 'Invalid username or password')
            return redirect('login')
    return render(req, 'account/login.html')
        
               
          
def logoutPage(req):
    logout(req)
    return redirect('login')

@login_required
def profilePage(req):
    user = req.user.profile
    if req.method == 'POST':
        form = ProfileUpdateForm(req.POST, req.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')






    form = ProfileUpdateForm(instance=user)
    context = {
        'form': form
    }
    return render(req, 'pages/profile.html', context)

@login_required
def bookPage(req):
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            book =form.save(commit=False)
            book.user = req.user
            book.save()
            return redirect('book')


    data=BookModel.objects.filter(user=req.user)
    form = BookForm()
    context = {
        'form': form,
        'book': data
    }

    return render(req, 'pages/book.html', context)



@login_required
def sellBookPage(req):
    if req.method == 'POST':
        form = SellBookForm(req.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sell_by = req.user 
            sale.save()
            return redirect('sell')
        
    data =SellBookModel.objects.filter(sell_by=req.user)
    
    form = SellBookForm()
    context = {
        'form': form,
        'sell': data
    }
    return render(req, 'pages/sell_book.html', context)