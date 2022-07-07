import requests
from time import sleep
import os
import os.path as op
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as ww
import threading



def get_list(basic_url):
    '''
	#这里是无界面浏览器相关操作，不想要弹出界面的话，
	#把下边那行换成这些就ok
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('--headless')
    browser = webdriver.Chrome(options=browser_options)
    '''
    browser = webdriver.Chrome()  #这行就是那行（手动滑稽）
    wait = ww(browser, 20)
    try:
        browser.get(basic_url)
        print('访问成功！！')
        sleep(1)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#rightModule > div.search-wrapper > div > div > div > input')))
        click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rightModule > div.search-wrapper > div > div > div > div > button')))
        input.send_keys(keyword)
        sleep(2)
        click.click()
        sleep(1)
        print('搜索成功！')
        browser.switch_to.window(browser.window_handles[1])
        for i in range(0, 2001, 250):
            browser.execute_script(f'window.scrollBy(0, {i})')
            print(f'\r加载中。。。{i/2000:.1%}', end='')
            sleep(3)
        print('')
        clicks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.link.title')))
        cnt = 0
        want = 10  ## 爬取页面数
        for clc in clicks[: want]:
            clc.click()
            sleep(2)
            cnt += 1
            browser.switch_to.window(browser.window_handles[1])
            print(f'\r已打开{cnt}个界面，比例{cnt/want:.2%}', end='')
        print()
        for num in range(want):
            browser.switch_to.window(browser.window_handles[num + 2])
            try:
                img = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[src]'))) #.article-content div .pgc-img img[src]
            except:
                pass
            for mg in img:
                url = mg.get_attribute('src')
                if url.startswith('http://p'):
                    lst.append(url)
    except Exception as t:
        print(t)


def download_pic1():
    path = r'C:\Users\PXO\Desktop\杂\Toutiao_pic\\' + keyword
    if not op.exists(path):
        os.mkdir(path)
    ln = len(lst)
    id = [i for i in range(ln)]
    cnt = 1
    for url in lst[:ln//2]:
        r = requests.get(url)
        pic_path = path + '\\' + f'{keyword}_pic_{id.pop(0)}.jpg'
        with open(pic_path, 'wb+') as ff:
            ff.write(r.content)
            ff.close()
        op1 = cnt*120//ln
        en = 60 - op1
        opp, enn = '-'*op1, '*'*en
        print(f'\r[1]下载ing：已下{cnt}/{ln//2}张，[{opp}>{enn}] {(2 * cnt) / len(lst):.1%}', end='')
        cnt += 1


def download_pic2():
    path = r'C:\Users\PXO\Desktop\杂\Toutiao_pic\\' + keyword
    if not op.exists(path):
        os.mkdir(path)
    ln = len(lst)
    id = [i for i in range(ln)]
    id.reverse()
    cnt = 1
    for url in lst[ln//2:]:
        r = requests.get(url)
        pic_path=path+'\\'+f'{keyword}_pic_{id.pop(0)}.jpg'
        with open(pic_path, 'wb+') as ff:
            ff.write(r.content)
            ff.close()
        op1 = cnt*120//ln
        en = 60 - op1
        opp, enn = '-'*op1, '*'*en
        print(f'\r[2]下载ing：已下{cnt}/{ln//2}张，[{opp}>{enn}] {(2 * cnt) / len(lst):.1%}', end='')
        cnt += 1


def main():
    global keyword, lst
    lst = []
    keyword = '鬼刀'
    basic_url = 'https://www.toutiao.com/'
    get_list(basic_url)
    threads = []
    th1=threading.Thread(target=download_pic1)
    threads.append(th1)
    th2=threading.Thread(target=download_pic2)
    threads.append(th2)
    for th in threads:
        th.setDaemon(True)
        th.start()
    th.join()




main()
