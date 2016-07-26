import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest

from hayeonsoo.app import Astrid
from hayeonsoo.http import response, render


def test_response():
    test_cases = (
        ('Hello World', b'Hello World', 200, 'text/html'),
        (b'Hello World', b'Hello World', 200, 'text/html'),
        ({'Hello': 'World'}, b'{"Hello": "World"}', 200, 'application/json'),
        (1234, b'1234', 200, 'text/html'),
    )

    for case in test_cases:
        content, expect_body, expect_status, expect_content_type = case
        resp = response(content)
        assert resp.body == expect_body
        assert resp.status == expect_status
        assert resp.content_type == expect_content_type


def test_render(tmpdir):
    with pytest.raises(Exception) as exec:
        render('test.html')
    assert exec.type is AttributeError

    template = tmpdir.mkdir("html").join("test.html")
    template.write("{% block body %}<h1>{{ hello }}</h1>{% endblock %}")
    template_path = template.dirpath().__str__()

    test_cases = (
        ("", {}, b"wrong template path, test.html", 200, "text/html"),
        (template_path, {}, b"<h1></h1>", 200, "text/html"),
        (template_path, {"hello": "world"}, b"<h1>world</h1>", 200, "text/html"),
    )

    from aiohttp.web import Response
    for case in test_cases:
        template_path, data, expect_body, expect_status, expect_content_type = case
        _ = Astrid(template_path=template_path)
        obj = render("test.html", data)
        assert type(obj) is Response
        assert obj.body == expect_body
        assert obj.status == expect_status
        assert obj.content_type == expect_content_type
