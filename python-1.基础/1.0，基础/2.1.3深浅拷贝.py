# @Project   : Python
# @File      : 2.1.3深浅拷贝.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/22, 16:05
#

print("--------------------列表内存图----------------------")

'''
列表：
    列表内存图
'''

list01 = ["张无忌","赵敏"]
list02 = list01
# 修改的是列表第一个元素
list01[0] = "无忌"
print(list02[0])    # 无忌


list01 = ["张无忌","赵敏"]
list02 = list01
# list01 重新赋值了
list01 = ["无忌"]
print(list02[0])    # 张无忌


list01 = [800,1000]
# 通过切片，生成了一个新列表
list02 = list01[:]
list01[0] = [900]
print(list02[0])  # 800
list01 = [500]
print(list02[0])  # 800


list01 = [800,[1000,500]]
list02 = list01
list01[1][0] = 900
print(list02[1][0])  # 900
print(list02)       # [800,[900,500]]



list01 = [800,[1000,500]]
# 浅拷贝
# list02 = list01[:]      # 只复制一层  不会复制深层变量绑定的变量
list02 = list01.copy()      # [800,[1000,500]]

list01[1][0] = 900      # [800,[900,500]]
print(list02[1][0])  #





print("-------------------- copy ----------------------")
import copy

list01 = [800,[1000,500]]
# 深拷贝
# 生成一个新列表 list02 = [800,[1000,500]]  和list01是两个列表，互不相关了
list02 = copy.deepcopy(list01)
list01[1][0] = 900      # list01 = [800,[900,500]]
# list02列表内的值并没有改变
print(list02[1][0])  # 1000



# 练习1：
#       将列表[54,25,12,42,35,17]中，大于30的数字存入另一个列表
#


old_list = [54,25,12,42,35,17]
new_list = []
for item in old_list:
    if item > 30:
        new_list.append(item)
print(new_list)


# 练习2：
#       在控制台中录入5个数字，并打印最大值（不使用max），
#
'''
max_value = 0
for item in range(5):
    nums = int(input(f"请输入第{item+1}个数字:"))
    if max_value < nums:
        max_value = nums
print(max_value)
'''

# 练习3：
#       在列表中[54,25,12,42,35,17]，选出最大值（不使用max），
#
list01 = [54,25,12,42,35,17]

max_value = list01[0]
for item in list01:
    if max_value < item:
        max_value = item
print(max_value)


# 或者：
list02 = [54,25,12,42,35,100,17]
# 假设第一个是最大的
max_value = list02[0]
# 与后面（索引1开始）元素进行比较
for i in range(1,len(list02)):
    if max_value < list02[i]:
        # 如果发现更大的，则替换之前假设的
        max_value = list02[i]
print(max_value)


# 练习4：
#      在列表中[9,25,12,8],删除大于10的数字

list01 = [9,25,12,8]

for item in list01:
    if item > 10:
        # 删除元素： 删除一个元素后，后一个替换前一个
        list01.remove(item)
print(list01)       # [9, 12, 8]   出现错误

####  删除元素，后一个替换前一个

# 倒着删除
#       按索引
for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)


for i in range(-1,-len(list01),-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)



































