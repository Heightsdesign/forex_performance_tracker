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
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from live import views as live_views
from trades import views as trades_views
from users import views as users_views
from info import views as info_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', live_views.homepage),
    path('live_charts/', live_views.live_charts),
    path('about_us/', info_views.about_us),
    path('legal/', info_views.legal),
    path('user_page/<int:user_id>/', users_views.user_page),
    path('login/', users_views.login),
    path('sign_up/', users_views.sign_up),
    path('performance/', trades_views.performance)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

