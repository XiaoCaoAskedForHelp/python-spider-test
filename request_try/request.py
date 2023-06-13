'''
Author: Amos Cao
Date: 2023-03-06 17:41:48
LastEditors: Amos Cao
LastEditTime: 2023-03-07 15:04:19
Description: sad代码dog
'''

import requests;

url = "https://www.sogou.com"
result = requests.get(url)
print(result.text)
with open('./test/sogou.html','w',encoding='utf-8') as fp:
    fp.write(result.text)