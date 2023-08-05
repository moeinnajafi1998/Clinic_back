from django.urls import path
from .views import *

urlpatterns = [
    path('clinics/', ClinicListCreateView.as_view(), name='clinic-list-create'),
    path('clinics/<int:pk>/', ClinicRetrieveUpdateDeleteView.as_view(), name='clinic-retrieve-update-delete'),
    
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),

    path('warehouses/', WhareHouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WhareHouseRetrieveUpdateDeleteView.as_view(), name='warehouse-retrieve-update-delete'),

    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-retrieve-update-delete'),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
]