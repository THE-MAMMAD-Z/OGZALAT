# Generated by Django 4.2.3 on 2023-07-24 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallpaper',
            old_name='color',
            new_name='category',
        ),
    ]