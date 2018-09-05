#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月24日
@author: QQ:281431280
'''
import random
import sys
class RandHelper(object):
    @staticmethod
    def nextInt(n = None):
        if n == None:
            return random.randint(0,sys.maxint)
        else:
            return random.randint(0,n)
        pass
    @staticmethod
    def nextFloat():
        return random.random()
    @staticmethod
    def choice(sequence):
        return random.choice(sequence)