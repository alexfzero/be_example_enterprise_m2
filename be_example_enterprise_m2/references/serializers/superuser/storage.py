from rest_framework.serializers import ModelSerializer

from ...models.storage import Storage, StorageOperation


class SuperUserStorageSerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class SuperUserStorageOperationSerializer(ModelSerializer):
    class Meta:
        model = StorageOperation
        fields = '__all__'
