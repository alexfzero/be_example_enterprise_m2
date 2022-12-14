from rest_framework.permissions import BasePermission


class IsGlobalAdminPermission(BasePermission):

    def has_permission(self, request, view):
        # TODO: Поискать авторизацию через свою модель
        abc = request.user.extenduser
        return request.user.extenduser is not None and request.user.extenduser.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.extenduser is not None and request.user.extenduser.is_superuser


class IsLocalAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.extenduser is not None and request.user.extenduser.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.extenduser is not None and request.user.extenduser.is_admin


class IsStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.extenduser is not None and request.user.extenduser.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.extenduser is not None and request.user.extenduser.is_staff


class IsBookerAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.extenduser is not None and request.user.extenduser.is_booker

    def has_object_permission(self, request, view, obj):
        return request.user.extenduser is not None and request.user.extenduser.is_booker
