from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.superadmin import (
    SuperAdminPositionViewSet,
    SuperAdminDepartmentViewSet,
    SuperAdminStatusViewSet,
    SuperAdminOperationTypeViewSet
)

temps_router = SimpleRouter()
temps_router.register(prefix='positions', viewset=SuperAdminPositionViewSet, basename='positions')
temps_router.register(prefix='departments', viewset=SuperAdminDepartmentViewSet, basename='departments')
temps_router.register(prefix='statuses', viewset=SuperAdminStatusViewSet, basename='statuses')
# TODO: переместить к операциям склада под урлом operations/types
temps_router.register(prefix='operations', viewset=SuperAdminOperationTypeViewSet, basename='operations')

urlpatterns = [
    path('', include(temps_router.urls)),
]
