from selenium import webdriver
import time
#创建谷歌浏览器对象
driver = webdriver.Chrome()
#打开京东网址
driver.get("http://www.JD.com")

#窗口最大化
driver.maximize_window()

# 寻找搜索输入框
driver.find_element_by_id("key").send_keys('电脑')

#点击搜索按钮
driver.find_element_by_xpath("//*[@class='button']").click()

# driver.find_element_by_xpath("//*[@src='//img13.360buyimg.com/n2/jfs/t1/193933/35/19114/584484/611f6af3Ec5a3f34c/f5acc049805c7457.jpg']").click()
# driver.find_element_by_xpath("//*[@id='nav-chaoshi']").click()

driver.find_element_by_xpath("//*[@class='gl-i-wrap']").click()
#直接打开网址
driver.get("http://item.jd.com/10444729665.html")
time.sleep(3)

# #退出浏览器
driver.quit()