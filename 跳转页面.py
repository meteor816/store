import time
from selenium import  webdriver

driver = webdriver.Chrome()

driver.get(r"E:/自动化/自动化测试/Python自动化/练习的html/练习的html/跳转页面/pop.html")

driver.maximize_window()

# driver.find_element_by_id("accountID")

driver.find_element_by_xpath("//*[@id='goo']").click()

time.sleep(2)

# 关闭浏览器
driver.quit()