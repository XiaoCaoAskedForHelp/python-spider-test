'''
Author: Amos Cao
Date: 2023-03-16 09:36:01
LastEditors: Amos Cao
LastEditTime: 2023-03-16 14:55:50
Description: sad代码dog
'''
'''
Author: Amos Cao
Date: 2023-03-16 09:36:01
LastEditors: Amos Cao
LastEditTime: 2023-03-16 14:54:45
Description: sad代码dog
'''
# 基于浏览器自动化的模块


from selenium import webdriver
import time
from lxml import etree

driver = webdriver.Edge(executable_path='./test/selenium/msedgedriver')
 
driver.get(r'https://www.baidu.com/')

page_text = driver.page_source
response = etree.HTML(page_text)
li_list = response.xpath('//*[@id="hotsearch-content-wrapper"]/li')
for li in li_list:
    name = li.xpath("./a/span[2]/text()")[0]
    print(name)

 
time.sleep(5)
driver.close()
