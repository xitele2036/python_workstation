#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from SSH import SSHCreat
import os
import time


init_path = os.path.dirname(os.path.realpath(__file__))
hostnames = "192.168.102.1"

usernames = "szhw"
username = "admin"
password = "Modifyme_123"
local_path = "https://" + hostnames


def main():

    ss = SSHCreat(username, password, hostnames)
    ss.connect()
    nums = ss.sends("cfg.lua get usermanage.@global[0].cur_user_count")
    print(nums)
    ss.send("cfg.lua add usermanage user_cfg")
    ss.send("cfg.lua set usermanage.@user_cfg["+ nums +"].user_level='1'")
    ss.send("cfg.lua set usermanage.@user_cfg["+ nums +"].password='Changeme_123'")
    ss.send("cfg.lua set_apply_t usermanage.@user_cfg["+ nums +"].user_name='"+usernames+"' 1")
    time.sleep(15)
    results = ss.send("cfg.lua show usermanage")
    print(results)
    ss.close()

    ss2 = SSHCreat(usernames, password, hostnames)
    ss2.connect()
    status = ss2.send("cfg.lua get usermanage.@user_cfg["+nums+"].login_status_ssh")
    print(status)
    ss2.close()

main()