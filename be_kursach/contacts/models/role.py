from django.db.models import Model
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE

from ...temps.models import Position


class Role(Model):
    pass
