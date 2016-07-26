import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from hayeonsoo.utils import MessageType


def test_message_type():
    test_cases = (
        ('text', 0x1),
        ('binary', 0x2),
        ('ping', 0x9),
        ('pong', 0xa),
        ('close', 0x8),
        ('closed', 20),
        ('error', 21),
    )
    for case in test_cases:
        attribute, expect_value = case
        assert getattr(MessageType, attribute) == expect_value
