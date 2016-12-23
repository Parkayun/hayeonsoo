import json

from aiohttp.web import Response
from jinja2.exceptions import TemplateNotFound

from .app import get_jinja_env


def render(html, data={}):
    try:
        template = get_jinja_env().get_template(html)
        body = template.render(**data).encode('utf-8')
    except TemplateNotFound:
        body = ' '.join(('wrong template path,', html)).encode('utf-8')
    return response(body)


def response(body, charset='utf-8', content_type='text/html', status_code=200):
    kwargs = {'body': body, 'charset': charset, 'content_type': content_type, 'status': status_code}

    if isinstance(body, str):
        kwargs['body'] = body.encode('utf-8')
    elif isinstance(body, dict):
        kwargs['content_type'] = 'application/json'
        kwargs['body'] = json.dumps(body).encode('utf-8')
    elif isinstance(body, int) or isinstance(body, float):
        kwargs['body'] = str(body).encode('utf-8')

    return Response(**kwargs)

