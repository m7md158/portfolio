from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Skills(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50) 
    birth_date = models.DateField()
    website  = models.URLField(max_length=300)
    email = models.EmailField()
    cv = models.FileField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    


    
    

    
