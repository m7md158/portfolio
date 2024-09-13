from django.db import models
from django.utils.text import slugify
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
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    