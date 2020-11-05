import pytest

from src.helpers.sample_helper import SampleHelper


class TestSampleHelper(object):

    def test_get_ip_address(self, app):
        assert SampleHelper.get_ip_address() != '0.0.0.0'
