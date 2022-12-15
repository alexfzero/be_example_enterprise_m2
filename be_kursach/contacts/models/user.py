from django.db.models import Model
from django.db.models.fields import CharField, DateField, BooleanField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from temps.models import Position
from django.contrib.auth.models import User


class ExtendUser(Model):
    user = OneToOneField(User, related_name='extended_user', on_delete=CASCADE)
    sex = CharField(max_length=1)
    birthday = DateField()
    number = CharField(max_length=11)
    position = ForeignKey(Position, related_name='extend_users', on_delete=CASCADE, blank=True, null=True)
    is_admin = BooleanField(default=False)
    is_booker = BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            ExtendUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.extended_user.save()
