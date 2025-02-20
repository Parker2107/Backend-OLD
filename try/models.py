from django.db import models

class userProfile(models.Model):
    regno = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return f"{self.id} - {self.name} - {self.age} - {self.regno}"