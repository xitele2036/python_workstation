#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from SSH import SSHCreat
import os
import random
import string
import time
import json
import serial
import sys
import time
from io import StringIO
import datetime
from selenium import webdriver
from pysnmp.hlapi import *
from User import user
from Snmp import snmp
from Web import creat_web
from Wireless import creat_wireless
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from readconf import ReadConfig
from Quick import quick
from RT_wireless import rt_wireless



init_path = os.path.dirname(os.path.realpath(__file__))
hostnames = "129.9.6.88"

username1 = "lct"
username = "jason"
password = "HuaweiR34"
local_path = "https://" + hostnames
hostpaths = "192.168.102.1"
localpaths = "192.168.102.2"
v3trapnames = "trap001"
authtypes = "MD5"
authkeyss = "Changeme_123"
encrypttypes = "AES"
encryptkeys = "Changeme_123"
versions = "V1"
readnames = "public123"
writenames = "public123"
port_ids = "162"
communitys = "root@123"
countrys = "OTHER" # 大写国家全称
bandwidths = "80M" # 10M,20M,40M-,40M+,80M
channels = ["5180","5745","5500","5300","5100"]
ssid = "BULL_DOG"
secu = "secu" # open,secu
passwd = "Changeme_123"
mcss = "9"
sta_countrys = "AUTO"
powers = "1"
user = ["dandan","batianhu","tomme","xueshan","jason","xuhao","benren","yucheng","jiali","ouyang","junwen","shengli","xinren","duandi"]




def main():
    weboper = creat_web(local_path)
    driver = weboper.login(username, password)
    # for x in range(3,5):
    #     smp = snmp(driver, "192.168.10."+ str(x))
    #     smp.creat_snmp("V1", driver)
    # for x in range(9,10):
    #     smp = snmp(driver, "192.168.10." + str(x))
    #     smp.creat_snmp("V2", driver)
    # for x in range(123,200):
    #     smp = snmp(driver, "192.168.10." + str(x))
    #     smp.creat_snmp("V3", driver)
    while True:
        smp = snmp(driver, "192.168.102.116")
        smp.creat_snmp("V3", driver)
        smp.snmp_setting()
        smp.snmp_del("192.168.102.116", "SNMP V3")

main()

