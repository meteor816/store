from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("厨具")

driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.find_element_by_xpath('//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_02:0070641261_10820446614"]').click()
# 获取浏览器所有的窗口句柄
data = driver.window_handles # ["s001","s002"]
# 切换具体窗口
driver.switch_to.window(data[1])

driver.find_element_by_xpath("//*[@id='addCart']").click()

data=driver.window_handles
driver.switch_to.window(data[1])

driver.find_element_by_xpath("//html/body/div[38]/div/div[2]/div/div[1]/a").click()

time.sleep(2)
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()

time.sleep(3)

driver.quit()













