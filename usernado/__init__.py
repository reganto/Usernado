__version__ = "0.2.1"
__all__ = ["Handler"]

from usernado.torntriplets import APIHandler, WebHandler, WebSocketHandler


class Handler:
    API = APIHandler
    Web = WebHandler
    WebSocket = WebSocketHandler
