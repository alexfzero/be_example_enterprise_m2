from rest_condition.permissions import Or

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from utils.viewsets import MultiSerializerViewSet, ACTIONS
from contacts.permissions import IsGlobalAdminPermission
from ...models.storage import Storage, StorageOperation
from ...serializers.superuser import (
    SuperUserStorageSerializer,
    SuperUserStorageOperationSerializer,
    SuperUserStorageOperationCreateSerializer,
    SuperUserStorageOperationUpdateSerializer,
)


class SuperUserStorageViewSet(ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = SuperUserStorageSerializer
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]


class SuperUserStorageOperationViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = StorageOperation.objects.all()
    serializer_class = SuperUserStorageOperationSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserStorageOperationCreateSerializer,
        ACTIONS.PUT: SuperUserStorageOperationUpdateSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]

