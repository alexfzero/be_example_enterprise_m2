from rest_framework.viewsets import ModelViewSet

from ...models import ExtendUser
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import SuperUserExtendUserSerializer


class SuperUserExtendUserViewSet(ModelViewSet):
    queryset = ExtendUser.objects.all()
    serializer_class = SuperUserExtendUserSerializer
    permission_classes = [IsGlobalAdminPermission]
