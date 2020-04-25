#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

import serial
import sys
import os
import time
import paramiko
from io import StringIO

hostname = "192.168.102.1"
port = 22
username = "szhw"
password = "Changeme_123"
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
login = "login_shell"
stdin,stdout,stderr = s.exec_command(login.encode())

while True:
    cmd = "wlanconfig ath1 list | awk 'NR==2{print $1}'"
    stdin,stdout,stderr = s.exec_command(cmd.encode())
    line = stdout.read()
    if len(line.decode()) == 0:
        print("WIFI未连接")
        #stdin, stdout, stderr = s.exec_command(adduser.encode())
        #print("add success")
        time.sleep(t1)
    else:
        print("-------------------分割线----------------------")
        print ("WIFI已连接")
        print(line.decode())
        s.exec_command("wifi load")
        print("WIFI重新加载")
        i = i + 1
        print("断连次数：%d" %i )
        for t in range(t):
            time.sleep(1)
            print('*',end='',flush=True)
        print(' ')


