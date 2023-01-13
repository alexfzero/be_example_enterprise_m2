from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ...models.contract import Contract, FlowFunds


class SuperUserContractSerializer(ModelSerializer):
    client = SerializerMethodField()
    status = SerializerMethodField()

    class Meta:
        model = Contract
        fields = '__all__'

    def get_client(self, obj):
        return {
            'value': obj.client.pk,
            'text': obj.client.short_name,
        }

    def get_status(self, obj):
        return {
            'value': obj.status.pk,
            'text': obj.status.name,
        }


class SuperUserCreateContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class SuperUserFlowFundsSerializer(ModelSerializer):
    contract = SerializerMethodField()

    class Meta:
        model = FlowFunds
        fields = '__all__'

    def get_contract(self, obj):
        return {
            'value': obj.contract.pk,
            'text': obj.contract.number,
        }


class SuperUserCreateFlowFundsSerializer(ModelSerializer):
    class Meta:
        model = FlowFunds
        fields = '__all__'
