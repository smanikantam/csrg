from django.db import models
from django import forms
from .models import Fyles


# Create your models here.

class Fyles(models.Model):
    file = models.FileField()
    name=models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    added_by=models.CharField(max_length=25)
    file_size=models.CharField(max_length=25)
    class FileUploadForm(forms.ModelForm):
        class Meta:
            model = Fyles
            fields = ['name', 'added_by', 'file']



