from django.contrib import admin

from categories.models import Categories
from product.models import Product

# Register your models here.
admin.site.register(Categories)
admin.site.register(Product)