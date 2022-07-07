# @Project   : Python
# @File      : 5..爬取肯德基餐厅信息.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 10:38
#
import json

import requests

if __name__ == "__main__":
    # 指定url
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

    # 获取关键字参数
    keyword = input("请输入地址：")
    params = {
        "cname":"",
        "pid":"",
        "keyword": keyword,
        "pageIndex": "1",
        "pageSize": "10",
    }

    # 进行伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    # 发生请求
    response = requests.get(url=url,params=params,headers=headers)

    # # 返回的数据以text形式存储
    # page_text = response.text
    #
    # fileName = keyword + ".html"
    # # 将返回的数据写入到文件fileName中，以html的格式
    # with open(fileName,"w",encoding="utf-8") as fp:
    #     fp.write(page_text)

    page_json = response.json()

    fileName = keyword + ".json"
    fp = open(fileName,"w",encoding="utf-8")
    json.dump(page_json,fp=fp,ensure_ascii=False)

    print("结束！！")











































