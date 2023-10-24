from django.db import models


# Create your models here.

class Fyles(models.Model):
    file = models.FileField(upload_to='media/')
    name=models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    added_by=models.CharField(max_length=25)
    file_size=models.CharField(max_length=25)



