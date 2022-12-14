from django.urls import path, include


urlpatterns = [
    path('', include(('temps.urls.superadmin', 'temps'), namespace='temps')),
]
