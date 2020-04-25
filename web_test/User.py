# $language = "python"
# $interface = "1.0"

import time


__author__ = 'Jason Liu'


class user():


# 初始化
    def __init__(self,driver):
        self.driver = driver


# 进入用户配置界面
    def user_setting(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//img[@id='down_pic']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id('Accountpage_Select').click()
        self.driver.implicitly_wait(100)


# 创建新的管理员用户
    def user_creat(self,new_username,new_password):
        self.driver.find_element_by_xpath("//div[@class='Tab_container_1z3z2']//span[1]").click()
        self.driver.find_element_by_id('input_username').click()
        self.driver.find_element_by_id('input_username').send_keys(new_username)
        self.driver.find_element_by_id('icon_user_group').click()
        self.driver.find_element_by_xpath("//li[@value='1']").click()
        self.driver.find_element_by_id('input_newpassword').click()
        self.driver.find_element_by_id('input_newpassword').send_keys(new_password)
        self.driver.find_element_by_id('input_confirmpassword').click()
        self.driver.find_element_by_id('input_confirmpassword').send_keys(new_password)
        self.driver.find_element_by_xpath(".//*[@id=\"div_add_account\"]/div/div[3]/button[1]/span").click()
        time.sleep(30)
        # self.driver.implicitly_wait(100)
        # self.driver.find_element_by_id('Homepage_Select').click()
        # self.driver.implicitly_wait(100)


# 删除用户
    def user_del(self,name):
        lis = self.driver.find_elements_by_xpath("//div[@id=\"div_account_access_list\"]/li")
        # print(type(lis))
        for li in lis:
            divs = li.find_elements_by_xpath("./div")
            if divs[0].text == name:
                divs[3].find_element_by_xpath("./button[contains(@id,\"account_del\")]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='div_confirm_delete']/div/div[3]/button[1]/span").click()
        time.sleep(10)





