from rest_framework.permissions import BasePermission

class IsSupplierOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            (request.user.is_staff or hasattr(request.user, 'supplier_profile'))
        )