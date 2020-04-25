#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          UsmUserData('trap001', 'Changeme_123', 'Changeme_123',
                                      authProtocol=usmHMACMD5AuthProtocol,
                                      privProtocol=usmAesCfb128Protocol
                                      ),
                          UdpTransportTarget(('192.168.102.1', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNeMemo', 0))):

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