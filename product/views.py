from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listing(request):
    return HttpResponse('this is inserting')
def adding(request):
    return HttpResponse('this is adding')
def updating(request):
    return HttpResponse('this is updating')
def deleting(request):
    return HttpResponse('this is deleting')
