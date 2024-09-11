from django.db import models

# Create your models here.






class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete= models.CASCADE) 
    image = models.ImageField(upload_to='portfolio/')
    github = models.URLField()
 


    def __str__(self):
        return self.title
    