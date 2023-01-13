from .models import movie
from django import forms

class movie_update_form(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','img']