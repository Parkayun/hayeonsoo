hayeonsoo
======


.. image:: https://secure.travis-ci.org/Parkayun/hayeonsoo.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/hayeonsoo


.. image:: https://img.shields.io/coveralls/Parkayun/hayeonsoo.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/Parkayun/hayeonsoo


aiohttp for humans.


Installing
~~~~~~~~~~

This is under development, You should install via Github.

.. sourcecode:: bash

   ~ $ pip install git+https://github.com/Parkayun/hayeonsoo.git


Quick start
~~~~~~~~~~~

app.py

.. sourcecode:: python

   import os

   from hayeonsoo import Hayeonsoo

   from sample import container


   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   TEMPLATES = os.path.join(BASE_DIR, 'templates')

   hayeonsoo = Hayeonsoo(template_path=TEMPLATES)

   hayeonsoo.register_container(container, prefix='/test')

   if __name__ == '__main__':
       hayeonsoo.run()

sample.py

.. sourcecode:: python

   from hayeonsoo.http import render, response
   from hayeonsoo.utils import MessageType
   from hayeonsoo.container import Container


   container = Container()


   @container.route('/')
   def index_handler(request):
       return response("Hello 세계")

   @container.route('/json')
   def json_handler(request):
       return response({"Hello": "세계"})

   @container.route('/render')
   def render_handler(request):
       return render('index.html', {'message': "Hello World"})

   @container.route('/ws', is_websocket=True)
   def websocket_handler(request, ws):
       ws.prepare(request)
       for msg in ws:
           if msg.tp == MessageType.text:
               if msg.data != "close":
                   ws.send_str("Hello Websocket")
               else:
                   ws.close()
           elif msg.tp == MessageType.error:
               print("Exception: %s" % ws.exception())
       return ws


Working with Gunicorn
~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

   ~ $ gunicorn app:hayeonsoo.app --worker-class aiohttp.worker.GunicornWebWorker
   
Reload

.. sourcecode:: bash

   ~ $ kill -9 {gunicorn pid}
