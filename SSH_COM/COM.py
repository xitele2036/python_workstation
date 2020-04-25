#!/usr/bin/python3
# -*- coding: utf-8 -*-


import serial





if __name__ == '__main__':
    # serial = serial.Serial('COM26', 115200, timeout=0.5)  #/dev/ttyUSB0
    # if serial.isOpen() :
    #     print("open success")
    # else :
    #     print("open failed")
    #
    ser = serial.Serial()
    ser.port = 'COM25'
    ser.baudrate = 115200
    ser.timeout = 0.5

    txpower = "cfg.lua show snmpd\r"


    ser.write(txpower.encode())
    # for i in serial.readlines():
    #     print(i.decode())
    print(ser.readall().decode())



# import serial
#
# class COMUtility:
#
#     # 初始化
#     def __init__(self,COM):
#         self.ser = serial.Serial()
#         self.ser.port = 'COM25'
#         self.ser.baudrate = 115200
#         self.ser.timeout = 0.5
#
#     def send(self,comm):
#         self.ser.write(comm.encode())
#         result = self.ser.readall().decode()
#         return result
#
#
#
# if __name__ == "__main__":
#
#     CM = COMUtility('COM25')
#     CM.send("cfg.lua show snmpd")