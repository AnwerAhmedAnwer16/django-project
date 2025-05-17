from django.urls import path
from .views import *
urlpatterns = [
    path('',listall,name = 'a' )
]