from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField
from rest_framework.fields import SerializerMethodField

from ...models import Position, Status, Department, OperationType


class SuperUserPositionSerializer(ModelSerializer):
    department = SerializerMethodField()

    class Meta:
        model = Position
        fields = '__all__'

    def get_department(self, obj):
        return {
            'value': obj.department.pk,
            'text': obj.department.name
        }


class SuperUserUpdatePositionSerializer(ModelSerializer):
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
