"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin as local_urls

from .accounts import urlpatterns as accounts_urls
from .superuser import urlpatterns as superuser_urls
from .selectors import urlpatterns as selector_urls

urlpatterns = [
    path('local/', local_urls.site.urls),
    path('accounts/', include((accounts_urls, 'accounts'), namespace='accounts')),
    path('selectors/', include((selector_urls, 'selectors'), namespace='selectors')),
    path('super/', include((superuser_urls, 'super'), namespace='super')),
]
