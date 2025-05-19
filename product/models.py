from django.db import models
from categories.models import Categories

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='product/', blank=True, default='product/img.png')
    stock = models.IntegerField(default=1)
    catid = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE,
       )
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.name
