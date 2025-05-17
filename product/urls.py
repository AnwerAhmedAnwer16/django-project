from django.urls import path
from .views import *
urlpatterns = [
    path('listing', listing ,name = 'listing'),
    path('updating', updating ,name = 'updating'),
    path('adding', adding ,name = 'adding'),
    path('deleting', deleting ,name = 'deleting'),
]