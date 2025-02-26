from django.db import models

class userProfile(models.Model):
    regno = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    hostel = models.CharField(max_length=5)
    block = models.CharField(max_length=5)
    number = models.CharField(max_length=15, unique=True)
    admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.regno}"
    
class formData(models.Model):
    regno = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    domain = models.TextField()
    
    def __str__(self):
        return f"{self.regno}"