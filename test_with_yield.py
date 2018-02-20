'''
pytest example using a yield fixture
'''

import os
import shutil
import pytest

@pytest.fixture(scope='module')
def output_dir():
    return 'test-output'

@pytest.fixture(scope='module', autouse=True)
def clean_output(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)
    os.mkdir(output_dir)
    yield
    shutil.rmtree(output_dir)

def test_write_file(output_dir):
    with open(os.path.join(output_dir, 'test.txt'), 'w') as f:
        f.write('Hello!')
    assert os.path.exists(os.path.join(output_dir, 'test.txt'))

def test_read_file(output_dir):
    with open(os.path.join(output_dir, 'test.txt'), 'r') as f:
        assert f.read() == 'Hello!'
