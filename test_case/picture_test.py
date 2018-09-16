import string
from lib2to3.pgen2.grammar import line

import pytesseract
from pytesser3 import *
from urllib3.connectionpool import xrange

from biz.picture_operation import IMG

im = Image.open('yzm.png')
im = im.convert('P')
w, h = im.size
I = IMG()
# 验证码图片处理
I._processImg(I.codeImg)
# 去除干扰线
I.pIx()
text = I.Pytess('yzm.png')
# # data = im.capitalize()
# table = []
# for i in range(256):
#     if i < 140:
#         table.append(0)
#     else:
#         table.append(1)
# binaryImage = im.point(table, '1')
# binaryImage.show()
# my_text = pytesseract.image_to_string(binaryImage, config='-psm 6')
for char in string.punctuation:
    text = text.replace(char, '')
print(text)




