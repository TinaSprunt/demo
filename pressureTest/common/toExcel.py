from common.getData import GetData
from common.utils import Utils


class ToExcel():

    def __init__(self,input_name):
        self.input_data = GetData(input_name)  # 打开当前的读入excel
        self.write_data = GetData(r"D:\PycharmProjects\demo2\report\test_result.xls") #打开写入的excel


    def write_msg_info(self,i,id,headers):
        """
        写入info
        :param i:
        :param id:
        :param headers:
        :return:
        """
        self.write_data.write_test_info(i - 5, 0, id)  # 写入测试id
        self.write_data.write_test_info(i - 5, 1, self.input_data.opExcel.get_cell_value(0, 1))  # 写入测试名称
        self.write_data.write_test_info(i - 5, 2, self.input_data.opExcel.get_cell_value(1, 1))  # 写入测试接口
        self.write_data.write_test_info(i - 5, 3, self.input_data.opExcel.get_cell_value(2, 1))  # 写入测试请求方法
        self.write_data.write_test_info(i - 5, 4, headers)  # 写入测试请求头
        self.write_data.write_test_info(i - 5, 5, self.input_data.opExcel.get_cell_value(i, 0))  # 写入测试备注


