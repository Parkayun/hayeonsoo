class Container(object):

	views = []

	def route(self, payload, methods=['GET'], is_websocket=False):
		def _decorator(handler):
			self.views.append((payload, handler, methods, is_websocket))
			return handler
		return _decorator