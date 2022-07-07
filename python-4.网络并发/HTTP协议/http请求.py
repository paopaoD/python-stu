# @Project   : Python
# @File      : http请求.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/27, 11:30
#

'''
    http请求响应测试
'''

from socket import *

# http使用tcp传输
s = socket()
s.bind(('0.0.0.0',8000))

s.listen(3)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

c.close()
s.close()
















































