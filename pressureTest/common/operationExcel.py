#操作Excel

import xlrd



class OperationExcel():
    def __init__(self,file_name = None,sheet_id = None):
        """
        接收excel文件名，以及sheet数，如果没有就新建
        :param file_name:
        :param sheet_id:
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            #根据接口名创建例如UserLoginResult的xls文件
            self.file_name = "D://PycharmProjects//demo2//report//test_result.xls"
            self.sheet_id = 0
        self.tables = self.get_tables()






    def get_tables(self):
        """
        返回sheet对象table
        :return:
        """
        excel = xlrd.open_workbook(self.file_name) #获得该名称的excel对象
        table = excel.sheet_by_index(self.sheet_id)#获得该excel对象的sheet_id获取sheet对象
        return table



    def get_table_row(self):
        """
        获取table的行数
        :return:
        """
        return self.tables.nrows

    def get_table_col(self):
        """
        获取table的列数
        :return:
        """
        return self.tables.ncols

    def get_data_by_row(self,row):
        """
        根据行号返回该行值，限定传入行号不小于0，也不大于table最大行号
        :param row:
        :return:
        """
        if row < 0:
            row = 0;
        if row > self.get_table_row():
            row = self.get_table_row()
        data = self.tables.row_values(row)
        return data


    def get_data_by_col(self,col):
        """
        根据列号返回该列值
        :param col:
        :return:
        """
        if col<0:
            col=0
        if col>self.get_table_col():
            col=self.get_table_col()
        data = self.tables.col_values(col)
        return data

    def get_cell_value(self,row,col):
        """
        返回指定单元格的值
        :param row:
        :param col:
        :return:
        """
        if row < 0:
            row = 0;
        if row > self.get_table_row():
            row = self.get_table_row()
        if col<0:
            col=0
        if col>self.get_table_col():
            col=self.get_table_col()
        data = self.tables.cell_value(row,col)
        return data








