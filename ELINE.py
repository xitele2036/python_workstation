#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import *
import os
import time
import sys
import serial
import subprocess
import os
import  linecache
from itertools import combinations, permutations
import datetime
basepath = "E:"

class Eline():## 配置登录信息
    def __init__(self):
        self.ser = serial.Serial("COM26",115200)
        self.ser.close()
        self.ser.open()
        self.card = self.get_card()
        print(self.card)
    def get_card(self):
        result = os.popen('ipconfig')
        res = result.read()
        C=0
        str_list=[]
        for line in res.splitlines():
            C=C+1
            str_list.append(line)
            if "192.168.102.2" in line :
                print(reversed(str_list))
                for EE in reversed(str_list):
                    if "适配器" in EE:
                        print(EE)
                        card=str(EE)[7:-1]
                        break
                break
            else:
                card="网口没插好 or 本地没有IP:102.2"
                pass
                
        return  card
    def Filter_capture(self,filter="id"):
        dirPath = "D:\\"
        time.sleep(5)
        linecache.clearcache()
        if (os.path.exists(dirPath+"LLDP.txt")):
            capture_lldp = open("D:\\LLDP.txt",encoding="utf-8")
            lines = capture_lldp.readlines()
            capture_lldp.close()
            CC = 0
            for line in lines:
                line = line.strip('\r\n')
                CC = CC + 1
#   print(CC)
            C = 1
            s = filter
            VLAN_LIST=[]
#   print(s)
            while C < CC:
                the_line = linecache.getline("D:\\LLDP.txt", C)
                if s in the_line:
#                    print(the_line,"+++行数:",C)
                    the_line=the_line[:-1]
                    the_line=the_line.split(":")
                    VLAN_LIST.append(the_line[-1])
                else:
                    pass
                C = C + 1
        else:
            print("抓包失败")
#        os.remove("D:\\LLDP.txt")
#       print(VLAN_LIST)
#       print(list(set(VLAN_LIST)))
        linecache.clearcache()
        return list(set(VLAN_LIST)) 

    def CAPTURE_lldp(self,time_=20):
        if (os.path.exists( "D:\\LLDP.txt")):
            os.remove("D:\\LLDP.txt")
        cmd = "tshark -i "+str(self.card)+"  -V -a duration:"+str(time_)+"  -t ad ether dst host 01:80:c2:00:00:0e > D:/LLDP.txt"
        os.system(cmd)
        time.sleep(3)
        print(self.Filter_capture(filter="Chassis Id:"))
        print(self.Filter_capture(filter="Port Id:"))
        print(self.Filter_capture(filter="Seconds:"))
        print(self.Filter_capture(filter="System Name:"))
        print(self.Filter_capture(filter="System Description:"))
        print(self.Filter_capture(filter="Management Address:"))
        print(self.Filter_capture(filter="Port Description:"))
        print(self.Filter_capture(filter="Maximum Frame Size:"),"MFL")
        print(self.Filter_capture(filter="Port VLAN Identifier:"))
        print(self.Filter_capture(filter="802.1Q Virtual LAN,"),"VLAN ID")

    def dut_ping(self):
        IP = "129.9.0.145"
        NN = 15
        cmd = "ping " + str(IP) + "  -n " + str(NN)
        result = os.popen(cmd)
        res = result.read()
        I = 0
        for line in res.splitlines():
            #    print(line)
            if "TTL" in line and IP in line:
                I = I + 1
        strs = print("IP", "通:" + str(I), "不通：" + str(NN - I))
        log.write(str(strs))


    def send(self,command):
#        print(command)
        self.ser.write(command.encode())
        time.sleep(1)
        self.ser.write(b'\r\n')
        
    def chenxueshan(self): 
      self.send("cfg.lua del ethmanage @e_port[6] 0")
      self.send("cfg.lua del ethmanage @e_port[6] 0")

    def NEW_UNI_Source(self,port="eth1",type="QINQ",whether=0):#新建UNI源端口
        if port == "eth0":
            ID = 0
        elif port == "eth1":
            ID = 1
        elif port == "ath1":
            ID = 2
        self.send("cfg.lua set ethmanage.@ethmanage["+str(ID)+"].encapsulation_type="+str(type))
        self.send("cfg.lua add ethmanage e_port")
        self.send("cfg.lua set ethmanage.@e_port[6].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_port[6].port_name="+str(port))
        self.send("cfg.lua set ethmanage.@e_port[6].port_type='UNI'")
        self.send("cfg.lua set ethmanage.@e_port[6].board='eline'")
        self.send("cfg.lua set ethmanage.@e_port[6].uni_type='source_interface'")
        if  whether == 1 :
            self.send("cfg.lua set ethmanage.@e_port[6].vlan_id='1000'")
            
    def NEW_UNI_Sink(self,port="eth1",type="802.1Q",whether=0):  # 新建UNI宿端口
        if port == "eth0":
            ID = 0
        elif port == "eth1":
            ID = 1
        elif port == "ath1":
            ID = 2
        self.send("cfg.lua set ethmanage.@ethmanage["+str(ID)+"].encapsulation_type="+str(type))
        self.send("cfg.lua add ethmanage e_port")
        self.send("cfg.lua set ethmanage.@e_port[7].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_port[7].port_name="+str(port))
        self.send("cfg.lua set ethmanage.@e_port[7].port_type='UNI'")
        self.send("cfg.lua set ethmanage.@e_port[7].board='eline'")
        self.send("cfg.lua set ethmanage.@e_port[7].uni_type='sink_interface'")
        if  whether == 1 :
            self.send("cfg.lua set ethmanage.@e_port[6].vlan_id='1000'")

    
    def NEW_NNI_Sink(self,port="eth1",type="QINQ"):  # 新建NNI端口
        if port == "eth0":
            ID = 0
        elif port == "eth1":
            ID = 1
        elif port == "ath1":
            ID = 2
        self.send("cfg.lua set ethmanage.@ethmanage["+str(ID)+"].encapsulation_type="+str(type))
        self.send("cfg.lua add ethmanage e_port")
        self.send("cfg.lua set ethmanage.@e_port[7].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_port[7].port_name="+str(port))
        self.send("cfg.lua set ethmanage.@e_port[7].port_type='NNI'")
        self.send("cfg.lua set ethmanage.@e_port[7].board='eline'")
        self.send("cfg.lua set ethmanage.@e_port[7].qinq_id='789'")
        self.send("cfg.lua set ethmanage.@e_port[7].vlan_id='1000'")

    def NEW_NNI_Source(self,port="eth1",type="QINQ"):  # 新建NNI端口
        if port == "eth0":
            ID = 0
        elif port == "eth1":
            ID = 1
        elif port == "ath1":
            ID = 2
        self.send("cfg.lua set ethmanage.@ethmanage["+str(ID)+"].encapsulation_type="+str(type))
        self.send("cfg.lua add ethmanage e_port")
        self.send("cfg.lua set ethmanage.@e_port[6].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_port[6].port_name="+str(port))
        self.send("cfg.lua set ethmanage.@e_port[6].port_type='NNI'")
        self.send("cfg.lua set ethmanage.@e_port[6].board='eline'")
        self.send("cfg.lua set ethmanage.@e_port[6].qinq_id='456'")
        self.send("cfg.lua set ethmanage.@e_port[6].vlan_id='1000'")

    def NEW_EINE_UNI_UNI(self):  # 新建UNI_UNI专线
        self.send("cfg.lua add ethmanage e_line")
        self.send("cfg.lua set ethmanage.@e_line[0].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_line[0].service_name='ELINE1000'")
        self.send("cfg.lua set ethmanage.@e_line[0].direction='UNI_UNI'")
        self.send("cfg.lua set_apply ethmanage.@e_line[0].service_id='123'") 
    
    def NEW_EINE_UNI_NNI(self):  # 新建UNI_NNI专线
        self.send("cfg.lua add ethmanage e_line")
        self.send("cfg.lua set ethmanage.@e_line[0].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_line[0].service_name='ELINE1000'")
        self.send("cfg.lua set ethmanage.@e_line[0].direction='UNI_NNI'")
        self.send("cfg.lua set ethmanage.@e_line[0].sink_linkid='789'") 
        self.send("cfg.lua set_apply ethmanage.@e_line[0].service_id='123'")   
    
    def NEW_EINE_NNI_NNI(self):  # 新建NNI_NNI专线
        self.send("cfg.lua add ethmanage e_line")
        self.send("cfg.lua set ethmanage.@e_line[0].service_id='123'")
        self.send("cfg.lua set ethmanage.@e_line[0].service_name='ELINE1000'")
        self.send("cfg.lua set ethmanage.@e_line[0].direction='NNI_NNI'")
        self.send("cfg.lua set ethmanage.@e_line[0].source_linkid='456'")
        self.send("cfg.lua set ethmanage.@e_line[0].sink_linkid='789'")
        self.send("cfg.lua set_apply ethmanage.@e_line[0].service_id='123'")
    def DEL_ELINE(self): 
        self.send("cfg.lua del ethmanage @e_line[0] 2")   
    def ser_close(self):
        self.ser.close()



lists = [[] for i in range(15)]
lists[0]=["eth0","NULL","0"]
lists[1]=["eth1","NULL","0"]
lists[2]=["ath1","NULL","0"]
lists[3]=["eth0","802.1Q","0"]
lists[4]=["eth0","802.1Q","1"]
lists[5]=["eth1","802.1Q","0"]
lists[6]=["eth1","802.1Q","1"]
lists[7]=["ath1","802.1Q","0"]
lists[8]=["ath1","802.1Q","1"]
lists[9]=["eth0","QINQ","0"]
lists[10]=["eth0","QINQ","1"]
lists[11]=["eth1","QINQ","0"]
lists[12]=["eth1","QINQ","1"]
lists[13]=["ath1","QINQ","0"]
lists[14]=["ath1","QINQ","1"]


log = open("D:\\LLDP.txt", 'a+')
chen = list(permutations(lists,2))
CC=Eline()
print("开始时间",datetime.datetime.now())
#########  UNI-UNI 30种
for x  in chen :
     if x[0][1] == x[1][1] and x[0][2] == x[1][2]:
         print(x, "U-U")
         CC.chenxueshan()
         CC.NEW_UNI_Source(port=x[0][0],type=x[0][1],whether=x[0][2])
         CC.NEW_UNI_Sink(port=x[1][0],type=x[1][1],whether=x[1][2])
         CC.NEW_EINE_UNI_UNI()
         time.sleep(5)
         CC.dut_ping()
         CC.DEL_ELINE()
#######################################
## 列表 U-N 生成
i =0
xue=[]
shan=[]
for x in lists:
    if x[1] == "QINQ":
        break
    xue.append(x)
    shan.append(x[0])
    i =i +1
l3=[(x,y) for x in xue for y in shan if x!=y  ]
qwe = [[] for i in range(54)]
qq=0
for x in  l3 :
    if x[0][0] != x[1] :
        # print(x[0][0],x[0][1],x[0][2])
        # print(x[1])
        qwe[qq] = [x[0][0],x[0][1],x[0][2],x[1]]
        qq=qq+1
qwe = list(set([tuple(t) for t in qwe]))
qwe = [list(v) for v in qwe]
print(qwe)
#### qwe 是U-N的列表
########  UNI-NNI  18种
for x  in qwe :
    print(x,"U-N")
    CC.chenxueshan()
    CC.NEW_UNI_Source(port=x[0],type=x[1],whether=x[2])
    CC.NEW_NNI_Sink(port=x[3])
    CC.NEW_EINE_UNI_NNI()
    time.sleep(5)
    CC.dut_ping()
    CC.DEL_ELINE()
########  NNI -NNI  专线   6种
ABC=["eth0","eth0","eth1","eth1","ath1","ath1"]
XYZ=["eth1","ath1","eth0","ath1","eth0","eth1"]
for a,z in zip (ABC,XYZ):
    print(a,z,"N-N")
    CC.chenxueshan()
    CC.NEW_NNI_Source(port=str(a))
    CC.NEW_NNI_Sink(port=str(z))
    CC.NEW_EINE_NNI_NNI()
    time.sleep(5)
    CC.dut_ping()
    CC.DEL_ELINE()
print("结束时间",datetime.datetime.now())
CC.ser_close()