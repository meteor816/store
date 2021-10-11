from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.JD.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad  e580")

driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]").click()
# 切换窗口
# 获取浏览器所有的窗口句柄
data = driver.window_handles # ["s001","s002"]
# 切换具体窗口
driver.switch_to.window(data[1])

driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
#账户登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18935414893")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("Rb0921!!")

driver.find_element_by_xpath("//*[@id='loginsubmit']").click()


driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(5)

driver.quit()







