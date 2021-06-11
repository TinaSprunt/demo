import requests
import json


class Headers():
    def __init__(self):
        self.headers ={
            'Host': '10.0.20.126',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept':'*/*',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate',
            'Content-Type':'application/x-www-form-urlencoded',
            'Auth-Token':'',
            'Content-Length':'164',
            'Connection':'keep-alive',
            'Referer':'http://10.0.20.126/'
            }

    def update_header_Token(self,auth_token):
        """
        更新authToken
        :param authToken:
        :return:
        """
        self.headers['Auth-Token'] = auth_token


    def update_header_len(self,data_len):
        """
        更新dataLen
        :param header:
        :param dataLen:
        :return:
        """
        self.headers['Content-Length'] = data_len

    def get_headers(self):
        return self.headers










