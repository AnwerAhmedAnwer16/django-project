from django.db import models
from categories.models import *



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    img = models.ImageField(upload_to='product/',blank=1)
    catid = models.ForeignKey(to = Categories, on_delete= models.CASCADE)
