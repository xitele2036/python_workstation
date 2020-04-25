# $language = "python"
# $interface = "1.0"

# 官方的实例可以在未连接任何服务器的情况下进行ssh连接
import json, time, datetime, os

COM = "25"
IMAGE = "R3_V1.0.119.358.dakota_huawei_20190118.img"

'''
# 连接你的AP设备
ap = crt.Session.ConnectInTab("/S " + "192.168.3.1")
ap.Screen.Send(":lognew:\"szhw\",\"Changeme_123\"\r")
ap.Screen.WaitForString("password")
ap.Screen.WaitForString("#")
'''

# 连接RT设备
rt = crt.Session.ConnectInTab("/S " + "Serial-COM" + "\"" + COM + "\"")
rt.Screen.WaitForString("With watchdog Hit any key to stop autoboot:  2")
rt.Screen.Send("\r")
crt.Sleep(3000)
rt.Screen.Send("setenv machid e000201\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("setenv ipaddr 192.168.2.116\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("setenv serverip 192.168.2.66\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("tftpboot " + IMAGE + "\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("cp.b 0x840000bc 0x84000000 0xf80bec\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("imgaddr=0x84000000 && source $imgaddr:script\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("setenv bootalt 0\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("saveenv\r")
rt.Screen.WaitForString("(IPQ40xx) #")
crt.Sleep(3000)
rt.Screen.Send("reset\r")
