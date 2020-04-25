#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

__author__ = 'Jason Liu'


class quick:

# 初始化
    def __init__(self,driver):
        self.driver = driver

# 进入开局配置页面
    def Q_start(self):
        self.driver.find_element_by_id("icon-quickstart").click()

# 选择ap模式或者rt模式
    def Q_mode(self, mode):
        self.driver.implicitly_wait(100)
        modes = self.driver.find_element_by_id("quick_start_mode").get_attribute('value')
        if mode == "ap":
            if mode == modes:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='ap_radio']//span[@class='el-radio__inner']").click()
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_xpath(".//*[@id='div_change_device_mode']/div/div[3]/button[1]/span").click()
                self.driver.implicitly_wait(100)
        else:
            if mode == modes:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='sta_radio']//span[@class='el-radio__inner']").click()
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_xpath(".//*[@id='div_change_device_mode']/div/div[3]/button[1]/span ").click()
                self.driver.implicitly_wait(100)

# rt模式下配置设备信息
    def Qrt(self,devname,devinfo):
        self.driver.find_element_by_id('input_quick_start_device_name').click()
        self.driver.find_element_by_id('input_quick_start_device_name').clear()
        self.driver.find_element_by_id('input_quick_start_device_name').send_keys(devname)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id('input_quick_start_remark').click()
        self.driver.find_element_by_id('input_quick_start_remark').clear()
        self.driver.find_element_by_id('input_quick_start_remark').send_keys(devinfo)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='finish_btn']/span/span").click()
        self.driver.implicitly_wait(100)

# ap模式下配置设备信息，国家码，信道，以及ip地址的分配方式
    def Qap(self,
            devname,
            devinfo,
            country,
            bandwidth,
            channel,
            ipmode = "dhcp",
            ipaddr = "192.168.102.88",
            netmask = "255.255.255.0",
            gateway = "192.168.102.1"):
        self.driver.find_element_by_id('input_quick_start_device_name').click()
        self.driver.find_element_by_id('input_quick_start_device_name').clear()
        self.driver.find_element_by_id('input_quick_start_device_name').send_keys(devname)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id('input_quick_start_remark').click()
        self.driver.find_element_by_id('input_quick_start_remark').clear()
        self.driver.find_element_by_id('input_quick_start_remark').send_keys(devinfo)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//button[@id='next_btn']//*[@id='svg_next']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_country']").click()
        self.driver.find_element_by_xpath("//li[contains(text(),'"+country+"')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_bandwidth']").click()
        if bandwidth == "10M":
            self.driver.find_element_by_xpath("//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'10M')]").click()
        elif bandwidth == "20M":
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'20M')]").click()
        elif bandwidth == "40M+":
            self.driver.find_element_by_xpath(
                "//li[contains(text(),'40M+')]").click()
        elif bandwidth == "40M-":
            self.driver.find_element_by_xpath(
                "//li[contains(text(),'40M-')]").click()
        else:
            self.driver.find_element_by_xpath(
                "//ul[@id='ul_bandwidth']//li[@class='el-select-dropdown__item'][contains(text(),'80M')]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_frequency']").click()
        self.driver.implicitly_wait(100)
        for ch in channel:
            self.driver.find_element_by_xpath("//li[@id='" + ch + "']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_frequency']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='micro_para']/div/div[4]/div/div[2]/button/span/span").click()
        self.driver.implicitly_wait(100)
        modes = self.driver.find_element_by_id("hidden_wizard_ip_config").get_attribute('value')
        if ipmode == "dhcp":
            if ipmode == modes:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='wizard_automatically_radio']//span[@class='el-radio__inner']").click()
        else:
            if ipmode == modes:
                pass
            else:
                self.driver.find_element_by_xpath(
                    "//span[@id='wizard_manually_radio']//span[@class='el-radio__inner']").click()
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_id('input_wizard_dcn_ipaddr').click()
                self.driver.find_element_by_id('input_wizard_dcn_ipaddr').clear()
                self.driver.find_element_by_id('input_wizard_dcn_ipaddr').send_keys(ipaddr)
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_id('input_wizard_dcn_netmask').click()
                self.driver.find_element_by_id('input_wizard_dcn_netmask').clear()
                self.driver.find_element_by_id('input_wizard_dcn_netmask').send_keys(netmask)
                self.driver.implicitly_wait(100)
                self.driver.find_element_by_id('input_wizard_dcn_gateway').click()
                self.driver.find_element_by_id('input_wizard_dcn_gateway').clear()
                self.driver.find_element_by_id('input_wizard_dcn_gateway').send_keys(gateway)
                self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(
            ".//*[@id='ap_finish_btn']/span/span").click()

