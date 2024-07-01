from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username=request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
                print("username taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
                print("email already exists")
            else:
                user = User.objects.create_user(first_name=first_name, email=email, password=password, username=username)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, "passwords do not match")
            return redirect('register')
            print("passwords do not match");
    else:     
        return render(request, 'register.html' )
    

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Account does not exist")
            return redirect("register")
    else:
        return render(request, 'login.html')