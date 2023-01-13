from utils.selectors import SelectorBaseByMethodModelSerializer

from ...models.contract import Contract
from ...models.storage import Storage


class ContractSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Contract


class StorageSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Storage
