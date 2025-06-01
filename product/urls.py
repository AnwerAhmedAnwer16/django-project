from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('listing', listing ,name = 'listing'),
    path('updating/<int:id>', updating ,name = 'updating'),
    path('adding', adding ,name = 'adding'),
    path('hard/<int:id>', hardy, name = 'hard'),
    path('soft/<int:id>', deleting, name = 'soft'),
    path('new/', addingf, name = 'new'),
    path('neww/<int:id>', updatingf, name = 'neww'),
    path('listingf/', views.Listingcbv.as_view(), name = 'listo'),
    path('delel/<int:pk>', views.Deletingcbv.as_view(), name = 'deleo'),
    path('products/', product_list_create, name='product-list-create'),
    path('products/<int:id>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:id>/', ProductDetailView.as_view()),

]