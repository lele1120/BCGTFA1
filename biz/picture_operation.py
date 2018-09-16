# -*- coding:utf-8 -*-
import os
import re
import time

import pytesseract
from pytesser3 import *
from urllib3.connectionpool import xrange

webSite = ''
webUser = ''
webPass = ''

CodesImg = os.path.join(os.getcwd(), 'codes.png')


class IMG(object):

    def __init__(self):
        self.codeImg = 'yzm.png'
        self.iMg = self._openImg(self.codeImg)
        self.Im = self._openImg(self.codeImg.capitalize())
        self.w, self.h = self.Im.size
        self.cookies = ''

    def _openImg(self, name):
        try:
            im = Image.open(name)
            return im
        except:
            print
            '[!] Open %s failed' % name
            exit()

    def _processImg(self, name):
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img = self._openImg(name)
        imgry = img.convert('L')
        out = imgry.point(table, '1')
        filename = self.codeImg.capitalize()
        out.save(filename)

    def pIx(self):
        data = self.Im
        w = self.w
        h = self.h
        try:
            for x in xrange(1, w - 1):
                if x > 1 and x != w - 2:
                    left = x - 1
                    right = x + 1

                for y in xrange(1, h - 1):
                    up = y - 1
                    down = y + 1

                    if x <= 2 or x >= (w - 2):
                        data.putpixel((x, y), 255)

                    elif y <= 2 or y >= (h - 2):
                        data.putpixel((x, y), 255)

                    elif data.getpixel((x, y)) == 0:
                        if y > 1 and y != h - 1:
                            up_color = data.getpixel((x, up))
                            down_color = data.getpixel((x, down))
                            left_color = data.getpixel((left, y))
                            left_down_color = data.getpixel((left, down))
                            right_color = data.getpixel((right, y))
                            right_up_color = data.getpixel((right, up))
                            right_down_color = data.getpixel((right, down))

                            if down_color == 0:
                                if left_color == 255 and left_down_color == 255 and \
                                        right_color == 255 and right_down_color == 255:
                                    data.putpixel((x, y), 255)
                                    data.save("text2.png", "png")

                            elif right_color == 0:
                                if down_color == 255 and right_down_color == 255 and \
                                        up_color == 255 and right_up_color == 255:
                                    data.putpixel((x, y), 255)
                                    data.save("text3.png", "png")

                        if left_color == 255 and right_color == 255 \
                                and up_color == 255 and down_color == 255:
                            data.putpixel((x, y), 255)
                    else:
                        pass
                    data.save("test.png", "png")
        except:
            return False

    def Pytess(self, name):
        threshold = 140
        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        rep = {'O': '0',
               'I': '1',
               'L': '1',
               'Z': '2',
               'S': '8',
               'Q': '0',
               '}': '7',
               '*': '',
               'E': '6',
               ']': '0',
               '`': '',
               'B': '8',
               '\\': '',
               ' ': ''
               }

        data = self._openImg(name)
        imgry = data.convert('L')
        out = imgry.point(table, '1')
        try:
            # text = image_to_string(out)
            text = pytesseract.image_to_string(out)
            text = text.strip()
            text = text.upper()
        except:
            text = 0

        for r in rep:
            text = text.replace(r, rep[r])

        return text


if __name__ == '__main__':
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
        codes = I.Pytess('yzm.png')
        print(codes)
        print("---------------")
        print(re.findall(r"\d+\.?\d*", codes))

