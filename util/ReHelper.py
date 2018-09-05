#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月24日
@author: QQ:281431280
'''
import re
class ReHelper(object):
    @staticmethod
    def findAll(pattern,string):
        regex = re.compile(r'%s'%pattern,re.DOTALL)
        return regex.findall(string)
    @staticmethod
    def sub(pattern,string ,substr = ""):
        regex = re.compile(r'%s'%pattern,re.I)
        return regex.sub(substr,string)