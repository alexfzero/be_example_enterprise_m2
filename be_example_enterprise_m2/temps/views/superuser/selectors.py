from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from temps.models import Department, Position, OperationType, Status
from temps.serializers.superuser import (
    DepartmentSelectorSerializer,
    PositionSelectorSerializer,
    StatusSelectorSerializer,
    OperationTypeSelectorSerializer
)


class DepartmentSelectorViewSet(ListAPIView):
    serializer_class = DepartmentSelectorSerializer
    queryset = Department.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]


class PositionSelectorViewSet(ListAPIView):
    serializer_class = PositionSelectorSerializer
    queryset = Position.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]


class StatusSelectorViewSet(ListAPIView):
    serializer_class = StatusSelectorSerializer
    queryset = Status.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]


class OperationTypeSelectorViewSet(ListAPIView):
    serializer_class = OperationTypeSelectorSerializer
    queryset = OperationType.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]
