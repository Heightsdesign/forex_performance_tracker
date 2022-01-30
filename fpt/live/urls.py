from django.urls import path
from . import views

urlpatterns = [
    path('live_charts/', views.live_charts, name='live_charts'),
]