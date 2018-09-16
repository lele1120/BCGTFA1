import os

from bs4 import BeautifulSoup

dir_list = os.listdir(r'../report')
dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(r'../report', x)))

url = r'../report/' + dir_list[-1]

htmlfile = open(url, 'r')  #以只读的方式打开本地html文件
htmlpage = htmlfile.read()
print(htmlpage)
print('**********************')
soup = BeautifulSoup(htmlpage, "html.parser")  #实例化一个BeautifulSoup对象
print(soup.title.string)
print(soup('p')[0])
print("\n")
print(soup('p')[1])
print("\n")
print(soup('p')[2])
