'''
pytest example
'''

import pytest

# pylint: disable=missing-docstring

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

def test_split():
    a_string = 'hello world'
    assert a_string.split() == ['hello', 'world']
    with pytest.raises(TypeError):
        a_string.split(2)
