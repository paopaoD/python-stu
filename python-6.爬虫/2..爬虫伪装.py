# @Project   : Python
# @File      : 2..爬虫伪装.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 9:05
#

'''
    # User-Agent: 请求载体的身份标识

    UA检测：门户网站的服务器会检测对应请求载体的身份标识，如果检测到请求载体是
            基于某一款浏览器的，那么说明该请求是一个正常的请求
            但是，如果检测到请求载体不是基于某一款浏览器的，则表示该请求是不正
            常的请求，则服务端很有可能拒绝该次请求

    UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''

#### 爬取百度指定词条对应的搜索结果页面

import requests

if __name__ == '__main__':
    # 获取url地址
    url = "https://www.baidu.com/s"

    # 处理url中携带的参数，封装到字典中
    kw = input("请输入关键字：")   # 要搜索的内容
    params = {
        'wd': kw
    }

    # UA伪装：伪装成是一个浏览器在发送请求，而不是爬虫
    header = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
        }

    # 发送get请求 并在请求过程中加入了关键字参数和UA伪装
    response = requests.get(url=url,params=params,headers=header)

    #
    page_text = response.text
    # 创建一个文件，存储爬取内容，以html的格式
    filename = kw + '.html'
    # 将爬取的内容写入文件内
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,"爬取成功了！！")





