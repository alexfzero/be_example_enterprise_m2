from rest_framework.viewsets import ModelViewSet

from contacts.permissions import IsGlobalAdminPermission
from ...models.storage import Storage, StorageOperation
from ...serializers.superuser import SuperUserStorageSerializer, SuperUserStorageOperationSerializer


class SuperUserStorageViewSet(ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = SuperUserStorageSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperUserStorageOperationViewSet(ModelViewSet):
    queryset = StorageOperation.objects.all()
    serializer_class = SuperUserStorageOperationSerializer
    permission_classes = [IsGlobalAdminPermission]
