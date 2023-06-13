# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20

import requests;
import json;
url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
param = {
    "type": '24',
    "interval_id": "100:90",
    "action": "",
    "start": '0',
    "limit": '20'
}
result = requests.get(url,params=param,headers=headers)
# print(result.json())

fp = open("./test/豆瓣电影.json",'w',encoding='utf-8')
json.dump(result.json(),fp=fp,ensure_ascii=False)