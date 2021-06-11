import requests
import queue
import threading
import uuid
import time
import pytz
import datetime
from common.mockMessage import Mock
from common.runMain import RunMain

#教程代码   https://www.cnblogs.com/zhangb8042/p/10251276.html
#并发代码   https://www.iteye.com/blog/darklipeng-1591753

mock = Mock()
runer = RunMain()
status_code_list = []
exec_time = 0

class MyThreadPool:
    def __init__(self, maxsize):
        """
        初始化，新建长度不超过maxsize的线程池队列_pool，向线程池里插入线程
        :param maxsize:
        """
        self.maxsize = maxsize
        self._pool = queue.Queue(maxsize)
        for _ in range(maxsize):
            self._pool.put(threading.Thread) #向队列也就是当前线程池尾部插入一个线程


    def get_thread(self):
        return self._pool.get()

    def add_thread(self):
        self._pool.put(threading.Thread)

def request_time(func):
    def inner(*args, **kwargs):
        global exec_time
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time-start_time

    return inner


def get_url(url):
    # global status_code_list,x
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    #            }
    # #response = requests.get(url,headers=headers)
    #
    # postData = {
    #     "userName":uuid.uuid1(),
    #     "passWord":"123456"
    # }
    #
    #
    # response = mock.main(method="POST", url=url, data = postData,header=headers)
    # code = response['returnState']['stateCode']
    # #print("完成用户{}登录".format(postData))
    # status_code_list.append(code)
    # return code
    pass


def add_user():
    print("添加用户执行")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        }
    method = "POST"
    addUserUrl = "http://10.0.20.126/VMS2Service.cgi?Cmd=UserAddUser"
    for i in range(0,10):
        addUserData = {
            "accountInfo":{
                "userID": 233 + i,
                "userName":"meimei"+str(i),
                "passWord": "123456",
                "functionalRoleList": [
                    {"functionalRole": "11111111110"},
                    {"functionalRole": "11111111111"}
                ],
                "resourceRoleList": [
                    {"resourceRole": "11111111112"},
                    {"resourceRole": "11111111113"}
                ]
            }
        }
        res,res_headers = runer.main(method=method,url=addUserUrl,data=addUserData,headers=headers)
        print(res)





def get_count(_url='http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin',_count=100):
    '''
    :param count: 每个线程请求的数量
    '''
    global status_code_list,url,count
    for i in range(count):
        print(i)
        add_user()
        #get_url(url)








def request_status():
    count_num = len(status_code_list)
    set_code_list = set(status_code_list)
    status_dict = {}
    for i in set_code_list:
        status_dict[i] = str(status_code_list).count(str(i))
    echo_str(count_num, set_code_list, status_dict)

def echo_str(count_num,set_code_list,status_dict):
    print('=======================================')
    print('请求总次数:%s'%count_num)
    print('请求时长:%s秒'%int(exec_time))
    if(int(exec_time) != 0):
        second_request = count_num / int(exec_time)
        print('每秒请求约:%s次' % int(second_request))
    else:
        pass

    print('状态码 | 次数')

    for k,v in status_dict.items():
        print(str(k)+'    | '+str(v))
    print('=======================================')


@request_time
def run(url,thread_num=1,thread_pool=1):
    '''
    :param thread_num: 总共执行的线程数(总的请求数=总共执行的线程数*每个线程循环请求的数量)
    :param thread_pool: 线程池数量
    :param count :单个线程请求数量
    :param url: 请求的域名地址
    '''
    global x,status_code_list
    print("run执行")
    #建立线程池队列，限定最大长度为thread_pool，并建立线程
    pool = MyThreadPool(thread_pool)
    for i in range(thread_num):
        # 从线程池里面拿取thread_num个线程
        t = pool.get_thread()
        #实例化当前线程，指定当前线程执行函数
        obj = t(target=get_count,args=(i,))
        obj.start()
        obj.join()



if __name__ == '__main__':
    count = 10   #单个线程的请求数
    url = 'http://10.0.20.126/VMS2Service.cgi?Cmd=UserLogin'


    start_time = datetime.datetime.now(pytz.timezone('PRC'))
    print(start_time)
    print("开始测试，当前是北京时间：{}".format(start_time.strftime('%Y-%m-%d %H:%M:%S')))


    run(url,1,1)
    request_status()


    end_time = datetime.datetime.now(pytz.timezone('PRC'))
    time_difference = end_time - start_time
    print("执行完毕，当前是北京时间：{},一共耗时：{}秒".format(end_time.strftime('%Y-%m-%d %H:%M:%S'),time_difference.seconds))