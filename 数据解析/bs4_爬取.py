'''
Author: Amos Cao
Date: 2023-03-09 11:19:06
LastEditors: Amos Cao
LastEditTime: 2023-03-09 13:27:33
Description: sad代码dog
'''
from bs4 import BeautifulSoup
import requests

# fp = open('./test/数据解析/迪丽热巴.html','r',encoding='utf-8')
# soup = BeautifulSoup(fp,'lxml')
# soup = soup1.encode_contents(encoding='utf-8')
# print(soup.a)
# print(soup.find('a'))
# print(soup.find('div',class_="b_scerr"))
# print(soup.findAll('div',class_="img_cont hoff"))
# print(soup.select('.img_cont'))
# print(soup.select('.img_cont > img')[0]) # 一个层级
# print(soup.select('.img_cont img')[0]) # 多个层级
# print(soup.select('.img_cont > img')[0]) # 文本内容text/get_text()可以获取某一个标签下的所有文本内容，不直系也行
                                            # stirng值可以获取该标签下的直系文本内容
# print(soup.select('.img_cont > img')[0]["src"])

url = "https://www.dushu.com/showbook/114797/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
page_text = page_text = requests.get(url,headers=headers).text
soup = BeautifulSoup(page_text,'lxml')

td_list = soup.select('#ctl00_c1_volumes_ctl00_chapters > tr > td')
print(td_list)
fp = open('./test/数据解析/sanguo.txt','w',encoding='utf-8')
for item in td_list:
    title = item.a.string
    detail_url = "https://www.dushu.com" + item.a['href']
    print("title:",title,"detail_url",detail_url)
    content_text = requests.get(url=detail_url,headers=headers).text
    detail_soup = BeautifulSoup(content_text,"lxml")
    div_tag = detail_soup.find('div',class_ = "content_txt")
    content = div_tag.text
    fp.write(title+':\n'+ content+'\n')
    print("ok")
