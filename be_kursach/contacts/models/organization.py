from django.db.models import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from .user import User


class Organization(Model):
    bank_number = CharField(max_length=30, unique=True)
    bank_name = CharField(max_length=255)
    bic = CharField(max_length=30)
    corres_number = CharField(max_length=30)
    legal_address = CharField(max_length=255)
    mail_address = CharField(max_length=255)
    contact_person = ForeignKey(User, related_name='organizations', on_delete=CASCADE)
    inn = CharField(max_length=21)
    kpp = CharField(max_length=21)
