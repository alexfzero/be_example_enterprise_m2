from rest_condition.permissions import Or

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ...models.order import PurchaseOrder
from ...serializers.superuser import (
    SuperUserPurchaseOrderSerializer,
    SuperUserCreatePurchaseOrderSerializer,
    SuperUserUpdatePurchaseOrderSerializer
)
from contacts.permissions import IsGlobalAdminPermission
from utils.viewsets import MultiSerializerViewSet, ACTIONS


class SuperUserPurchaseOrderViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = PurchaseOrder.objects.all()
    serializer_class = SuperUserPurchaseOrderSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserCreatePurchaseOrderSerializer,
        ACTIONS.PUT: SuperUserUpdatePurchaseOrderSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]
