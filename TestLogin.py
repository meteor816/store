from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import InitPage
from LoginOperation import LoginOpera
import time

@ddt
class TestLogin(TestCase):
    # 在所有方法执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8080/HKR")
        self.driver.maximize_window()
    time.sleep(3)
    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  # 退出浏览器
        time.sleep(3)
    # @data(*InitPage.login_success_data)
    @data(*InitPage.L[0,2])
    # @unpack
    def testSuccessCase1(self,testdata):

        # 提取数据
        username = testdata["username"]
        password =  testdata["password"]
        expect =  testdata["expect"]
        time.sleep(2)
        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        data = loginObj.getSuccessResult()
        #  断言
        self.assertEqual(data,expect)


    # @data(*InitPage.login_error_data)
    @data(*InitPage.L[2,4])
    def testSuccessCase2(self,testdata):

        # 提取数据
        username = testdata["username"]
        password =  testdata["password"]
        expect =  testdata["expect"]

        # 调用被测操作类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        data = loginObj.getErrorResult()

        #  断言
        self.assertEqual(data,expect)
    #





















