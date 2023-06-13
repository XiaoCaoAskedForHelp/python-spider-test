'''
Author: Amos Cao
Date: 2023-03-16 14:22:49
LastEditors: Amos Cao
LastEditTime: 2023-03-16 14:52:38
Description: sad代码dog
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from lxml import etree
from selenium.webdriver import ActionChains

edge_driver_path_obj = Service('./test/selenium/msedgedriver')
driver = webdriver.Edge(service=edge_driver_path_obj)

driver.get("https://qzone.qq.com/")

driver.switch_to.frame('login_frame')
driver.find_element(By.ID,"switcher_plogin").click()

driver.find_element(By.ID,"u").send_keys("2062587813")
driver.find_element(By.ID,"p").send_keys("cdn082544941105")

time.sleep(5)

driver.find_element(By.ID,"login_button").click()

time.sleep(5)

driver.close()