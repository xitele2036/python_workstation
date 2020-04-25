import threading
import paramiko
import sys
import random  # str(random.randint(192,))
from random import *
import time 


class SSH():
    def __init__(self):
        self.usernames = "fuck"
        self.passwords = "Changeme_1234"
        self.hostnames = "172.16.40.150"
    def sends(self,comm):
        try:
            self.s = paramiko.SSHClient()
            self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.s.connect(self.hostnames,22,self.usernames,self.passwords)
            stdin, stdout, stderr = self.s.exec_command(comm.encode())
            line = stdout.read()
            self.s.close()
            return  line
        except Exception as e:
            print(e)
    def UPGRADE(self,firmware):
        try:
            # qq.sends(" echo  0  > /tmp/nand_flash/check_image")
            # qq.sends(" echo  0  > /tmp/check_image")
            qq.sends("cfg.lua exec_native  szhw  WEB  /sbin/sysupgrade   /tmp/nand_reserve/"+str(firmware))  # echo  1  > /tmp/nand_flash/check_image
            print("升级版本"+str(firmware)+"..........",end="--")
        except Exception as e:
            print(e)
            #self.UPGRADE(firmware=firmware)
            print("SSH connect fail")
        time.sleep(300)
        VER = qq.sends(" cfg.lua get_version")
        print("升级完成",end="--")
        print(VER)
        if firmware[33:41] in str(VER):
            print("SSH connect fail")
        else:
            print("升级失败",firmware,str(VER))
        
    def GET_VERSION(self,boot=1):
        try:
            qq.sends("fw_setenv  bootalt "+str(boot)+" && reboot -f ")
        except Exception as e:
            pass
        time.sleep(340)
        try:
            VER = qq.sends(" cfg.lua get_version")
            #print(VER)
        except Exception as e:
            print(e)
        return VER
qq=SSH()
img_list=["R3_V1.0.2746.dakota_huawei_Debug_20200323.img","R3_V1.0.2746.dakota_huawei_Debug_20200323.img"]#固件名称(全称)，固件上传至设备/tmp/nand_reserve/
while True:
    for img in img_list:
        qq.UPGRADE(img)
        # AA=qq.GET_VERSION(0)
        # BB=qq.GET_VERSION(1)
    #     if AA == BB  :
    #         #print("同步成功")
    #         sys=0
    #         up=0
    #         if img[33:41] in str(AA) and img[33:41] in str(BB):
    #             print("升级成功",img,img[33:41],AA,BB)
    #             up=0
    #         else:
    #             print("升级失败",img,img[33:41],AA,BB)
    #             up=1
    #             break
    #     else:
    #         print("升级同步失败",AA,BB)
    #         sys=1
    #         up=1
    #         break
    # if int(up)==1 or int(sys)==1:
    #     print("升级或者同步失败")
    #     break
    # else:
    #     pass
