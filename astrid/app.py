import os
import sys

import asyncio
from aiohttp import web


class Astrid(object):

    def __init__(self, template_path='/'):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop)
        Astrid.template_path = template_path

    def add_payload(self, payload, handler, methods):
        for method in methods:
            self.app.router.add_route(method, payload,
                                      asyncio.coroutine(handler))

    def route(self, payload, methods=['GET']):
        def _decorator(handler):
            self.add_payload(payload, handler, methods)
            return handler
        return _decorator

    def run(self, host='127.0.0.1', port=8080):
        @asyncio.coroutine
        def _run():
            srv = yield from self.loop.create_server(self.app.make_handler(),
                                                     host, port)
            return srv

        self.loop.run_until_complete(_run())
        try:
            print('Server started with http://', host+":"+str(port))
            self.loop.run_forever()
        except KeyboardInterrupt:
            print('')


def get_template_path():
    return Astrid.template_path
