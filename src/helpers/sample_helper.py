# sample_helper.py

import json
import requests

from src.helpers.base_helper import BaseHelper


class SampleHelper(BaseHelper):

    @staticmethod
    def get_ip_address():
        with requests.Session() as s:
            response = s.get('https://api64.ipify.org?format=json')

        return response.json().get('ip', '0.0.0.0') if response.status_code == requests.codes.ok else '0.0.0.0'
