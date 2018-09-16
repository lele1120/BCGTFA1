# -*- coding: UTF-8 -*-
import glob
import os
import subprocess
import time

from common.service.excel_case_facade import GetExcelCaseDate


class My_Operation:

    def my_Click(self, driver, method_name, row_id):
        """点击操作封装"""
        if method_name == "id":
            eid = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_id(eid).click()
            time.sleep(1)
        elif method_name == "name":
            ename = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_name(ename).click()
            time.sleep(1)
        elif method_name == "xpath":
            expath = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_xpath(expath).click()
            time.sleep(1)
        else:
            print("获取控件错误！！！！！")

    def my_sendkeys(self, driver, method_name, row_id, value):
        """输入操作封装"""
        if method_name == "id":
            eid = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_id(eid).send_keys(value)
        elif method_name == "name":
            ename = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_name(ename).send_keys(value)
        elif method_name == "xpath":
            expath = GetExcelCaseDate().get_case_data(method_name, row_id)
            driver.find_element_by_xpath(expath).send_keys(value)
        else:
            print("获取控件错误！！！ ！！")

    def fast_input(str, element):
        """快速输入"""
        x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
        element.click()
        time.sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s' % (x, str), shell=True)
        time.sleep(0.5)




if __name__ == '__main__':
    My_Operation().get_file_list(r'/Users/xuchen/PycharmProjects/BCGTFA/report')




