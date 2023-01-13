from temps.models import Department, Status, OperationType, Position
from utils.selectors import SelectorBaseByMethodModelSerializer


class DepartmentSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Department


class StatusSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Status


class OperationTypeSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = OperationType


class PositionSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Position
