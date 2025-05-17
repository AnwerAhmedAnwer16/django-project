from django.db import models
from categories.models import Categories  # More explicit import

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Increased max_digits
    stock = models.IntegerField()
    img = models.ImageField(upload_to='products/', blank=True)  # Changed to boolean
    catid = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.name