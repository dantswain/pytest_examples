'''
pytest example using monkeypatching
'''

from collections import namedtuple
import http.client

import pytest

from dev_null_client import DevNull

DummyResponse = namedtuple('DummyResponse', ['status'])

class DummyConnection(object):
    def __init__(self):
        self.last_method = None
        self.last_path = None
        self.last_params = None
        self.host = None

    def request(self, method, path, params):
        self.last_method = method
        self.last_path = path
        self.last_params = params

    def getresponse(self):
        return DummyResponse(status=200)

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
