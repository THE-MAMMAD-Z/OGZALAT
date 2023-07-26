from django.shortcuts import render
from django.http import HttpResponse 
from  .models import *
# Create your views here.

def kome(request) :
    return render(request,'walls/Home.html')

def contact(request) :
    return render(request,'walls/contact.html')

def y_wallpapers(request) :
    return render(request,'walls/your-wallpapers.html')

def collection(request) :
    return render(request,'walls/collection.html')



def nature(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/nature.html',context)

def abstract(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/abstract.html',context)

def cars(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/cars.html',context)

def architecture(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/architecture.html',context)

def animals(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/animals.html',context)

def space(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/space.html',context)

def games(request,):
    wall = Wallpaper.objects.all()
    context = {
        "photolist" : wall,
        "photocount" : wall.count()
    }
    return render(request ,'walls/category/games.html',context)

