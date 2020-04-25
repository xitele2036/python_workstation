#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

g = getCmd(SnmpEngine(),
           UsmUserData('szhwMD5', 'HuaweiR3', 'HuaweiR3'),
           UdpTransportTarget(('192.168.2.36', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('OPTIX-GLOBAL-PM-DATA-RTN-MIB','ethPortPmCurEid',0))
           )
errorIndication, errorStatus, errorIndex, varBinds = next(g)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))