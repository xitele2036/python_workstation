#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

N,R = 0,25
errorIndication, errorStatus, errorIndex,varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public123', mpModel=0),
           UdpTransportTarget(('192.168.102.1', 161)),
           ContextData(),
           #N,R,
           #ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr',0)),
           ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNeMemo',0 ))
            )
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))


#print(errorIndication)
#print(errorStatus)
#print(varBinds)
#print(errorIndex)