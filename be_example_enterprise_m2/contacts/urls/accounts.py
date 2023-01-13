from django.urls import path, include

from rest_framework.routers import SimpleRouter

from ..views.superuser import ExtendUserViewSet

accounts_routers = SimpleRouter()
accounts_routers.register(prefix='', viewset=ExtendUserViewSet, basename='accounts')

urlpatterns = [
    path('', include(accounts_routers.urls))
]
