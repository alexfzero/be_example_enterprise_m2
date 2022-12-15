from rest_framework.viewsets import ModelViewSet

from ...models import Organization
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import SuperUserOrganizationSerializer


class SuperUserOrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = SuperUserOrganizationSerializer
    permission_classes = [IsGlobalAdminPermission]
