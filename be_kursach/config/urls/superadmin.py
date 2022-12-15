from django.urls import path, include


urlpatterns = [
    path('temps/', include(('temps.urls.superadmin', 'temps'), namespace='temps')),
]
