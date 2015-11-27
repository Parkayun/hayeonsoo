astrid
======


A simple web framework based on aiohttp.


Quick start
-----------

.. sourcecode:: python

   import os

   from astrid import Astrid
   from astrid.http import render, response
   from astrid.utils import MessageType


   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   TEMPLATES = os.path.join(BASE_DIR, 'templates')

   app = Astrid(template_path=TEMPLATES)

   @app.route('/')
   def index_handler(request):
       return response("Hello 세계")

   @app.route('/json')
   def json_handler(request):
       return response({"Hello": "세계"})

   @app.route('/render')
   def render_handler(request):
       return render('index.html', {'message': "Hello World"})

   @app.route('/ws', is_websocket=True)
   def websocket_handler(requset, ws):
       await ws.prepare(request)
       async for msg in ws:
           if msg.tp == MessageType.text:
               if msg.data != "close":
                   ws.send_str("Hello Websocket")
               else:
                   await ws.close()
           elif msg.tp == MessageType.error:
               print("Exception: %s" % ws.exception())
       return ws

   app.run()
