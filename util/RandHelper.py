#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月24日
@author: QQ:281431280
'''
import random
import sys
import itertools
import time
class RandHelper(object):
    @staticmethod
    def nextInt(n = None):
        if n == None:
            return random.randint(-sys.maxint,sys.maxint)
        else:
            return random.randint(0,n)
        pass
    @staticmethod
    def nextFloat():
        return random.random()
    @staticmethod
    def choice(sequence):
        return random.choice(sequence)
    @staticmethod
    def randIndex(rateArr ,totalWeight):
        if rateArr != None and len(rateArr) > 0:
            rand = RandHelper.nextInt(totalWeight)
            print 
            upper = 0
            for i in range(len(rateArr)):
                if rand < rateArr[i] + upper:
                    return i
                upper = upper + rateArr[i]
        return None
if __name__ == '__main__':
    ii = []
    for i in itertools.combinations([1,3,4,6,7,11,16,18,19,20,22,23,24,25,27,29,31,33],6):
        ii.append(i) 
    lan = [4,6,9,10,11]
    for i in range(10):
        time.sleep(1)
        print ii[RandHelper.nextInt(len(ii)-1)]
        print lan[RandHelper.nextInt(3)]
    print len(ii)
    