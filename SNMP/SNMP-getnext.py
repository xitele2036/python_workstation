#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

g = nextCmd(SnmpEngine(),
            CommunityData('public',mpModel=0),
            UdpTransportTarget(('192.168.2.36',161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0))
            )

errorIndication, errorStatus, errorIndex,varBinds = next(g)
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))




