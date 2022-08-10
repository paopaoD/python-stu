
# 1 获取字典中的key
dict01 = {"a":"AA","b":"BB","c":{"q":"QQ","w":"WW","p":{"v":"TT"}}}

for key in dict01:
    print(key)
    if type(dict01[key]) == dict:
        for key02 in dict01[key]:
            print(key02)
            if type(dict01[key][key02]) == dict:
                for key03 in dict01[key][key02]:
                    print(key03)

# 2 按字典中value值排序
dict01 = {"a":11,"b":33,"q":44,"w":5,}

# 1) lamabda表达式
print(sorted(dict01.items(),key=lambda k:k[1]))

# 2)
for item in dict01.items():
    print(item)

print(sorted(dict01.items(),key=lambda item:item[1]))


# 3)按key值排序
print(sorted(dict01.items(),key=lambda item:item[0]))

# 4) zip
dict = {'a': 1, 'b': 4, 'c': 2, 'd': 12}

a = zip(dict.keys(), dict.values())
print(a)
b = sorted(a)
print(b)

print(dict.items())
lsit01 = list(dict.items())
print(lsit01)


# 3 列表数组去重方法：

list01 = [1,2,3,4,5,6,6,5,4,3,2,1]

# 1
d = {}
new_d = d.fromkeys(list01)
print(new_d)
obj = new_d.keys()
print(obj)
new_l = list(obj)
print(new_l)
# new_l是去重之后的列表

# 2
l = list(set(list01))
print(l)

# 3
new_l = []
for i in list01:
    if i not in new_l:
        new_l.append(i)
print(new_l)



# 字典和json的区别
a = {'a': '1','b': '2','c': '3'}
print(type(a))

import json

aa = json.loads('{"age": "12"}')  # 参数是str行，loads之后，变成dict字典了
print(aa)
print(type(aa))

# 99乘法表
for i in range(1,10):
    for n in range(1,i+1):
        print(n,"*",i,"=",i*n,end="\t")
    print()


# 菱形
for i in range(-3,4):
    print(abs(i) * " ",end="" +(7-2*abs(i)) * '*')
    print()


s = 'python'
print(s[::-1])
# 方法2、使用reverse()方法：
l = list(s)
re = l.reverse()
print(re)
print(''.join(l))


'''  # 14，打印100内的斐波那契数列  '''
a = 0
b = 1

while b<100:
    print(b)
    a,b = b,a+b


'''  # 14，打印斐波那契数列第101项  '''
a = 0
b = 1
count = 1
while True:
    c = a+b
    count += 1
    print(count,c)
    if count == 101:
        break
    a = b
    b = c


# 杨辉三角
n = 6
t = [[1],[1,1]]
for i in range(2,n):
    cur = [1]
    tem = t[i-1]
    for j in range(i-1):
        cur.append(tem[j]+tem[j+1])
    cur.append(1)
    t.append(cur)
print(t)

# 2
n = 6
t = []
for i in range(n):
    cur = [1]
    if i != 0:
        for j in range(i-1):
            cur.append(t[j]+t[j+1])
        cur.append(1)
    print(cur)
    t = cur


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
bubble_sort(l)
print(l)


for i in range(len(l)-1):
    for n in range(i+1,len(l)-1):
        if l[i] > l[n]:
            l[i],l[n] = l[n],l[i]
print(l)




# 手写装饰器
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("running time is %s "%(stop_time-start_time))
    return deco

@timer
def time_test():
    time.sleep(1)
    print("in the test 1")


time_test()




print("************")
def extendList(val,list=[]):
    list.append(val)
    return list

l01 = extendList(10)
l02 = extendList(2,[])
l03 = extendList("a")

print(l01)
print(l02)
print(l03)
# print("list1=%s"%list01)




# # num = int(input("a:"))
# l = len(str(num))
# w = 10**(l-1)
#
# for i in range(1,l+1):
#     a = num // w
#     num = num % w
#     print(a,num)
#     w = w //10
#
# # a = int(input('num= '))
# count = len(str(a))     # 输入的数字的位数
# w = 10**count
# for i in range(count):
#     x = a // w    # 如果输入的数字是5位，循环第一次，得出万位数字，循环第二次，得出千位数字......
#     a = a % w     # 循环第一次，得出后面几位余数
#     print(x,a)
#     w = w//10


# 水仙花数
temp = []
for i in range(100,1000):
    a = i //100
    b = i//10 % 10
    c = i %10
    if a**3+b**3+c**3 == i:
        temp.append(i)
print(temp)


a = input("num=")
b = []
for i in range(len(a)):
    x = (int(a[i])+3)%9
    b.append(x)
b[0], b[2] = b[2], b[0]
b[1], b[3] = b[3], b[1]

for i in b:
    print(i,end='')