'''
pytest example using monkeypatching
'''

from collections import namedtuple
import http.client

import pytest

from dev_null_client import DevNull

DummyResponse = namedtuple('DummyResponse', ['status'])

# pylint: disable=too-few-public-methods

class DummyConnection(object):
    '''
    A standin for HTTPSConnection used when testing DevNull
    '''

    def __init__(self):
        self.last_method = None
        self.last_path = None
        self.last_params = None
        self.host = None

    def request(self, method, path, params):
        '''
        patches the request method and captures the parameters
        '''
        self.last_method = method
        self.last_path = path
        self.last_params = params

    @staticmethod
    def getresponse():
        '''
        patches the getresponse method and returns a 200 status code
        '''
        return DummyResponse(status=200)

# pylint: disable=missing-docstring,redefined-outer-name

@pytest.fixture
def dummy_conn(monkeypatch):
    dummy = DummyConnection()
    def get_dummy(host):
        dummy.host = host
        return dummy
    monkeypatch.setattr(http.client, 'HTTPSConnection', get_dummy)
    return dummy

def test_post(dummy_conn):
    dev_null = DevNull()
    assert dev_null.post({'a': 1}) == 200
    assert dummy_conn.last_method == "POST"
    assert dummy_conn.last_path == "/dev/null"
    assert dummy_conn.last_params == 'a=1'
    assert dummy_conn.host == 'devnull-as-a-service.com'
