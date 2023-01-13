from django.contrib.auth.models import User

from rest_framework.fields import CharField, BooleanField
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from contacts.models.user import ExtendUser


class SuperUserExtendUserSerializer(ModelSerializer):
    fio = SerializerMethodField()
    position = SerializerMethodField()
    is_staff = CharField(source='user.is_staff')
    username = CharField(source='user.username')

    class Meta:
        model = ExtendUser
        exclude = ['user']

    def get_fio(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name} {obj.middle_name}"

    def get_position(self, obj):
        return {
            'value': obj.position.pk,
            'text': obj.position.name
        }



class SuperUserDeleteExtendUserSerializer(ModelSerializer):
    class Meta:
        model = ExtendUser
        fields = '__all__'


class SuperUserCreateUpdateExtendUserSerializer(ModelSerializer):
    user = CharField(required=False)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_booker = BooleanField(default=False)

    class Meta:
        model = ExtendUser
        fields = '__all__'

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        is_staff = validated_data['is_staff']
        validated_data.pop('first_name')
        validated_data.pop('last_name')
        validated_data.pop('username')
        validated_data.pop('password')
        validated_data.pop('is_staff')
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
        )

        extended_user = ExtendUser.objects.get(user=user)
        extended_user.middle_name = validated_data['middle_name']
        extended_user.sex = validated_data['sex']
        extended_user.birthday = validated_data['birthday']
        extended_user.number = validated_data['number']
        extended_user.position = validated_data['position']
        extended_user.is_admin = validated_data['is_admin']
        extended_user.is_booker = validated_data['is_booker']
        extended_user.save()
        self.fields.pop('first_name')
        self.fields.pop('last_name')
        self.fields.pop('username')
        self.fields.pop('password')
        self.fields.pop('is_staff')

        return extended_user


class SuperUserUpdateExtendUserSerializer(ModelSerializer):
    user = CharField(required=False)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_booker = BooleanField(default=False)

    class Meta:
        model = ExtendUser
        fields = "__all__"

    def update(self, instance, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        is_staff = validated_data['is_staff']
        validated_data.pop('first_name')
        validated_data.pop('last_name')
        validated_data.pop('username')
        validated_data.pop('is_staff')

        extended_user = instance
        user = extended_user.user

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.is_staff = is_staff
        user.save()

        extended_user.middle_name = validated_data['middle_name']
        extended_user.sex = validated_data['sex']
        extended_user.birthday = validated_data['birthday']
        extended_user.number = validated_data['number']
        extended_user.position = validated_data['position']
        extended_user.is_admin = validated_data['is_admin']
        extended_user.is_booker = validated_data['is_booker']
        extended_user.user = user
        extended_user.save()
        self.fields.pop('first_name')
        self.fields.pop('last_name')
        self.fields.pop('username')
        self.fields.pop('is_staff')

        return extended_user
