from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ...models.storage import Storage, StorageOperation


class SuperUserStorageSerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class SuperUserStorageOperationSerializer(ModelSerializer):
    order = SerializerMethodField()
    product = SerializerMethodField()
    operation_type = SerializerMethodField()

    class Meta:
        model = StorageOperation
        fields = '__all__'

    def get_order(self, obj):
        return {
            'value': obj.order.pk,
            'text': obj.order.order_number
        }

    def get_product(self, obj):
        return {
            'value': obj.product.pk,
            'text': obj.product.product_number
        }

    def get_operation_type(self, obj):
        return {
            'value': obj.operation_type.pk,
            'text': obj.operation_type.name
        }


class SuperUserStorageOperationCreateSerializer(ModelSerializer):
    class Meta:
        model = StorageOperation
        fields = '__all__'


class SuperUserStorageOperationUpdateSerializer(ModelSerializer):
    class Meta:
        model = StorageOperation
        exclude = ['date_time']
