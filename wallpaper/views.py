from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from  .models import *
from django.core.paginator import Paginator
from django.http import FileResponse
from .forms import ContactForm
from django.shortcuts import get_object_or_404
# Create your views here.

def kome(request) :
    return render(request,'walls/Home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            

            form.save()
            return render(request,'walls/success.html')  # Replace 'contact_success' with the URL name for the success page
    else:
        form = ContactForm()

    return render(request, 'walls/contact.html', {'form': form})



def collection(request) :
    return render(request,'walls/collection.html')



def nature(request,):
    wall = Wallpaper.objects.filter(category="NATURE")
    paginator = Paginator(wall, 3)  # Display 10 items per page
    esm="NATURE"
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def abstract(request,):
    wall = Wallpaper.objects.filter(category="ABSTRACT")
    paginator = Paginator(wall, 3)  
    esm="ABSTRACT"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def cars(request,):
    wall = Wallpaper.objects.filter(category="CARS")
    paginator = Paginator(wall, 6)  # Display 10 items per page
    esm="CARS"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def architecture(request,):
    wall = Wallpaper.objects.filter(category="ARCHITECTURE")
    paginator = Paginator(wall, 3)  # Display 10 items per page
    esm="ARCHITECTURE"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def animals(request,):
    wall = Wallpaper.objects.filter(category="ANIMALS")
    paginator = Paginator(wall, 3)  # Display 10 items per page
    esm="ANIMLAS"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def space(request,):
    wall = Wallpaper.objects.filter(category="SPACE")
    paginator = Paginator(wall, 3)  # Display 10 items per page
    esm="SPACE"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def games(request,):
    
    wall = Wallpaper.objects.filter(category="GAMES")
    paginator = Paginator(wall, 6)  # Display 10 items per page
    esm="GAMES"

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : wall,
        "photocount" : wall.count(),
        'page_obj': page_obj,
        "esm": esm
    }
    return render(request ,'walls/category/caategory.html',context)

def download_file(request, file_id):
    my_file = get_object_or_404(Wallpaper, id=file_id)
    file_path = my_file.photo.path

    # Use Django's FileResponse to serve the file for download
    response = FileResponse(open(file_path, 'rb'))
    return response


# def test(request,):
#     if(2==2):
#         return render(request ,'walls/category/caategory.html')
#     else :
#         return render(request ,'walls/category/caategory.html')


def live_wallpaper(request):
    walls = LiveWalls.objects.all()
    paginator = Paginator(walls, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "photolist" : walls,
        "photocount" : walls.count(),
        'page_obj': page_obj
    }
    return render(request ,'walls/live_wallpapers.html',context)


def d_live(request,num):
    live = LiveWalls.objects.get(id=num)
    context={
        "live":live
    }

    return render(request,"walls/downloadlive.html",context)
