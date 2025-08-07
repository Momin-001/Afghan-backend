from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy', 'update', 'partial_update']:
            return request.user.is_authenticated and request.user.is_super_admin
        
        return request.user.is_authenticated


class IsAuthenticatedOrRetrieveOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return True
        return request.user and request.user.is_authenticated
