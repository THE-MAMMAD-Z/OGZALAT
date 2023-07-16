from django.urls import path
from . import views 

urlpatterns = [
    path('home/',views.kome),
    path('contact/',views.contact,name="contact"),
    path('your_wallpapers/',views.y_wallpapers),
    path('index/',views.index),
    path('collection/',views.collection),
    path('games/',views.games)
]