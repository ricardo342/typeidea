# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: craw_url_photo
@time:2023/7/21
@Author:majiaqin 170479
@Desc:获取url中的详情页图片
'''
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''获取网页源代码'''
def html_content(url, chrome_path, chromedriver):
    from bs4 import BeautifulSoup
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = chrome_path
    browser = webdriver.Chrome()
    # 低版本谷歌浏览器或者selenium(注释上一行用下一行)
    # browser = webdriver.Chrome(chromedriver, options=options)
    browser.get(url)
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    browser.quit()
    return soup

'''获取详情页图片链接'''
def get_photo_url(url, chrome_path, chromedriver):
    import re
    html_contents = html_content(url, chrome_path, chromedriver)
    # 获取所有background-image下的链接
    image_link = re.findall(r'//.*?.jpg.avif', str(html_contents))
    image_link_list = ['https:'+i for i in image_link]
    return image_link_list

'''将图片链接下载到文件夹下'''
def download_path(url, path_file='D:\download_photo',
                  chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                  chromedriver="C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\chromedriver.exe"):
    import requests, re, os
    try:
        os.mkdir(path_file)
    except FileExistsError:
        pass
    # 获取链接中的code
    code = re.findall(r'\d+', url)[0]
    path = path_file+'\\'+code
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    print('尊敬的婵姐, 开始下载文件')
    photo_url_list = get_photo_url(url, chrome_path, chromedriver)
    for i in range(len(photo_url_list)):
        pprint('正在下载链接: {0}'.format(photo_url_list[i]))
        resp = requests.get(photo_url_list[i])
        with open(path+'\\'+str(i)+'.jpg.avif', 'wb') as f:
            f.write(resp.content)
    print('当前链接下载的图片数量为: {0}'.format(str(len(photo_url_list))))
    return '图片下载到以下地址: \n{0}'.format(path)

if __name__ == '__main__':
    pprint(download_path('https://item.jd.com/100042725231.html',
                         chrome_path=r'C:\Users\22907\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\chrome.exe',
                         chromedriver=r'C:\Users\22907\AppData\Local\Programs\Python\Python38\chromedriver.exe'))