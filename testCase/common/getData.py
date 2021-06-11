import requests
from common.data_config import *
from common.operationExcel import OperationExcel
from common.data_config import PresetGlobalValue
from common.utils import Utils
from xlutils.copy import copy
import xlrd
import base64

class GetData():
    # 初始化
    def __init__(self,need_excel):
        self.opExcel = OperationExcel(need_excel, 0)
        self.prefix_url = "http://10.0.20.126/VMS2Service.cgi?Cmd="

    def get_case_lines(self):
        """
        获取测试用例条数
        :return:
        """
        row = get_test_lines_row()
        col = get_test_lines_col()
        lines = int(self.opExcel.get_cell_value(row,col))
        return lines

    def get_request_url(self):
        """
        获取请求地址url（拼接接口）
        :param row:
        :return:
        """
        row = get_request_url_row()
        col = get_request_url_col()
        request_url = self.prefix_url+self.opExcel.get_cell_value(row,col)
        return request_url

    def get_request_method(self):
        """
        获取接口请求类型
        :param row:
        :return:
        """
        method_row = get_request_method_row()
        method_col = get_request_method_col()
        request_method =self.opExcel.get_cell_value(method_row,method_col)
        return request_method

    def get_requests_id(self,row):
        """
        获取测试id
        :param row:
        :return:
        """
        col = getTestIdcol()
        id = self.opExcel.get_cell_value(row,col)
        return str(int(id))

    def get_request_data(self,row):
        """
        获取接口的请求参数,传往后端的data
        :param row:
        :return:
        """
        fields_col = get_fields()#获取首个参数列表的col值
        data_dict = {}
        i = 0
        #向右读取参数字段，循环追加参数列表到request_data中，直至参数字段为空
        while self.opExcel.get_cell_value(row-1, fields_col) != "":
            i = i+1
            key_value = self.opExcel.get_cell_value(row-1, fields_col) #键
            data_value = self.opExcel.get_cell_value(row, fields_col) #值

            #如果值是float型,先转换为int再转换为str
            if isinstance(data_value,float):
                data_value = str(int(data_value))
            else:
                data_value = data_value
            field = {str(key_value):data_value}
            data_dict.update(field)#追加参数进入字典request_data
            fields_col = fields_col + 1


        #dict_tem = {"accountInfo":data_dict}

        user = (data_dict['userID'],data_dict['username'],data_dict['password'],data_dict['functionalRoleList'],data_dict['resourceRoleList'])
        tem = '{"accountInfo":{"userID":"%s","username":"%s","password":"%s",' \
              '"functionalRoleList":"%s","resourceRoleList":"%s"}}' % user

        return tem

    def get_expected_code(self,row):
        """
        获取预期结果stateCode
        :param row:
        :return:
        """
        col = getExpectedResultcol()
        expected_state_code = self.opExcel.get_cell_value(row,col)
        return int(expected_state_code)


    def write_actual_value(self,row,value):
        """
        写入实际结果
        :param row:
        :param value:
        :return:
        """
        col = getActualResultcol()
        work_book = xlrd.open_workbook(self.opExcel.file_name,formatting_info=True)

        #先通过xlutils.copy下copy复制Excel
        write_to_work = copy(work_book)

        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(self.opExcel.sheet_id)

        # 去掉已经有数据的行，在其后进行追加
        lines = self.opExcel.tables.nrows
        row = row + lines

        sheet_data.write(row,col,str(value))
        # 这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(self.opExcel.file_name)


    def write_test_info(self,row,col,value):
        """
        写入测试info信息
        :param row:
        :param col:
        :param value:
        :return:
        """
        work_book = xlrd.open_workbook(self.opExcel.file_name,formatting_info=True)
        write_to_work = copy(work_book)
        sheet_data = write_to_work.get_sheet(self.opExcel.sheet_id)
        lines = self.opExcel.tables.nrows
        row = row + lines
        sheet_data.write(row,col,str(value))
        write_to_work.save(self.opExcel.file_name)



    def write_test_res(self,row,value):
        """
        写入测试结果
        :param row:
        :param value:
        :return:
        """
        col = getTestResultcol()
        work_book = xlrd.open_workbook(self.opExcel.file_name,formatting_info=True)
        write_to_work = copy(work_book)
        sheet_data = write_to_work.get_sheet(self.opExcel.sheet_id)
        lines = self.opExcel.tables.nrows
        row = row + lines
        sheet_data.write(row,col,str(value))
        write_to_work.save(self.opExcel.file_name)




if __name__=="__main__":
    op = GetData()
    op.write_test_res()

