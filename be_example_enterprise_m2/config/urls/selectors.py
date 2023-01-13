from django.urls import path, include


urlpatterns = [
    path('', include(('temps.urls.selectors', 'temps'), namespace='temps')),
    path('', include(('contacts.urls.selectors', 'contacts'), namespace='contacts')),
    path('', include(('references.urls.selectors', 'references'), namespace='references')),
    path('', include(('orders.urls.selectors', 'orders'), namespace='orders')),
]
