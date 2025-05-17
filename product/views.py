from itertools import product

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from categories.models import *
from .models import *
# Create your views here.
def listing(request):
    dict = {'products': product.object.all()}
    return render(request, 'product/productbase', dict)
def adding(request):
    if request.method == 'POST':
        if request.POST['name'] and request.FILES['img'] and request.POST['product_id']:
            Product.objects.create(
                name = request.POST['name'],
                description = request.POST['description'],
                price = request.POST['price'],
                # catid =  Categories.objects.get(pk=request.POST['cat_id'])
            )
    return render(request, 'product/insert.html')
def updating(request, id):
    return render(request, 'product/update.html')
def deleting(request):
    return HttpResponse('this is deleting')
def test(request):
    return render(request, 'product/productbase.html')
