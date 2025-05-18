from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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
    pass
def deleting(request, id):
    p = get_object_or_404(Product ,id = id)
    p.status = False
    p.save()
    return redirect('listing')

def hardy(request, id):
    print(id)
    Product.objects.filter(id=id).delete()
    return redirect('listing')