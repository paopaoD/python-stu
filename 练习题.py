


# 2 按字典中value值排序
dict01 = {"a": 11, "b": 33, "q": 44, "w": 5, "s": 28}

result = sorted(dict01.items(), key=lambda key: key[1])
print(result)



# 递归函数
def factorial(num):
    result =  1
    for i in range(2,num + 1):
        result *= i
    return result


def fact(num):
    if num ==1:
        return 1
    else:
        return num * fact(num - 1 )

re = fact(5)
print(re)


# 打印斐波那契数列第101项
# 第一：
a = 0
b = 1
count = 1
while True:
    c = a+b
    count += 1
    if count == 101:
        break
    a = b
    b = c
print(count,c)

# 第二种：迭代方式编写斐波那契数列
def fact1(n):
    f1 = f2 = 1
    for i in range(n-2):
        f1,f2 = f2,f1+f2
    print(f2)

fact1(9)

# 第三种：递归函数编写斐波那契数列
def f(n):
    f1 = f2 = 1
    if n <= 2:
        return 1
    return f(n-2)+f(n-1)


print(f(5))


print("-------------水仙花数-----------------")
# 1000以内的水仙花数
temp = []
for i in range(100,1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        temp.append(i)
print(temp)




# 手写装饰器
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        # run_time = end_time - start_time
        print(f"运行了{end_time - start_time}秒。")
    return deco

@timer
def time_test():
    time.sleep(2)
    print("执行了")

time_test()



# 冒泡排序
list1 = [5,8,6,66,7,1,24,53]
for i in range(len(list1)-1):
    for c in range(i+1,len(list1)):
        if list1[i] > list1[c]:
            list1[i],list1[c] = list1[c],list1[i]
print(list1)



# 杨辉三角
num = 6
l = []
for i in range(num):
    cur = [1]
    if i != 0:
        for j in range(i-1):
            cur.append(l[j]+l[j+1])
        cur.append(1)
    # print(cur)
    l = cur
print(l)




# 菱形
n = 7
l = n // 2
for i in range(-l,l+1):
    print(abs(i) * " ",end="" + (n-2*abs(i))*"*")
    print()



# 99乘法表
for i in range(1,10):
    for n in range(1,i+1):
        print(n,"*",i,"=",i*n,end="\t")
    print()


# 猴子吃桃
peach = 1   # 第10天剩余的1个，其实第九天已经剩下1个了
for i in range(9):     # 计数9天
    peach = 2 * (peach+1)
print(peach)



# 修改一处
# 修改第二处
