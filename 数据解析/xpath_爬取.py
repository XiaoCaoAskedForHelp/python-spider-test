from lxml import etree


# parser = etree.HTMLParser(encoding="utf-8")
# tree = etree.parse('./test/数据解析/test.html',parser=parser)

# r = tree.xpath('/html/body//font') //为多层，/ 为一层
# r = tree.xpath('/html/body//select[@name="select4"]')

# r = tree.xpath('/html/body//select[@name="select4"]/option[3]')
# r = tree.xpath('/html/body//select[@name="select4"]/option[3]/text()')[0]
# r = tree.xpath('/html/body//td/input[@name="text9"]/@type')
# r = tree.xpath('./html/body//td/input[@name="text9"]/@type') //从同层次下开始
# print(r)


import requests;
import os;

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
# url = 'https://cn.58.com/ershoufang/'
# page_text = requests.get(url,headers=headers).text
# page = requests.get(url,headers=headers).headers
# print(page)
# with open("./test/数据解析/58.html",'w',encoding="utf-8") as fp:
#     fp.write(page_text)
# # print(page_text)

# tree = etree.HTML(page_text)
# title = tree.xpath('//section[@class="list"]//h3/text()')
# with open("./test/数据解析/58_二手房.html",'w',encoding="utf-8") as fp:
#     for item in title:
#         fp.write(item + '\n')


# url = 'http://pic.netbian.com/4kmeinv/'
# response = requests.get(url,headers=headers)
# # response.encoding = 'utf-8'
# page_text = response.text
# tree = etree.HTML(page_text)
# # title = tree.xpath('//ul[@class="clearfix"]/li/a/img/@alt')
# # img_urls = tree.xpath('//ul[@class="clearfix"]/li/a/img/@src')

# img_list = tree.xpath('//ul[@class="clearfix"]/li/a/img')
# if not os.path.exists('./test/数据解析/meinv'):
#     os.mkdir('./test/数据解析/meinv')
# for item in img_list:
#     img_src = "http://pic.netbian.com" + item.xpath("./@src")[0]
#     img_alt = item.xpath("./@alt")[0] + '.jpg'
#     # 通用处理中文乱码的解决方案
#     img_name = img_alt.encode("iso-8859-1").decode('gbk')
#     print(img_src,img_name)
#     img_data = requests.get(img_src,headers=headers).content
#     img_path = './test/数据解析/meinv/'+img_name
#     with open(img_path,'wb') as fp:
#         fp.write(img_data)
#         print(img_name + "下载成功")


url = 'http://www.aqistudy.cn/historydata/'
response = requests.get(url,headers=headers)
# response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
city = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')
print(city)