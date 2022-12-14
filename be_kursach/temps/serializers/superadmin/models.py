from rest_framework.serializers import ModelSerializer

from ...models import Position, Status, Department, OperationType


class SuperAdminPositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class SuperAdminStatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class SuperAdminDepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SuperAdminOperationTypeSerializer(ModelSerializer):
    class Meta:
        model = OperationType
        fields = '__all__'
