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

]
