'''
    线程  t = Thread()
        功能：创建线程对象
        参数：target   绑定线程函数
             args     元组 给线程函数位置传参
             kwargs   字典 给线程函数键值传参
'''
import os
from threading import Thread

from time import sleep

### 单线程
# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：黄河大合唱")

# 创建线程对象
t = Thread(target=music)

# 启动线程
t.start()

# 回收线程
t.join()




### 多线程
# 线程函数1
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：黄河大合唱")

# 创建线程对象
t = Thread(target=music)

# 启动线程
t.start()

# 线程函数2
for i in range(4):  # 多线程  和第一个线程可以同时进行 互不影响
    sleep(1)
    print(os.getpid(),"播放：葫芦娃")


# 回收线程
t.join()