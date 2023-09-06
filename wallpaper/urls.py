from django.urls import path
from .views import *

app_name='wall'
urlpatterns = [
    path('',kome,name='home'),
    path('contact/',contact,name="contact"),
    path('collection/',collection,name='collection'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('live_wallpapers/',live_wallpaper,name="live"),
    path('download_livewallpapers/<int:num>/',d_live,name="d_live"),
    path('category/<str:name>/',category,name="category")
]