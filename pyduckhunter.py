#!/usr/bin/python env
#-*-coding:utf-8-*-
import os,sys,time
sys.dont_write_bytecode = True
from config import *
from logo import *
print logo()
def choise0():
    demo.demo()
def choise1():
    Powershell_payload.Powershell_payload()
def choise2():
    wireless_payload.wireless_payload()
dict = {0: choise0,1:choise1,2:choise2}
while True:
        n = raw_input("[\033[1;32;1mpyduckhunter>\033[0m]")
        try:
            if n == "show":
                print show()
            elif n == "help":
                print hp()
            elif n == "exit":
                print "感谢使用！"
                exit()
            try:
                dict[int(n)]()
            except ValueError:
                None
            dict[str(n)]()
        except KeyError:
            None