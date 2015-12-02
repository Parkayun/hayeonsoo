from astrid.http import response


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
