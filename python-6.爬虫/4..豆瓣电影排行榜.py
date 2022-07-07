# @Project   : Python
# @File      : 4..豆瓣电影排行榜.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 10:20
#
import json

import requests

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"

    params = {
        "type": "24",
        "interval_id": "100:90",
        "action":"",
        "start": "0",  # 从库中的第几部电影去取
        "limit": "20",  # 一次取出的个数
    }
    # 2 进行UA伪装：
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    response = requests.get(url=url,params=params,headers=headers)

    list_data = response.json()

    fp = open("./douban.json","w",encoding="utf-8")
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print("结束！！！")

