"""
    面向过程
"""
list_name = ["台湾省", "香港", "内蒙古"]

# 1. 读取列表全部元素
# for ... 列表
for item in list_name:
    if len(item) == 3:
        print(item)

# 2. 修改列表全部元素
# for ... range
for i in range(len(list_name)):
    if len(list_name[i]) == 2:
        list_name[i] = ""

# 练一练：所有治愈人数增加1
# 1:for i
# 2:for item
# 读取列表元素,修改字典键值对
list_epidemics = [
    {
        "region": "台湾", "now": 4523061,
        "total": 4545636, "cure": 13742,
    },
    {
        "region": "香港", "now": 277529,
        "total": 354454, "cure": 67427,
    },
    {
        "region": "内蒙古", "now": 2,
        "total": 2166, "cure": 2163,
    },
]
for item in list_epidemics:
    item["cure"] += 1
# for i in range(len(list_epidemics)):
#     list_epidemics[i]["cure"] += 1





# 3.函数嵌套调用
def condition_by_region(epidemic):
    return epidemic["region"] == "香港" # 4

def get_epidemics():
    for item in list_epidemics: # 2
        if condition_by_region(item): # 3
            return item

result = get_epidemics() # 1
print(result)
