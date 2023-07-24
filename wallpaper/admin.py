from django.contrib import admin
from .models import *

class WallpaperAdmin(admin.ModelAdmin):
    list_display=['title','created_time','category']
    date_hierarchy = 'created_time'
    search_fields = ['title']
    list_filter = ['category']

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','created_time']
    date_hierarchy = 'created_time'
    search_fields = ['name','message']


admin.site.register(Wallpaper,WallpaperAdmin)
admin.site.register(Contact,ContactAdmin)