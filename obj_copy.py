#! /usr/bin/env/ python
# coding=utf-8
# 深拷贝与浅拷贝
import copy
a=[[1],[2],[3]]
b=copy.copy(a)
c=copy.deepcopy(a)
print "before=>"
print a
print b
print c
a[0][0] = 0
a[1]=None
print 'after=>'
print a
print b
print c
x = 3.14
import sys
