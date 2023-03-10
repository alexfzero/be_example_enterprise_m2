from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from temps.models import Status
from contacts.models import ExtendUser


class Contract(Model):
    number = CharField(max_length=30, unique=True)
    client = ForeignKey(ExtendUser, related_name='org_contracts', on_delete=CASCADE)
    Document = CharField(max_length=255)
    status = ForeignKey(Status, related_name='contracts', on_delete=CASCADE)
    formalized = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number}"


class FlowFunds(Model):
    number = CharField(max_length=30)
    contract = ForeignKey(Contract, related_name='flows', on_delete=CASCADE)
    name = CharField(max_length=255)
    date_time = DateTimeField(auto_now_add=True)
    currency = CharField(max_length=10)
    value = CharField(max_length=255)
    came_from = CharField(max_length=30)

    class Meta:
        unique_together = ['number', 'contract']

    def __str__(self):
        return f"{self.number} {self.name}"
