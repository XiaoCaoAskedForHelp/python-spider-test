'''
Author: Amos Cao
Date: 2023-03-08 11:05:42
LastEditors: Amos Cao
LastEditTime: 2023-03-08 16:16:00
Description: sad代码dog
'''
# coding=utf-8
# https://gw.alicdn.com/tps/i3/2200657715182/O1CN017h15X31o9PEPbAtID_!!2200657715182-0-sm.jpg_Q75.jpg

import requests;
import json;
import re;
from urllib.parse import unquote
from urllib import parse
import os,base64
import time
# https://cn.bing.com/images/async?q=%e8%bf%aa%e4%b8%bd%e7%83%ad%e5%b7%b4&first=36&count=35&cw=1177&ch=593&relp=35&datsrc=I&layout=ColumnBased&apc=0&mmasync=1&dgState=c*6_y*1564s1668s1466s1751s1729s1627_i*36_w*186&IG=906C6799FD3043659FD9065E16DFF81B&SFX=2&iid=images.5563
# q: 迪丽热巴
# first: 36
# count: 35
# cw: 1177
# ch: 593
# relp: 35
# datsrc: I
# layout: ColumnBased
# apc: 0
# mmasync: 1
# dgState: c*6_y*1564s1668s1466s1751s1729s1627_i*36_w*186
# IG: 906C6799FD3043659FD9065E16DFF81B
# SFX: 2
# iid: images.5563
# https://cn.bing.com/images/async?q=%e8%bf%aa%e4%b8%bd%e7%83%ad%e5%b7%b4&first=73&count=35&cw=1177&ch=593&relp=70&apc=0&datsrc=I&layout=ColumnBased&mmasync=1&dgState=c*6_y*3030s3042s3284s3127s3021s3079_i*71_w*186&IG=906C6799FD3043659FD9065E16DFF81B&SFX=3&iid=images.5563
# q: 迪丽热巴
# first: 73
# count: 35
# cw: 1177
# ch: 593
# relp: 70
# apc: 0
# datsrc: I
# layout: ColumnBased
# mmasync: 1
# dgState: c*6_y*3030s3042s3284s3127s3021s3079_i*71_w*186
# IG: 906C6799FD3043659FD9065E16DFF81B
# SFX: 3
# iid: images.5563

# first: 115
if not os.path.exists("./test/数据解析/迪丽热巴"):
    os.mkdir('./test/数据解析/迪丽热巴')

# url = "https://cn.bing.com/images/search"
url = "https://cn.bing.com/images/async"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
# param = {
#     "q": "迪丽热巴",
#     "form": "HDRSC3",
#     "first": "1",
#     "cw": "1177",
#     "ch": "593"
# }


param = {
    "q": "迪丽热巴",
    "count": "35",
    "first": "1",
    "cw": "1177",
    "ch": "593"
}
ex = '<div class="img_cont hoff"><img.*?data-src="(.*?)" alt=.*?</div>'
result = requests.get(url,headers=headers,params=param).text
list = re.findall(ex,result,re.S)
print(list)
print(len(list))
mediaUrls = []
for item in list:
    try:
        print("first url:",item)
        url = unquote(item)
        print("now url:",url)
        result = parse.urlparse(url)
        query_dict = parse.parse_qs(result.query)
        print(query_dict)
        uri = url.split('?')[0]
        print(uri)
        img_data = requests.get(url=uri,headers=headers,params=query_dict).content
        # 图片名称
        # name = url.split('/')[-1]
        with open("./test/数据解析/迪丽热巴/"+str(time.time())+".jpg",'wb') as fp:
            fp.write(img_data)
        time.sleep(0.1)
    except Exception as e:
        print(e)

# ex2 = "processEmbImg.*?data:image.*?;base64,(.*?)'\);"
# list2 = re.findall(ex2,result,re.S)
# print('--------------------------------------')
# # print(list2)
# print(len(list2))
# for item in list2:
#     try:
#         imgdata = base64.b64decode(item)
#         with open("./test/数据解析/迪丽热巴/"+str(time.time())+".jpg",'wb') as fp:
#             fp.write(imgdata)
#         print('下载成功')
#         time.sleep(0.1)
#     except Exception as e:
#         print(e)

print("Operation completed")



# with open("./test/数据解析/迪丽热巴.html",'w',encoding='utf-8') as fp:
#     fp.write(result)

# with open("./test/数据解析/taobao/bao.jpg","wb") as fp:
#     fp.write(img_data)
