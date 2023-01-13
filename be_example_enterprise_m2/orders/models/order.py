from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, DateField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from contacts.models import ExtendUser, Organization
from references.models import Contract


class PurchaseOrder(Model):
    order_number = CharField(max_length=30, unique=True)
    provider = ForeignKey(Organization, related_name='orders', on_delete=CASCADE)
    contact_person = ForeignKey(ExtendUser, related_name='contact_orders', on_delete=CASCADE)
    order_reg_date = DateField(auto_now_add=True)
    date_arrival = DateField()
    quantity = IntegerField()
    price = IntegerField()
    contract_number = ForeignKey(Contract, related_name='contract_orders', on_delete=CASCADE)
    purchase_manager = ForeignKey(ExtendUser, related_name='manager_orders', on_delete=CASCADE)
    vat = IntegerField()
    summary = CharField(max_length=255)

    def __str__(self):
        return f"{self.order_number} {self.provider}"
