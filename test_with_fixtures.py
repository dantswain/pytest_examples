'''
pytest example using fixtures
'''

import pytest

# pylint: disable=too-few-public-methods

class Message(object):
    '''
    Holds a message, can be added together
    '''
    def __init__(self, content):
        self.content = content

    def reverse(self):
        '''
        Returns the message but in reverse
        '''
        return self.content[::-1]

    def __add__(self, other_msg):
        return Message(' '.join([self.content, other_msg.content]))

# pylint: disable=missing-docstring,redefined-outer-name

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
