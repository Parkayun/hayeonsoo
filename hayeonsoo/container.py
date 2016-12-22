class Container(object):

    views = None

    def __init__(self):
        self.views = []

    def route(self, payload, methods=None, is_websocket=None):
        if methods is None:
            methods = ["GET"]
        if is_websocket is None:
            is_websocket = False
        def _decorator(handler):
            self.views.append((payload, handler, methods, is_websocket))
            return handler
        return _decorator
