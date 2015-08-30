import os
import json

from aiohttp.web import Response
from jinja2.exceptions import TemplateNotFound

from .app import get_jinja_env


def render(html, data={}):
    body = b''
    try:
        template = get_jinja_env().get_template(html)
        body = template.render(**data).encode('utf-8')
    except TemplateNotFound:
        body = ' '.join(('wrong template path,', html)).encode('utf-8')
    return response(body)


def response(body, content_type='text/html; charset=utf-8'):
    kwargs = {'body': body, 'content_type': content_type}

    if isinstance(body, str):
        kwargs['body'] = body.encode('utf-8')
    elif isinstance(body, dict):
        kwargs['content_type'] = 'application/json; charset=utf-8'
        kwargs['body'] = json.dumps(body).encode('utf-8')
    elif isinstance(body, int) or isinstance(body, float):
        kwargs['body'] = str(body).encode('utf-8')

    return Response(**kwargs)
