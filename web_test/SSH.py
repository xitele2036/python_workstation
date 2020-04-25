#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

__author__ = 'Jason Liu'



#private_key = paramiko.RSAKey.from_private_key_file('E:\\works\\Security\\id_rsa102.txt')

class SSHCreat:

# 初始化
    def __init__(self,usernames,passwords,hostnames):
        self.usernames = usernames
        self.passwords = passwords
        self.hostnames = hostnames
        self.s = paramiko.SSHClient()
        self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 允许连接不在know_hosts文件中的主机

# 建立SSH连接
    def connect(self):
        self.s.connect(self.hostnames,22,self.usernames,self.passwords)

# 发送命令并返回结果
    def send(self,comm):
        stdin, stdout, stderr = self.s.exec_command(comm.encode())
        line = stdout.read()
        return line.decode()

# 发送命令返回不带result的结果
    def sends(self,comm):
        stdin, stdout, stderr = self.s.exec_command(comm.encode())
        line = stdout.read()
        return line[18:35].decode()

# 关闭SSH连接
    def close(self):
        self.s.close()









