from django.urls import path
from .views import *

urlpatterns = [
    # path('', listall, name='a'),
    path('', Listing.as_view(), name='category-list'),
    path('new', Adding.as_view(), name='category-create'),
    path('edit/<int:pk>', Updating.as_view(), name='category-update'),
    path('delete/<int:pk>', Deleting.as_view(), name='category-delete'),
]