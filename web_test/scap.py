#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time
import os
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Dot1Q, Ether, ARP

data = 'jasonliu'

#dpkt  = sniff(iface = "Intel(R) Dual Band Wireless-AC 7260", count = 10)



mac="52:54:00:2E:23:92"
eth=Dot1Q(vlan=60, prio=1)
pkt=IP(src='192.168.102.2',dst='172.16.80.62')/TCP(sport=12345,dport=5555)/data
pack=eth/pkt
send(pack,inter=1,count=100,iface="Intel(R) Dual Band Wireless-AC 7260")

'''
#
mac="52:54:00:2E:23:92"
eth=Ether(src=mac,type=0x8100)
arp=IP(src='192.168.102.1',dst='172.16.80.62')/TCP(sport=12345,dport=5555)
a=eth/arp
a.show()
sendp(a,inter=1,count=100,iface="Intel(R) Dual Band Wireless-AC 7260")
'''