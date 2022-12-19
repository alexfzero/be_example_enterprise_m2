from rest_framework.serializers import ModelSerializer

from ...models.order import PurchaseOrder


class SuperUserPurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
