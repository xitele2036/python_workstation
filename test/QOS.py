# $language = "python"
# $interface = "1.0"

import datetime
import json
import sys
import os
import time

list = ['10000','100000','200000','300000','400000','500000','1000000']

while True:
    for num in range(0,8):
        crt.Screen.Send("cfg.lua set_apply qosconfig.@cosmap_ehq[2].out_cvlan=" + str(num)+ "\r")
        for mb in list:
            crt.Screen.Send("cfg.lua set_apply qosconfig.@qos_policy[3].port_pir=" + str(mb) + "\r")
            for m in range(3):
                time.sleep(100)


