from ...models.user import ExtendUser
from ...models.organization import Organization
from utils.selectors import SelectorBaseByMethodModelSerializer


class ExtendUserSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = ExtendUser

    def get_text(self, object):
        return f"{object.user.last_name} {object.user.first_name} {object.middle_name}"


class OrganizationSelectorSerializer(SelectorBaseByMethodModelSerializer):
    class Meta:
        model = Organization

    def get_text(self, obj):
        return f"{obj.short_name}"
