from rest_condition.permissions import Or

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from utils.viewsets import MultiSerializerViewSet, ACTIONS
from contacts.permissions import IsGlobalAdminPermission
from ...models.contract import Contract, FlowFunds
from ...serializers.superuser import (
    SuperUserContractSerializer,
    SuperUserCreateContractSerializer,
    SuperUserFlowFundsSerializer,
    SuperUserCreateFlowFundsSerializer,
)


class SuperUserContractViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = Contract.objects.all()
    serializer_class = SuperUserContractSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserCreateContractSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]


class SuperUserFlowFundsViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = FlowFunds.objects.all()
    serializer_class = SuperUserFlowFundsSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserCreateFlowFundsSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]
