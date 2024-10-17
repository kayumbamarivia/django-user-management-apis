from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def home(request):
    # u1 = Users()
    # u1.id = 1
    # u1.name = "KAYUMBA JMV"
    # u1.email = "kayumbaj88@gmail.com"
    
    # u2 = Users()
    # u2.id = 2
    # u2.name = "BISANGWA Eugene"
    # u2.email = "bisangwa@gmail.com"
    
    # u3 = Users()
    # u3.id = 3
    # u3.name = "MUGABE Rashid"
    # u3.email = "rashid@gmail.com"
    
    # u4 = Users()
    # u4.id = 4
    # u4.name = "MWIZERE Dieudonne"
    # u4.email = "dieudonne@gmail.com"
    # return render(request,'home.html',{'users':[u1, u2, u3, u4]})
    
    users = Users.objects.all()
    return render(request, 'home.html', {"users":users})

def add(request):
    var1 = int(request.POST["num1"])
    var2 = int(request.POST["num2"])
    res = var1 + var2
    return render(request, 'result.html',{"result":res})