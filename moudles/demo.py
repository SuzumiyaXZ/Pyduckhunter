#!/usr/bin/python env
#-*-coding:utf-8-*-
import os,sys
#demo 测试
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