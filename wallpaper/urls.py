from django.urls import path
from . import views 

app_name='wall'
urlpatterns = [
    path('',views.kome,name='home'),
    path('contact/',views.contact,name="contact"),
    path('your_wallpapers/',views.y_wallpapers,name='your_wallpapers'),
    path('collection/',views.collection,name='collection'),
    path('games/',views.games,name='games'),
    path('nature/',views.nature,name='nature'),
    path('animals/',views.animals,name='animals'),
    path('space/',views.space,name='space'),
    path('abstract/',views.abstract,name='abstract'),
    path('architecture/',views.architecture,name='architecture'),
    path('cars/',views.cars,name='cars')
]