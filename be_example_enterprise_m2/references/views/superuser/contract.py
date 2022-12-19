from rest_framework.viewsets import ModelViewSet

from contacts.permissions import IsGlobalAdminPermission
from ...models.contract import Contract, FlowFunds
from ...serializers.superuser import (
    SuperUserContractSerializer,
    SuperUserFlowFundsSerializer,
)


class SuperUserContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = SuperUserContractSerializer
    permission_classes = [IsGlobalAdminPermission]


class SuperUserFlowFundsViewSet(ModelViewSet):
    queryset = FlowFunds.objects.all()
    serializer_class = SuperUserFlowFundsSerializer
    permission_classes = [IsGlobalAdminPermission]
