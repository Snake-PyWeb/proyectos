from .models import post
from django import forms 

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['titulo','descripcion',]


