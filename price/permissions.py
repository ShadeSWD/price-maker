from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('destroy', ):
            return False
        if view.action in ('create', 'list', 'retrieve', 'update', 'partial_update'):
            return request.user.is_vendor
        return True
