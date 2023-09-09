from django import forms

from .models import Photo

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'category']
        
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Enter your photo description...',
                }
            ),
        }