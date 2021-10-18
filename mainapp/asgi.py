"""
ASGI config for mainapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from data_generator_app.routings import ws_urlpatterns
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = get_asgi_application()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')

application = ProtocolTypeRouter({
  
  "websocket": AuthMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    ),
})
