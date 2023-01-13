from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .user import ExtendUser
from .organization import Organization
from ...serializers.superuser import ExtendUserSelectorSerializer, OrganizationSelectorSerializer


class ExtendUserSelectorViewSet(ListAPIView):
    serializer_class = ExtendUserSelectorSerializer
    queryset = ExtendUser.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]


class OrganizationSelectorViewSet(ListAPIView):
    serializer_class = OrganizationSelectorSerializer
    queryset = Organization.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]
