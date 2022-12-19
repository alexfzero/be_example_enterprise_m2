from rest_framework.serializers import ModelSerializer

from contacts.models.user import ExtendUser


class SuperUserExtendUserSerializer(ModelSerializer):
    class Meta:
        model = ExtendUser
        fields = '__all__'
