# @Project   : Python
# @File      : http����.py
# @Auther    : �ȵ���Ҷ���
# @Time      : 2022/6/27, 11:30
#

'''
    http������Ӧ����
'''

from socket import *

# httpʹ��tcp����
s = socket()
s.bind(('0.0.0.0',8000))

s.listen(3)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

c.close()
s.close()
















































