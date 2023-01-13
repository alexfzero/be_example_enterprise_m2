from rest_framework.serializers import ModelSerializer, SerializerMethodField

from contacts.models.organization import Organization


class SuperUserOrganizationSerializer(ModelSerializer):
    contact_person = SerializerMethodField()

    class Meta:
        model = Organization
        fields = '__all__'

    def get_contact_person(self, obj):
        return {
            'value': obj.contact_person.pk,
            'text': f"{obj.contact_person.user.last_name} {obj.contact_person.user.first_name} {obj.contact_person.middle_name}"
        }


class SuperUserCreateOrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class SuperUserUpdateOrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
