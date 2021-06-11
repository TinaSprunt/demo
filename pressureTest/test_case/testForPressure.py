# coding=utf8
import threading
import pytz
import datetime
import queue
from common.mockMessage import Mock
from common.getData import GetData
from common.updataHeaders import Headers
from common.runMain import RunMain
from common.utils import Utils

class DataPool:
    def __init__(self):
        """
        创建队列
        """
        self.add_pool = queue.Queue()
        self.login_pool = queue.Queue()
        self.res_pool = queue.Queue()
        self.del_pool = queue.Queue()


class TestForPressure:
    def __init__(self):
        """
        初始化
        """
        self.runMethod = RunMain()#根据method值进行get、post调用
        self.getData = GetData()#获取参数
        self.getHeader = Headers()#获取消息头
        self.mock = Mock()#模拟校验信息
        self.utils = Utils()
        self.dataPool = DataPool()


    def prepare_queue(self):
        """
        准备数据，填充队列queue
        :return:
        """
        for i in range(0, 100):
            addUserData = '{"accountInfo":{' \
                          '"userID":"%s","username":"%s",' \
                          '"password":"123456",' \
                          '"functionalRoleList":[{"functionalRole":"1"}],' \
                          '"resourceRoleList":[{"resourceRole":"11"}]}}'%(str(400+i),"meimei"+str(400+i))

            self.dataPool.add_pool.put(addUserData)
            self.dataPool.login_pool.put('{"accountInfo":{"userID":"%s",'
                                     '"username":"%s",'
                                     '"password":"123456"}}'%(str(400+i),"meimei"+str(400+i)))
            self.dataPool.del_pool.put('{"userID":"%s"}'%(str(400+i)))
        print("队列添加完成")

    def prepare_login(self):
        # 模拟登录操作，更新headers
        print("删除开始执行")
        k_url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin'
        k_headers = self.utils.encapsulate_headers("admin", "123456")
        preprocessing_res, preprocessing_res_heders = self.runMethod.main(method='POST', url=k_url, data=None, headers=k_headers)
        self.getHeader.update_header_Token(preprocessing_res_heders['auth-token'])



    def check_response(self):
        pass

    def createAddThread(self,threadNum,pressure_num):
        """
        创建添加用户线程
        :param threadNum:
        :param pressure_num:
        :return:
        """
        # 创建数组存放线程
        threads = []
        try:
            # 创建线程
            for i in range(0, threadNum):
                # 针对函数创建线程
                t = threading.Thread(target=self.add_user_runing, args=())
                # 把创建的线程加入线程组
                threads.append(t)
        except Exception as e:
            print("创建子线程出现异常，异常信息为：{}".format(e))

        for thread in threads:
            thread.start()
            thread.join()



    def add_user_runing(self):
        """
        添加用户IO操作
        :return:
        """
        headers = self.getHeader.get_headers()
        method = 'POST'
        test_url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser'  # 接口URL
        add_user_data = self.dataPool.add_pool.get()
        res, res_headers = self.runMethod.main(method=method, url=test_url, data=add_user_data, headers=headers)
        print(res)
        print("用户添加完成")

    def createThread(self,threadNum,pressure_num):
        """
        创建登录用户子线程
        :param threadNum:
        :param pressure_num:
        :return:
        """
        # 创建数组存放线程
        threads = []
        try:
            # 创建线程
            for i in range(0, threadNum):
                # 针对函数创建线程
                t = threading.Thread(target=self.test_runing, args=())
                # 把创建的线程加入线程组
                threads.append(t)
        except Exception as e:
            print("创建子线程出现异常，异常信息为：{}".format(e))

        for thread in threads:
            thread.start()
            thread.join()


    def test_runing(self):
        """
        登录用户IO
        :return:
        """
        login_data = eval(self.dataPool.login_pool.get())
        print(login_data['accountInfo']['username'],login_data['accountInfo']['password'])
        headers = self.utils.encapsulate_headers(login_data['accountInfo']['username'], login_data['accountInfo']['password'])
        method = 'POST'
        test_url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin'  #接口URL
        res, res_headers = self.runMethod.main(method=method, url=test_url, data=login_data, headers=headers)
        print(res)
        print("用户登录成功")

    def deleteUser(self):
        """
        删除用户IO
        :return:
        """
        headers = self.getHeader.get_headers()
        method = 'POST'
        test_url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserDeleteUser'  # 接口URL
        del_user_data = self.dataPool.del_pool.get()
        print(del_user_data)
        res, res_headers = self.runMethod.main(method=method, url=test_url, data=del_user_data, headers=headers)
        print("用户删除完成")

    def createDeleteThread(self,threadNum,pressure_num):
        """
        创建多线程
        :param threadNum:
        :param pressure_num:
        :return:
        """
        # 创建数组存放线程

        threads = []
        try:
            # 创建线程
            for i in range(0, threadNum):
                # 针对函数创建线程
                print("创建删除线程")
                t = threading.Thread(target=self.deleteUser, args=())
                # 把创建的线程加入线程组
                threads.append(t)
        except Exception as e:
            print("创建子线程出现异常，异常信息为：{}".format(e))

        for thread in threads:
            thread.start()
            thread.join()

if __name__ == '__main__':
    start_time = datetime.datetime.now(pytz.timezone('PRC'))
    print(start_time)
    print("开始测试，当前是北京时间：{}".format(start_time.strftime('%Y-%m-%d %H:%M:%S')))
    testDemo = TestForPressure()

    threadNum = 100
    pressure_num = 1000
    interval_time = 1
    duration = 60

    testDemo.prepare_queue()
    testDemo.prepare_login()
    testDemo.createAddThread(threadNum,pressure_num)
    testDemo.createThread(threadNum,pressure_num)
    testDemo.createDeleteThread(threadNum, pressure_num)



    end_time = datetime.datetime.now(pytz.timezone('PRC'))
    time_difference = end_time - start_time
    print("执行完毕，当前是北京时间：{},一共耗时：{}秒".format(end_time.strftime('%Y-%m-%d %H:%M:%S'),time_difference.seconds))










