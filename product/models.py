from django.db import models
from categories.models import Categories

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products/', blank=True)
    catid = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        default = 1
    )


    def __str__(self):
        return self.name
