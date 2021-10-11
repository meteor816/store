from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")
driver.maximize_window()
#点击教师登录
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
#输入账号密码
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
time.sleep(1)
#点击登录
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(1)
#点击教师管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()

#点击查询框
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[2]/a[1]/span[1]').click()
#输入查询框内容
driver.find_element_by_xpath('//*[@id="sear_teaname"]').send_keys("李艳")
#点击查询
driver.find_element_by_xpath('//*[@id="search_user"]').click()

driver.find_element_by_xpath('//*[@id="main_panel"]/div/div/div[2]/div[2]/div[2]').click()
# 重置密码
driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a').click()
time.sleep(1)
driver.switch_to.alert.accept()
#点击学生管理
driver.find_element_by_xpath('//*[@id="_easyui_tree_12"]/span[4]/a').click()
#点击页面的学生管理
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[3]/a[1]/span[1]').click()
#输入姓名和电话号码
driver.find_element_by_xpath('//*[@id="J-stu"]').send_keys('大霞')
driver.find_element_by_xpath('//*[@id="J-phone"]').send_keys('18391768468')
#点击查询
driver.find_element_by_xpath('//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]/a').click()
time.sleep(1)
#设置毕业状态
driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[11]/div/a').click()
time.sleep(1)
#点击确定
driver.find_element_by_xpath('/html/body/div[9]/div[3]/a').click()
time.sleep(1)

#课程管理
driver.find_element_by_xpath('//*[@id="_easyui_tree_13"]/span[4]/a').click()
#点击课程管理
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[4]/a[1]').click()
#点击添加课程
driver.find_element_by_xpath('//*[@id="course_panel"]/div/div/div[1]/table/tbody/tr/td/a').click()
time.sleep(1)
#输入课程名和课程描述
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('汉字')
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('文字的乐趣')
time.sleep(1)
#点击添加
driver.find_element_by_xpath('/html/body/div[9]/div[3]/a[1]/span').click()
#添加成功点击确定
driver.find_element_by_xpath('/html/body/div[12]/div[3]/a').click()
time.sleep(1)
#输入课程名和课程描述
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('汉字')
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('文字的乐趣')
time.sleep(1)
#点击取消
driver.find_element_by_xpath('/html/body/div[9]/div[3]/a[2]/span').click()
time.sleep(1)
#评价
driver.find_element_by_xpath('//*[@id="_easyui_tree_14"]/span[3]/a').click()
#点击今日评价
driver.find_element_by_xpath('//*[@id="_easyui_tree_15"]/span[4]/a').click()
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[5]/a[1]').click()
#输入
driver.find_element_by_xpath('//*[@id="J-xl"]').click()
driver.find_element_by_xpath('//*[@id="laydate_y"]').click()
#输入年月日
driver.find_element_by_xpath('//*[@id="laydate_ys"]/li[8]').click()
driver.find_element_by_xpath('//*[@id="laydate_m"]').click()
# 点击查询
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[2]/a/span').click()
time.sleep(1)
#导出当前评价
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
#点击评价报表
driver.find_element_by_xpath('//*[@id="_easyui_tree_16"]/span[4]/a').click()
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[6]/a[1]/span[1]')
time.sleep(1)
#点击日志
driver.find_element_by_xpath('//*[@id="_easyui_tree_18"]/span[4]/a').click()
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li[7]/a[1]/span[1]').click()
# driver.find_element_by_xpath('//*[@id="J-history"]').send_keys('')
# driver.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[2]/a').click()
# driver.find_element_by_xpath('')
#导出当前日志
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[4]/a').click()
#分页显示
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[10]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[10]/a').click()
time.sleep(2)
driver.quit()



