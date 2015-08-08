# -*- coding:utf-8 -*-
import asyncio
from aiohttp import web


class Astrid(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop)

    def run(self):
        def _run():
            srv = yield from self.loop.create_server(self.app.make_handler(),
                                                     '127.0.0.1', 8080)
            return srv

        self.loop.run_until_complete(_run())
        self.loop.run_forever()
