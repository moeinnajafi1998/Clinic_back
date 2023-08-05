from rest_framework.permissions import BasePermission

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    

class IsClinicAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'Clinic_Admin'
    

class IsTypical_User(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'Typical_User'
