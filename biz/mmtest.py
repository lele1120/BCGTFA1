# coding=utf-8
import re
import time

from appium import webdriver
# from pytesser3 import *
import pytesseract
from PIL import Image

from biz.picture_operation import IMG

pytesseract.pytesseract.tesseract_cmd='/usr/local/Cellar/tesseract/3.05.02/bin/tesseract'
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.bs.finance',
    'appActivity': 'ui.common.WelcomeActivity',
    'automationName': 'Uiautomator2',
    "noReset": True
}
# command1 ='adb shell ime set io.appium.android.ime/.UnicodeIME'
# os.system(command1)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(20)
el1 = driver.find_element_by_id("com.bs.finance:id/iv_user")
el1.click()
time.sleep(2)
el3 = driver.find_element_by_id("com.bs.finance:id/et_phone")
el3.send_keys("13911645993")
time.sleep(2)
el2 = driver.find_element_by_id("com.bs.finance:id/get_msg_code")
el2.click()
time.sleep(5)
tamp = 'yzm'
filename = '%s.png' % tamp
driver.get_screenshot_as_file(filename)
box = (415, 415, 590, 478)
image = Image.open(filename)
newImage = image.crop(box)
newImage.save(filename)
im = Image.open(filename)
im = im.convert('P')

print("----------")

time.sleep(1)

I = IMG()

# 验证码图片处理
I._processImg(I.codeImg)
time.sleep(1)

# 去除干扰线
I.pIx()
time.sleep(1)
I = IMG()

# 验证码图片处理
I._processImg(I.codeImg)
time.sleep(1)

# 去除干扰线
I.pIx()
time.sleep(3)

# 获取验证码
codes = I.Pytess('test.png')
print(codes)
print("---------------")
print(re.findall(r"\d+\.?\d*", codes))


