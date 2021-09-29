import json

import pytest
import requests

import yaml


import os

from test_attachment.test_code_rule.utils.tools import tools


class TestRule:


    def setup(self):
        self.access_token=tools.get_accessToken()
        self.url=tools.get_url()




    def test_get_code(self):
        url=f"{self.url}/kapi/app/base/getOnlineCode"
        headers = {"accessToken": self.access_token}
        response=requests.get(url=url,headers=headers)
        print(response.json())


    def test_getLadingUrl(self):
        url=f"{self.url}/kapi/app/base/getLadingURL"
        headers = {"accessToken": self.access_token}
        response=requests.get(url=url,headers=headers)
        print(response.json())


    def test_getPreSalesChatURL(self):
        url=f"{self.url}/kapi/app/base/getPreSalesChatURL"
        headers = {"accessToken": self.access_token}
        response=requests.get(url=url,headers=headers)
        print(response.json())



















