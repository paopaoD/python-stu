# @Project   : Python
# @File      : 1..初识requests.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/16, 22:17
#


import requests

if __name__ == "__main__":
    # 1，指定url
    url = 'https://www.sogou.com/'
    # 2，发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    # 3，获取响应数据 .text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # 4,持久化存储
    with open('./sogou.html', "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("爬取结束！！！")
























