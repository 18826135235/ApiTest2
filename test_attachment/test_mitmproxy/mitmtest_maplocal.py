import json

import mitmproxy.http
from mitmproxy.tools.main import mitmdump


class Events:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP CONNECT request was received. Setting a non 2xx response on
            the flow will return the response to the client abort the
            connection. CONNECT requests and responses do not generate the usual
            HTTP handler events. CONNECT requests are only valid in regular and
            upstream proxy modes.
        """
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP request headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):


        """
        测试mapLocal
        :param flow:
        :return:
        """
        """
            The full HTTP request has been read.
        """
        if "https://feature.kingdee.com:2024/baseline_a/form/batchInvokeAction.do?appId=bos&f=bos_portal_personalinfo&ac=customEvent" in flow.request.url:

            data=json.load(open("F:\signature.json",'r',encoding="utf-8"))
            data[4]["p"][1]["v"]="我把你名字改了"
            with open("F:\signature.json",'w',encoding="utf-8") as f:
                json.dump(data,f)

            #重新读入数据

            with open("F:\signature.json",'r',encoding="utf-8") as f:
                flow.response=mitmproxy.http.HTTPResponse.make(200,f.read())




    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP response headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://feature.kingdee.com:1026/patchcore/getUserLanguage.do?" in flow.request.url:
            flow.response.text='{"language":"English","userId":"966416219416561664_13466739"}'

    def error(self, flow: mitmproxy.http.HTTPFlow):
        pass


addons=[Events()]
if __name__ == '__main__':
    mitmdump(['-p','8888','-s',__file__])