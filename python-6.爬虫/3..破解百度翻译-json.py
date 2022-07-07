# @Project   : Python
# @File      : 3..破解百度翻译-json.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 9:40
#
import json

import requests

if __name__ == "__main__":
    # 1 指定url
    post_url = "https://fanyi.baidu.com/sug"

    # 2 进行UA伪装：
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    # 3 post请求参数处理(同get请求一样)
    # 将搜索的参数动态化
    word = input("输入关键字：")
    data = {
        "kw" : word
    }
    # 4 发送请求
    response = requests.post(url=post_url,data=data,headers=headers)

    # 5 获取响应数据:json()方法返回的是object
    # 只有确认响应数据是一个json类型(也就是Content-Type: application/json)
    # 才可以使用json()方法
    dic_json = response.json()

    # 6 持久化存储   导入json模块
    fileName = word + ".json"       # 创建一个名字为word的json格式文件
    fp = open(fileName,"w",encoding="utf-8")
    json.dump(dic_json,fp=fp,ensure_ascii=False)

    print("爬取结束！！")


















