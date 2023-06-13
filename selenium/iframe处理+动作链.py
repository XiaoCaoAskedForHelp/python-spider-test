# https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from lxml import etree
from selenium.webdriver import ActionChains

edge_driver_path_obj = Service('./test/selenium/msedgedriver')
driver = webdriver.Edge(service=edge_driver_path_obj)
 
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签存在于iFrame标签中，则必须通知如下操作在及进行标签定位
driver.switch_to.frame('iframeResult') # 切换浏览器标签定位的作用域
div = driver.find_element(By.ID,"droppable")
print(div)

time.sleep(2)

#动作链
action = ActionChains(driver=driver)
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    print(i)
    # perform()立即执行动作连操作
    action.move_by_offset(17,0).perform()
    time.sleep(0.3)

action.release().perform()

driver.close()


