# @Project   : Python
# @File      : 6.爬取图片.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 19:49
#

'''
    爬取图片

'''

import requests


if __name__ == '__main__':
    # 如何爬取图片
    url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg2.hackhome.com%2Fimg2014%2F20149%2F2014091560053909.png&refer=http%3A%2F%2Fimg2.hackhome.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1658577167&t=c4cdd635bd4364d8fa0d91b64d9e8926"
    # content返回的是二进制的图片数据
    # text(字符串)   content(二进制)  ison()  (对象)
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)

    print("over!")



























































