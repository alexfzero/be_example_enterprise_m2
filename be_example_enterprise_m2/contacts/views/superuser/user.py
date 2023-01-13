from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.decorators import action
from rest_condition.permissions import Or
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ...models import ExtendUser
from utils.viewsets import MultiSerializerViewSet, ACTIONS
from contacts.permissions import IsGlobalAdminPermission
from ...serializers.superuser import (
    SuperUserExtendUserSerializer,
    SuperUserCreateUpdateExtendUserSerializer,
    SuperUserDeleteExtendUserSerializer,
    SuperUserUpdateExtendUserSerializer,
)


class SuperUserExtendUserViewSet(
    ModelViewSet,
    MultiSerializerViewSet
):
    queryset = ExtendUser.objects.all()
    serializer_class = SuperUserExtendUserSerializer
    serializers_class = {
        ACTIONS.POST: SuperUserCreateUpdateExtendUserSerializer,
        ACTIONS.DELETE: SuperUserDeleteExtendUserSerializer,
        ACTIONS.PUT: SuperUserUpdateExtendUserSerializer
    }
    permission_classes = [
        Or(
            AllowAny,
            IsGlobalAdminPermission,
        )
    ]

    def perform_destroy(self, instance):
        instance.user.delete()
        super().perform_destroy(instance)


class ExtendUserViewSet(ModelViewSet):
    queryset = ExtendUser.objects.all()
    serializer_class = None
    permission_classes = [AllowAny]

    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        user = authenticate(**request.data)
        if not user:
            return HttpResponseBadRequest('Invalid user data!')

        login(request=request, user=user)
        return HttpResponse('Authenticated successfully!')

    @action(methods=['POST'], detail=False, url_path='logout')
    def logout(self, request, *args, **kwargs):
        resp = logout(request)
        return HttpResponse('Logout successfully!')
