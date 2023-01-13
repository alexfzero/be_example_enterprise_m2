from rest_framework.permissions import BasePermission


class IsGlobalAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.is_superuser


class IsStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.is_staff


class IsLocalAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.extended_user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.extended_user.is_admin


class IsBookerAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.extended_user.is_booker

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.extended_user is not None and request.user.extended_user.is_booker
