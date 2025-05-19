from django.urls import path
from .views import *
urlpatterns = [
    path('listing', listing ,name = 'listing'),
    path('updating/<int:id>', updating ,name = 'updating'),
    path('adding', adding ,name = 'adding'),
    path('hard/<int:id>', hardy, name = 'hard'),
    path('soft/<int:id>', deleting, name = 'soft')

]