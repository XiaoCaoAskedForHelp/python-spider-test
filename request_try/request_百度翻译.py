import requests;
import json;

url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
data = {
    "kw": "request"
}
result = requests.post(url,headers=headers,data=data)
print(result.json())

fp = open("./test/request.json",'w',encoding='utf-8')
json.dump(result.json(),fp=fp,ensure_ascii=False)