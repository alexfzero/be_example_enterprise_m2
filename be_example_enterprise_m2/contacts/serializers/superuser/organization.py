from rest_framework.serializers import ModelSerializer

from contacts.models.organization import Organization


class SuperUserOrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
