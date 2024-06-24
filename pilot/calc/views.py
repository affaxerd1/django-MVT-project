from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':"Kemei"});

def add(request):

    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    res= num1+num2
    return render(request, 'result.html', {'result':res})