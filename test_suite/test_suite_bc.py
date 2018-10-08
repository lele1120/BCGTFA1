# -*- coding:UTF-8 -*-

import os
import sys
sys.path.append('/Users/xuchen/venv/bin')
sys.path.append('/Users/xuchen/PycharmProjects/BCGTFA/')
sys.path.append('/Users/xuchen/PycharmProjects/BCGTFA/test_case')
# sys.path.append('/Users/xuchen/venv/BCGTFA/bin/beautifulsoup4-4.6.3.dist-info')
os.chdir(sys.path[0])
# 312321321321
# from test_case import firstTest
from test_case.firstTest import MyTestCase

from common.service import suiteReporter_facade

from bs4 import BeautifulSoup

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr

sys.path.append('/Users/xuchen/venv/BCGTFA/lib/python3.7/site-packages')
sys.path.append('/Users/xuchen/PycharmProjects/BCGTFA')
sys.path.append('../')
sys.path.append('../..')

# 先定义署名格式化函数
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


business = suiteReporter_facade.SuiteReporter_Utils()
"""
    添加测试套件说明
    1.引入被测模块
    2.运行被测模块并生成报告
    所需参数说明：
    test_module:被测模块（也就是第一步引入的模块）
    report_file_name:测试报告的名字
    title:报告标题
    description:报告描述
"""

'''引入被测模块'''
test_module = [MyTestCase()]

'''运行测试套件并生成报告'''
business.run_and_report(
    test_module=test_module,
    report_file_name="bc_gui_andorid",
    title=u"BICAI_GUI_FOR_ANDROID",
    description=u"autotest_gui_android")

# 发送人
sender = '357072695@qq.com'
pwd = 'eqaykvvzbsoebjdc'
# receiver='xuchen@bicai365.com'
# 接收人
receiver= ['357072695@qq.com', 'xuchen@bicai365.com']

# 格式化的署名和接收人信息
message = MIMEMultipart()
# message['From'] = _format_addr('这是xx<%s>'%sender)
message['From'] = _format_addr(sender)
message['To'] = _format_addr(receiver)
message['Subject'] = ('BICAI_GUI_FOR_ANDROID_REPORT')

# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>"""

dir_list = os.listdir(r'../report')
dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(r'../report', x)))
url = r'../report/' + dir_list[-1]
htmlfile = open(url, 'r')  #以只读的方式打开本地html文件
htmlpage = htmlfile.read()

soup = BeautifulSoup(htmlpage, "html.parser")  #实例化一个BeautifulSoup对象

message.attach(MIMEText('<html><body>'
                        +'<h1>比财安卓UI自动化报告</h1>'
                        +str(htmlpage)
                        +'<p>请您注意查收附件'
                        +'</body></html>', 'html', 'utf-8'))

# 根据report文件夹内报告创建时间取最新创建报告作为附件

att1 = MIMEText(open(r'../report/' + dir_list[-1], 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="bc_gui_andorid.html"'
message.attach(att1)


# 发送邮件！

try:
    smtpobj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpobj.login(sender, pwd)
    smtpobj.sendmail(sender, receiver, message.as_string())
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，Case:%s' % e)
