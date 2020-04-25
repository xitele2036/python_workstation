#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paramiko
import serial
import sys
import os
import time


hostname = "129.9.4.2"
port = 22
username = "fuck"
password = "Changeme_1234"

s = paramiko.SSHClient()                               # 绑定实例
s.load_system_host_keys()                                # 加载本地HOST主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
s.connect(hostname,port,username,password)
#"wlanconfig ath1 list | awk 'NR==2{print $1}'"
while True:
    cmd = input("cmd: ")
    stdin,stdout,stderr = s.exec_command(cmd.encode())
    print(stderr.readlines())
    print(stdout.readlines())