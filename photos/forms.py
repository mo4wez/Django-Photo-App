from django import forms

from .models import Photo

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'category',]
