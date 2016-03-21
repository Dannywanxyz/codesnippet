#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import string
# 利用urllib读取页面源码
sock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
source = sock.read()
sock.close()
# 匹配字符
# print source
data = re.findall(r'<!--(.+?)-->', source, re.S)
# print data
charlist = re.findall(r'([a-zA-Z])', data[1])
print string.join(charlist)








