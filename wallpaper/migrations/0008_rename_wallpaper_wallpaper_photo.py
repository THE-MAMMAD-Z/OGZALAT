# Generated by Django 4.1.6 on 2023-07-27 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0007_alter_wallpaper_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallpaper',
            old_name='Wallpaper',
            new_name='photo',
        ),
    ]
