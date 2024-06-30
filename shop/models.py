from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, default='indoor', blank=True, null=True)
    
    def __str__(self):
        return self.name
    


class Project(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True, default='Project')
    description = models.TextField()
    employee = models.CharField(max_length=100, blank=True, null=True, default='IUST')
    img_proj = models.FileField(upload_to='images', default=None)
    img_emp = models.FileField(upload_to='images', default=None)
    created = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def img_empURL(self):
        try:
            url = self.img_emp.url
        except:
            url = ''
        return url

    @property
    def img_projURL(self):
        try:
            url = self.img_proj.url
        except:
            url = ''
        return url



class Product(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=200, null=True, blank=True, default='See More')
    description = models.TextField()
    description2 = models.TextField(blank=True, null=True, default=None)
    img = models.FileField(upload_to='images', default=None)
    created = models.DateTimeField(auto_now_add=True)
    

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category_products')

    @property
    def imgURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
    






