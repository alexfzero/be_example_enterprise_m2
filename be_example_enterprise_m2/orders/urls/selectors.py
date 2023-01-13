from django.urls import path

from ..views.superuser import PurchaseOrderSelectorView


urlpatterns = [
    path(route='orders/', view=PurchaseOrderSelectorView.as_view(), name='orders'),
]
