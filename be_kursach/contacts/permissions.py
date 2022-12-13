from rest_framework.permissions import BasePermission


class IsGlobalAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.db_user is not None and request.user.db_user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.db_user is not None and request.user.db_user.is_superuser


class IsStaffPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.db_user is not None and request.user.db_user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.db_user is not None and request.user.db_user.is_staff
