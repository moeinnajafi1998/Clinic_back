from django.urls import path
from .views import *

urlpatterns = [
    # APIs for Clinic Model
    path('clinics/', ClinicListView.as_view(), name='clinic-list'),
    path('clinic-create/', ClinicCreateView.as_view(), name='clinic-create'),
    path('clinic-retrieve/<int:pk>/', ClinicRetrieveView.as_view(), name='clinic-retrieve'),
    path('clinic-update/<int:pk>/', ClinicUpdateView.as_view(), name='clinic-update'),
    path('clinic-delete/<int:pk>/', ClinicDeleteView.as_view(), name='clinic-delete'),
    # APIs for Category Model
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('category-retrieve/<int:pk>/', CategoryRetrieveView.as_view(), name='category-retrieve'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    # APIs for WareHouse Model
    path('warehouses/', WarehouseListView.as_view(), name='warehouse-list'),
    path('warehouse-create/', WarehouseCreateView.as_view(), name='warehouse-create'),
    path('warehouse-retrieve/<int:pk>/', WarehouseRetrieveView.as_view(), name='warehouse-retrieve'),
    path('warehouse-update/<int:pk>/', WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('warehouse-delete/<int:pk>/', WarehouseDeleteView.as_view(), name='warehouse-delete'),
    # APIs for Item Model
    path('items/', ItemListView.as_view(), name='item-list'),
    path('item-create/', ItemCreateView.as_view(), name='item-create'),
    path('item-retrieve/<int:pk>/', ItemRetrieveView.as_view(), name='item-retrieve'),
    path('item-update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
    # APIs for Permission Model
    path('permissions/', ListPermissionsView.as_view(), name='permission-list'),
    path('permission-create/',CreatePermissionView.as_view(),name='permission-create'),
    path('permission-retrieve/<int:pk>/', PermissionRetrieveView.as_view(), name='permission-retrieve'),
    path('permission-update/<int:pk>/',UpdatePermissionView.as_view(),name='permission-update'),
    path('permission-delete/<int:pk>/',DeletePermissionView.as_view(),name='permission-delete'),
    # APIs for User Model
    path('users/', UserListView.as_view(), name='user-list'),
    path('clinic-admins/', ClinicAdminViewSet.as_view(), name='clinic-admin-list'),
    path('typical-users/', TypicalUserViewSet.as_view(), name='typical-user-list'),
    path('nurses/', NurseViewSet.as_view(), name='nurse-list'),
    path('sicks/', SickViewSet.as_view(), name='sick-list'),
    path('warehouse-keepers/', WarehouseKeeperViewSet.as_view(), name='warehouse-keeper-list'),
    path('financial-managers/', FinancialManagerViewSet.as_view(), name='financial-manager-list'),
    path('user-create/', CreateUser.as_view(), name='user-create'),
    path('user-retrieve/<int:pk>/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('user-update/<int:pk>/',UpdateUserView.as_view(),name='user-update'),
    path('user-delete/<int:pk>/', DeleteUserView.as_view(), name='user-delete'),
    # other APIs
    path('user-recognization',UserRecognization.as_view(),name='user-recognization'),
    path('test-token',TestToken.as_view(),name='test-token'),





]