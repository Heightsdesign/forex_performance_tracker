from django.urls import path
from .consumers import LiveConsumer

app_name = "live"

ws_urlpatterns = [path("ws/live/", LiveConsumer.as_asgi())]
