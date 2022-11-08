from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length = 100)     

class restaurants(models.Model):
    name = models.CharField(max_length=100)   
    rating = models.CharField(max_length=100)
    description = models.CharField(max_length=500) 
    image = models.ImageField(null=True, blank=True, upload_to="images/")

class menu(models.Model):
    name = models.CharField(max_length=250)
    food = models.CharField(max_length=250)
    price = models.IntegerField(default=100)

class comment(models.Model):
    name = models.CharField(max_length=250, null = True, blank = True)
    text = models.TextField(blank=True, null=True)


    

    


# class details(models.Model):
#     name = models.CharField(max_length=100)   
#     item_name = models.CharField(max_length=100) 
#     price = models.IntegerField(default=0)
#     slug = models.SlugField(max_length=1000, null=True, blank=True)
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         if not self.sulg:
#             self.slug = slugify(self.name)
#         return super().save(*args, **kwargs)               