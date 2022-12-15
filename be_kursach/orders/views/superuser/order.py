from rest_framework.viewsets import ModelViewSet

from ...models.order import PurchaseOrder
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import SuperUserPurchaseOrderSerializer


class SuperUserPurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = SuperUserPurchaseOrderSerializer
    permission_classes = [IsGlobalAdminPermission]
