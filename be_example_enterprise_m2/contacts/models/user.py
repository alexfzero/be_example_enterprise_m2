from django.db.models import Model
from django.db.models.fields import CharField, DateField, BooleanField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from temps.models import Position
from django.contrib.auth.models import User


class ExtendUser(Model):
    user = OneToOneField(User, related_name='extended_user', on_delete=CASCADE)
    middle_name = CharField(max_length=100, blank=True, null=True)
    sex = CharField(max_length=1)
    birthday = DateField()
    number = CharField(max_length=11)
    position = ForeignKey(Position, related_name='extend_users', on_delete=CASCADE, blank=True, null=True)
    is_admin = BooleanField(default=False)
    is_booker = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        default = {
            'middle_name': 'middle_name',
            'sex': 'N',
            'birthday': timezone.now().date(),
            'number': 'number',
            'position': Position.objects.all()[0],
        }
        if created:
            ExtendUser.objects.create(user=instance, **default)
        instance.extended_user.save()

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.extended_user.save()
