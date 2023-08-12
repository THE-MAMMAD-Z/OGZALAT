from django.urls import path
from .views import *

app_name='wall'
urlpatterns = [
    path('',kome,name='home'),
    path('contact/',contact,name="contact"),
    path('collection/',collection,name='collection'),
    path('games/',games,name='games'),
    path('nature/',nature,name='nature'),
    path('animals/',animals,name='animals'),
    path('space/',space,name='space'),
    path('abstract/',abstract,name='abstract'),
    path('architecture/',architecture,name='architecture'),
    path('cars/',cars,name='cars'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('live_wallpapers/',live_wallpaper,name="live"),
    path('download_livewallpapers/<int:num>/',d_live,name="d_live")
]