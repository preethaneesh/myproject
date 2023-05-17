from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
class Team(models.Model):
    nam=models.CharField(max_length=250)
    ig=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.nam

        
    
