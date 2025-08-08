from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['destroy', 'update', 'partial_update']:
            return request.user.is_authenticated and request.user.is_super_admin
        
        return request.user.is_authenticated
