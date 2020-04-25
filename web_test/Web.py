# $language = "python"
# $interface = "1.0"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Jason Liu'

optons = webdriver.ChromeOptions()
optons.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=optons)
driver.maximize_window()

class creat_web:

# 初始化
    def __init__(self,local_path):
        self.driver = driver
        self.local_ip = local_path

# 启动浏览器，登入网页
    def login(self,username,password):
        self.driver.get(self.local_ip)  # 打开网页
        self.driver.find_element_by_id('luci_username').click()  # 点击用户名输入框
        self.driver.find_element_by_id('luci_username').send_keys(username)  # 自动敲入用户名
        self.driver.find_element_by_id('luci_password').click()  # 点击密码输入框
        self.driver.find_element_by_id('luci_password').send_keys(password)  # 自动敲入密码
        self.driver.find_element_by_id('login_button').click()  # 点击“登录”按钮
        self.driver.implicitly_wait(100)
        return self.driver

# 退出网页
    def logout(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//span[@class='Header_logout_1otSR']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_class_name("Button_button_Mvymr").click()


# 退出网页，关闭浏览器
    def close(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//span[@class='Header_logout_1otSR']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_class_name("Button_button_Mvymr").click()
        self.driver.implicitly_wait(100)
        # self.driver.close()
        # self.driver.quit()