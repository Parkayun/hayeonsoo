# -*- coding:utf-8 -*-
import sys

import asyncio
from aiohttp import web


class Astrid(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop)

    def add_payload(self, payload, handler):
        self.app.router.add_route('GET', payload, asyncio.coroutine(handler))

    def route(self, payload):
        def _decorator(handler):
            self.add_payload(payload, handler)
            return handler
        return _decorator

    def run(self):
        @asyncio.coroutine
        def _run():
            srv = yield from self.loop.create_server(self.app.make_handler(),
                                                     '127.0.0.1', 8080)
            return srv

        self.loop.run_until_complete(_run())
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            sys.stdout.write('\n')
