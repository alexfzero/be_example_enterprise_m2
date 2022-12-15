from django.db.models import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from .user import ExtendUser


class Organization(Model):
    full_name = CharField(max_length=255)
    short_name = CharField(max_length=100)
    bank_number = CharField(max_length=30)
    bank_name = CharField(max_length=255)
    bic = CharField(max_length=30)
    corres_number = CharField(max_length=30)
    legal_address = CharField(max_length=255)
    mail_address = CharField(max_length=255)
    contact_person = ForeignKey(ExtendUser, related_name='organizations', on_delete=CASCADE)
    inn = CharField(max_length=21)
    kpp = CharField(max_length=21)

    class Meta:
        unique_together = ['full_name', 'short_name', 'bank_number']

    def __str__(self):
        return f"{self.short_name}"
