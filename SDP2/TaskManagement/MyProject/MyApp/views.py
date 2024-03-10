from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def account(request):
    return render(request,'account.html')

def notification(request):
    return render(request,'notification.html')

def feedback(request):
    return render(request,'feedback.html')
