from django.urls import path, include


urlpatterns = [
    path('temps/', include(('temps.urls.superuser', 'temps'), namespace='temps')),
    path('contacts/', include(('contacts.urls.superuser', 'contacts'), namespace='contacts')),
    path('references/', include(('references.urls.superuser', 'references'), namespace='references')),
    path('orders/', include(('orders.urls.superuser', 'orders'), namespace='orders')),
]
