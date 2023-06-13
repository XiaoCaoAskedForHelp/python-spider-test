'''
Author: Amos Cao
Date: 2023-03-08 16:16:12
LastEditors: Amos Cao
LastEditTime: 2023-03-24 10:48:04
Description: sad代码dog
'''
import os
import sys
import time
import urllib
import requests
import re
from bs4 import BeautifulSoup
import time
 
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
# 数量 35
# 起始位置36 77 119
#relp 35 70 105 无用
url = "https://cn.bing.com/images/async?q={0}&first={1}&count={2}&cw=1177&ch=593&relp=35&apc=0&datsrc=I&layout=ColumnBased&apc=0&mmasync=1&dgState=c*6_y*1630s1814s1668s1591s1607s1545_i*36_w*186&IG=AADC57EEA7664CF59683373D1F9D200E&SFX={3}&iid=images.5562"
       
 
def getImage(url, count):
    '''从原图url中将原图保存到本地'''
    try:
        time.sleep(0.5)
        urllib.request.urlretrieve(url, './test/数据解析/杨幂/' + str(count + 1) + '.jpg')
    except Exception as e:
        time.sleep(1)
        print("本张图片获取异常，跳过...")
    else:
        print("图片+1,成功保存 " + str(count + 1) + " 张图")
 
 
def findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx, count):
    '''从缩略图列表页中找到原图的url，并返回这一页的图片数量'''
    soup = BeautifulSoup(html, "lxml")
    link_list = soup.find_all("a", class_="iusc")
    url = []
    for link in link_list:
        result = re.search(rule, str(link))
        #将字符串"amp;"删除
        url = result.group(0)
        print(url)
        #组装完整url
        url = url[8:len(url)]
        print(url)
        #打开高清图片网址
        getImage(url, count)
        count += 1
    #完成一页，继续加载下一页
    return count
 
 
def getStartHtml(url, key, first, loadNum, sfx):
    '''获取缩略图列表页'''
    page = urllib.request.Request(url.format(key, first, loadNum, sfx),
                                  headers=header)
    html = urllib.request.urlopen(page)
    return html
 
 
if __name__ == '__main__':
    name = "杨幂"    #图片关键词
    path = './test/数据解析/杨幂'   #图片保存路径
    countNum = 100  #爬取数量
    key = urllib.parse.quote(name)
    first = 1
    loadNum = 35
    sfx = 1
    count = 0
    rule = re.compile(r"\"murl\"\:\"http\S[^\"]+")
    if not os.path.exists(path):
        os.makedirs(path)
    while count < countNum:
        html = getStartHtml(url, key, first, loadNum, sfx)
        count = findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx,
                                   count)
        first = count + 1
        sfx += 1