import asyncio
from datetime import datetime

from aiohttp.web import WebSocketResponse


@asyncio.coroutine
def request_logger(app, handler):
    @asyncio.coroutine
    def middleware(request):
        print(datetime.now(), request._method, request.path)
        if handler.__name__ in getattr(app, 'web_socket_handlers', []):
            return (yield from handler(request, WebSocketResponse()))
        return (yield from handler(request))
    return middleware



@asyncio.coroutine
def web_socket(app, handler):
    @asyncio.coroutine
    def middleware(request):
        if handler.__name__ in getattr(app, 'web_socket_handlers', []):
            return (yield from handler(request, WebSocketResponse()))
        return (yield from handler(request))
    return middleware
