from rest_framework.viewsets import ModelViewSet

from ...models import Position, Status, Department, OperationType
from rest_framework.permissions import AllowAny
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superadmin import (
    SuperAdminPositionSerializer,
    SuperAdminOperationTypeSerializer,
    SuperAdminDepartmentSerializer,
    SuperAdminStatusSerializer
)


class SuperAdminPositionViewSet(ModelViewSet):
    queryset = Position.objects.all().order_by('id')
    serializer_class = SuperAdminPositionSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperAdminStatusViewSet(ModelViewSet):
    queryset = Status.objects.all().order_by('id')
    serializer_class = SuperAdminStatusSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperAdminDepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = SuperAdminDepartmentSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperAdminOperationTypeViewSet(ModelViewSet):
    queryset = OperationType.objects.all().order_by('id')
    serializer_class = SuperAdminOperationTypeSerializer
    permission_classes = [IsGlobalAdminPermission]
