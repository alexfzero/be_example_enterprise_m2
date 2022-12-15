from django.urls import path, include

from rest_framework.routers import SimpleRouter

from ..views.superuser import SuperUserPurchaseOrderViewSet

orders_routers = SimpleRouter()
orders_routers.register(prefix='orders', viewset=SuperUserPurchaseOrderViewSet, basename='orders')

urlpatterns = [
    path('', include(orders_routers.urls))
]
