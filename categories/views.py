from django.shortcuts import render
from .models import Categories
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def listall(request):
    a = {'categories':Categories.objects.all()}
    return render(request, 'categories/categories.html', a)
class Listing(ListView):
    model = Categories
    template_name = 'categories/clist.html'
    context_object_name = 'categories'

class Adding(CreateView):
    model = Categories
    template_name = 'categories/form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

class Updating(UpdateView):
    model = Categories
    template_name = 'categories/form.html'
    fields = ['name', 'description']
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')

class Deleting(DeleteView):
    model = Categories
    template_name = 'categories/confirm_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category-list')
