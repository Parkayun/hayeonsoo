# -*- coding:utf-8 -*-
__all__ = ('response',)

import json

from aiohttp.web import Response


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
