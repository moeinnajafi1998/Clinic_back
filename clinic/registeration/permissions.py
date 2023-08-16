from rest_framework.permissions import BasePermission
from managment.models import Clinic
from django.shortcuts import get_object_or_404
from .models import *

class IsThisTypical_UserForClinic(BasePermission):
    def has_permission(self, request, view):
        typical_user = request.user.username
        request_session_id = view.kwargs.get('pk')
        request_session = get_object_or_404(RequestSession, id=request_session_id)
        clinics = Clinic.objects.filter(typical_user=typical_user, name=request_session.clinic)

        if clinics.exists():
            return True

        return False
    

class IsThisTypical_UserForClinic_2(BasePermission):
    def has_permission(self, request, view):
        typical_user = request.user.username
        clinic = request.data.get("clinic")
        clinics = Clinic.objects.filter(typical_user=typical_user, name=clinic)

        if clinics.exists():
            return True

        return False
    

class IsThisTypical_UserForClinic_3(BasePermission):
    def has_permission(self, request, view):
        typical_user = request.user.username
        medical_appointment_id = view.kwargs.get('pk')
        medical_appointment = get_object_or_404(MedicalAppointment, id=medical_appointment_id)
        clinics = Clinic.objects.filter(typical_user=typical_user, name=medical_appointment.clinic)

        if clinics.exists():
            return True

        return False
    

class IsSuperUserOrWhareHouseKeeper(BasePermission):
    def has_permission(self, request, view):
        user = request.user.username


        if user=="Warehouse_Keeper" or request.user.is_superuser:
            return True

        return False