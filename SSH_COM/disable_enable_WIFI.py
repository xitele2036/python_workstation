#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

import serial
import sys
import os
import time
import paramiko
from io import StringIO
import datetime
import json
from selenium import webdriver



init_path = os.path.dirname(os.path.realpath(__file__))
hostname = "192.168.102.1"
local_path = "https://" + str(hostname)
port = 22
username = "szhw"
password = "Changeme_123"
basepath = "E:"
i = 0
t = 50
t1 = 80

key_str = """-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDAU7yzkwduDZIIE/U3N6uqzVAbB8hADf9vw43OJ+4VdH8i/qMp
1+oZCOkO3gXF7xiApR5zGvxrEETKRoMudxwFijUkfBz8r8e5akT3HQd2YDoCqjJi
eVP27hz/I5CQknFhgRwKwtFgnWu39lMn/s4gZ51EPe2a/oBjivwqqfRkWQIDAQAB
AoGBAJS7rUDKQYKwZ/BrTsWm/dEW+g4NVKWErbfG6VE2u/5Hm1J6zb+8REOcCm/+
70QFBVPnXcbyZaZ+bFRpd2Vlo3qk49HdkyeHma8/BK7yLrntXMxKXAMufE329Xki
ZdQuI91rf0scldmGADtTMZ01upmTRZC4lPeJt8lyltKT6GqpAkEA8TpEX5BVMfNJ
Vi74zcFiMd9NbG/Tzao5/8GHTbJW4YEmVeMFDR17aZC848xIqSEP3YUaNjnShStG
wCW6870N4wJBAMwa2u6hN36hwsgbiikEsmGUNiO5noIgF9rKyz//OfGh+LhBi6U7
NCbtAaly9XtmDLOEjQAq6F+OF9chcw/g2ZMCQGKG+gZOXX3ZcMrSxKzFn+Xe3zC7
PDd0n9vmn+0MOpBAv/e0kguZTx7/Dye7+LGb328LPnmHhIT/+BXjU0janyECQQCZ
yh5usfEjrHUc3ItkztIt7kRA9Or3d4Eh7a3qIcCiTf4fr9ut+4cXUXvwFtvbSBCH
73diyfHflixmgCC3tR+bAkEAvFL1Jq9/Br6MeuCL5fvxMZIKq/gnKEvd6DThyCAI
Bri4UsVmRQ2gwr0aPztzhKIglL0XB6QivBL+wfwCEGxaSA==
-----END RSA PRIVATE KEY-----"""


#private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
#transport = paramiko.Transport(('192.168.2.36',22))
#transport.connect(username='root',pkey=private_key)

private_key = paramiko.RSAKey.from_private_key_file('E:\\works\\Security\\id_rsa102.txt')

s = paramiko.SSHClient()                               # 绑定实例
#s._transport = transport
#s.load_system_host_keys()                                # 加载本地HOST主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
s.connect(hostname,port,username,password,pkey=private_key)
# 连接远程主机
#f = open(r"C:\\Users\\ke.liu\\.PyCharm2018.3\\config\\scratches\\conf.json")
#conf = json.loads(f.read())
#adduser = conf.get("SNMP")

if os.path.exists(basepath + "\\log\\countrycode\\") == False:
    os.makedirs(basepath + "\\log\\countrycode\\")
countrycode_path = basepath + "\\log\\countrycode\\" + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
countrycode_log = open(countrycode_path, 'a+')


def Enable_disabled_wifi(def_user,def_password):
    optons = webdriver.ChromeOptions()
    optons.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=optons)
    driver.maximize_window() #最大化浏览器
    driver.get(local_path) # 打开网页
    time.sleep (3)
    driver.find_element_by_id('luci_username').click() # 点击用户名输入框
    driver.find_element_by_id('luci_username').send_keys(def_user) # 自动敲入用户名
    driver.find_element_by_id('luci_password').click() # 点击密码输入框
    driver.find_element_by_id('luci_password').send_keys(def_password) # 自动敲入密码
    driver.find_element_by_id('login_button').click() # 点击“登录”按钮
    time.sleep(10)
    driver.find_element_by_link_text('微波配置').click()
    time.sleep(10)
    driver.find_element_by_xpath("//span[contains(text(),'高级微波配置')]").click()
    time.sleep(10)
    driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
    time.sleep(10)
    driver.find_element_by_xpath("//div[@id='div_radio_switch']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
    time.sleep(15)
    driver.find_element_by_link_text('退出').click()
    time.sleep(2)
    driver.find_element_by_class_name("Button_button_Mvymr").click()
    driver.close()

def check_wifi_status():
    check = "cfg.lua get wireless.@wifi-iface[1].disabled"
    stdin, stdout, stderr = s.exec_command(check.encode())
    line = stdout.read()
    state = line.decode()[7]
    countrycode_log.write("检查结果：" + line.decode()[7] + '\n\n')
    countrycode_log.flush()
    return state

def change_web():
    change = "cp /tmp/log/html/sysauth.htm /usr/lib/lua/luci/view/sysauth.htm"
    stdin, stdout, stderr = s.exec_command(change.encode())

def main():
    booled = False
    if booled == False:
        change_web()
        booled = True
    cmd = "cfg.lua get wireless.@wifi-iface[1].disabled"
    stdin,stdout,stderr = s.exec_command(cmd.encode())
    line = stdout.read()
    states = line.decode()[7]
    countrycode_log.write(
            '******************************' + datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + ' ******************************\n' + "初始化结果： " + line.decode() + '\n\n')
    countrycode_log.flush()
    num = 0
    for i in range(5):
        if int(states) == num:
            Enable_disabled_wifi(username,password)
            countrycode_log.write("关闭 wifi\n")
            states = check_wifi_status()
        else:
            Enable_disabled_wifi(username,password)
            countrycode_log.write("打开 wifi\n")
            states = check_wifi_status()

    countrycode_log.close()

main()


