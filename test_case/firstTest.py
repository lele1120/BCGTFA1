# -*- coding: UTF-8 -*-
import os
import unittest
import logging
import sys
import time

from appium import webdriver
# from selenium import webdriver
from common.module.testcase_module import TestCasePrint
from common.service import excel_case_facade as ecf
from biz.my_operation import My_Operation as mo
from biz.swipe_operation import Swope_Operation as swo
import inspect

logger = logging.getLogger()
logger.level = logging.INFO
logger.addHandler(logging.StreamHandler(sys.stdout))


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.excel_facade = ecf.GetExcelCaseDate()
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.1',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.bs.finance',
            'appActivity': 'ui.common.WelcomeActivity',

            'unicodeKeyboard': True,
            'resetKeyboard': True,

            # 'automationName': 'uiautomator2',
            "noReset": True
        }
        global driver

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logging.info("*** 启动app *** \n")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        pass
        # driver.quit()
        logging.info("*** 关闭app *** \n")

    def setUp(self):
        time.sleep(3)

    def tearDown(self):
        pass

    # def test_login(self):
    #     """登录状态验证"""
    #
    #     for i in range(3):
    #         swo().swipeLeft(driver, 500)
    #         logging.info("滑动"+str(i+1)+"次屏幕 \n")
    #         time.sleep(1)
    #
    #     mo().my_Click(driver, "xpath", 3)
    #     logging.info("点击立即体验 \n")
    #
    #     mo().my_Click(driver, "id", 4)
    #     logging.info("点击我知道了 \n")
    #
    #     mo().my_Click(driver, "id", 1)
    #     logging.info("*** 点击登录按钮 *** \n")
    #     time.sleep(2)
    #
    #     mo().my_sendkeys(driver, "id", 5, "13911645988")
    #     logging.info("*** 输入手机号 *** \n")
    #
    #     mo().my_Click(driver, "id", 6)
    #     logging.info("*** 点击获取验证码 *** \n")
    #     time.sleep(1)
    #
    #     mo().my_sendkeys(driver, "id", 7, "123456")
    #     logging.info("*** 输入验证码 *** \n")
    #     time.sleep(2)
    #
    #     mo().my_Click(driver, "id", 8)
    #     logging.info("*** 点击立即登录 *** \n")
    #     time.sleep(2)
    #
    #     TouchAction(driver).tap(x=661, y=253).perform()
    #     time.sleep(3)
    #     login_state = driver.find_element_by_id("com.bs.finance:id/tv_user_status").text
    #     print(login_state)
    #     self.assertEqual(login_state, "已登录", "验证是否登录成功")

    def test_bc_01(self):
        """已登录状态下，状态验证"""
        print("img/123.png")
        login_state = driver.find_element_by_id("com.bs.finance:id/tv_user_status").text
        self.assertEqual(login_state, "已登录", "验证是否登录成功")

        logging.info("*** app已登录验证 *** \n")
        # imgPath = os.path.join('/Users/xuchen/PycharmProjects/BCGTFA/test_suite/images', '%s.png' % str(sys._getframe().f_code.co_name))
        # driver.save_screenshot(imgPath)
        # print('img/' +str(sys._getframe().f_code.co_name) + '.png')


    def test_bc_02(self):
        """排行榜按钮点击跳转"""
        mo().my_Click(driver, "id", 9)
        logging.info("*** 排行榜按钮点击 *** \n")
        time.sleep(2)
        product_type_name = ["货币基金", "理财产品", "纯债基金"]

        for i in range(product_type_name.__len__()):
            product_type = driver.find_element_by_id("com.bs.finance:id/tv_title").text
            # self.assertEqual(product_type, product_type_name[i], "产品类型验证")
            TestCasePrint().assertEqual(product_type, product_type_name[i], "产品类型验证")
            logging.info("*** 产品类型为：" + product_type_name[i] + "验证 *** \n")
            if i is not 2:
                swo().swipeLeft(driver, 500)
                time.sleep(2)
            time.sleep(2)
    #
    # def test_bc_03(self):
    #     """排行榜返回icon点击"""
    #     mo().my_Click(driver, "xpath", 10)
    #     time.sleep(2)
    #     login_state = driver.find_element_by_id("com.bs.finance:id/tv_user_status").text
    #     self.assertEqual(login_state, "已登录", "验证从排行榜页面返回首页")
    #     logging.info("*** 返回icon点击 *** \n")
    #     time.sleep(2)
    #
    # def test_bc_04(self):
    #     """排行榜中货币基金导航栏按钮点击跳转"""
    #     mo().my_Click(driver, "id", 9)
    #     logging.info("*** 排行榜按钮点击 *** \n")
    #     time.sleep(2)
    #
    #     qrnh_button_type = driver.find_element_by_id("com.bs.finance:id/line_1").is_displayed()
    #     self.assertTrue(qrnh_button_type)
    #     logging.info("*** 进入排行榜默认选择 七日年化 *** \n")
    #     time.sleep(2)
    #
    #     mo().my_Click(driver, "id", 11)
    #     logging.info("*** 点击万份收益 *** \n")
    #     time.sleep(2)
    #
    #     wfsy_button_type = driver.find_element_by_id("com.bs.finance:id/line_0").is_displayed()
    #     self.assertTrue(wfsy_button_type)
    #     logging.info("*** 万份收益下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 13)
    #     logging.info("*** 点击销量（笔） *** \n")
    #     time.sleep(2)
    #
    #     xl_button_type = driver.find_element_by_id("com.bs.finance:id/line_2").is_displayed()
    #     self.assertTrue(xl_button_type)
    #     logging.info("*** 销量（笔）下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 14)
    #     logging.info("*** 点击关注量 *** \n")
    #     time.sleep(2)
    #
    #     gzl_button_type = driver.find_element_by_id("com.bs.finance:id/line_3").is_displayed()
    #     self.assertTrue(gzl_button_type)
    #     logging.info("*** 关注量下划线显示 *** \n")
    #
    # def test_bc_05(self):
    #     """货币基金右上角搜索图标点击"""
    #     mo().my_Click(driver, "xpath", 15)
    #     time.sleep(2)
    #     product_name_input = driver.find_element_by_id("com.bs.finance:id/et_key").text
    #     self.assertEqual(product_name_input, "请输入产品名称", "页面跳转产品输入框内容")
    #     logging.info("*** 点击货币基金搜索图标 *** \n")
    #
    # def test_bc_06(self):
    #     """输入货币基金产品名称查看搜索结果"""
    #     driver.find_element_by_id("com.bs.finance:id/et_key").send_keys(u"测试产品")
    #     logging.info("*** 输入产品名称为：测试产品 *** \n")
    #
    #     time.sleep(5)
    #     mo().my_Click(driver, "xpath", 16)
    #     logging.info("*** 点击搜索图标 *** \n")
    #
    #     time.sleep(10)
    #     tv_prd_name = driver.find_element_by_id("com.bs.finance:id/tv_prd_name").text
    #     self.assertEqual(tv_prd_name, "测试产品", "搜索货币基金产品查询")
    #     logging.info("*** 对比搜索出的产品名称 *** \n")
    #
    #     mo().my_Click(driver, "xpath", 10)
    #     time.sleep(2)
    #     logging.info("*** 点击返回icon *** \n")
    #
    # def test_bc_07(self):
    #     """排行榜中理财产品导航栏按钮点击跳转"""
    #     mo().my_Click(driver, "id", 9)
    #     logging.info("*** 排行榜按钮点击 *** \n")
    #     time.sleep(2)
    #
    #     swo().swipeLeft(driver, 500)
    #     logging.info("*** 滑动到理财产品 *** \n")
    #
    #     yjnhsy_button_type = driver.find_element_by_id("com.bs.finance:id/line_1").is_displayed()
    #     self.assertTrue(yjnhsy_button_type)
    #     logging.info("*** 进入排行榜理财产品 默认选择预计年化收益 *** \n")
    #     time.sleep(2)
    #
    #     mo().my_Click(driver, "id", 11)
    #     logging.info("*** 点击理财期限 *** \n")
    #     time.sleep(2)
    #
    #     lcsy_button_type = driver.find_element_by_id("com.bs.finance:id/line_0").is_displayed()
    #     self.assertTrue(lcsy_button_type)
    #     logging.info("*** 理财期限下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 13)
    #     logging.info("*** 点击销量（笔） *** \n")
    #     time.sleep(2)
    #
    #     xl_button_type = driver.find_element_by_id("com.bs.finance:id/line_2").is_displayed()
    #     self.assertTrue(xl_button_type)
    #     logging.info("*** 销量（笔）下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 14)
    #     logging.info("*** 点击关注量 *** \n")
    #     time.sleep(2)
    #
    #     gzl_button_type = driver.find_element_by_id("com.bs.finance:id/line_3").is_displayed()
    #     self.assertTrue(gzl_button_type)
    #     logging.info("*** 关注量下划线显示 *** \n")
    #
    # def test_bc_08(self):
    #     """理财产品右上角搜索图标点击"""
    #     mo().my_Click(driver, "xpath", 15)
    #     time.sleep(2)
    #     product_name_input = driver.find_element_by_id("com.bs.finance:id/et_key").text
    #     self.assertEqual(product_name_input, "请输入产品名称", "页面跳转产品输入框内容")
    #     logging.info("*** 点击理财产品搜索图标 *** \n")
    #
    # def test_bc_09(self):
    #     """输入理财产品名称查看搜索结果"""
    #     driver.find_element_by_id("com.bs.finance:id/et_key").send_keys(u"日日盈")
    #     logging.info("*** 输入产品名称为：日日盈 *** \n")
    #     time.sleep(2)
    #
    #     driver.find_element_by_id("com.bs.finance:id/btn_ok").click()
    #     logging.info("*** 点击确定按钮 *** \n")
    #     time.sleep(2)
    #
    #     tv_prd_name = driver.find_element_by_id("com.bs.finance:id/tv_prd_name").text
    #     self.assertEqual(tv_prd_name, "日日盈", "搜索理财产品查询")
    #     logging.info("*** 对比搜索出的产品名称 *** \n")
    #
    #     mo().my_Click(driver, "xpath", 10)
    #     time.sleep(2)
    #     logging.info("*** 点击返回icon *** \n")
    #
    # def test_bc_10(self):
    #     """排行榜中理财产品导航栏按钮点击跳转"""
    #     mo().my_Click(driver, "id", 9)
    #     logging.info("*** 排行榜按钮点击 *** \n")
    #     time.sleep(2)
    #
    #     swo().swipeLeft(driver, 500)
    #     logging.info("*** 滑动到理财产品 *** \n")
    #     time.sleep(2)
    #
    #     swo().swipeLeft(driver, 500)
    #     logging.info("*** 滑动到纯债基金 *** \n")
    #
    #     jsgyzf_button_type = driver.find_element_by_id("com.bs.finance:id/line_1").is_displayed()
    #     self.assertTrue(jsgyzf_button_type)
    #     logging.info("*** 进入排行榜纯债基金 默认选择近三个月涨幅 *** \n")
    #     time.sleep(2)
    #
    #     mo().my_Click(driver, "id", 11)
    #     logging.info("*** 点击累计净值 *** \n")
    #     time.sleep(2)
    #
    #     lcsy_button_type = driver.find_element_by_id("com.bs.finance:id/line_0").is_displayed()
    #     self.assertTrue(lcsy_button_type)
    #     logging.info("*** 累计净值下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 13)
    #     logging.info("*** 点击销量（笔） *** \n")
    #     time.sleep(2)
    #
    #     xl_button_type = driver.find_element_by_id("com.bs.finance:id/line_2").is_displayed()
    #     self.assertTrue(xl_button_type)
    #     logging.info("*** 销量（笔）下划线显示 *** \n")
    #
    #     mo().my_Click(driver, "id", 14)
    #     logging.info("*** 点击关注量 *** \n")
    #     time.sleep(2)
    #
    #     gzl_button_type = driver.find_element_by_id("com.bs.finance:id/line_3").is_displayed()
    #     self.assertTrue(gzl_button_type)
    #     logging.info("*** 关注量下划线显示 *** \n")
    #
    # def test_bc_11(self):
    #     """纯债基金右上角搜索图标点击"""
    #     mo().my_Click(driver, "xpath", 15)
    #     time.sleep(2)
    #     product_name_input = driver.find_element_by_id("com.bs.finance:id/et_key").text
    #     self.assertEqual(product_name_input, "请输入产品名称", "页面跳转产品输入框内容")
    #     logging.info("*** 点击理财产品搜索图标 *** \n")
    #
    # def test_bc_12(self):
    #     """输入纯债基金产品名称查看搜索结果"""
    #     driver.find_element_by_id("com.bs.finance:id/et_key").send_keys(u"财富宝")
    #     logging.info("*** 输入产品名称为：财富宝 *** \n")
    #
    #     time.sleep(5)
    #     mo().my_Click(driver, "xpath", 16)
    #     logging.info("*** 点击搜索图标 *** \n")
    #
    #     time.sleep(10)
    #     tv_prd_name = driver.find_element_by_id("com.bs.finance:id/tv_prd_name").text
    #     self.assertEqual(tv_prd_name, "财富宝", "搜索纯债基金产品查询")
    #     logging.info("*** 对比搜索出的产品名称 *** \n")
    #
    #     mo().my_Click(driver, "xpath", 10)
    #     time.sleep(2)
    #     logging.info("*** 点击返回icon *** \n")
    #
    # def test_bc_13(self):
    #     """点击比收益按钮"""
    #     driver.find_element_by_id("com.bs.finance:id/iv_bsy").click()
    #     logging.info("*** 点击比收益按钮 *** \n")

    # @classmethod
    # def getImage(self,driver):
    #     """
    #     截取图片,并保存在images文件夹
    #     :return: 无
    #     """
    #
    #
    #     print('screenshot:', timestrmap, '.png')


if __name__ == '__main__':
    unittest.main()
