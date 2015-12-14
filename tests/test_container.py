import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from astrid.container import Container


def test_container():
    container = Container()
    assert type(container.views) is list
    assert len(container.views) == 0

    test_cases = (
        (None, "/a", 1, ["GET"], None, False),
        (["POST"], "/b", 2, ["POST"], True, True),
        (["GET", "POST"], "/c", 3, ["GET", "POST"], None, False),
    )
    for idx, case in enumerate(test_cases):
        methods, expect_url, expect_view_count, expect_methods, is_websocket, expect_websocket = case
        @container.route("/"+chr(97+idx), methods=methods, is_websocket=is_websocket)
        def _dummy():
            return None
        assert len(container.views) == expect_view_count
        assert container.views[idx][0] == expect_url
        assert container.views[idx][1] is _dummy
        assert container.views[idx][2] == expect_methods
        assert container.views[idx][3] is expect_websocket
