"""
ASGI config for training_assistant_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
from .wsgi import *
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.routing import get_default_application
from django.core.asgi import get_asgi_application
from sber_backend import router

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# from configurations import importer
# importer.install()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            router.websocket_urlpatterns
        )
    ),
})
