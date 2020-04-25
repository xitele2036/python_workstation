# $language = "python"
# $interface = "1.0"

import datetime
import json
import sys
import os
import time


#初始值
init_path = os.path.dirname(os.path.realpath(__file__))
init_SSID = "PIT_BULL"
init_channel = "161"
init_bandwidth = "20M"
init_country_code = "32800"
AP_IP = "192.168.102.1"
RT_COM = "25"
basepath = "E:"
AP_MAC = "14:09:dc:fa:80:44"
init_txpower = "30"
fixed_mcs = "2"
init_antgain = "0"


# 连接你的AP设备
ap = crt.Session.ConnectInTab("/S " + AP_IP)
ap.Screen.Send(":lognew:\"szhw\",\"Changeme_123\"\r")
ap.Screen.WaitForString("password")
ap.Screen.WaitForString("#")

# 连接你的RT设备
rt = crt.Session.ConnectInTab("/S " + "Serial-COM" + RT_COM)
rt.Screen.Send("\r")
#rt.Screen.WaitForString("Wireless login")
#rt.Screen.Send("root\r")
#rt.Screen.WaitForString("password")
#rt.Screen.Send("Changeme_123\r")


j = open(init_path + "\\config.js")
s = json.loads(j.read())
#获取begin的对应值没有就获取NA
begin = s.get("BEGIN")
#获取end的对应值没有就获取NA
end = s.get("END")


#判断工作带宽是否切换成功
def switch_ap_bandwidth_success():
    ap.Screen.Send(":radio-cfg-get-wlan-bandwidth:3,0xff\r")
    ap.Screen.WaitForString(">")
	#要加判断
    return True

#判断信道是否切换成功
def switch_ap_channel_success():
    ap.Screen.Send(":radio-cfg-get-real-channel:3,0xff\r")
    #ap.Screen.WaitForString(">")
    #row = ap.Screen.CurrentRow - 3
    #current_chanel = (ap.Screen.Get(row, 1, row, 48).strip())[-3:]
    #要加判断
    return  True

#开始与结束的范围
def get_index(cl, cc):
    for i in cl:
        if i.get("short_name") == cc:
            return cl.index(i)
    return 0

#初始化，配置AP的国家码，带宽，信道，SSID
def init_switch_ap_radio_parameter(country_code,bandwidth,channel,SSID):
    ap.Screen.Send(":trans-begin:unlock\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-region:3,0xff," + hex(int(country_code)) + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-wlan-bandwidth:3,0xff," + bandwidth + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-dfs-en:3,0xff,enable,1," + channel + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-hp-encrypt:3,0xff,NONE,\"NOPASSWORD\"\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-ap-ssid:3,0xff,\"" + SSID + "\"" + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":trans-commit:\"summary\"\r")
    return True

#初始化，配置RT连接AP，配置RT的SSID
def init_switch_rt_countrycode(SSID,antgain,power):
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-device[1].txpower=\'" + str(power) + "\'" + "\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-device[1].antgain=\'" + str(antgain) + "\'" + "\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-iface[1].ssid=\'" + SSID + "\'" + "\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-iface[1].encryption='none'\r")
    crt.Sleep(15000)
    rt.Screen.Send("\r")
    rt.Screen.WaitForString("#")



#初始化，等待RT连接AP
def init_wait_rt_connect():
    rt.Screen.WaitForString('Associated with AP',180)
    crt.Sleep(30000)
    rt.Screen.Send('wlanconfig ath1 list\r')
    rt.Screen.WaitForString("szhw@RTN510 RT II:~#")
    return datetime.datetime.now()

#AP切换国家码。带宽，信道
def switch_ap_radio_parameter(country_code,bandwidth,channel):
    ap.Screen.Send(":trans-begin:unlock\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-region:3,0xff," + hex(int(country_code)) + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-wlan-bandwidth:3,0xff," + bandwidth + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":radio-cfg-set-dfs-en:3,0xff,enable,1," + str(channel) + "\r")
    time.sleep(1)
    crt.Sleep(1000)
    ap.Screen.Send(":trans-commit:\"summary\"\r")
    return True

#等待RT连接AP
def wait_rt_connect(countrycode_log,CONNECT):
    rt.Screen.WaitForString('Associated with AP',180)
    crt.Sleep(30000)
    rt.Screen.Send("wlanconfig ath1 list | awk 'NR==2{print $1}'\r")
    if rt.Screen.WaitForString(AP_MAC,10) == True:
        CONNECT = 1
    else:
        CONNECT = 0
    return CONNECT


def exchange_mcs(msc):
    rt.Screen.Send("\r")
    rt.Screen.Send("wlanconfig ath1 list | awk 'NR==2{print $1}'\r")
    rt.Screen.WaitForString(AP_MAC)
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-sta[1].fixed_mcs='" + str(msc) + "'\r")
    rt.Screen.Send("cfg.lua set_apply wireless.@wifi-sta[1].mcs_mode='0'\r")
    return True

def main():
    if os.path.exists(basepath + "\\log\\countrycode\\") == False:
        os.makedirs(basepath + "\\log\\countrycode\\")
    countrycode_path = basepath + "\\log\\countrycode\\" + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
    countrycode_log = open(countrycode_path, 'a+')
    #初始化,AP与RT连接
    init_switch_ap_radio_parameter(init_country_code,init_bandwidth,init_channel,init_SSID)
    init_switch_rt_countrycode(init_SSID,init_antgain,init_txpower)
    init_wait_rt_connect()
    countrycode_log.write(
        '******************************' + datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S') + ' ******************************\n' + '进行初始化\n' + 'SSID: ' + init_SSID + '\n'
        + '国家码: ' + init_country_code + '\n' + '带宽: ' + init_bandwidth + '\n' + '信道: ' + init_channel + '\n' + '完成初始化\n')
    json_path = init_path + "\\countrycode.js"
    f = open(json_path)
    list = json.loads(f.read())
    #开始遍历
    for i in range(get_index(list,begin),get_index(list,end)+1):
        #b = get_index(list,begin)
        #e = get_index(list,end)+1
        #countrycode_log.write("begin: " + str(b) + '\n' + "end: " + str(e) + '\n')
        country_info = list[i]
        country_name = country_info.get("short_name")
        country_code = country_info.get("code")
        countrycode_log.write(
            '****************************** Begin ' + str(country_name) + ' ' + datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + ' ******************************\n')
        time.sleep(2)

        for bw in country_info.get("bandwidth_info"):
            bandwidth = bw.get("bandwidth")

            for channel in bw.get("channels",[]):
                switch_ap_radio_parameter(country_code,bandwidth,channel)
                time.sleep(10)
                crt.Sleep(1000 * 10)
                #start_time = datetime.datetime.now()
                switch_ap_bandwidth_success()
                time.sleep(2)
                switch_ap_channel_success()
                nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                time.sleep(2)
                CONNECT = 0
                CONNECTED = wait_rt_connect(countrycode_log,CONNECT)
                crt.Sleep(10000)
                #countrycode_log.write("CONNECTED: " + str(CONNECTED) + '\n')
                #association_time = wait_rt_connect() - start_time
                if CONNECTED == 1:
                    countrycode_log.write(
                    nowtime + " countrycode: " + str(country_name) + " bandwidth: " + bandwidth + " channel: " + str(
                        channel)
                    + " Successful" + '\n')
                    for num in range(1, 10):
                        exchange_mcs(num)
                        countrycode_log.write("设置MCS值：" + str(num) + "    检查结果MCS值TX为：")
                        crt.Sleep(10000)
                        rt.Screen.Send("cfg.lua get_cur wireless.@wifi-device[1].txpower\r")
                        rt.Screen.WaitForString("szhw@RTN510 RT II:~#")
                        screenrow = rt.Screen.CurrentRow - 1
                        result = rt.Screen.Get(screenrow, 8, screenrow, 9)
                        countrycode_log.write(result + '\n')
                        countrycode_log.flush()
                else:
                    countrycode_log.write(
                        nowtime + " countrycode: " + str(
                            country_name) + " bandwidth: " + bandwidth + " channel: " + str(
                            channel)
                        + " Fail" + '\n')
                    countrycode_log.flush()
    f.close()
    countrycode_log.close()

main()

