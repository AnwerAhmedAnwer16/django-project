from django.shortcuts import render
from .models import Categories


# Create your views here.
def listall(request):
    a = {'categories':Categories.objects.all()}
    return render(request, 'categories/categories.html', a)