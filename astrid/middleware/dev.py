import asyncio

from datetime import datetime


@asyncio.coroutine
def request_logger(app, handler):
    @asyncio.coroutine
    def middleware(request):
        print(datetime.now(), request._method, request.path)
        return (yield from handler(request))
    return middleware
