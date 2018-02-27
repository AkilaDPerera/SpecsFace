from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage()

class Image(models.Model):
    # url = models.URLField(unique=True) #The url to the evesite
    image = models.ImageField(upload_to="", storage=fs)