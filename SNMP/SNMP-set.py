#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

g = setCmd(SnmpEngine(),
           CommunityData('public@HWR3','private@HWR3',mpModel=0),
           UdpTransportTarget(('192.168.2.36',161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0),'CPU-X86'),
           ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0),'ARM-BTC'),
           ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0),'APPLE_XXI')
            )
errorIndication, errorStatus, errorIndex,varBinds = next(g)
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))

v = getCmd(SnmpEngine(),
           CommunityData('public@HWR3',mpModel=0),
           UdpTransportTarget(('192.168.2.36',161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0))
           )
errorStatus,errorIndication,errorIndex,varBinds = next(v)
for varBind in varBinds:
    print(' = '.join(x.prettyPrint() for x in varBind))