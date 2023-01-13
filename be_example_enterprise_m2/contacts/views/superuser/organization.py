from rest_condition.permissions import Or

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ...models import Organization
from utils.viewsets import MultiSerializerViewSet, ACTIONS
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import (
    SuperUserOrganizationSerializer,
    SuperUserCreateOrganizationSerializer,
    SuperUserUpdateOrganizationSerializer,
)


class SuperUserOrganizationViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = Organization.objects.all()
    serializer_class = SuperUserOrganizationSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserCreateOrganizationSerializer,
        ACTIONS.PUT: SuperUserUpdateOrganizationSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]
