from django.urls import path
from .views import *

urlpatterns = [
    path('clinics/', ClinicListCreateView.as_view(), name='clinic-list-create'),
    path('clinics/<int:pk>/', ClinicRetrieveUpdateDeleteView.as_view(), name='clinic-retrieve-update-delete'),
]