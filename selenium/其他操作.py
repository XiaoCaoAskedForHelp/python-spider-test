'''
Author: Amos Cao
Date: 2023-03-16 13:16:15
LastEditors: Amos Cao
LastEditTime: 2023-03-16 13:33:45
Description: sad代码dog
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from lxml import etree

edge_driver_path_obj = Service('./test/selenium/msedgedriver')
driver = webdriver.Edge(service=edge_driver_path_obj)
 
driver.get(r'https://www.taobao.com')

driver.find_element(by=By.ID,value="q").send_keys("iphone")

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(2)

driver.find_element(by=By.CLASS_NAME,value="btn-search").click()

time.sleep(2)

driver.get("https://www.baidu.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

driver.quit()

