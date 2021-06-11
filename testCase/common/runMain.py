import requests
import time
import demjson
import base64



class RunMain():

    """
    封装get函数
    """
    def get(self,url,headers):
        if headers:
            # 如果有消息头
            response = requests.get(url=url,headers=headers,verify = False)
            response.close()
        else:
            response = requests.get(url=url,verify = False)
            response.close()
        return response.json(),response.headers

    """
    封装post函数
    """
    def post(self,url,data,headers):
        if headers:
            response = requests.post(url=url,data = data,headers = headers)
        else:
            response = requests.post(url=url,data = data)
        return response.json(),response.headers


    """
    判断请求的类型为get还是post
    """
    def main(self,method,url,data,headers):
        if method == "POST":
            res,res_headers = self.post(url,data,headers)
        else:
            res,res_headers = self.get(url, headers)
        return res,res_headers




