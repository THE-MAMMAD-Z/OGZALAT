from django import forms
from wallpaper.models import Contact
from django.core.validators import EmailValidator



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'phone')
