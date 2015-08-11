astrid
======


A simple web framework based on aiohttp.


Quick start
-----------

.. sourcecode:: python

   from astrid import Astrid
   from astrid.http import response


   app = Astrid()

   @app.route('/')
   def index_handler(request):
       return response("Hello 세계")

   @app.route('/json')
   def json_handler(request):
       return response({"Hello": u"세계"})

   app.run()
