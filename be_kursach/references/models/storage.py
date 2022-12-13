from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, DateField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from temps.models import OperationType
from orders.models import PurchaseOrder


class Storage(Model):
    product_number = CharField(max_length=30, unique=True)
    product_name = CharField(max_length=100)
    product_article = CharField(max_length=100)
    quantity = IntegerField()


class StorageOperation(Model):
    number_operation = CharField(max_length=30, unique=True)
    order = ForeignKey(PurchaseOrder, related_name='order_operations', on_delete=CASCADE)
    date = DateField(auto_now_add=True)
    product = ForeignKey(Storage, related_name='operations', on_delete=CASCADE, )
    operation_type = ForeignKey(OperationType, related_name='type_operations', on_delete=CASCADE)
