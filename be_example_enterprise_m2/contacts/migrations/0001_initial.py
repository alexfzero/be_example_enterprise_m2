# Generated by Django 4.1.4 on 2022-12-15 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=1)),
                ('birthday', models.DateField()),
                ('Number', models.CharField(max_length=11)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_booker', models.BooleanField(default=False)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extend_users', to='temps.position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extende_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_number', models.CharField(max_length=30, unique=True)),
                ('bank_name', models.CharField(max_length=255)),
                ('bic', models.CharField(max_length=30)),
                ('corres_number', models.CharField(max_length=30)),
                ('legal_address', models.CharField(max_length=255)),
                ('mail_address', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=21)),
                ('kpp', models.CharField(max_length=21)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='contacts.extenduser')),
            ],
        ),
    ]