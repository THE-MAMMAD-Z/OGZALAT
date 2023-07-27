from django.shortcuts import render
from django.http import HttpResponse 
from  .models import *
from django.core.paginator import Paginator

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
    wall = Wallpaper.objects.filter(category="ANIMALS")
    paginator = Paginator(wall, 3)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/nature.html',context)

def abstract(request,):
    wall = Wallpaper.objects.filter(category="ABSTRACT")
    paginator = Paginator(wall, 3)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/abstract.html',context)

def cars(request,):
    wall = Wallpaper.objects.filter(category="CARS")
    paginator = Paginator(wall, 6)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/cars.html',context)

def architecture(request,):
    wall = Wallpaper.objects.filter(category="ARCHITECTURE")
    paginator = Paginator(wall, 3)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/architecture.html',context)

def animals(request,):
    wall = Wallpaper.objects.filter(category="ANIMALS")
    paginator = Paginator(wall, 3)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/animals.html',context)

def space(request,):
    wall = Wallpaper.objects.filter(category="SPACE")
    paginator = Paginator(wall, 3)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/space.html',context)

def games(request,):
    wall = Wallpaper.objects.filter(category="GAMES")
    paginator = Paginator(wall, 6)  # Display 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/category/games.html',context)

