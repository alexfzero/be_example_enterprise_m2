from django.urls import path, include

from rest_framework.routers import SimpleRouter

from ..views.superuser import (
    SuperUserContractViewSet,
    SuperUserFlowFundsViewSet,
    SuperUserStorageViewSet,
    SuperUserStorageOperationViewSet,
)

references_routers = SimpleRouter()
references_routers.register(prefix='contracts', viewset=SuperUserContractViewSet, basename='contracts')
references_routers.register(prefix='funds', viewset=SuperUserFlowFundsViewSet, basename='funds')
references_routers.register(prefix='storages', viewset=SuperUserStorageViewSet, basename='storages')
references_routers.register(prefix='operations', viewset=SuperUserStorageOperationViewSet, basename='operations')

urlpatterns = [
    path('', include(references_routers.urls))
]
