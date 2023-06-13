'''
Author: Amos Cao
Date: 2023-03-16 16:15:51
LastEditors: Amos Cao
LastEditTime: 2023-03-16 16:46:29
Description: sad代码dog
'''
 
# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver import EdgeOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import random
 
# 去除浏览器识别
option = EdgeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)
 
# 实例化一个浏览器对象（传入浏览器的驱动程序）
edge_driver_path_obj = Service('./test/selenium/msedgedriver')
driver = webdriver.Chrome(service=edge_driver_path_obj, options=option)
 
# 让浏览器发起一个对12306url的请求
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
 
# 解决特征识别
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
driver.execute_script(script)
 
sleep(1)
 
# 标签定位到账号密码输入框中
userName_tag = driver.find_element(By.ID,'J-userName')
password_tag = driver.find_element(By.ID,'J-password')
 
# 输入账号
userName_tag.send_keys('15906134267')
sleep(1)
# 输入密码
password_tag.send_keys('cqdO82544')
sleep(1)
 
# 点击登陆
btn = driver.find_element(By.ID,'J-login')
btn.click()
 
sleep(5)
 
# 标签定位滑块id
span = driver.find_element(By.ID,'nc_1__scale_text')
 
action = ActionChains(driver)  # 行为链实例化
action.click_and_hold(span)
 
t = 0.1
for i in range(10):
    action.move_by_offset(32, 0).perform()   # perform()立即执行动作链操作，move_by_offset(x, y):x水平方向  y竖直方向
    t = t-0.01
    print(t)
    sleep(t)
 
# 释放行为链
action.release()
 
