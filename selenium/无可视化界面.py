from selenium import webdriver
import time
from lxml import etree
# 无可视化界面
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

edge_options = Options()
# # 使用无头模式
# edge_options.add_argument('--headless')
# # 禁用GPU，防止无头模式出现莫名的BUG
# edge_options.add_argument('--disable-gpu')

# 开启开发者模式
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 禁用启用Blink运行时的功能
edge_options.add_argument('--disable-blink-features=AutomationControlled')

edge_driver_path_obj = Service('./test/selenium/msedgedriver')
driver = webdriver.Edge(service=edge_driver_path_obj, options=edge_options)



driver.get(r'https://www.baidu.com/')

page_text = driver.page_source
response = etree.HTML(page_text)
li_list = response.xpath('//*[@id="hotsearch-content-wrapper"]/li')
for li in li_list:
    name = li.xpath("./a/span[2]/text()")[0]
    print(name)

 
time.sleep(5)
driver.close()