# $language = "python"
# $interface = "1.0"

import os
import time

AP_IP = "172.16.40.145"  #AP端的IP
RT_COM = "25"
AP_COM = "26"



def ConnetSSH():
    ssh = crt.Session.ConnectInTab("/S " + AP_IP)
    crt.Sleep(10*1000)
    ssh.Screen.Send("\r")
    ssh.Screen.WaitForString("cfg_sh>")
    ssh.Screen.Send("q\r")


def update(safe):

    rt.Screen.Send("\r")
    rt.Screen.WaitForString("login:")
    rt.Screen.Send("szhw\r")
    rt.Screen.WaitForString("Password:")
    rt.Screen.Send("Changeme_1234\r")
    rt.Screen.WaitForString(">")
    rt.Screen.Send("login_shell\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("sysupgrade /tmp/nand_reserve/" + str(safe))
    rt.Screen.Send("\r")
    crt.Sleep(450*1000)
    rt.Screen.Send("\r")

def login_COM(mode):
    mode.Screen.Send("\r")
    mode.Screen.WaitForString("login:")
    mode.Screen.Send("szhw\r")
    mode.Screen.WaitForString("Password:")
    mode.Screen.Send("Changeme_1234\r")
    mode.Screen.WaitForString(">")
    mode.Screen.Send("login_shell\r")
    mode.Screen.WaitForString("#")

ap = crt.Session.ConnectInTab("/S " + "Serial-COM" + AP_COM)
rt = crt.Session.ConnectInTab("/S " + "Serial-COM" + RT_COM)

login_COM(ap)
login_COM(rt)

while True:
    ap.Screen.Send("\r")
    ap.Screen.WaitForString("#")
    ap.Screen.Send("cfg.lua set_apply network.@interface[3].dcn_mode='ipdcn'\r")
    rt.Screen.Send("\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("cfg.lua set_apply network.@interface[3].dcn_mode='ipdcn'\r")
    crt.Sleep(120*1000)
    ap.Screen.Send("\r")
    ap.Screen.WaitForString("#")
    ap.Screen.Send("cfg.lua set_apply network.@interface[3].dcn_mode='l2dcn'\r")
    rt.Screen.Send("\r")
    rt.Screen.WaitForString("#")
    rt.Screen.Send("cfg.lua set_apply network.@interface[3].dcn_mode='l2dcn'\r")
    crt.Sleep(120*1000)


# img_list=["R3_V1.0.2383.dakota_huawei_Debug_20191227.img","R3_V1.0.2455.dakota_huawei_Debug_20200118.img","R3_V1.0.2502.dakota_huawei_Debug_20200218.img"]
# while True:
#     for img in img_list:
#         update(img)
#         ConnetSSH()

