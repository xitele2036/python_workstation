'''
def connect_snmpv1v2(read,host,version):
    if version == "V1":
        num = 0
    else:
        num = 1
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(read, mpModel=num),
               UdpTransportTarget((host, 161)),
               ContextData(),
               # N,R,
               #ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
               ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNeMemo', 0))
               )
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind])[30:41])
            var = ' = '.join([x.prettyPrint() for x in varBind])[30:41]
    return var

def connect_snmpv3(v3trapname,authtype,authkeys,encrypttype,encryptkey,host):

    if authtype == "MD5":
        auth = 'authProtocol=usmHMACMD5AuthProtocol'
    else:
        auth = 'authProtocol=usmHMACSHAAuthProtocol'
    if encrypttype == "DES":
        priv = 'privProtocol=usmDESPrivProtocol'
    else:
        priv = 'privProtocol=usmAesCfb128Protocol'

    auth = 'authProtocol=usmHMACMD5AuthProtocol'
    priv = 'privProtocol=usmAesCfb128Protocol'
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
                UsmUserData(v3trapname, authkeys, encryptkey,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmAesCfb128Protocol
                            ),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity('OPTIX-NE-MIB', 'optixNeMemo', 0))
               )
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind])[30:41])
            #var = ' = '.join([x.prettyPrint() for x in varBind])[30:41]
    #return var


def change_web():
    change = "cp /tmp/log/html/sysauth.htm /usr/lib/lua/luci/view/sysauth.htm"
    SS.send(change)

def main():
    booled = False
    if booled == False:
        change_web()
        booled = True
    #add_snmpv1v2(username,password,localnames,readnames,writenames,port_ids,communitys,"V1")
    #time.sleep(60)
    #add_snmpv1v2(username, password, localnames, readnames, writenames, port_ids, communitys, "V2")
    #time.sleep(60)
    #add_snmpv3(username,password,localnames,port_ids,v3trapnames,authtypes,authkeyss,encrypttypes,encryptkeys)
    #time.sleep(60)
    connect_snmpv1v2(readnames,hostnames,"V1")
    time.sleep(10)
    connect_snmpv1v2(readnames, hostnames, "V2")
    time.sleep(10)
    #connect_snmpv3(v3trapnames,authtypes,authkeyss,encrypttypes,encryptkeys,hostnames)
main()


init_path = os.path.dirname(os.path.realpath(__file__))
hostnames = "192.168.102.1"
localnames = "192.168.102.2"
v3trapnames = "trap001"
authtypes = "MD5"
authkeyss = "Changeme_123"
encrypttypes = "AES"
encryptkeys = "Changeme_123"
versions = "V1"
readnames = "public123"
writenames = "public123"
port_ids = "162"
communitys = "root@123"
local_path = "https://" + str(hostnames)
port = 22
username = "szhw"
password = "Changeme_123"
basepath = "E:"


#private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
#transport = paramiko.Transport(('192.168.2.36',22))
#transport.connect(username='root',pkey=private_key)

#private_key = paramiko.RSAKey.from_private_key_file('E:\\works\\Security\\id_rsa102.txt')

#s = paramiko.SSHClient()                               # 绑定实例
#s._transport = transport
#s.load_system_host_keys()                                # 加载本地HOST主机文件
#s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
#s.connect(hostnames,port,username,password)
#s.connect(hostnames,port,username,password,pkey=private_key)
# 连接远程主机
#f = open(r"C:\\Users\\ke.liu\\.PyCharm2018.3\\config\\scratches\\conf.json")
#conf = json.loads(f.read())
#adduser = conf.get("SNMP")
#SS = SSHConnect(username,password,hostnames)
'''

