from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ...models.order import PurchaseOrder


class SuperUserPurchaseOrderSerializer(ModelSerializer):
    provider = SerializerMethodField()
    contact_person = SerializerMethodField()
    contract_number = SerializerMethodField()
    purchase_manager = SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def get_provider(self, obj):
        return {
            'value': obj.provider.pk,
            'text': obj.provider.short_name
        }

    def get_contact_person(self, obj):
        return {
            'value': obj.contact_person.pk,
            'text': f"{obj.contact_person.user.last_name} {obj.contact_person.user.first_name} "
                    f"{obj.contact_person.middle_name}"
        }

    def get_contract_number(self, obj):
        return {
            'value': obj.contract_number.pk,
            'text': obj.contract_number.number
        }

    def get_purchase_manager(self, obj):
        return {
            'value': obj.purchase_manager.pk,
            'text': f"{obj.contact_person.user.last_name} {obj.contact_person.user.first_name} "
                    f"{obj.contact_person.middle_name}"
        }


class SuperUserCreatePurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class SuperUserUpdatePurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        exclude = ['order_reg_date']