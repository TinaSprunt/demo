#预设所有数据参数

class PresetGlobalValue():

    """
    标注在excel中的参数列
    """
    #参数读入excel
    test_name_col=1 #测试名称列
    test_name_row=0 #测试名称行

    request_url_col = 1 #请求地址列
    request_url_row = 1 #请求地址行

    request_method_col = 1 #请求方法 post get
    request_method_row = 2 #请求方法 post get

    test_lines_col = 1  #测试条数列
    test_lines_row = 3  #测试条数行

    fields = 3 #首个参数字段
    expected_state_code = 2 #预期结果列号
    test_id_col=1 #测试编号列


    #参数写入excel

    request_header = 4 #请求头列号
    actual_res = 6 #实际结果列号
    test_res = 7 #测试结果列号






def get_test_name_col():
    """
    获取测试名称的列号
    :return:
    """
    return PresetGlobalValue.test_name_col

def get_test_name_row():
    """
    获取测试名称的行号
    :return:
    """
    return PresetGlobalValue.test_name_row

def get_request_url_col():
    """
    获取请求接口的列号
    :return:
    """
    return PresetGlobalValue.request_method_col

def get_request_url_row():
    """
    获取请求接口的行号
    :return:
    """
    return PresetGlobalValue.request_url_row


def get_request_method_col():
    """
    获取请求方法的列号
    :return:
    """
    return PresetGlobalValue.request_method_col

def get_request_method_row():
    """
    获取请求方法的行号
    :return:
    """
    return PresetGlobalValue.request_method_row

def get_test_lines_col():
    """
    获取测试条数列号
    :return:
    """
    return PresetGlobalValue.test_lines_col

def get_test_lines_row():
    """
    获取测试条数行号
    :return:
    """
    return PresetGlobalValue.test_lines_row


def getTestIdcol():
    """
    获取测试编号的列号
    :return:
    """
    return PresetGlobalValue.test_id_col


def getRequestHeadercol():
    """
    获取请求头的列号
    :return:
    """
    return PresetGlobalValue.request_header




def getExpectedResultcol():
    """
    获取预期结果的列号
    :return:
    """
    return PresetGlobalValue.expected_state_code

def getActualResultcol():
    """
    获取实际结果的列号
    :return:
    """
    return PresetGlobalValue.actual_res

def getTestResultcol():
    """
    测试结果的列号
    :return:
    """
    return PresetGlobalValue.test_res

def get_headers():
    return headers

def get_fields():
    """
    获取首个参数列号
    :return:
    """
    return PresetGlobalValue.fields



#头部字典封装
headers={
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-CN',
   'Authorization': 'Basic YWRtaW46MTIzNDU2', # admin:123456
   'Cache-Control': 'no-cache',
   'Connection': 'Keep-Alive',
   'Content-Length': '0',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Host': '10.0.20.126',
   'Referer': 'http://10.0.20.126/',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

headers2 = {
    "Host": "10.0.20.126",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Auth-Token": "1567485039",
    "Content-Length":"121",
    "Connection": "keep-alive",
    "Referer": "http://10.0.20.126/"
}
