from django.db.models import Model
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from ...temps.models import Position
from django.contrib.auth.models import User


class ExtendUser(User):
    sex = CharField(max_length=1)
    birthday = DateField()
    Number = CharField(max_length=11)
    position = ForeignKey(Position, related_name='extend_users', on_delete=CASCADE, blank=True, null=True)
