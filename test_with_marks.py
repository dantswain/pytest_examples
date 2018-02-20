'''
Demonstrating pytest marks
'''

import pytest

@pytest.mark.skip
def test_never_runs():
    assert False

@pytest.mark.xfail
def test_would_fail():
    assert False

@pytest.mark.parametrize('x, double_x',
                         [(1, 2),
                          (-1, -2),
                          ('a', 'aa')],
                         ids=['integer', 'negative integer', 'string'])
def test_parametrized(x, double_x):
    assert x * 2 == double_x
