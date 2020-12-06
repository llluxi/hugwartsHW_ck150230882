from selenium.webdriver.common.by import By

from web.podemo1.page import main_page
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element(By.ID, "username").send_keys("李四")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("ck15002")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("150000000000")
