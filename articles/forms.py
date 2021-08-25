from django import forms
from . import models

class ArticleCreate(forms.ModelForm):
    class Meta:
        model=models.Articles
        fields=['title','slug','body','image']
