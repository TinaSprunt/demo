import requests
from common.dataConfig import *
from common.operationExcel import OperationExcel
from xlutils.copy import copy
import xlrd
import base64
import uuid

class GetData():

    # 初始化
    def __init__(self,):
        pass


    def get_register_date(self,num):
        """
        用户注册data
        :param i:
        :return:
        """
        pressure_data = []
        for i in range(num):
            data = {
                'userID':1000+i,
                'username':'meimei'+str(i),
                'password':'123456',
                'functionalRoleList':'',
                'resourceRoleList':''
            }
            pressure_data.append(data)
        print(pressure_data)
        return pressure_data




if __name__=="__main__":
    op = GetData()


