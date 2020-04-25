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
from selenium import webdriver
from pysnmp.hlapi import *
from SSH import SSHCreat


init_path = os.path.dirname(os.path.realpath(__file__))
hostnames = "192.168.102.1"
localnames = "192.168.102.2"
local_path = "https://" + str(hostnames)
port = 22
username = "szhw"
username1 = "dandan"
password = "Changeme_123"
basepath = "E:"

hostname = "192.168.102.1"
SS = SSHCreat(username1, password, hostname)
SS.connect()


#SS.send("login_shell")

if os.path.exists(basepath + "\\log\\weibo\\") == False:
    os.makedirs(basepath + "\\log\\weibo\\")
weibo_path = basepath + "\\log\\weibo\\" + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
weibo_log = open(weibo_path, 'a+')


def mode_wireless():
    wifi_mode = SS.send("cfg.lua get wireless.@wifi-iface[1].mode")
    print(wifi_mode[7:10])
    #weibo_log.write(str(mode[7:10]))
    #weibo_log.flush()
    return wifi_mode

def disabled_wireless():
    wifi_disabled = SS.send("cfg.lua get wireless.@wifi-iface[1].disabled")
    print(wifi_disabled[7:8])
    return wifi_disabled

def ssid_wireless():
    wifi_ssid = SS.send("cfg.lua get wireless.@wifi-iface[1].ssid")
    print(wifi_ssid[7:16])
    return wifi_ssid


def weibo(username,password):
    num = 0
    #weibo_log.write(str(mode[7:10]) + str(disabled[7:8]) + str(ssid[7:16]))
    #weibo_log.flush()
    optons = webdriver.ChromeOptions()
    optons.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=optons)
    driver.maximize_window() #最大化浏览器
    driver.get(local_path) # 打开网页
    time.sleep (3)
    driver.find_element_by_id('luci_username').click() # 点击用户名输入框
    driver.find_element_by_id('luci_username').send_keys(username) # 自动敲入用户名
    driver.find_element_by_id('luci_password').click() # 点击密码输入框
    driver.find_element_by_id('luci_password').send_keys(password) # 自动敲入密码
    driver.find_element_by_id('login_button').click() # 点击“登录”按钮
    time.sleep(10)
    driver.find_element_by_xpath("//a[contains(text(),'微波配置')]").click()
    time.sleep(10)
    #driver.find_element_by_xpath("//i[@id='icon_country']").click()
    #time.sleep(10)
    #driver.find_element_by_xpath("//li[contains(text(),'VENEZUELA')]").click()
    #time.sleep(10)
    driver.find_element_by_xpath("//span[contains(text(),'高级微波配置')]").click()
    time.sleep(10)
    weibo_log.write("-----------------当前微波开关------------------\n")
    time.sleep(3)
    mode = mode_wireless()
    time.sleep(3)
    disabled = disabled_wireless()
    time.sleep(3)
    ssid = ssid_wireless()
    time.sleep(3)
    # mode = SS.send("cfg.lua get wireless.@wifi-iface[1].mode")
    # print(mode)
    # time.sleep(3)
    # disabled = SS.send("cfg.lua get wireless.@wifi-iface[1].disabled")
    # time.sleep(3)
    # ssid = SS.send("cfg.lua get wireless.@wifi-iface[1].ssid")
    # time.sleep(3)
    weibo_log.write( "模式：" + str(mode[7:10]) + "  disabled:" + str(disabled[7:8]) + "  ssid:" + str(ssid[7:16]))
    weibo_log.flush()
    time.sleep(5)
    weibo_log.write("-----------------循环微波开关------------------\n")
    while True:
        wifi = driver.find_element_by_id("hidden_radio_switch").get_attribute('value')
        print(wifi)
        #print("当前wifi状态"+wifi)
        num = num + 1
        #SS = SSH.SSHConnect(username, password, hostname)
        #mode = SS.send("cfg.lua get wireless.@wifi-iface[1].mode")
        #disabled = SS.send("cfg.lua get wireless.@wifi-iface[1].disabled")
        #ssid = SS.send("cfg.lua get wireless.@wifi-iface[1].ssid")
        if int(wifi) == 0:
            # pass
            driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@id='div_radio_switch']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
            #driver.find_element_by_xpath("//*[@id='div_radio_switch']/div/div[3]/button[1]/span").click()
            time.sleep(35)
            mode = mode_wireless()
            print(mode)
            time.sleep(3)
            disabled = disabled_wireless()
            time.sleep(3)
            ssid = ssid_wireless()
            time.sleep(3)
            # mode = SS.send("cfg.lua get wireless.@wifi-iface[1].mode")
            # print(mode)
            # time.sleep(3)
            # disabled = SS.send("cfg.lua get wireless.@wifi-iface[1].disabled")
            # time.sleep(3)
            # ssid = SS.send("cfg.lua get wireless.@wifi-iface[1].ssid")
            # time.sleep(3)
            #snmp = SS.send("cfg.lua show snmpd")
            #print(snmp)
            weibo_log.write("成功次数：" + str(num) + "  微波关闭\n" + "模式：" + str(mode[7:10]) + "  disabled:" + str(disabled[7:8]) + "  ssid:" + str(ssid[7:16]))
            weibo_log.flush()
            time.sleep(30)
        else:
            time.sleep(5)
            driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@id='div_radio_switch']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
            time.sleep(35)
            mode = mode_wireless()
            print(mode)
            time.sleep(3)
            disabled = disabled_wireless()
            time.sleep(3)
            ssid = ssid_wireless()
            # time.sleep(3)
            # mode = SS.send("cfg.lua get wireless.@wifi-iface[1].mode")
            # print(mode)
            # time.sleep(3)
            # disabled = SS.send("cfg.lua get wireless.@wifi-iface[1].disabled")
            # time.sleep(3)
            # ssid = SS.send("cfg.lua get wireless.@wifi-iface[1].ssid")
            time.sleep(3)
            weibo_log.write("成功次数：" + str(num) + "  微波开启\n" + "模式：" + str(mode[7:10]) + "  disabled:" + str(disabled[7:8]) + "  ssid:" + str(ssid[7:16]))
            weibo_log.flush()
            time.sleep(30)


def main():

    weibo(username,password)

main()
