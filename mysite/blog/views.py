from django.shortcuts import render, HttpResponse
from blog.models import Category,Blog

# Create your views here.
def login(request):
    return render(request,'blog/login.html')

def contactus(request):
    return render (request,'blog/contactus.html')

def home(request):
    return render(request,'blog/home.html')