import json

import pytest
import requests


class TestUpload:

    access_token=''


    def setup(self):
        # global access_token

        parms={
            "user": "18826135235",
            "password": "1234567",
            "language": "zh_CN",
            "accountId": "966416219416561664",
            "logintype":"2"
        }

        url="https://feature.kingdee.com:1026/patchcore/api/login.do"
        response=requests.post(url,json.dumps(parms))
        print(response.text)
        # content =json.loads(response.content)
        data=response.json()

        #获取accessToken:
        if data['state']== "success":
            self.access_token = data['data']["access_token"]


    @pytest.mark.parametrize("filename",["data2.txt"])
    def test_uploadfile(self,filename):
        url="https://feature.kingdee.com:1026/patchcore/attachment/upload.do"
        filepath=f'D:\{filename}'
        file = {'file':(filepath, open(filepath, 'rb'))}
        payload={
            "file":file,
            "url":filename
        }

        params={"access_token":self.access_token}

        response=requests.post(url,params=params,files=file,data=payload)
        print(response.content)