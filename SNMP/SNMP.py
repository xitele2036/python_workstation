#!/usr/bin/python3
# -*- coding: utf-8 -*-


from pysnmp.hlapi import *
from io import StringIO
import serial
import sys
import os
import time
import paramiko
import json

key_str = """-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDAU7yzkwduDZIIE/U3N6uqzVAbB8hADf9vw43OJ+4VdH8i/qMp
1+oZCOkO3gXF7xiApR5zGvxrEETKRoMudxwFijUkfBz8r8e5akT3HQd2YDoCqjJi
eVP27hz/I5CQknFhgRwKwtFgnWu39lMn/s4gZ51EPe2a/oBjivwqqfRkWQIDAQAB
AoGBAJS7rUDKQYKwZ/BrTsWm/dEW+g4NVKWErbfG6VE2u/5Hm1J6zb+8REOcCm/+
70QFBVPnXcbyZaZ+bFRpd2Vlo3qk49HdkyeHma8/BK7yLrntXMxKXAMufE329Xki
ZdQuI91rf0scldmGADtTMZ01upmTRZC4lPeJt8lyltKT6GqpAkEA8TpEX5BVMfNJ
Vi74zcFiMd9NbG/Tzao5/8GHTbJW4YEmVeMFDR17aZC848xIqSEP3YUaNjnShStG
wCW6870N4wJBAMwa2u6hN36hwsgbiikEsmGUNiO5noIgF9rKyz//OfGh+LhBi6U7
NCbtAaly9XtmDLOEjQAq6F+OF9chcw/g2ZMCQGKG+gZOXX3ZcMrSxKzFn+Xe3zC7
PDd0n9vmn+0MOpBAv/e0kguZTx7/Dye7+LGb328LPnmHhIT/+BXjU0janyECQQCZ
yh5usfEjrHUc3ItkztIt7kRA9Or3d4Eh7a3qIcCiTf4fr9ut+4cXUXvwFtvbSBCH
73diyfHflixmgCC3tR+bAkEAvFL1Jq9/Br6MeuCL5fvxMZIKq/gnKEvd6DThyCAI
Bri4UsVmRQ2gwr0aPztzhKIglL0XB6QivBL+wfwCEGxaSA==
-----END RSA PRIVATE KEY-----"""


f = open("E:\\Python-project\\test1\\conf.js",'rb')
conf = json.loads(f.read())
HOST_NAME = conf.get("hostname")
USER = conf.get("username")
PASSWD = conf.get("password")
PORT_ID = conf.get("port")
VIEW_LOCK = conf.get("view_offlock")
SNMPV1 = conf.get("snmpv1")
SNMPV2 = conf.get("snmpv2")




private_key = paramiko.RSAKey.from_private_key_file('E:\\works\\Security\\id_rsa102.txt')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(HOST_NAME,PORT_ID,USER,PASSWD,pkey=private_key)



#snmpv1 walk节点的值
def snmpv1_walk(MIB_NAME, MIB_OID, HOST_NAME):

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public@HWR31',mpModel=0),
                              UdpTransportTarget((HOST_NAME, 161)),
                              ContextData(),
                              #0,3,
                              ObjectType(ObjectIdentity(MIB_NAME, MIB_OID)),
                              #ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNePosition',0)),
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

#snmpv1 set节点的值
def snmpv1_set(MIB_NAME, MIB_OID, SET_MIB_OID_VALUE, HOST_NAME):
    errorIndication, errorStatus, errorIndex, varBinds = next(setCmd(SnmpEngine(),
               CommunityData('public@HWR31','private@HWR31',mpModel=0),
               UdpTransportTarget((HOST_NAME, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(MIB_NAME, MIB_OID, 0), SET_MIB_OID_VALUE)
               ))
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))



#snmpv1 get节点的值
def snmpv1_get(MIB_NAME, MIB_OID, HOST_NAME):
    errorStatus, errorIndication, errorIndex, varBinds = next(getCmd(SnmpEngine(),
               CommunityData('public@HWR31',mpModel=0),
               UdpTransportTarget((HOST_NAME, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(MIB_NAME, MIB_OID, 0))
               ))
    for varBind in varBinds:
        print(' = '.join(x.prettyPrint() for x in varBind))

#snmp walk节点的值
def snmpv2_walk(MIB_NAME, MIB_OID, HOST_NAME):

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public@HWR32',mpModel=1),
                              UdpTransportTarget((HOST_NAME, 161)),
                              ContextData(),
                              #0,3,
                              ObjectType(ObjectIdentity(MIB_NAME, MIB_OID)),
                              #ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNePosition',0)),
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

#snmp set节点的值
def snmpv2_set(MIB_NAME, MIB_OID, SET_MIB_OID_VALUE, HOST_NAME):
    errorIndication, errorStatus, errorIndex, varBinds = next(setCmd(SnmpEngine(),
               CommunityData('public@HWR32','private@HWR32',mpModel=1),
               UdpTransportTarget((HOST_NAME, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(MIB_NAME, MIB_OID, 0), SET_MIB_OID_VALUE)
               ))
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))



#snmp get节点的值
def snmpv2_get(MIB_NAME, MIB_OID, HOST_NAME):
    errorStatus, errorIndication, errorIndex, varBinds = next(getCmd(SnmpEngine(),
               CommunityData('public@HWR32',mpModel=1),
               UdpTransportTarget((HOST_NAME, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(MIB_NAME, MIB_OID, 0))
               ))
    for varBind in varBinds:
        print(' = '.join(x.prettyPrint() for x in varBind))





if __name__ == '__main__':
    if type(SNMPV1) is list:
        command = ('&&').join(SNMPV1)
        stdin, stdout, stderr = s.exec_command(command.encode())
        print("success")
    else:
        stdin, stdout, stderr = s.exec_command(SNMPV1.encode())
    snmpv1_walk('SNMP-VIEW-BASED-ACM-MIB', 'vacmGroupName', HOST_NAME)

    if type(SNMPV1) is list:
        command = ('&&').join(SNMPV2)
        stdin, stdout, stderr = s.exec_command(command.encode())
        print("success")
    else:
        stdin, stdout, stderr = s.exec_command(SNMPV2.encode())

    snmpv2_get('SNMP-VIEW-BASED-ACM-MIB', 'vacmGroupName', HOST_NAME)

#    snmpv1_set('OPTIX-OID-MIB', 'optixNeName', 'BA', HOST_NAME)
#    snmpv1_get('OPTIX-OID-MIB', 'optixNeName', HOST_NAME)

#if snmpv1_set('OPTIX-OID-MIB','optixNeName','BATIANHU',HOST_NAME) == snmpv1_get('OPTIX-NE-MIB','optixNeName',HOST_NAME):
#    print("PASS")
#else:
#    print("FAIL")