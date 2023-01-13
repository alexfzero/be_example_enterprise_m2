from rest_condition.permissions import Or

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ...models import Position, Status, Department, OperationType
from contacts.permissions import IsGlobalAdminPermission
from utils.viewsets import MultiSerializerViewSet, ACTIONS
from ...serializers.superuser import (
    SuperUserPositionSerializer,
    SuperUserUpdatePositionSerializer,
    SuperUserOperationTypeSerializer,
    SuperUserDepartmentSerializer,
    SuperUserStatusSerializer
)


class SuperUserPositionViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = Position.objects.all().order_by('id')
    serializer_class = SuperUserPositionSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserUpdatePositionSerializer
    }
    permission_classes = [AllowAny]
    # Or(
    #     AllowAny,
    #     IsGlobalAdminPermission,
    # )


class SuperUserStatusViewSet(ModelViewSet):
    queryset = Status.objects.all().order_by('id')
    serializer_class = SuperUserStatusSerializer
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission
        )
    ]


class SuperUserDepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = SuperUserDepartmentSerializer
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]


class SuperUserOperationTypeViewSet(ModelViewSet):
    queryset = OperationType.objects.all().order_by('id')
    serializer_class = SuperUserOperationTypeSerializer
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]
