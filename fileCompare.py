#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''比较两个文件脚本，以html格式输出'''
import difflib
import sys


try:
    scriptname=sys.argv[0]  #脚本名称
    textfile1=sys.argv[1]   #第一个配置文件路径参数
    textfile2=sys.argv[2]   #第二个配置文件路径参数
except Exception, e:
    print "Error:" +str(e)
    print "Usage: %s filename1 filename2" % scriptname
    sys.exit()


def readfile(filename):  #文件读取分隔函数
    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines() #文件读取后以行分割
        fileHandle.close()
        return text
    except IOError as error:
        print('Read files Error:'+str(error))
        sys.exit()


if textfile1 =="" or textfile2 =="":  #判断参数是否为空
    print "Usage: %s filename1 filename2" % scriptname
    sys.exit()


text1_lines = readfile(textfile1)  #调取readfile函数，获取分隔后的字符串
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()  #创建HtmlDiff()对象
print d.make_file(text1_lines,text2_lines) #通过make_file方法输出HTML格式的比对结果
