# -*- coding: UTF-8 -*-
import os
import sys
from common.module import excel_module
sys.path.append("..")


class GetExcelCaseDate:
    """
    初始化获取excelData
    1、获取对应id的行的内容
    2、获取url
    3、获取请求方式
    4、获取请求参数，并进行转码
    5、获取预期结果
    6、将预期结果转换为字典
    7、设置headers
    8、获取response
    9、获取字典格式的response
    :param file_name: 测试数据的文件名
    :param sheet_index: sheet表的索引
    :param id: caseId
    :return:
    """

    def __init__(self):
        self.url = ''
        self.method = ''
        self.data_res = ''
        self.exp_resp = ''
        self.data = ''

    # def get_case_data(self, file_name, sheet_index=0, row_id=0, data=None, **kwargs):
    #     """
    #     1、获取对应id的行的内容
    #     2、获取url
    #     3、获取请求方式
    #     4、获取请求参数，并进行转码
    #     5、获取预期结果
    #     8、获取string类型response
    #     :param file_name: 测试数据的文件名
    #     :param sheet_index: sheet表的索引
    #     :param id: caseId
    #     :return:exp_resp_dic,act_resp_dic
    #     """
    #     excel_handle = excel_module.Read_Excel(file_name)
    #     sheet = excel_handle.get_sheet_by_index(sheet_index)
    #     case_data_list = excel_handle.get_row_values(sheet, row_id)
    #     path = case_data_list[1]
    #     self.method = case_data_list[2]
    #     self.data_res = case_data_list[3]
    #     self.exp_resp = case_data_list[4]

    def get_case_data(self, method_name, row_id=0):
        file_name = os.path.abspath('../data/bc_gui.xlsx')
        # print(os.path.abspath('../data'))
        excel_handle = excel_module.Read_Excel(file_name)
        sheet_index = excel_handle.get_sheet_by_index(0)
        if method_name == "id":
            return excel_handle.get_cell_value(sheet_index, row_id, 1)
        elif method_name == "name":
            return excel_handle.get_cell_value(sheet_index, row_id, 2)
        elif method_name == "xpath":
            return excel_handle.get_cell_value(sheet_index, row_id, 3)


if __name__ == '__main__':
    GetExcelCaseDate().get_case_data(method_name="id", row_id=1)
