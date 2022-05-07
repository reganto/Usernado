__version__ = "0.2.4"
__all__ = ["Usernado"]

from usernado.torntriplets import APIHandler, WebHandler, WebSocketHandler


class Usernado:
    API = APIHandler
    Web = WebHandler
    WebSocket = WebSocketHandler
