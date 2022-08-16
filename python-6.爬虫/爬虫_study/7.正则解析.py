# @Project   : Python
# @File      : 7.正则解析.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 20:48
#
import os
import re

import requests


if __name__ == '__main__':
    # 创建一个文件夹，保存所有图片
    if not os.path.exists('../qiutuLibs'):
        os.mkdir('../qiutuLibs')

    # 设置伪装请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    # 设置一个通用的url模板 从第1页到最后一页
    url = "https://www.woyaogexing.com/tupian/index_%d.html"

    for index_num in range(2,4):
        # 对应页码的url
        new_url = format(url%index_num)

        # 对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

        # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex =r'<div class="txList\b.+?">.*?<img class="lazy" src="(.*?)" width.*?</div>'

        # 使用正则，将解析出来的所有图片放入列表中
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)

        count = 1
        for src in img_src_list:
            # 拼接出一个完整的图片地址url
            src = "https:" + src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            # 生成图片名称
            img_name = src.split("/")[-1]

            imPath = './qiutuLibs/' + img_name

            with open(imPath,'wb') as fp:
                fp.write(img_data)
                print(f"第{count}张下载成功！！名称：",img_name)
            count += 1






# <div class="txList ">
# <a href="/tupian/dongman/2022/208536.html" class="img" target="_blank" title="特喜欢最好看情侣头像动漫"><img class="lazy" src="//img2.woyaogexing.com/2022/06/23/e4ccb7a54fbbf024!400x400.jpg" width="180" height="180"></a>
#     <a href="/tupian/dongman/2022/208536.html" class="imgTitle" target="_blank" title="特喜欢最好看情侣头像动漫">特喜欢最好看情侣头像动漫</a>
#     <p><span>06月23日</span><a href="/user/1907138" target="_blank">bwkkIyku</a></p>
#     <div class="plIco" data-id="208536">
#         <a href="###" class="t" onclick="javascript:bAction.Digg(this,'good',208536,91);return false;" title="喜欢"></a>
#         <a href="###" class="d" onclick="javascript:bAction.Digg(this,'not',208536,91);return false;" title="心碎"></a>
#         <a href="###" class="f" onclick="javascript:bAction.addFava(this,'fava',208536,91);return false;" title="收藏"></a>
#     </div>
# </div>
#magnet:?xt=urn:btih:93827283DEFCD6519E6EC7967048B6E8FAE7F661



































































