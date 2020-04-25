#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

__author__ = 'Jason Liu'



#private_key = paramiko.RSAKey.from_private_key_file('E:\\works\\Security\\id_rsa102.txt')

class SSHConnect:
    def __init__(self,usernames,passwords,hostnames):
        self.usernames = usernames
        self.passwords = passwords
        self.hostnames = hostnames

    def send(self,comms):
        user = self.usernames
        passwd = self.passwords
        host = self.hostnames
        arg = comms
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        s.connect(host,22,user,passwd)
        stdin, stdout, stderr = s.exec_command(arg.encode())
        line = stdout.read()
        return line.decode()









