from django.urls import path

from ..views.superuser import ContractSelectorView, StorageSelectorView

urlpatterns = [
    path(route='contracts/', view=ContractSelectorView.as_view(), name='contracts'),
    path(route='storages/', view=StorageSelectorView.as_view(), name='storages'),
]
