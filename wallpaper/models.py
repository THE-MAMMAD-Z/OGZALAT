from django.db import models

class Wallpaper(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image/')
    Wallpaper=models.ImageField(upload_to='walls/')
    created_time = models.DateTimeField(auto_now=True)
    
    CATEGORY = [
        ('GAMES' , 'Games'),
        ('NATURE' , 'Nature'),
        ('ABSTRACT' , 'Abstract'),
        ('CARS' , 'Cars'),
        ('ANIMALS' , 'Animals') ,
        ('ARCHITECTURE' , 'Architecture'),
        ('SPACE' , 'Space'), 
        ('RANDOM' , 'Random'),
    ]
    category = models.CharField(max_length=15, choices=CATEGORY , default='Random')

    def __str__(self) :
        return self.title
    


class Contact(models.Model) :

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    phone=models.IntegerField()
    created_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


