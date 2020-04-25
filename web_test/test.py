#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from SSH import SSHCreat
import os
import threading
import random
import string
import time
import json
import serial
import sys
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
hostnames = "172.16.40.150"



image_2347 = r"C:\Users\ke.liu\Desktop\image_2347.img"
image_2348 = r"C:\Users\ke.liu\Desktop\image_2348.img"
img_list = [image_2347,image_2348]

basepath = "E:"
username = "szhw"
password = "Changeme_1234"
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
channels = ["5180","5260","5500","5580","5745"]
ssid = "BULL_DOG"
secu = "secu" # open,secu
passwd = "Changeme_123"
mcss = "9"
sta_countrys = "AUTO"
powers = "1"
user = ["dandan","batianhu","tomme","xueshan","jason","xuhao","benren","yucheng","jiali","ouyang","junwen","shengli","xinren","duandi"]


def main():
    # if os.path.exists(basepath + "\\log\\") == False:
    #     os.makedirs(basepath + "\\log\\")
    # version_path = basepath + "\\log\\" + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
    # version_log = open(version_path, 'a+')
    us = creat_web(local_path)
    while True:
        # for img in img_list:
        #     version_log.write("升级版本:"+img[24:34] + '\n')
        #     ver_bf = img[30:34]
        us.login(username,password)
        time.sleep(20)
            # driver.find_element_by_id('Devicepage_Select').click()
            # time.sleep(3)
            # driver.find_element_by_id('btn_flashops').click()
            # time.sleep(3)
            # driver.find_element_by_id("image").send_keys(img)
            # time.sleep(3)
            # driver.find_element_by_xpath("//*[@id=\"upgrade_form\"]/div/div[1]/div/div/input[4]").click()
            # time.sleep(30)
            # driver.find_element_by_xpath("//*[@id=\"device_page\"]/div/div/div/div/div[2]/div/form[2]/input[4]").click()
        us.logout()
        time.sleep(20)
    #         time.sleep(300)
    #         ss = SSHCreat(username, password, hostnames)
    #         ss.connect()
    #         result = ss.sends("cfg.lua get_version")
    #         version_log.write("升级后版本:"+ result)
    #         ver_af = result[12:16]
    #         if ver_bf != ver_af:
    #             version_log.write("升级不成功 " + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '\n\n')
    #         else:
    #             version_log.write("升级成功\n\n")
    #         ss.close()
    #         version_log.flush()
    # version_log.close()
    # while True:
    #     try:
    #         ss2 = SSHCreat(username, password, hostnames)
    #         ss2.connect()
    #         ss2.send("sysupgrade /tmp/nand_reserve/R3_V1.0.2746.dakota_huawei_Debug_20200323.img")
    #         print("update system\n")
    #         version_log.write("update system\n")
    #         # ss2.close()
    #         print("SSH close\n")
    #         version_log.write("SSH close\n")
    #         version_log.flush()
    #     except:
    #         version_log.write("connect fail\n")
    #         version_log.flush()
    #         print("connect fail\n")
    #     else:
    #         version_log.write("device reboot & wait 300s\n"+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    #         version_log.flush()
    #         print("device reboot & wait 300s\n"+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    #         time.sleep(180)
    #         print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    #
    # version_log.close()

    # ss3 = SSHCreat(usernamess, password, hostnames)
    # ss3.connect()
    # results = ss3.send("cfg.lua show usermanage")
    # print(results)
    # ss3.close()
    # ss2 = SSHCreat(usernames, password, hostnames)
    # print(ss2.connect())
    # result = ss.send("cfg.lua show usermanage")
    # for t in t_list:
    #         t.join()
    # thread_list = []
    # for i in range(10):
    #     t = threading.Thread(target=test(ss))
    #     thread_list.append(t)
    #
    # for i in thread_list:
    #     i.start()
    #     i.join()
    #     print(threading.current_thread())




    # d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
    # d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
    # delta = d1 - d2
    # print(delta.days)
    # num = "1000"
    # a = "var action=document.documentElement.scrollTop=" + str(num) + '"'
    # print(a)
    # cff = ReadConfig()
    # dut_ip = cff.getConfVal("DUT", "DUT_IP")
    # ssh_ip = cff.getConfVal("SSH", "ssh_user1")
    # print(dut_ip)
    # print(ssh_ip)weboper = creat_web(local_path)
    # driver = weboper.login(username, password)
    # wifi = creat_wireless(driver)
    # wifi.wireless_setting()
    # wifi.advanced_setting()
    # wifi.jtrans_switch("enable")
    # wifi.radio_switch("enable")
    #
    # wifi.radio_setting()
    # wifi.wireless_mode("ap")
    # wifi.ap_country("UNITED STATES")
    # wifi.ap_bandwidth("80M")
    # wifi.ap_channel(channels)
    # wifi.ap_power("20")
    # wifi.ap_ssidname("FUCK")
    # wifi.ap_secumode("no-open","Changeme_123")
    # wifi.apply()
    # time.sleep(10)
    # wifi.wireless_mode("sta")
    # wifi.rt_country("AUTO",channels)
    # wifi.rt_power("25")
    # wifi.rt_mcs("8")
    # wifi.apply()
    # time.sleep(30)
    # wifi.access_setting()
    # wifi.rt_connectAP("9C-B7-93-E6-EA-AD","12345678")

    # smp = snmp(driver,"192.168.102.2")
    # smp.snmp_setting()
    # time.sleep(5)
    # smp.snmp_add()
    # smp.snmp_version("V3")
    # smp.snmp_ip("199.199.199.6")
    # smp.snmp_permission("readwrite")
    # smp.snmp_port("65500")
    # smp.snmp_sdh("trap")
    # smp.snmp_rmon("trap")
    # smp.snmp_alarm("trap")
    # smp.snmp_trapname("jason@123")
    # smp.snmp_traplevel()
    # smp.snmp_auth("MD5")
    # smp.snmp_authkey("HuaweiR3")
    # smp.snmp_encr("MD5")
    # smp.snmp_encrkey("HuaweiR3")
    # smp.snmp_save()
    # smp.snmp_comp("disabled")
    #     # smp.snmp_access("ALL")
    #     # smp.snmp_apply()
    # for x in range(3,8):
    #     smp = snmp(driver, "192.168.102."+ str(x))
    #     smp.creat_snmp("V1", driver)
    # smp.snmp_setting()
    # smp.snmp_del("192.168.102.6", "SNMP V1")
    # weboper.logout()
            # weboper.login(username1, password)
            # time.sleep(30)
            # weboper.logout()
    # weboper.close()
    # for x in range(3,4):
    #     smp = snmp(driver, "192.168.10."+ str(x))
    #     smp.creat_snmp("V1", driver)
    # for x in range(4, 6 ):
    #     smp = snmp(driver, "192.168.10." + str(x))
    #     smp.creat_snmp("V2", driver)
    # for x in range(100,200):
    #     smp = snmp(driver, "192.168.10." + str(x))
    #     smp.creat_snmp("V3", driver)
        # smp.snmp_setting()
        # smp.snmp_del("192.168.102." + str(x), "SNMP V3")
    # aps = creat_wireless(driver)
    # aps.ap()
    # aps.access_setting()
    # aps.safety_control()
    # us = user(driver)
    # us.user_setting()
    # while True:
    #     ss = SSHCreat(username, password, hostnames)
    #     ss.connect()
    #     res = ss.send("\n")
    #     print(res + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') )
    #     ss = SSHCreat(username1, password, hostnames)
    #     ss.connect()
    #     resu = ss.send("echo $LOGNAME")
    #     print(resu + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') )
    # for num in range(1,10):
    #     seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*"
    #     sa = []
    #     for i in range(30):
    #         sa.append(random.choice(seed))
    #     salt = ''.join(sa)
    #     print(salt)
    #     ss.sends("cfg.lua add usermanage user_cfg")
    #     time.sleep(3)
    #     ss.sends("cfg.lua set_apply_t usermanage.@user_cfg[" + str(num) + "].user_name='" + salt + "' 1")
    #     time.sleep(3)
    #     print(num)


    # smp = snmp(driver,"172.16.40.142")
    # smp.creat_snmp("V1", driver)
    # smp.creat_snmp("V2", driver)
    # smp.creat_snmp("V3")
    # weboper.close()
    # result = ss.send("cat /tmp/run/spectralscan.log")
    # print(result)
    # results = ss.sends("cfg.lua get snmpd.@system[0].sysObjectID")
    # print(results)
    # wire = rt_wireless(driver)
    # driver.find_element_by_id("Microwavepage_Select").click()
    # driver.implicitly_wait(100)
    # wire.advanced_setting()
    # wire.rt_radio_switch("0")
    # wire.rt_JTRANS("1")
    # smp = snmp(driver,localpaths)
    # smp.snmp_setting()
    # smp.snmp_add()
    # smp.snmp_version("V3")
    # smp.snmp_sdh("no")
    # smp.snmp_rmon("no")
    # smp.snmp_alarm("no")
    # smp.snmp_Comp("disabled")
    # us = user(driver)
    # # us.user_del("xitele2036")
    # # us.user_del("dandan")
    # # us.user_del("xueshan")
    # # us.user_del("xuhao")
    # us.user_setting()
    # us.user_creat("pitbull",newpass)
    # us.user_setting()
    # us.user_creat("snake", newpass)
    # us.user_setting()
    # us.user_creat("queen", newpass)
    # us.user_setting()
    # us.user_creat("kingsnake", newpass)
    # us.user_setting()
    # us.user_creat("kingcobra", newpass)
    # time.sleep(5)
    # driver.find_element_by_link_text('高级安全功能').click()
    # time.sleep(5)
    # lis = driver.find_elements_by_xpath("//div[@id=\"div_account_access_list\"]/li")
    # # print(type(lis))
    # for li in lis:
    #     divs = li.find_elements_by_xpath("./div")
    #     if divs[0].text == "dandan":
    #         divs[3].find_element_by_xpath("./button[contains(@id,\"account_del\")]").click()
        # print(divs[2].text)
    #         if mode == "edit":
    #             divs[4].find_element_by_xpath("./button[contains(@id,\"snmp_edit\")]").click()
    #         else:
    #             divs[4].find_element_by_xpath("./button[contains(@id,\"snmp_del\")]").click()
    # divs[4].find_element_by_xpath("./button[@id=\"snmp_edit_0\"]").click()
    # smp.snmp_setting()
    # smp.snmp_del("192.168.1.10", "SNMP V1")
    # smp.snmp_setting()
    # smp.snmp_del("192.168.102.2", "SNMP V2")
    # smp.snmp_setting()
    # smp.snmp_del("192.168.1.8", "SNMP V3")
    # smp.snmp_setting()
    # smp.snmp_del("192.168.102.10", "SNMP V3")
    # smp.snmp_setting()
    # smp.snmp_del("172.16.40.142", "SNMP V3")
    # qck = quick(driver)
    # qck.start()
    # qck.Qmode("ap")
    # qck.Qap("Hello","Li","OTHER","80M",channels)
    # qck.Qrt("hello","dear")
    # time.sleep(3)
    # driver.find_element_by_link_text('设备管理').click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[contains(text(),'网络配置')]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[contains(text(),'SNMP接入管理')]").click()
    # time.sleep(3)
    # lis = driver.find_elements_by_xpath("//div[@id=\"div_snmp_access_list\"]/li")
    # # print(type(lis))
    # for li in lis:
    #     divs = li.find_elements_by_xpath("./div")
    #     # print(divs[0].text)
    #     # print(divs[2].text)
    #     if divs[0].text == "172.18.10.65" and divs[2].text == "SNMP V3":
    #         if mode == "edit":
    #             divs[4].find_element_by_xpath("./button[contains(@id,\"snmp_edit\")]").click()
    #         else:
    #             divs[4].find_element_by_xpath("./button[contains(@id,\"snmp_del\")]").click()
            # divs[4].find_element_by_xpath("./button[@id=\"snmp_edit_0\"]").click()

        # for div in divs:
        #     num = div.text
        #     if num == "192.168.1.10" and num == "SNMP V2":
        #         print()

    # weboper.close()
        # for div in divs:
        #     print(div.text)
        #     # print(li.text)
        # # print(mode.index("SNMP v2"))

    # driver.find_element_by_xpath("//div[@id='div_snmp_access_list']").find_element_by_xpath("//li[1]//div[5]//button[1]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[contains(text(),'网络配置')]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//span[contains(text(),'SNMP接入管理')]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//div_snmp_access_list/Table_header_3ZTG1 Table_row_3GvID/Table_column_3vuAy/test()").click()
    # print(path)
    # aps.ap_ssidname("SNAKE")
    # aps.commit()
    # aps.rt_mode()
    # aps.commit()
    # aps.ap(countrys,bandwidths,channels,powers,ssid,secu,passwd)
    # aps.sta(sta_countrys,channels,powers,mcss,ssid,secu,passwd)
    # users = user(driver)
    # users.user_setting()
    # users.user_creat("batianhu2036", newpass)
    # users.user_creat("dandan2036", newpass)
    # users.user_creat("xueshan2036", newpass)
    # users.user_creat("sadsad2312", newpass)
    # np = snmp(localpaths)
    # np.creat_snmp("V1",driver)
    # np.creat_snmp("V2",driver)
    # np.creat_snmp("V3",driver)
    # weboper.close()
main()






#SS = SSH.SSHConnect(username,password,hostname)
#snmp = SS.send("cfg.lua add usermanage user_cfg")
#snmp = SS.send("cfg.lua set_apply_t usermanage.@user_cfg[1].user_name='jason' 1")
#snmpa = SS.send("cfg.lua show usermanage")
#print(snmpa)

#
# driver.find_element_by_link_text('微波配置').click()
#     time.sleep(10)
#     driver.find_element_by_xpath("//span[contains(text(),'高级微波配置')]").click()
#     time.sleep(5)
#     wifi = driver.find_element_by_id("hidden_radio_switch").get_attribute('value')
#     if int(wifi) == 0:
#         pass
#     else:
#         driver.find_element_by_xpath("//span[@id='span_radio_switch']").click()
#         time.sleep(10)
#         driver.find_element_by_xpath(
#             "//div[@id='div_radio_switch']//span[@class='Button_text_1quix'][contains(text(),'确定')]").click()
#


# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# j = open(init_path + "\\config.js")
# json_path = init_path + "\\countrycode_MCS.js"
# print(json_path)
# print(j)
#
# #配置Chrome浏览器的路径
# chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# #注册浏览器类型
# web.register('chrome', None, web.BackgroundBrowser(chromepath))
# #打开Chrome并连接
# web.get("chrome").open("https://192.168.2.38")
#
# j = open(init_path + "\\config.js")
# s = json.loads(j.read())
# begin = s.get("BEGIN")
# end = s.get("END")
# j.close()
#
#
# def get_index(cl, cc):
#     for i in cl:
#         if i.get("short_name") == cc:
#             return cl.index(i)
#     return 0

# def rt_txpower(txpower_var):
#     crt.Screen.Send("\r")
#     crt.Screen.Send("wlanconfig ath1 list | awk 'NR==2{print $1}'\r")
#     crt.Screen.WaitForString(AP_MAC,10)
#     crt.Screen.Send("cfg.lua set_apply wireless.@wifi-device[1].txpower='" + str(txpower_var) + "'\r")
#     return True

#
# j = open(init_path + "\\countrycode.js")
# list = json.loads(j.read())
#
#
# for i in range(get_index(list, begin),get_index(list,end)+1):
#     country_info = list[i]
#     country_name = country_info.get('short_name')
#     country_code = country_info.get('code')
#     #print(country_code)
#     #print(country_info)
#     print(country_name)
#     for ch_info in country_info.get('channel_info'):
#         h_channel = ch_info.get('high_chan')
#         l_channel = ch_info.get('low_chan')
#         txpower = ch_info.get('tx_power')
#         ant_gain = ch_info.get('ant_gain', 0)
#         for bw_info in country_info.get('bandwidth_info'):
#             bandwidth = bw_info.get('bandwidth')
#             for channel in bw_info.get('channels'):
#                 if int(txpower) <= 19:
#                     if h_channel >= channel >= l_channel:
#                         print("带宽:" + str(bandwidth) + " 信道:" + str(channel) + " 功率:" + str(txpower) + " 天线增益:" + str(ant_gain))
#                         # num = txpower + ant_gain - 16
#                         # print("功率 - 天线增益= " + str(num))
#                         # n = 8
#                         # if n != num:
#                         #     print("获取的值 " + str(n) + "不等于 " + str(num) + " 不通过")
#                         # else:
#                         #     print("获取的值 " + str(n) + "等于 " + str(num) + " 通过")
#                     else:
#                         continue
#                 else:
#                     continue
#






'''

def exchange_mcs(msc):
    crt.Screen.Send("\r")
    crt.Screen.Send("wlanconfig ath1 list | awk 'NR==2{print $1}'\r")
    crt.Screen.WaitForString("60:de:f3:3a:55:3d")
    crt.Screen.Send("cfg.lua set_apply wireless.@wifi-sta[1].mcs_peak='" + str(msc) + "'\r")
    crt.Screen.Send("cfg.lua set_apply wireless.@wifi-sta[1].mcs_mode='1'\r")
    return True


def main():
    if os.path.exists(basepath + "\\log\\countrycode\\") == False:
        os.makedirs(basepath + "\\log\\countrycode\\")
    countrycode_path = basepath + "\\log\\countrycode\\" + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M') + '.log'
    countrycode_log = open(countrycode_path, 'a+')


    rt_txpower(def_tp_var)
    countrycode_log.write("设置的txpower值：" + str(def_tp_var) + "    检查实际txpower值：")
    crt.Sleep(10000)
    crt.Screen.Send("cfg.lua get_cur wireless.@wifi-device[1].txpower\r")
    crt.Screen.WaitForString("root@Wireless:~#")
    screenrow = crt.Screen.CurrentRow - 1
    result = crt.Screen.Get(screenrow, 1, screenrow, 2)
    countrycode_log.write(result + '\n')
    #countrycode_log.write(result+1 + '\n')
    countrycode_log.flush()
    countrycode_log.close()
main()


for i in range(1,30):
    countrycode_path = basepath + "\\log\\countrycode\\" + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
    countrycode_log = open(countrycode_path, 'a+')
    crt.Screen.Send("wlanconfig ath1 list | awk 'NR==2{print $1}'\r")
    crt.Screen.WaitForString("root@Wireless:~#")
    crt.Screen.Send("cfg.lua get_cur wireless.@wifi-device[1].txpower\r")
    crt.Screen.WaitForString("root@Wireless:~#")
    #crt.Screen.Send("cfg.lua get_cur wireless.@wifi-device[1].txpower\r")
    #crt.Screen.WaitForString("root@Wireless:~#")
    screenrow = crt.Screen.CurrentRow - 1
    result = crt.Screen.Get(screenrow, 8, screenrow, 9)
    countrycode_log.write("获取的实际功率:" + str(result) + "\r")
    countrycode_log.flush()
    time.sleep(10)
'''