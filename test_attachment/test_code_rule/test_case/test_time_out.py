
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


    def test_time_out(self):
        url=f"{self.url}/form/batchInvokeAction.do?appId=bos&f=pc_main_console&ac=release"
        cookie='gr_user_id=ac4358de-1426-48c8-9467-ee6e528fdd4e; testvipclubsessionid=ZGYyYjg4OGMtY2JlMi00MzVjLThiN2MtMjUxYjFjMjQzZTNi; CSRF-TOKEN=0b2c5d96-1e87-4ddb-b347-24554af01ff5; tenant_patchcore_test_kdshareflag=; PPSESSION=ac27b7cb-fea3-4809-ba84-84b8050c794b; baseline_a_kdshareflag=; KERPSESSIONIDbaseline_a=1173910536060928000_D1kXy2ci2MxkmtMJ6IkBNCq4B5rQFPqOQ21w9eWSqZM1YjXBtFyEv4cSJecQWtvf9haag1XP1oey6f294WY9BeuxmLUCrtQNq8IV; kdvipclubsessionid=NWU2NjM3NDYtZjg2Zi00MjhhLTlkYmUtNzg4ODBjMjFjZmRj; KERPSESSIONIDtenant_patchcore_test=966416219416561664_lUvrjKdcE287lhqXr2R5749Wp1cIs3itkQAJgYAy622NUtFJDChATWSXje4uhus86iT1h3QnmfJum57SxVtQvI80ujC6znMH64lR; KERPSESSIONID=966416219416561664_lUvrjKdcE287lhqXr2R5749Wp1cIs3itkQAJgYAy622NUtFJDChATWSXje4uhus86iT1h3QnmfJum57SxVtQvI80ujC6znMH64lR'
        headers={'cookie':cookie}
        data={

            "page"



            }





















