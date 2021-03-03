# like 'urls' but for websockets

from django.urls import path
from .consumers import session

websocket_urlpatterns = [
    path('ws/session/establish/', session.SessionConsumer.as_asgi()),
]
