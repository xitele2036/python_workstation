#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

__author__ = 'Jason Liu'

class snmp:

# 初始化
    def __init__(self,driver,localpath):
        self.localpath = localpath
        self.driver = driver


# 进入snmp的配置页面
    def snmp_setting(self):
        self.driver.find_element_by_id('Devicepage_Select').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id('li_network_config').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='snmp_access_model']/div/button/span").click()
        self.driver.implicitly_wait(100)


# snmp的密码复杂度校验开关
    def snmp_comp(self,comple):
        Comp = self.driver.find_element_by_id("hidden_community_complexity_verify").get_attribute('value')
        if comple == "enabled":
            if Comp == comple:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='span_community_complexity_verify']").click()
        else:
            if Comp == comple:
                pass
            else:
                self.driver.find_element_by_xpath("//span[@id='span_community_complexity_verify']").click()


# snmp配置协议版本
    def snmp_access(self,ver):
        self.driver.find_element_by_xpath("//i[@id='icon_access_snmp_version']").click()
        if ver == "V1" or ver == "V2" or ver == "V3":
            self.driver.find_element_by_xpath("//ul[@id='ul_access_snmp_version']//li[@class='el-select-dropdown__item'][contains(text(),'SNMP " + ver + "')]").click()
        else:
            self.driver.find_element_by_xpath("//ul[@id='ul_access_snmp_version']//li[@class='el-select-dropdown__item'][contains(text(),'All')]").click()

# snmp页面的应用
    def snmp_apply(self):
        self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa Button_button-size--auto_LZhGd SNMPAccessManage_apply-btn_peHaJ']//span[@class='Button_text_1quix']").click()

# snmp添加配置
    def snmp_add(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//span[@class='Button_text_1quix']//div").click()
        self.driver.implicitly_wait(100)

# 通过ip和版本来判断要编辑snmp协议
    def snmp_edit(self,ipaddr,version):
        lis = self.driver.find_elements_by_xpath("//div[@id=\"div_snmp_access_list\"]/li")
        for li in lis:
            divs = li.find_elements_by_xpath("./div")
            if divs[0].text == ipaddr and divs[2].text == version:
                    divs[4].find_element_by_xpath(".//span[contains(text(),'编辑')]").click()
        self.driver.implicitly_wait(100)
        time.sleep(5)


# 通过ip和版本来删除snmp协议
    def snmp_del(self,ipaddr,version):
        lis = self.driver.find_elements_by_xpath("//div[@id=\"div_snmp_access_list\"]/li")
        for li in lis:
            divs = li.find_elements_by_xpath("./div")
            if divs[0].text == ipaddr and divs[2].text == version:
                    divs[4].find_element_by_xpath(".//span[contains(text(),'删除')]").click()
        self.driver.implicitly_wait(100)
        time.sleep(5)


# 配置NMS的ip地址
    def snmp_ip(self,ip):
        self.driver.find_element_by_id('input_nms_ip_address').click()
        self.driver.find_element_by_id('input_nms_ip_address').clear()
        self.driver.find_element_by_id('input_nms_ip_address').send_keys(ip)
        self.driver.implicitly_wait(100)

# 配置v1v2v3协议的读写权限
    def snmp_permission(self,permission):
        self.driver.find_element_by_xpath(".//*[@id='icon_permission']").click()
        if permission == "readonly":
            self.driver.find_element_by_xpath(".//*[@id='ul_permission']/li[1]").click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='ul_permission']/li[2]").click()


# 配置v1v2协议下读的团体名
    def snmp_read(self,readname):
        self.driver.find_element_by_id('input_read_community_name').click()
        self.driver.find_element_by_id('input_read_community_name').clear()
        self.driver.find_element_by_id('input_read_community_name').send_keys(readname)
        self.driver.implicitly_wait(100)


# 配置v1v2协议下写的团体名
    def snmp_write(self,writename):
        self.driver.find_element_by_id('input_write_community_name').click()
        self.driver.find_element_by_id('input_write_community_name').clear()
        self.driver.find_element_by_id('input_write_community_name').send_keys(writename)
        self.driver.implicitly_wait(100)


# 配置snmp的端口号
    def snmp_port(self,port_id):
        self.driver.find_element_by_id('input_trap_port').click()
        self.driver.find_element_by_id('input_trap_port').clear()
        self.driver.find_element_by_id('input_trap_port').send_keys(port_id)
        self.driver.implicitly_wait(100)


# 配置snmp携带信息
    def snmp_community(self,community):
        self.driver.find_element_by_id('input_trap_community').click()
        self.driver.find_element_by_id('input_trap_community').clear()
        self.driver.find_element_by_id('input_trap_community').send_keys(community)
        self.driver.implicitly_wait(100)


# 配置sdh的上报开关
    def snmp_sdh(self,sdh):
        self.driver.find_element_by_id('icon_sdh_trap').click()
        if sdh == "trap":
            self.driver.find_element_by_xpath("//div[@id='list_sdh_trap']//li[1]").click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='ul_sdh_trap']/li[2]").click()
        self.driver.implicitly_wait(100)


# 配置rmon的上报开关
    def snmp_rmon(self,rmon):
        self.driver.find_element_by_id('icon_rmon_trap').click()
        if rmon == "trap":
            self.driver.find_element_by_xpath("//div[@id='list_rmon_trap']//li[1]").click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='ul_rmon_trap']/li[2]").click()
        self.driver.implicitly_wait(100)


# 配置alarm的上报开关
    def snmp_alarm(self,alarm):
        self.driver.find_element_by_id('icon_alarm_trap').click()
        if alarm == "trap":
            self.driver.find_element_by_xpath("//div[@id='list_alarm_trap']//li[1]").click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='ul_alarm_trap']/li[2]").click()
        self.driver.implicitly_wait(100)

# 配置snmp的版本
    def snmp_version(self,version):
        self.driver.find_element_by_id('icon_trap_version').click()
        self.driver.find_element_by_xpath("//ul[@id='ul_trap_version']//li[@class='el-select-dropdown__item'][contains(text(),'SNMP " + version + "')]").click()
        self.driver.implicitly_wait(100)

# 配置snmpv3用户的用户名
    def snmp_trapname(self,trapname):
        self.driver.find_element_by_id('input_trap_user_name').click()
        self.driver.find_element_by_id('input_trap_user_name').clear()
        self.driver.find_element_by_id('input_trap_user_name').send_keys(trapname)
        self.driver.implicitly_wait(100)

# 配置snmpv3用户校验的等级
    def snmp_traplevel(self):
        self.driver.find_element_by_xpath("//i[@id='icon_trap_level']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='ul_trap_level']/li").click()
        self.driver.implicitly_wait(100)

# 配置snmpv3用户的验证模式
    def snmp_auth(self,auth):
        self.driver.find_element_by_xpath("//i[@id='icon_trap_authentication']").click()
        self.driver.implicitly_wait(100)
        if auth == "MD5":
            self.driver.find_element_by_xpath("//li[contains(text(),'MD5')]").click()
            self.driver.implicitly_wait(100)
        else:
            self.driver.find_element_by_xpath("//li[contains(text(),'SHA')]").click()
            self.driver.implicitly_wait(100)

# 配置snmpv3用户的验证密码
    def snmp_authkey(self,authkey):
        self.driver.find_element_by_id('input_trap_auth_key').click()
        self.driver.find_element_by_id('input_trap_auth_key').clear()
        self.driver.find_element_by_id('input_trap_auth_key').send_keys(authkey)
        self.driver.implicitly_wait(100)

# 配置snmpv3用户的加密模式
    def snmp_encr(self,encr):
        self.driver.find_element_by_xpath("//i[@id='icon_trap_encryption']").click()
        self.driver.implicitly_wait(100)
        if encr == "DES":
            self.driver.find_element_by_xpath("//li[contains(text(),'DES')]").click()
            self.driver.implicitly_wait(100)
        else:
            self.driver.find_element_by_xpath("//li[contains(text(),'AES')]").click()
            self.driver.implicitly_wait(100)

# 配置snmpv3用户的加密密码
    def snmp_encrkey(self,encryptkey):
        self.driver.find_element_by_id('input_trap_encrypt_key').click()
        self.driver.find_element_by_id('input_trap_encrypt_key').clear()
        self.driver.find_element_by_id('input_trap_encrypt_key').send_keys(encryptkey)
        self.driver.implicitly_wait(100)

# 保存配置
    def snmp_save(self):
        self.driver.find_element_by_xpath(
            ".//*[@id='div_snmp_add']/div[2]/div/div[3]/div/div[2]/button/span/span").click()
        self.driver.implicitly_wait(100)

# 取消，不保存配置
    def snmp_cancel(self):
        self.driver.find_element_by_xpath(
            ".//*[@id='div_snmp_add']/div[2]/div/div[3]/div/div[1]/button/span/span").click()
        self.driver.implicitly_wait(100)

# 创建默认的snmp协议，懒人专用
    def creat_snmp(self,
                   ver,
                   permission = "readwrite",
                   readname = "public@HWR3",
                   writename = "private@HWR3",
                   port_id = "162",
                   community = "Root@123",
                   trapname = "OID_test_one",
                   authtype = "MD5",
                   authkeys = "HuaweiR3",
                   encrypttype = "AES",
                   encryptkey = "HuaweiR3"
                   ):
        time.sleep(3)
        self.driver.find_element_by_id('Devicepage_Select').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id('li_network_config').click()
        time.sleep(3)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(".//*[@id='snmp_access_model']/div/button/span/span").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//span[@class='Button_text_1quix']//div").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//i[@id='icon_trap_version']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//div[@class='el-select']//li[@class='el-select-dropdown__item'][contains(text(),'SNMP " + ver + "')]").click()
        self.driver.implicitly_wait(100)
        if str(ver) == "V1" or (ver) == "V2":
            self.driver.find_element_by_id('input_nms_ip_address').click()
            self.driver.find_element_by_id('input_nms_ip_address').send_keys(self.localpath)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(".//*[@id='icon_permission']").click()
            if permission == "readonly":
                self.driver.find_element_by_xpath(".//*[@id='ul_permission']/li[1]").click()
            else:
                self.driver.find_element_by_xpath(".//*[@id='ul_permission']/li[2]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_read_community_name').click()
            self.driver.find_element_by_id('input_read_community_name').send_keys(readname)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_write_community_name').click()
            self.driver.find_element_by_id('input_write_community_name').send_keys(writename)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_trap_port').click()
            self.driver.find_element_by_id('input_trap_port').send_keys(port_id)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_trap_community').click()
            self.driver.find_element_by_id('input_trap_community').send_keys(community)
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_sdh_trap').click()
            self.driver.find_element_by_xpath(".//*[@id='ul_sdh_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_rmon_trap').click()
            self.driver.find_element_by_xpath(".//*[@id='ul_rmon_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_alarm_trap').click()
            self.driver.find_element_by_xpath(".//*[@id='ul_alarm_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            time.sleep(3)
            self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa Button_button-size--auto_LZhGd']//span[@class='ButtonGroup_button-text_MiN_s']").click()
            self.driver.implicitly_wait(100)
            time.sleep(30)

        else:
            self.driver.find_element_by_id('input_nms_ip_address').click()
            self.driver.find_element_by_id('input_nms_ip_address').send_keys(self.localpath)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//i[@id='icon_permission']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//li[contains(text(),'Read/Write')]").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_trap_port').click()
            self.driver.find_element_by_id('input_trap_port').send_keys(port_id)
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_sdh_trap').click()
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_sdh_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_rmon_trap').click()
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_rmon_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('icon_alarm_trap').click()
            self.driver.find_element_by_xpath(
                ".//*[@id='ul_alarm_trap']/li[1]").click()
            self.driver.implicitly_wait(100)
            # time.sleep(3)
            self.driver.find_element_by_id('input_trap_user_name').click()
            self.driver.find_element_by_id('input_trap_user_name').send_keys(trapname)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//i[@id='icon_trap_level']").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(".//*[@id='ul_trap_level']/li").click()
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//i[@id='icon_trap_authentication']").click()
            self.driver.implicitly_wait(100)
            if authtype == "MD5":
                self.driver.find_element_by_xpath("//li[contains(text(),'MD5')]").click()
                self.driver.implicitly_wait(100)
            else:
                self.driver.find_element_by_xpath("//li[contains(text(),'SHA')]").click()
                self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_trap_auth_key').click()
            self.driver.find_element_by_id('input_trap_auth_key').send_keys(authkeys)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath("//i[@id='icon_trap_encryption']").click()
            self.driver.implicitly_wait(100)
            if encrypttype == "DES":
                self.driver.find_element_by_xpath("//li[contains(text(),'DES')]").click()
                self.driver.implicitly_wait(100)
            else:
                self.driver.find_element_by_xpath("//li[contains(text(),'AES')]").click()
                self.driver.implicitly_wait(100)
            self.driver.find_element_by_id('input_trap_encrypt_key').click()
            self.driver.find_element_by_id('input_trap_encrypt_key').send_keys(encryptkey)
            self.driver.implicitly_wait(100)
            time.sleep(3)
            self.driver.find_element_by_xpath("//button[@class='Button_button_Mvymr Button_button-theme--primary_1GgVa Button_button-size--auto_LZhGd']//span[@class='ButtonGroup_button-text_MiN_s']").click()
            self.driver.implicitly_wait(100)
            time.sleep(30)

