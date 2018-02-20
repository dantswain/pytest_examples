'''
pytest example using fixtures
'''

import pytest

class Message(object):
    def __init__(self, content):
        self.content = content

    def reverse(self):
        return self.content[::-1]

    def __add__(self, other_msg):
        return Message(' '.join([self.content, other_msg.content]))

@pytest.fixture
def hello():
    return Message("Hello")

@pytest.fixture
def world():
    return Message("World")

def test_hello(hello):
    assert hello.reverse() == "olleH"

def test_hello_world(hello, world):
    assert (hello + world).content == "Hello World"
