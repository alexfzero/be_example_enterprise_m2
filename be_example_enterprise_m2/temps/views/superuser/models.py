from rest_framework.viewsets import ModelViewSet

from ...models import Position, Status, Department, OperationType
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import (
    SuperUserPositionSerializer,
    SuperUserOperationTypeSerializer,
    SuperUserDepartmentSerializer,
    SuperUserStatusSerializer
)


class SuperUserPositionViewSet(ModelViewSet):
    queryset = Position.objects.all().order_by('id')
    serializer_class = SuperUserPositionSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperUserStatusViewSet(ModelViewSet):
    queryset = Status.objects.all().order_by('id')
    serializer_class = SuperUserStatusSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperUserDepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = SuperUserDepartmentSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperUserOperationTypeViewSet(ModelViewSet):
    queryset = OperationType.objects.all().order_by('id')
    serializer_class = SuperUserOperationTypeSerializer
    permission_classes = [IsGlobalAdminPermission]
