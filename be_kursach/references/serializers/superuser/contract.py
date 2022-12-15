from rest_framework.serializers import ModelSerializer

from ...models.contract import Contract, FlowFunds


class SuperUserContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class SuperUserFlowFundsSerializer(ModelSerializer):
    class Meta:
        model = FlowFunds
        fields = '__all__'
