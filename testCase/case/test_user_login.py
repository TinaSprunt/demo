#cod-ing utf-8
import os
import json
import unittest
import HTMLTestRunner
import math
import time
from common.runMain import RunMain
from common.getData import GetData
from common.utils import Utils
from common.analogDataMock import Mock
from common.sendEmail import SendEmail
from common.headers import Headers
from common.ToExcel import ToExcel



class Test:
    def __init__(self,input_name):
        """
        初始化
        """
        self.runMethod = RunMain()#根据method值进行get、post调用
        self.toExcel = ToExcel(input_name)#对excel进行读入写入准备
        self.headers = Headers()#更新消息头
        self.utils = Utils()#加载工具类
        self.mock = Mock()#加载数据模拟
        self.sendEmail = SendEmail()#发送测试邮件到指定邮箱


    def run_test(self):
        """
        对inputExcel文档中的接口进行测试并生成报告
        :return:
        """
        row_counts = self.toExcel.input_data.get_case_lines()#获取测试用例总条数
        url = self.toExcel.input_data.get_request_url()
        method = self.toExcel.input_data.get_request_method()
        test_name = self.toExcel.input_data.get_request_url()
        test_pass = 0 #测试通过条数
        test_fail = 0 #测试失败条数
        percentage_pass = 0.0 #通过条数占比
        percentage_fail = 0.0 #失败条数占比


        for i in range(5,row_counts + 5):

            id = self.toExcel.input_data.get_requests_id(i)  # 获取当前条实例id
            data = self.toExcel.input_data.get_request_data(i) #获取当前实例参数
            expected_state_code = self.toExcel.input_data.get_expected_code(i)  # 获取预期stateCode
            print("\t\t\t\t\t当前测试用例id为:{}".format(id))#打印测试的接口的url
            print("url:{}".format(url))

            if test_name == "http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin":
                # 将用户名和密码进行base64加密,获得拼接后的请求头
                headers = self.utils.encapsulate_headers(*data)
            else:
                #模拟登录操作，更新headers
                k_url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin'
                k_headers = self.utils.encapsulate_headers("admin","123456")
                res,res_heders = self.runMethod.main(method='POST', url=k_url, data=None, headers=k_headers)
                print("auth-token值：{}".format(res_heders['auth-token']))

                # 更新请求头的Auth-Token以及Content-Length
                self.headers.update_header_Token(res_heders['auth-token'])
                self.headers.update_header_len('119')
                #print("提交数据长度：{}".format(len(str(data))))


            print("测试用例数据{}".format(data))
            #真实接口调用函数
            #print("添加用户传入headers:{}".format(self.headers.get_headers()))
            print("hea",self.headers.get_headers())
            res,test_heders = self.runMethod.main(method=method, url=url, data=data, headers=self.headers.get_headers())
            #print("当前请求头{}".format(res_heders.get('Auth-Token')))



            #将Auth-Token写入json文件保存
            # with open("../common/header.json", 'w') as f:
            #     self.headers.get_headers()['Auth-Token'] = headers["Auth-Token"]
            #     self.headers.get_headers()['Content-Length'] = headers['Content-Length']
            #     json.dump(self.headers, f)

            #模拟信息，调用mock
            #mock_res = self.mock.main(method=method,url=url,data=data,headers=headers)

            #断言,对比stateCode值

            #test_res = self.utils.is_ok_key(str(expected_state_code), eval(mock_res))
            print("预期code:{}".format(expected_state_code))
            print("实际返回code:{}".format(res["returnState"]["stateCode"]))
            test_res = self.utils.is_ok_key(expected_state_code,res)

            #写入测试结果
            if test_res:
                test_pass += 1
                self.toExcel.write_data.write_test_res(i-5, "PASS")  # 将测试结果进行self写入，存入excel
            else:
                test_fail += 1
                self.toExcel.write_data.write_test_res(i-5, "NO")

            self.toExcel.write_msg_info(i,id,self.headers.get_headers())   #写入info信息
            self.toExcel.write_data.write_actual_value(i-5, res)  # 写入实际结果

            #计算占比
            percentage_pass = float(test_pass)/row_counts
            percentage_fail = float(test_fail)/row_counts

            print("===========================================================")
            print("\t\t\t\t\t\t通过条数：{}".format(test_pass))
            print("\t\t\t\t\t\t失败条数：{}".format(test_fail))
            print("\t\t\t\t\t\t通过条数占比：{:.2%}".format(percentage_pass))
            print("\t\t\t\t\t\t失败条数占比：{:.2%}".format(percentage_fail))
            print("===========================================================")


if __name__=="__main__":

    #遍历该路径下的所有后缀名为xls的文件，并逐个实例化、调用run_test测试
    path = r"D:\PycharmProjects\demo2\common"
    f_list = os.listdir(path)
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.xls':
            input_name = path + "\\" + i
            print("当前读入的用例文件{}".format(i))
            test = Test(input_name)
            test.run_test()
    print("测试结果写入完成")



