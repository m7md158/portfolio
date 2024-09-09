from django.db import models


class WorkExperience(models.Model):
    title = models.CharField(max_length=35, null=True, blank=True)
    name_company = models.CharField(max_length=35)

    start_date = models.DateField(null=True, blank=True) 
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField()
    
    def  present_end_date(self):
        if self.end_date is None:
            return 'Present'
        
        return self.end_date
    
    def __str__(self):
        return self.title
        
        
        
class Education(models.Model):
    degree = models.CharField(max_length=100,null=True, blank=True)  # e.g., "Master's Degree"
    institution = models.CharField(max_length=100)  # e.g., university name
    start_date = models.DateField(null=True, blank=True)  
    end_date = models.DateField(null=True, blank=True)
    trac_name = models.CharField(max_length=50)
    description = models.TextField()
    
    
    def  present_end_date(self):
        if self.end_date is None:
            return 'Present'
        
        return self.end_date
        
        
        

    def __str__(self):
        return self.degree