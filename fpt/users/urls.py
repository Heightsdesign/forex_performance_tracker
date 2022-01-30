from django.urls import path, re_path
from . import views

app_name = 'users'

urlpatterns = [
    re_path(r"^(?P<user_id>[0-9]+)/$", views.user_page, name="user_page"),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    re_path(r'^performance/(?P<user_id>[0-9]+)/$', views.performance, name='performance'),
]