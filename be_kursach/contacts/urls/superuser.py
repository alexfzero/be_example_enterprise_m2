from django.urls import path, include

from rest_framework.routers import SimpleRouter

from ..views.superuser import SuperUserExtendUserViewSet, SuperUserOrganizationViewSet

contacts_routers = SimpleRouter()
contacts_routers.register(prefix='users', viewset=SuperUserExtendUserViewSet, basename='users')
contacts_routers.register(prefix='organizations', viewset=SuperUserOrganizationViewSet, basename='users')

urlpatterns = [
    path('', include(contacts_routers.urls))
]
