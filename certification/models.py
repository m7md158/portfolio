from django.db import models

# Create your models here.

class Certificate(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='certification/')
    
    
    
    