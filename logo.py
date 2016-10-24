#!/usr/bin/python env
#-*-coding:utf-8-*-
import sys,os
sys.dont_write_bytecode = True
def logo():
    logo =""" ____            _            _    _                 _
|  _ \ _   _  __| |_   _  ___| | _| |__  _   _ _ __ | |_ ___ _ __
| |_) | | | |/ _` | | | |/ __| |/ / '_ \| | | | '_ \| __/ _ \ '__|
|  __/| |_| | (_| | |_| | (__|   <| | | | |_| | | | | ||  __/ |
|_|    \__, |\__,_|\__,_|\___|_|\_\_| |_|\__,_|_| |_|\__\___|_|
       |___/

version:0.2.1

[\033[1;32;1m|..|\033[0m] Written By: Suzumiya QQ:1635123039                 [\033[1;32;1m|..|\033[0m]
[\033[1;32;1m|..|\033[0m] Blog: http://suzumiya.me                           [\033[1;32;1m|..|\033[0m]

这是一款快捷生成nethunter手机DUCKHUNTER功能的攻击代码项目！

show#(查看当前可用模块)
help#(查询帮助)

"""
    return logo
def hp():
    hp ="""
   help#(查看帮助)
   show#(列出所有模块)
   exit#(退出)
"""
    return hp
def show():
    show ="""
   0. Demo test
   1. Payloads for windows
   2. Payloads for wireless
"""
    return show
def input_duckhunter():
    pyduckhunter = "[\033[1;32;1mpyduckhunter>\033[0m]"
    return pyduckhunter