from django.urls import path
from .views import *

urlpatterns = [
    path('', listall, name='a'),
    path('categories/', Listing.as_view(), name='category-list'),
    path('categories/new/', Adding.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', Updating.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', Deleting.as_view(), name='category-delete'),
]