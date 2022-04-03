from django.urls import path
from .consumers import LiveConsumer


ws_urlpatterns = [path("ws/live/", LiveConsumer.as_asgi())]
