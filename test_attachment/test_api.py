
import  requests
import  unittest
import json
import jsonpath

class  TestApi(unittest.TestCase):

    global accesstoken
    baseUrl = "https://feature.kingdee.com:1026/patchcore/"
    test_url = "kapi/app/open/bindingAtt"
    global url
    url= baseUrl + test_url


    def test_access_token(self):
        global accesstoken
        parms={
            "user": "17299999999",
            "password": "1234567",
            "language": "zh_CN",
            "accountId": "201912161126422140",
            "logintype":"2"
           }

        url="https://feature.kingdee.com:1026/patchcore/api/login.do"
        response=requests.post(url,json.dumps(parms))
        print(response.text)
        content =json.loads(response.content)

        #获取accessToken:
        # if(response.content["state"] == "success"){
        # accessToken=response.content
        # }

        # if content['state']== "success":
        #     accesstoken=content['data']["access_token"]
        #     print(accesstoken)
        #     return  accesstoken

    def test_no_token( self):

        params={
                "formNumber":"testFormNumber",
                "billPkId":"836117104519284736",
                "data":{
                    "attachmentpanel":[
                        {
                            "entryPkId":"836117104519284737",
                            "fileName":"test.xlsx",
                            "size":95270,
                            "extName":"xlsx",
                            "path":"/dev/2020/86080/att/test.xlsx",
                            "createUserId":"36550"
                        }
                    ]
                }
            }

        headers = {"accessToken":self.test_access_token()}

        response = requests.post(url, data=json.dumps(params),headers=headers)
        print(response.content)


    def test_get_code(self):
        url="https://feature.kingdee.com:1026/patchcore/kapi/app/base/getOnlineCode"
        headers = {"accessToken": self.get_access_token()}
        response=requests.get(url=url,headers=headers);

        print((response.json())["success"])
        print(type(response.json()))

    def test_post_data(self):
        global accesstoken
        parms = {
            "user": "17299999999",
            "password": "1234567",
            "language": "zh_CN",
            "accountId": "201912161126422140",
            "logintype": "2"
        }

        url = "https://feature.kingdee.com:1026/patchcore/api/login.do"
        response = requests.post(url, data=parms)
        print(response.text)

    def test_jsonpath(self):
        url="https://feature.kingdee.com:2024/baseline_a/api/login.do"
        payload = {
            "user": "17299999999",
            "password": "1234567",
            "language": "zh_CN",
            "accountId": "201912161126422140",
            "logintype": "2"
        }
        response=requests.post(url,)









if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(TestApi('get_access_token'))
    # suite.addTest(TestApi('test1'))
    # suite.addTest(TestApi('test_no_token'))

    # suite.addTest(TestApi('test_get_code'))
    #
    #
    # unittest.TextTestRunner().run(suite)



