from rest_framework.permissions import BasePermission
from managment.models import Clinic
from django.shortcuts import get_object_or_404
from .models import RequestSession

class IsThisTypical_UserForClinic(BasePermission):
    def has_permission(self, request, view):
        typical_user = request.user.username
        request_session_id = view.kwargs.get('pk')
        request_session = get_object_or_404(RequestSession, id=request_session_id)
        clinics = Clinic.objects.filter(typical_user=typical_user, name=request_session.clinic)

        if clinics.exists():
            return True

        return False