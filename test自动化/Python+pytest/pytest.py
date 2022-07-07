# @Project   : Python
# @File      : requirements.txt.py
# @Auther    : �ȵ���Ҷ���
# @Time      : 2022/7/2, 19:14
#

'''
    pytest���

        pytestĬ�Ϲ���
            1,py�ļ��������� test_ ��ͷ���� _test ��β
            2,���� ������Test��ͷ
            3,�������������� test_ ��ͷ

        ע�⣺
            get����ͨ��params���ݲ�����
            post����ͨ��json����data���Ρ�
            �ļ��ϴ���ͨ��files���Σ�open�򿪵ķ�ʽ


        # data��json���ε�����

            data���ݱ��ģ�
                ��dict�ֵ����ͣ�Ĭ�����������ͷ��applilcation/x-www-form-urlencoded,
                ��ʾ��form���ķ�ʽ���Σ���ʽ��a=1&b=2&c=3
                str���ͣ�Ĭ������£�text/plain(������ֵ��ʽ��Ҫת����str��ʽ����)


            json���ݱ��ģ�
                ������dict����str���ͣ�Ĭ�϶���applilcation/json,��ʽ:{"a":1,"b":2}


                json.dumps(data)  ���л�       ���ֵ��ʽ������ת����str��ʽ
                json.loads(data)  �����л�      ��str��ʽת�����ֵ��ʽ


        �ܽ᣺
            dataֻ�ܴ��򵥵�ֻ�м�ֵ�Ե�dict����str��ʽ
            jsonһ��ֻ�ܴ�dict��ʽ(�򵥺�Ƕ�׵�dict��ʽ������)



    requestsȫ�ֹ�
        ����
            1,requests.get()        ����get����
            2,requests.post()       ����post����
            3,requests.delete()     ����delete����
            4,requests.put()        ����put����
            5,requests.request()    ����ĵķ���

        ��Ӧ��response����
            1,rep = requests.request()

            # �����ַ���������
            print(rep.text)

            # �����ֽڸ�ʽ������
            print(rep.content)

            # ����json(�ֵ�)��ʽ������
            print(rep.json())

            # ����״̬��
            print(rep.status_code)

            # ����״̬��Ϣ
            print(rep.reason)



'''


# ʾ��:
import requests

url = ""
params = {}
data = {}
headers = ""

##### 1 ����request������Ҫ��д�Ĳ���
rep = requests.request("get/post",url=url,params=params,data=data,headers=headers)



##### 2 ����get����
url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",  # �ӿ��еĵڼ�����Ӱȥȡ
    "limit": "20",  # һ��ȡ���ĸ���
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
# ����get����  ��Ҫ�Ĳ���
response01 = requests.get(url=url, params=params, headers=headers)



##### 3 ����post����
post_url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
data = {
    "kw":"����"
}
# ����post���� ��Ҫ�Ĳ���
response02 = requests.post(url=post_url, data=data, headers=headers)



#### 4 �������ݵĸ�ʽ

# �����ַ���������
print(rep.text)

# �����ֽڸ�ʽ������  Ҳ���Ƕ�����
print(rep.content)

# ����json(�ֵ�)��ʽ������
print(rep.json())

# ����״̬��
print(rep.status_code)

# ����״̬��Ϣ
print(rep.reason)




















































