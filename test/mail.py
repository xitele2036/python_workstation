#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import json
import sys
import os
import time

# 第三方 SMTP 服务
init_path = "E:\\log\\countrycode\\"
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "740251481@qq.com"  # 用户名
mail_pass = "ykdyeumdavycbdid"  # 口令

sender = "740251481@qq.com"
#receivers = ['batianhu2036@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#receivers = ['ke.liu@creatcomm.com']
receivers = ['qingfeng.zhang@creatcomm.com','ke.liu@creatcomm.com','batianhu2036@126.com']


j = open(init_path + "2019_04_21.log","r+", encoding='UTF-8')
mail_text = j.read()


message = MIMEText(mail_text, 'plain', 'utf-8')
message['From'] = Header("测试结果确认", 'utf-8')
message['To'] = Header("ME", 'utf-8')

subject = '每日测试结果汇总'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
