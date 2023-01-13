from utils.selectors import SelectorBaseByMethodModelSerializer

from ...models.order import PurchaseOrder


class PurchaseOrderSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = PurchaseOrder
