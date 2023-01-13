from django.urls import path

from ..views import (
    DepartmentSelectorViewSet,
    PositionSelectorViewSet,
    StatusSelectorViewSet,
    OperationTypeSelectorViewSet,
)

urlpatterns = [
    path(route='departments/', view=DepartmentSelectorViewSet.as_view(), name='department|model'),
    path(route='positions/', view=PositionSelectorViewSet.as_view(), name='position|model'),
    path(route='statuses/', view=StatusSelectorViewSet.as_view(), name='status|model'),
    path(route='operations/', view=OperationTypeSelectorViewSet.as_view(), name='operation|model'),
]
