from django.db import models
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name
    @classmethod
    def getbyid(cls,id):
        a = cls.objects.get(pk=id)
        return a.id


