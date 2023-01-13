from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from ...serializers.superuser import ContractSelectorSerializer, StorageSelectorSerializer
from ...models.contract import Contract
from ...models.storage import Storage


class ContractSelectorView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSelectorSerializer
    pagination_class = None
    permission_classes = [AllowAny]


class StorageSelectorView(ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSelectorSerializer
    pagination_class = None
    permission_classes = [AllowAny]
