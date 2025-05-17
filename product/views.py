from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listing(request):
    return HttpResponse('this is inserting')
def adding(request):
    return render(request, 'product/insert.html')
def updating(request, id):
    return render(request, 'product/update.html')
def deleting(request):
    return HttpResponse('this is deleting')
def test(request):
    return render(request, 'product/productbase.html')
