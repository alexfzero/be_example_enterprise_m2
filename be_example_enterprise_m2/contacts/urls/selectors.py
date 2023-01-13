from django.urls import path

from ..views.superuser import ExtendUserSelectorViewSet, OrganizationSelectorViewSet

urlpatterns = [
    path(route='users/', view=ExtendUserSelectorViewSet.as_view(), name='users'),
    path(route='organizations/', view=OrganizationSelectorViewSet.as_view(), name='organizations'),
]
