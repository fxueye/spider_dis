# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import hashlib
class Md5Util(object):
    @staticmethod
    def md5(string):
        m = hashlib.md5()
        m.update(string)
        return m.hexdigest()