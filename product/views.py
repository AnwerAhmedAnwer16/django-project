from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.context_processors import request
from rest_framework import generics
from django.views.generic import *
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from rest_framework.response import Response
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
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('listing')


@api_view(['GET', 'POST'])
def product_list_create(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'success': True,
            'count': len(serializer.data),
            'products': serializer.data
        })

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'product': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'  # or 'pk' if you prefer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'status': 'success',
            'message': 'Product updated successfully',
            'data': serializer.data
        })


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    all_products = Product.objects.all()
    product_serializer = ProductSerializer
    lookup_field = 'id'


