# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月24日
@author: QQ:281431280
'''
from lib.RandHelper import RandHelper

class UUID(object):
    #
    # ID | RandHelper.nextLong() >>> 8
    #
    @staticmethod
    def getUID4DB(tid):
        return (tid << 26) | (RandHelper.nextInt(999) << 24) | (RandHelper.nextInt() >> 8)
    @staticmethod
    def getUUID(sid):
        return (sid << 24) | (RandHelper.nextInt() & 0xffffff)
if __name__ == '__main__':
    data = []
    rdata = []
    while True:
        uid = UUID.getUID4DB(3)
        if data.count(uid) > 0:
            rdata.append(uid)
        else:
            data.append(uid)
        print len(data)
        if len(data) >= 1000000:
            break;
    print rdata
