from django.db.models import Model
from django.db.models.fields import CharField, BooleanField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE


class Status(Model):
    name = CharField(max_length=20, unique=True)


class Department(Model):
    name = CharField(max_length=50, unique=True)


class Position(Model):
    name = CharField(max_length=20)
    department = ForeignKey(Department, related_name='positions', on_delete=CASCADE)
    is_head = BooleanField(default=False)

    class Meta:
        unique_together = ['name', 'department']


class OperationType(Model):
    name = CharField(max_length=20, unique=True)
