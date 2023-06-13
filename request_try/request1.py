'''
Author: Amos Cao
Date: 2023-03-07 15:09:29
LastEditors: Amos Cao
LastEditTime: 2023-03-07 15:26:22
Description: sad代码dog
'''

# http://sogou.com/web?query=%E7%BE%8E%E5%A5%B3&_asf=www.sogou.com&_ast=&w=01015002&p=40040100&ie=utf8&from=index-nologin&s_from=index&oq=mein&ri=0&sourceid=sugg&suguuid=15257e11-a9c6-4816-b162-59e4f6ba6dd1&stj=0%3B15%3B0%3B0&stj2=0&stj0=0&stj1=15&hp=162&hp1=&suglabid=suglabId_1&sut=3134&sst0=1678172996200&lkt=5%2C1678172993066%2C1678172993827&sugsuv=1660788429992368&sugtime=1678172996200

# 网页采集器

import requests;

url = "http://sogou.com/web"
# kw = input("Input")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
param = {
    "query": "美女"
}
result = requests.get(url,param,headers=headers)
print(result.text)
with open("美女"+'.html','w',encoding='utf-8') as fp:
    fp.write(result.text)