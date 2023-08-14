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

    path('users/', UserListView.as_view(), name='user-list-create'),
    path('delete-user/<int:pk>/', DeleteUser.as_view(), name='delete-user'),

    path('create-user/', CreateUser.as_view(), name='user-create'),

    path('clinic-admins/', ClinicAdminViewSet.as_view(), name='clinic-admins-list'),
    path('typical-users/', TypicalUserViewSet.as_view(), name='typical-user-list'),
    path('nurse-list/', NurseViewSet.as_view(), name='nurse-list'),
    path('sick-list/', SickViewSet.as_view(), name='sick-list'),
    path('warehouse-keepers/', WarehouseKeeperViewSet.as_view(), name='warehouse-keeper-list'),
    path('financial-managers/', FinancialManagerViewSet.as_view(), name='financial-manager-list'),

    path('user-recognization',UserRecognization.as_view(),name='user-recognization'),
    path('test-token',TestToken.as_view(),name='test-token'),

    path('create-permission',CreatePermissionView.as_view(),name='create-permission'),
    path('update-permission/<int:pk>/',UpdatePermissionView.as_view(),name='update-permission'),
    path('delete-permission/<int:pk>/',DeletePermissionView.as_view(),name='delete-permission'),
    path('list-permissions/', ListPermissionsView.as_view(), name='list-permissions'),



]