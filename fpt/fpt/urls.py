"""fpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include
from live import views as live_views
from trades import views as trades_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', live_views.homepage, name='homepage'),
    re_path(r'^live/', include(('live.urls', 'live'), namespace='live')),
    re_path(r'^info/', include(('info.urls', 'info'), namespace='info')),
    re_path(r'^users/', include(('users.urls', 'users'), namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

