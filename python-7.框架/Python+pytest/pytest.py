# @Project   : Python
# @File      : requirements.txt.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/7/2, 19:14
#

'''
    pytest框架

        pytest默认规则
            1,py文件必须是以 test_ 开头或者 _test 结尾
            2,类名 必须以Test开头
            3,测试用例必须以 test_ 开头

        注意：
            get请求通过params传递参数。
            post请求通过json或者data传参。
            文件上传是通过files传参，open打开的方式


        # data和json传参的区别：

            data数据报文：
                以dict字典类型，默认情况下请求头：applilcation/x-www-form-urlencoded,
                表示以form表单的方式传参，格式：a=1&b=2&c=3
                str类型，默认情况下：text/plain(如果是字典格式需要转换成str格式传参)


            json数据报文：
                不管是dict还是str类型，默认都是applilcation/json,格式:{"a":1,"b":2}


                json.dumps(data)  序列化       把字典格式的数据转换成str格式
                json.loads(data)  反序列化      把str格式转换成字典格式


        总结：
            data只能传简单的只有键值对的dict或者str格式
            json一般只能传dict格式(简单和嵌套的dict格式都可以)



    requests全局观
        请求
            1,requests.get()        发送get请求
            2,requests.post()       发送post请求
            3,requests.delete()     发送delete请求
            4,requests.put()        发送put请求
            5,requests.request()    最核心的方法

        响应：response对象
            1,rep = requests.request()

            # 返回字符串的数据
            print(rep.text)

            # 返回字节格式的数据
            print(rep.content)

            # 返回json(字典)格式的数据
            print(rep.json())

            # 返回状态码
            print(rep.status_code)

            # 返回状态信息
            print(rep.reason)



'''


# 示例:
import requests

url = ""
params = {}
data = {}
headers = ""

##### 1 发生request请求，需要填写的参数
rep = requests.request("get/post",url=url,params=params,data=data,headers=headers)



##### 2 发送get请求
url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",  # 从库中的第几部电影去取
    "limit": "20",  # 一次取出的个数
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
# 发送get请求  需要的参数
response01 = requests.get(url=url, params=params, headers=headers)



##### 3 发送post请求
post_url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
data = {
    "kw":"杭州"
}
# 发送post请求 需要的参数
response02 = requests.post(url=post_url, data=data, headers=headers)



#### 4 返回数据的格式

# 返回字符串的数据
print(rep.text)

# 返回字节格式的数据  也就是二进制
print(rep.content)

# 返回json(字典)格式的数据
print(rep.json())

# 返回状态码
print(rep.status_code)

# 返回状态信息
print(rep.reason)




















































