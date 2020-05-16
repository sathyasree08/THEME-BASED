from django.db import models

# Create your models here.
class officialwebsites(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='LOGO')
    url= models.URLField(max_length = 200) 
class location(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=200)
class drive(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)



    

 