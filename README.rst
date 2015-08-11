astrid
======


A simple web framework based on aiohttp.


Quick start
-----------

.. sourcecode:: python

   from astrid import Astrid
   from astrid.http import render, response


   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   TEMPLATES = os.path.join(BASE_DIR, 'templates')

   app = Astrid(template_path=TEMPLATES)

   @app.route('/')
   def index_handler(request):
       return response("Hello 세계")

   @app.route('/json')
   def json_handler(request):
       return response({"Hello": u"세계"})

   @app.route('/render')
   def render_handler(request):
       return render('index.html', {'message': 'Hello World'})

   app.run()
