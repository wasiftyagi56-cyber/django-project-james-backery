from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def product(request):
    products=Product.objects.all()
    return render(request,'productsit.html', {'products':products})


def signup(request):
     if request.method=='POST':
      
      #fetch the value user from the foam

      user_name =request.POST['username']
      f_name =request.POST['first_name']
      l_name =request.POST['last_name']
      email =request.POST['email']
      password =request.POST['password']

      #create a New_user Object

      new_user =User.objects.create_user(username =user_name, first_name=f_name, last_name=l_name, email=email,password=password)

      messages.info(request,"User name Already Exists. Please try again")

      return redirect ('/login')
     return render(request, 'signup.html')



def login(request):
    if request.method=='POST':
        #fetch the value user from the form

        u_name =request.POST['username']
        password =request.POST['password']

        newuser1 =authenticate(request, username=u_name)
        if newuser1 is not None:
            login(request ,newuser1)
            messages.info(request, "You are Logged in successfully")
            return redirect('/Signup')

    return render (request,'login.html')


def shop(request):
    return render(request,'shop.html')


def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')