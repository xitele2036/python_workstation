# $language = "python"
# $interface = "1.0"

import time


__author__ = 'zhangdandan'


class rt_wireless:
    def __init__(self,driver):
        self.driver = driver

    def sta(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'微波配置')]").click()
        time.sleep(3)
        mode = self.driver.find_element_by_id("hidden_mode").get_attribute('value')
        if mode == "sta":
            pass
        else:
            self.driver.find_element_by_xpath("//span[@id='sta_radio']//span[@class='el-radio__inner']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                "//div[@id='div_change_mode']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
            time.sleep(35)

    def rt_country(self,sta_country,channel):
        self.driver.find_element_by_xpath("//i[@id='icon_country']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//li[contains(text(),'" + sta_country + "')]").click()
        time.sleep(2)
        if sta_country == "AUTO":
            pass
        else:
            self.driver.find_element_by_xpath("//i[@id='icon_frequency']").click()
            time.sleep(2)
            for ch in channel:
                self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//i[@id='icon_frequency']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']//span[@class='Button_text_1quix'][contains(text(),'保存')]").click()
            time.sleep(10)

    def rt_mcs(self,mcs):
        self.driver.find_element_by_xpath("//i[@id='icon_mcs']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//ul[@id='ul_mcs']//li[@class='el-select-dropdown__item'][contains(text(),'MCS" + mcs + "')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']//span[@class='Button_text_1quix'][contains(text(),'保存')]").click()
        time.sleep(10)

    def rt_power(self,power):
        power_value = self.driver.find_element_by_id("input_power").get_attribute('value')
        if int(power_value) == int(power):
            pass
        elif int(power_value) > int(power):
            tmp = int(power_value) - int(power)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-minus']").click()
            self.driver.find_element_by_xpath(
                "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']//span[@class='Button_text_1quix'][contains(text(),'保存')]").click()
            time.sleep(10)
        else:
            tmp = int(power) - int(power_value)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-plus']").click()
            self.driver.find_element_by_xpath(
                "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']//span[@class='Button_text_1quix'][contains(text(),'保存')]").click()
            time.sleep(10)

    def rt_ssid_key(self,ssid,encryption,key):
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[@class='Button_text_1quix'][contains(text(),'连接指定AP')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='input_specified_ssid']").click()
        self.driver.find_element_by_xpath("//input[@id='input_specified_ssid']").send_keys(ssid)
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@id='icon_specified_encryption']").click()
        if encryption == "open":
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_specified_encryption']//li[@class='el-select-dropdown__item'][contains(text(),'不加密')]").click()
        else:
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_specified_encryption']//li[@class='el-select-dropdown__item'][contains(text(),'WPA2-PSK')]").click()
            self.driver.find_element_by_xpath("//input[@id='input_specified_key']").click()
            self.driver.find_element_by_xpath("//input[@id='input_specified_key']").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//div[@id='div_connect_specified_ap']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
        time.sleep(10)

    def rt_connectAP(self,connectAP_key):
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'重新扫描')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        time.sleep(2)
        BSSID_value = self.driver.find_element_by_id("hidden_bssid").get_attribute('value')
        new_BSSID_value = BSSID_value.split(",")
        print(new_BSSID_value)
        BSSID_value_num = new_BSSID_value.index("9C:B7:93:00:A1:77")
        self.driver.find_element_by_xpath("//div[@id='div_connect_" + str(BSSID_value_num) + "']").click()
        #self.driver.find_element_by_id().get_attribute()
        encryption_value =self.driver.find_element_by_id("hidden_auth").get_attribute('value')
        new_encryption_value =encryption_value.split(",")
        if BSSID_value_num ==new_encryption_value.index("off"):
            pass
        else:
            self.driver.find_element_by_xpath("//input[@id='input_select_ap_key']").send_keys(connectAP_key)
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@id='div_connect_select_ap']//span[@class='Button_text_1quix'][contains(text(),'确定')] ").click()
            time.sleep(2)


    def advanced_setting(self):
        self.driver.find_element_by_id("li_advanced_radio_setting").click()
        self.driver.implicitly_wait(100)


    def rt_radio_switch(self,rt_disabled):
        rt_disabled_value = self.driver.find_element_by_id("hidden_radio_switch").get_attribute('value')
        print(rt_disabled_value)
        if int(rt_disabled) == int(rt_disabled_value):
            pass
        else:
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(
                ".//*[@id='div_radio_switch']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        time.sleep(20)

    def rt_JTRANS(self,JTRANS):
        jtrans_value = self.driver.find_element_by_id("hidden_jtrans").get_attribute('value')
        print(jtrans_value)
        if int(JTRANS) == int(jtrans_value):
            pass
        else:
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//span[@id='span_jtrans_mode']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(".//*[@id='div_jtrans_mode']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        time.sleep(20)

    def rt_disconnect(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//span[contains(text(),'Disconnect')]").click()
        self.driver.implicitly_wait(100)







    def rt_reconnect(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[contains(text(),'Reconnect')]").click()
        time.sleep(30)
























