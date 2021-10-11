from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.get("https://www.taobao.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='q']").send_keys("玩具")

driver.find_element_by_xpath("//*[@id='J_TSearchForm']/div[1]/button").click()

driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("18935414892")

driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("666666")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button")

time.sleep(10)

ele = driver.find_element_by_xpath("//*[@class='slider']")
ac = ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(42,0).perform() # perform执行
#
ac.release()
driver.quit()




