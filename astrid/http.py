import os
import json

from aiohttp.web import Response
from jinja2 import Template

from .app import get_template_path


def render(html, data):
    body = b'wrong template path'
    template_path = os.path.join(get_template_path(), html)
    with open(template_path, 'r') as template:
        body = Template(template.read()).render(**data).encode('utf-8')
    return Response(body=body, content_type='text/html; charset=utf-8')


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
