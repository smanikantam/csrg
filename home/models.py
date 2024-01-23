from django.db import models
from django import forms

class Fyles(models.Model):
    # file = models.FileField()
    name = models.CharField()
    date = models.DateField(auto_now_add=True)
    added_by = models.CharField()
    # file_size = models.CharField(max_length=25)

# Define a separate form class for file uploads
# class FileUploadForm(forms.ModelForm):
#     class Meta:
#         model = Fyles
#         fields = ['name', 'added_by', 'file']



