from django.urls import path, include


urlpatterns = [
    path('', include(('contacts.urls.accounts', 'accounts'), namespace='accounts')),
]
