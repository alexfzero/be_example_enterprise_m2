from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from ...models.order import PurchaseOrder
from ...serializers.superuser import PurchaseOrderSelectorSerializer


class PurchaseOrderSelectorView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSelectorSerializer
    pagination_class = None
    permission_classes = [AllowAny]
