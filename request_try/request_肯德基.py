'''
Author: Amos Cao
Date: 2023-03-07 16:31:21
LastEditors: Amos Cao
LastEditTime: 2023-03-07 16:38:54
Description: sad代码dog
'''
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword
import requests;
import json;
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
param = {
    "op": 'keyword'
}
data = {
    "cname": '',
    "pid": '',
    "keyword": "北京",
    "pageIndex": "1",
    "pageSize": "10"
}
result = requests.post(url,params=param,headers=headers,data=data)
# print(result.json())

fp = open("./test/肯德基.json",'w',encoding='utf-8')
json.dump(result.json(),fp=fp,ensure_ascii=False)