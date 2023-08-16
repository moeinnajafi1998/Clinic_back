from django.urls import path
from .views import *

urlpatterns = [
    # RequestSession routes
    path('requestsessions/', RequestSessionListView.as_view(), name='session-list'),
    path('requestsession-create/', RequestSessionCreateView.as_view(), name='session-create'),
    path('requestsession/<int:pk>/', RequestSessionRetrieveView.as_view(), name='session-detail'),
    path('requestsession-update/<int:pk>/', RequestSessionUpdateView.as_view(), name='session-update'),
    path('requestsession-delete/<int:pk>/', RequestSessionDeleteView.as_view(), name='session-delete'),
    path('requestsessionsforTypical_user/', RequestSessionsForTypical_user.as_view(), name='requestsessionsforTypical_user-list'), #(ها)تمام درخواست های جلسه مرتبط به یک منشی مشخص کلینیک
    path('requestsessionsforsick/', RequestSessionsForSick.as_view(), name='requestsessionsforsick-list'), #(بیمار) تمام درخواست های جلسه مرتبط به یک 
    # MedicalAppointment routes
    path('medicalappointments/', MedicalAppointmentListView.as_view(), name='appointment-list'),
    path('medicalappointment-create/', MedicalAppointmentCreateView.as_view(), name='appointment-create'),
    path('medicalappointment/<int:pk>/', MedicalAppointmentRetrieveView.as_view(), name='appointment-detail'),
    path('medicalappointment-delete/<int:pk>/', MedicalAppointmentDestroyView.as_view(), name='appointment-delete'),
    path('medicalappointment-update/<int:pk>/', MedicalAppointmentUpdateView.as_view(), name='appointment-update'),
    path('medicalappointmentsfortypical_user/', MedicalAppointmentsForTypical_user.as_view(), name='medicalappointmentsfortypical_user-list'), #(ها)تمام نوبت های پزشکی مرتبط به یک منشی مشخص کلینیک
    path('medicalappointmentsforsick/', MedicalAppointmentsForSick.as_view(), name='medicalappointmentsforsick-list'), #تمام نوبت های پزشکی مرتبط به یک بیمار مشخص 
    # RequestGoods routes
    path('goods/', RequestGoodsListView.as_view(), name='goods-list'),
    path('goods-create/', RequestGoodsCreateView.as_view(), name='goods-create'),
    path('good/<int:pk>/', RequestGoodsRetrieveView.as_view(), name='goods-detail'),
    path('good-delete/<int:pk>/', RequestGoodsDestroyView.as_view(), name='goods-delete'),
    path('good-update/<int:pk>/', RequestGoodsUpdateView.as_view(), name='goods-update'),
    path('requestgoodsfortypical_user/', RequestGoodsForTypical_user.as_view(), name='requestgoodsfortypical_user-list'), #(ها)تمام درخواست های آیتم مرتبط به یک منشی مشخص کلینیک
]
