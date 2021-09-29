import json

import allure
import pytest
import requests

import yaml


import os

from test_attachment.test_code_rule.utils.tools import tools


@allure.feature("Test code rule")
class TestRule:


    def setup(self):
        self.access_token=tools.get_accessToken()
        self.env=tools.get_url()
        self.key=tools.get_data('key')

    @allure.story("test_init")
    def test_init(self):
        url=f"{self.env}/kapi/app/base/idgenrelease?key={self.key}&releaseType=init"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)

    @allure.story("shut down")
    def test_shutdown(self):
        url=f"{self.env}/kapi/app/base/idgenrelease?key={self.key}&releaseType=downtime"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)


    # def test_distrubte_number(self):
    #ID生成器-模拟发号-普通型读号---新增读号
    @allure.story("test read number")
    def test_pre_readnumber(self):
        url=f"{self.env}/kapi/app/base/idgensigner?key={self.key}&signerEnum=read&initNumber=0&step=1&segmentLength=100"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)

    #ID生成器-模拟发号-普通型发号  保存发号
    def test_pre_sendnumber(self):
        url=f"{self.env}/kapi/app/base/idgensigner?key={self.key}&signerEnum=consume&initNumber=0&step=1&segmentLength=100&reqSequence=5"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers,verify=False)
        print(response.text)

    #高可靠读号
    def test_readnumber(self):
        url=f"{self.env}/kapi/app/base/idgensigner?key={self.key}&signerEnum=read_and_record&initNumber=0&step=1&segmentLength=100&reqSequence=0"

        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers,verify=False)
        r=response.json()
        assert (r["success"]==True and r["data"]["curseq"]==5)
        print(response.text)

    def test_send_number(self):
        url=f"{self.env}/kapi/app/base/idgensigner?key={self.key}&signerEnum=consume_and_record&initNumber=0&step=1&segmentLength=100&reqSequence=320"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)


    def test_config_cache(self):
        url=f"{self.env}/kapi/app/base/idgensearch?key={self.key}&searchEnum=config_cache"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)



    #测试发号缓存
    def test_signer_cache(self):
        url=f"{self.env}/kapi/app/base/idgensearch?key={self.key}&searchEnum=signer_cache"
        headers={"access_token":self.access_token}
        response=requests.get(url,headers=headers)
        print(response.text)

    def test_assure(self):
        assert 3==3
        assert  4==4











