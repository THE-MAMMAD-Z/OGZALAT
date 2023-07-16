from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def kome(request) :
    return render(request,'walls/Home.html')

def contact(request) :
    return render(request,'walls/contact.html')

def y_wallpapers(request) :
    return render(request,'walls/your-wallpapers.html')

def collection(request) :
    return render(request,'walls/collection.html')

def games(request) :
    return render(request,'walls/games.html')