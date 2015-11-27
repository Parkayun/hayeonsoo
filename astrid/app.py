import os
import sys
import asyncio

from aiohttp import web
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from .middleware import dev


class Astrid(object):

    def __init__(self, template_path='./', middlewares=[]):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop,
                                   middlewares=middlewares+[dev.request_logger,
                                                            dev.web_socket])
        self.setup_jinja(template_path)

    def add_payload(self, payload, handler, methods):
        for method in methods:
            _handler = handler if asyncio.iscoroutinefunction(handler) else asyncio.coroutine(handler)
            self.app.router.add_route(method, payload, _handler)

    def route(self, payload, methods=['GET'], is_websocket=False):
        def _decorator(handler):
            self.add_payload(payload, handler, methods)
            if is_websocket:
                if not hasattr(self.app, 'web_socket_handlers'):
                    setattr(self.app, 'web_socket_handlers', [])
                self.app.web_socket_handlers.append(handler.__name__)
            return handler
        return _decorator

    def run(self, host='127.0.0.1', port=8080):
        @asyncio.coroutine
        def _run():
            self.handler = self.app.make_handler()
            return (yield from self.loop.create_server(self.handler, host, port))

        self.srv = self.loop.run_until_complete(_run())
        try:
            print('Server started with http://', host+":"+str(port), '\n')
            self.loop.run_forever()
        except KeyboardInterrupt:
            print('')
        finally:
            self.loop.run_until_complete(self.handler.finish_connections(1.0))
            self.srv.close()
            self.loop.run_until_complete(self.srv.wait_closed())
            self.loop.run_until_complete(self.app.close())
        self.loop.close()

    @staticmethod
    def setup_jinja(template_path):
        _path = os.path.abspath(template_path)

        Astrid.jinja_env = Environment()
        Astrid.jinja_env.loader = FileSystemLoader(_path)


def get_jinja_env():
    return Astrid.jinja_env
