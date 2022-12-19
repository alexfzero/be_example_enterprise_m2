from rest_framework.serializers import ModelSerializer

from ...models import Position, Status, Department, OperationType


class SuperUserPositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class SuperUserStatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class SuperUserDepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SuperUserOperationTypeSerializer(ModelSerializer):
    class Meta:
        model = OperationType
        fields = '__all__'
