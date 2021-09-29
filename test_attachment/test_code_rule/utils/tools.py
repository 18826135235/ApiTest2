import json

import requests
import yaml


class tools():

    with open("../../../logindata.yaml",'r') as f:
        login_data=yaml.safe_load(f.read())
    default_env=login_data['default']



    @classmethod
    def get_accessToken(cls):

            parms={
                   'user': cls.login_data[cls.default_env]['user'],
                   'appId': cls.login_data[cls.default_env]['appId'],
                   'appSecuret': cls.login_data[cls.default_env]['appSecuret'],
                   'language': cls.login_data[cls.default_env]['language'],
                   'accountId': cls.login_data[cls.default_env]['accountId'],
                   'usertype': cls.login_data[cls.default_env]['usertype']
                    }

            url=f"{cls.get_url()}/api/login.do"
            response=requests.post(url,json.dumps(parms),verify=False)
            print(response.text)
            data=response.json()

        #获取accessToken:
            if data['state']== "success":
                cls.access_token = data['data']["access_token"]
                return cls.access_token
            else:
                raise Exception("token获取失败"+response.text)

    @classmethod
    def get_url(cls):
        url=cls.login_data[cls.default_env]['url']
        return url

    @classmethod
    def get_data(cls,key):
        with open("../../../test_data.yaml",'r') as f:
            test_data=yaml.safe_load(f.read())
        default_env=test_data['default']
        keys=test_data[default_env].keys()
        if key not in keys:
            raise KeyNotFoundException(key)

        for data in keys :
            if data == key:
                return test_data[default_env][key]


class KeyNotFoundException(Exception):
    def __init__(self,key):
        self.key = key
    def __str__(self):
        print("Key："+str(self.key)+"在配置文件中不存在")










