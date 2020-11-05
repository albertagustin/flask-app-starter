import pytest

from test.helpers.fixtures_helper import parse_json_file


@pytest.fixture(scope='function')
def error_response():
    return parse_json_file('test/files/sample_error.json')


@pytest.fixture(scope='function')
def ok_response():
    return parse_json_file('test/files/sample_ok.json')
