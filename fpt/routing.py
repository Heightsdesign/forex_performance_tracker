from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from live.routing import ws_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
            URLRouter(ws_urlpatterns)
        )
    })
