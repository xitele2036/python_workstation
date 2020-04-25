#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *
i = 1
for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in bulkCmd(SnmpEngine(),
                          CommunityData('public@HWR3',mpModel=1),
                          #UsmUserData('szhwMD5', 'HuaweiR3', 'HuaweiR3'),
                          UdpTransportTarget(('192.168.2.36', 161)),
                          ContextData(),
                          0,4,
                          ObjectType(ObjectIdentity('SNMP-VIEW-BASED-ACM-MIB','vacmGroupName')),
                          lexicographicMode=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))