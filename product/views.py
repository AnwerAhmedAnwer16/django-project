from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.context_processors import request
from django.views.generic import *
from django.urls import reverse_lazy

from product.forms import *
from categories.models import Categories
from .models import Product

def listing(request):
    dict = {'products': Product.objects.filter(status=True)}
    return render(request, 'product/productbase.html', dict)

def adding(request):
    if request.method == 'POST':
            prod=Product(
                name=request.POST['name'],
                description=request.POST['description'],
                price=request.POST['price'],
                stock=request.POST['stock'],
                img=request.FILES['img'],
                catid=Categories.objects.get(pk=request.POST['catid'])
            )
            prod.save()
            print(request.POST['name'])
            return redirect('listing')

    cats = Categories.objects.all()
    return render(request, 'product/insert.html', {'cats': cats})

def updating(request, id):
    context ={'oldobj':Product.getbyid(id), 'cats':Categories.objects.all()}
    if request.method == 'Post':
        oldy = Product.getbyid(id)
        oldy.name = request.POST['name']
        oldy.description = request.POST['description']
        oldy.price = request.POST['price']
        oldy.stock = request.POST['stock']
        oldy.catid = Categories.getbyid(request.POST['catid'])
        oldy.img = request.FILES['stock']
        oldy.save()
    return render(request, 'product/update.html', context)


def deleting(request, id):
    p = get_object_or_404(Product ,id = id)
    p.status = False
    p.save()
    return redirect('listing')

def hardy(request, id):
    print(id)
    Product.objects.filter(id=id).delete()
    return redirect('listing')

#####################
def addingf(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new')
    else:
        form = ProductForm()
    return render(request, 'product/new.html', {'form': form})
def updatingf(request,id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('listing')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/neww.html', {'form': form})


class Listingcbv(View):
    def get(self, request):
        products = Product.objects.filter(status=True)
        context = {
            'products': products
        }
        return render(request, 'product/listingcbv.html', context)


class Deletingcbv(View):
    def get(self, request, pk):
        # Get the product and delete it directly
        product = Product.objects.get(pk=pk)
        product.delete()
        # Redirect back to the listing page
        return redirect('listing')