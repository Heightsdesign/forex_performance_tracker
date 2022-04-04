from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.wsgi import get_wsgi_application
from channels.auth import AuthMiddlewareStack
from live.routing import ws_urlpatterns

application = ProtocolTypeRouter({
    'http': get_wsgi_application(),
    'websocket': AuthMiddlewareStack(
            URLRouter(ws_urlpatterns)
        )
    })
