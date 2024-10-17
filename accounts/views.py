from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       password1 = request.POST['password']
       password2 = request.POST['confirm_password']
       email = request.POST['email']
       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request, 'Username already taken')
           elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
           else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User created...')
                redirect('login')
       else:
           messages.info(request, 'Password does not match') 
       return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
       email = request.POST['email']
       password1 = request.POST['password']
       user = auth.authenticate(email=email, password1=password1)
       if user is not None:
           auth.login(request, user)
           return redirect('/')
       else:
           messages.info(request, 'Invalid credentials')
           return redirect('login')
    else:    
        return render(request, 'login.html')