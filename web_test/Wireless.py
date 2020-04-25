# $language = "python"
# $interface = "1.0"

import time


__author__ = 'Jason Liu'


class creat_wireless:


#初始化
    def __init__(self,driver):
        self.driver = driver


#首页频谱扫描
    def home_spectrum(self):
        self.driver.find_element_by_xpath(".//*[@id='spectrum_change']/p").click()
        self.driver.implicitly_wait(100)


#首页微波配置
    def home_radio(self):
        self.driver.find_element_by_xpath(".//*[@id='home_page']/div/div/div[1]/ul/li[2]/div/a/p").click()
        self.driver.implicitly_wait(100)


#首页设备警告
    def home_alarm(self):
        self.driver.find_element_by_xpath(".//*[@id='home_page']/div/div/div[1]/ul/li[3]/div/a/p").click()
        self.driver.implicitly_wait(100)


#首页天线对调
    def home_alignment(self):
        self.driver.find_element_by_xpath(".//*[@id='alignment_change']/p").click()
        self.driver.implicitly_wait(100)


# 进入微波配置页面
    def wireless_setting(self):
        self.driver.find_element_by_id("Microwavepage_Select").click()
        self.driver.implicitly_wait(100)


# 进入微波配置页面（二级）
    def radio_setting(self):
        self.driver.find_element_by_id("li_radio_setting").click()
        self.driver.implicitly_wait(100)


# 进入高级微波配置页面
    def advanced_setting(self):
        self.driver.find_element_by_id("li_advanced_radio_setting").click()
        self.driver.implicitly_wait(100)


# 进入接入管理配置页面
    def access_setting(self):
        self.driver.find_element_by_id("li_access_management").click()
        self.driver.implicitly_wait(100)


# 无线开关
    def radio_switch(self,switch):
        rt_disabled_value = self.driver.find_element_by_id("hidden_radio_switch").get_attribute('value')
        if switch == "enable":
            switch_num = 0
        else:
            switch_num = 1
        if int(switch_num) == int(rt_disabled_value):
            pass
        else:
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(
                ".//*[@id='div_radio_switch']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        time.sleep(20)


# jtrans开关
    def jtrans_switch(self,switch):
        jtrans_value = self.driver.find_element_by_id("hidden_jtrans").get_attribute('value')
        if switch == "enable":
            switch_num = 1
        else:
            switch_num = 0
        if int(switch_num) == int(jtrans_value):
            pass
        else:
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//span[@id='span_jtrans_mode']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(".//*[@id='div_jtrans_mode']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        time.sleep(20)


# 配置你想要的模式"ap"或"sta"
    def wireless_mode(self,mode):
        modes = self.driver.find_element_by_id("hidden_mode").get_attribute('value')
        if mode == "ap":
            if mode == modes:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='ap_radio']//span[@class='el-radio__inner']").click()
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_xpath(
                    ".//*[@id='div_change_mode']/div/div[3]/button[1]/span").click()
                self.driver.implicitly_wait(100)
        else:
            if mode == modes:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='sta_radio']//span[@class='el-radio__inner']").click()
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_xpath(
                    ".//*[@id='div_change_mode']/div/div[3]/button[1]/span").click()
                self.driver.implicitly_wait(100)
        time.sleep(10)


#动态选频
    def dynamic_channel(self,dynamic_channel_switch="0"):
        dynamic_channel_switch_value = self.driver.find_element_by_id("hidden_dynamic_channel").get_attribute('value')
        if int(dynamic_channel_switch) == int(dynamic_channel_switch_value):
            pass
        else:
            self.driver.find_element_by_xpath("//span[@id='span_dynamic_channel']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(".//*[@id='div_dynamic_channel']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)


#一键选频
    def Button_1quix(self):
        self.driver.find_element_by_xpath(".//*[@id='button_restart_acs']/span").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='button_restart_acs_yes']/span").click()
        self.driver.implicitly_wait(100)


# 安全控制（AP,默认为关闭）
    def safety_control(self,
                       white_enable="disabled",
                       access_rt_mac="9C:B7:93:00:A1:77",
                       access_mcs="MCS9"):
    #def safety_control(self,access_rt_mac,access_mcs):
        self.driver.find_element_by_xpath("//i[@id='icon_access_mode']").click()
        self.driver.implicitly_wait(100)
        white_enable_value = self.driver.find_element_by_id("hidden_white_enable").get_attribute('value')
        if white_enable == "white_enable_value":
            pass
        else:
            self.driver.find_element_by_xpath(".//*[@id='ul_access_mode']/li[2]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//input[@id='input_rt_mac']").send_keys(access_rt_mac)
            self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_tx_peak_mcs']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//ul[@id='ul_tx_peak_mcs']//li[@class='el-select-dropdown__item'][contains(text(),'" + access_mcs + "')] ").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='div_access_management']/div[3]/button/span").click()
        self.driver.implicitly_wait(100)
        time.sleep(30)


# ap模式下配置国家码需要大写的全称，可以参考华为提供国家码的json文件，"OTHER","ARMENIA"
    def ap_country(self,country):
        self.driver.find_element_by_id("icon_country").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//li[contains(text(),'" + country + "')]").click()
        self.driver.implicitly_wait(100)


# ap模式下配置带宽，"10M","20M","40M-","40M+","80M"
    def ap_bandwidth(self,bandwidth):
        self.driver.find_element_by_id("icon_bandwidth").click()
        self.driver.implicitly_wait(100)
        if bandwidth == "10M":
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'10M')]").click()
        elif bandwidth == "20M":
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'20M')]").click()
        elif bandwidth == "40M+":
            self.driver.find_element_by_xpath("//li[contains(text(),'40M+')]").click()
        elif bandwidth == "40M-":
            self.driver.find_element_by_xpath("//li[contains(text(),'40M-')]").click()
        else:
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'80M')]").click()
        self.driver.implicitly_wait(100)


# ap模式下配置信道，直接频率数字即可，"5180","5745"
    def ap_channel(self,channel):
        self.driver.find_element_by_id("icon_frequency").click()
        self.driver.implicitly_wait(100)
        for ch in channel:
            self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_frequency").click()
        self.driver.implicitly_wait(100)


# ap模式下配置功率
    def ap_power(self,power):
        self.driver.find_element_by_id("input_power").clear()
        self.driver.find_element_by_id("input_power").send_keys(power)
        # if int(power_value) == int(power):
        #     pass
        # elif int(power_value) > int(power):
        #     tmp = int(power_value) - int(power)
        #     for n in range(tmp):
        #         self.driver.find_element_by_xpath("//i[@class='el-icon-minus']").click()
        # else:
        #     tmp = int(power) - int(power_value)
        #     for n in range(tmp):
        #         self.driver.find_element_by_xpath("//i[@class='el-icon-plus']").click()
        self.driver.implicitly_wait(100)


# ap模式下配置SSID
    def ap_ssidname(self,ssidname):
        self.driver.find_element_by_id("input_ssid").click()
        self.driver.find_element_by_id("input_ssid").clear()
        self.driver.find_element_by_id('input_ssid').send_keys(ssidname)
        self.driver.implicitly_wait(100)


# ap模式下配置加密方式与密码
    def ap_secumode(self,secumode,password):
        self.driver.find_element_by_id("icon_encryption").click()
        if secumode == "open":
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_encryption']/li[1]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(
                "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']").click()
        else:
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_encryption']/li[2]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id("input_key").click()
            self.driver.find_element_by_id("input_key").clear()
            self.driver.find_element_by_id('input_key').send_keys(password)


# 保存配置
    def apply(self):
        self.driver.find_element_by_xpath(
            "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']").click()


# rt模式下配置国家码与信道
    def rt_country(self,sta_country,channel):
        self.driver.find_element_by_id("icon_country").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//li[contains(text(),'" + sta_country + "')]").click()
        self.driver.implicitly_wait(100)
        if sta_country == "AUTO":
            pass
        else:
            self.driver.find_element_by_id("icon_frequency").click()
            self.driver.implicitly_wait(100)
            for ch in channel:
                self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id("icon_frequency").click()
            self.driver.implicitly_wait(100)


# rt模式下配置功率
    def rt_power(self,power):
        self.driver.find_element_by_id("input_power").clear()
        self.driver.find_element_by_id("input_power").send_keys(power)
        # if int(power_value) == int(power):
        #     pass
        # elif int(power_value) > int(power):
        #     tmp = int(power_value) - int(power)
        #     for n in range(tmp):
        #         self.driver.find_element_by_xpath("//i[@class='el-icon-minus']").click()
        # else:
        #     tmp = int(power) - int(power_value)
        #     for n in range(tmp):
        #         self.driver.find_element_by_xpath("//i[@class='el-icon-plus']").click()
        self.driver.implicitly_wait(100)


# rt模式下指定MCS
    def rt_mcs(self,mcs):
        self.driver.find_element_by_xpath("//i[@id='icon_mcs']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(
            "//ul[@id='ul_mcs']//li[@class='el-select-dropdown__item'][contains(text(),'MCS" + mcs + "')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(
            "//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']//span[@class='Button_text_1quix'][contains(text(),'保存')]").click()
        self.driver.implicitly_wait(100)


# rt模式下指定AP连接
    def rt_connect(self,ssid,secumode,password):
        self.driver.find_element_by_id("button_specified_ap").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//input[@id='input_specified_ssid']").click()
        self.driver.find_element_by_xpath("//input[@id='input_specified_ssid']").send_keys(ssid)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_specified_encryption").click()
        if secumode == "open":
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_specified_encryption']/li[1]").click()
        else:
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_specified_encryption']/li[2]").click()
            self.driver.find_element_by_id("input_specified_key").click()
            self.driver.find_element_by_id("input_specified_key").send_keys(password)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(
            ".//*[@id='div_connect_specified_ap']/div/div[4]/button[1]/span").click()
        self.driver.implicitly_wait(100)


# rt模式下扫描连接AP
    def rt_connectAP(self,ap_mac,connectAP_key):
        self.driver.find_element_by_xpath("//span[contains(text(),'接入管理')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'重新扫描')]").click()
        time.sleep(10)
        lis = self.driver.find_elements_by_xpath("//div[@id=\"li_ap_table\"]/li")
        for li in lis:
            divs = li.find_elements_by_xpath("./div")
            if divs[2].text == ap_mac:
                auth = divs[4].text
                divs[6].find_element_by_xpath(".//div[contains(text(),'连接')]").click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
        if auth == "NONE":
            pass
        else:
            self.driver.find_element_by_xpath("//input[@id='input_select_ap_key']").send_keys(connectAP_key)
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@id='div_connect_select_ap']//span[@class='Button_text_1quix'][contains(text(),'确定')] ").click()
            time.sleep(2)


# 配置ap模式，懒人专用
    def ap(self,
           country = "OTHER",
           bandwidth = "80M",
           channel = ["5180","5745","5500","5300","5100"],
           power = "19",
           ssidname = "Huawei500",
           secumode = "WPA2-PSK",
           password = "Changeme_123"):
        self.driver.find_element_by_id("Microwavepage_Select").click()
        self.driver.implicitly_wait(100)
        mode = self.driver.find_element_by_id("hidden_mode").get_attribute('value')
        if mode == "ap":
            pass
        else:
            self.driver.find_element_by_xpath("//span[@id='ap_radio']//span[@class='el-radio__inner']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(
                ".//*[@id='div_change_mode']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_country").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//li[contains(text(),'" + country + "')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_bandwidth").click()
        self.driver.implicitly_wait(100)
        if bandwidth == "10M":
            self.driver.find_element_by_xpath("//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'10M')]").click()
        elif bandwidth == "20M":
            self.driver.find_element_by_xpath("//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'20M')]").click()
        elif bandwidth == "40M+":
            self.driver.find_element_by_xpath("//li[contains(text(),'40M+')]").click()
        elif bandwidth == "40M-":
            self.driver.find_element_by_xpath("//li[contains(text(),'40M-')]").click()
        else:
            self.driver.find_element_by_xpath("//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'80M')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_frequency").click()
        self.driver.implicitly_wait(100)
        for ch in channel:
            self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_frequency").click()
        self.driver.implicitly_wait(100)
        power_value = self.driver.find_element_by_id("input_power").get_attribute('value')
        if int(power_value) == int(power):
            pass
        elif int(power_value) > int(power):
            tmp = int(power_value) - int(power)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-minus']").click()
        else:
            tmp = int(power) - int(power_value)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-plus']").click()
        self.driver.find_element_by_id("input_ssid").click()
        self.driver.find_element_by_id("input_ssid").clear()
        self.driver.find_element_by_id('input_ssid').send_keys(ssidname)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_encryption").click()
        if secumode == "open":
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_encryption']/li[1]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']").click()
        else:
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_encryption']/li[2]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id("input_key").click()
            self.driver.find_element_by_id("input_key").clear()
            self.driver.find_element_by_id('input_key').send_keys(password)
            self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']").click()


# 配置rt模式，同样懒人张专用
    def sta(self,
            sta_country = "AUTO",
            channel = ["5180","5745","5500","5300","5100"],
            power = "19",
            mcs = "9",
            ssid = "Huawei500",
            secumode = "WPA2-PSK",
            password = "Changeme_123"):
        self.driver.find_element_by_id("Microwavepage_Select").click()
        self.driver.implicitly_wait(100)
        mode = self.driver.find_element_by_id("hidden_mode").get_attribute('value')
        if mode == "sta":
            pass
        else:
            self.driver.find_element_by_xpath("//span[@id='sta_radio']//span[@class='el-radio__inner']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(
                ".//*[@id='div_change_mode']/div/div[3]/button[1]/span").click()
            self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_country").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//li[contains(text(),'" + sta_country + "')]").click()
        self.driver.implicitly_wait(100)
        if sta_country == "AUTO":
            pass
        else:
            self.driver.find_element_by_id("icon_frequency").click()
            self.driver.implicitly_wait(100)
            for ch in channel:
                self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id("icon_frequency").click()
            self.driver.implicitly_wait(100)
        power_value = self.driver.find_element_by_id("input_power").get_attribute('value')
        if int(power_value) == int(power):
            pass
        elif int(power_value) > int(power):
            tmp = int(power_value) - int(power)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-minus']").click()
        else:
            tmp = int(power) - int(power_value)
            for n in range(tmp):
                self.driver.find_element_by_xpath("//i[@class='el-icon-plus']").click()
        self.driver.find_element_by_id("icon_mcs").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//ul[@id='ul_mcs']//li[@class='el-select-dropdown__item'][contains(text(),'MCS" + mcs + "')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("li_access_management").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("button_specified_ap").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("input_specified_ssid").click()
        self.driver.find_element_by_id("input_specified_ssid").send_keys(ssid)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("icon_specified_encryption").click()
        if secumode == "open":
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_encryption']/li[1]").click()
        else:
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_specified_encryption']/li[2]").click()
            self.driver.find_element_by_id("input_specified_key").click()
            self.driver.find_element_by_id("input_specified_key").send_keys(password)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(
            ".//*[@id='div_connect_specified_ap']/div/div[4]/button[1]/span").click()
        self.driver.implicitly_wait(100)