from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.superuser import (
    SuperUserPositionViewSet,
    SuperUserDepartmentViewSet,
    SuperUserStatusViewSet,
    SuperUserOperationTypeViewSet
)

temps_router = SimpleRouter()
temps_router.register(prefix='positions', viewset=SuperUserPositionViewSet, basename='positions')
temps_router.register(prefix='departments', viewset=SuperUserDepartmentViewSet, basename='departments')
temps_router.register(prefix='statuses', viewset=SuperUserStatusViewSet, basename='statuses')
# TODO: переместить к операциям склада под урлом operations/types
temps_router.register(prefix='operations', viewset=SuperUserOperationTypeViewSet, basename='operations')

urlpatterns = [
    path('', include(temps_router.urls)),
]
