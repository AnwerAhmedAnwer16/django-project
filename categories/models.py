from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=1)
    def __str__(self):
        return self.name