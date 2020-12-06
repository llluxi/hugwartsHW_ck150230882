from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestWxwork():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'True'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def test_addman(self):
        self.driver.implicitly_wait(5)
        # 选择通讯录
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ec6' and @text='通讯录']").click()
        # 点击添加成员
        self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @text='添加成员']").click()
        # 点击手动输入添加
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/d08' and @text='输入成员信息加入企业通讯录']").click()

        # 填写表单信息
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/b3c' and @text='必填']").send_keys("李四")
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/fiv' and @text='手机号']").send_keys(
            "15000000004")
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/b46' and @text='设置部门']").click()
        # 点击确定
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/gkt' and @text='确定(1)']").click()

        # 点击保存
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hxt' and @text='保存']").click()

    def test_hamrest(self):
        assert_that()


    def teardown_class(self):
        sleep(5)
        self.driver.quit()
