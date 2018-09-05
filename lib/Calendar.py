# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年11月15日
@author: QQ:281431280
'''
from datetime import datetime
import time

class Calendar(object):
    _year = None
    _month = None
    _day = None
    _hour = None
    _minute = None
    _second = None
    def __init__(self):
        d = datetime.now()
        self._year = d.year
        self._month = d.month
        self._day = d.day
        self._hour = d.hour
        self._minute = d.minute
        self._second = d.second
    def getYear(self):
        return self._year
    def setYear(self, year):
        self._year = year
    def getMonth(self):
        return self._month
    def setMonth(self, month):
        self._month = month
    def getDay(self):
        return self._day
    def setDay(self, day):
        self._day = day
    def getHour(self):
        return self._hour
    def setHour(self, hour):
        self._hour = hour
    def getMinute(self):
        return self._minute
    def setMinute(self, minute):
        self._minute = minute
    def getSecond(self):
        return self._second
    def setSecond(self, second):
        self._second = second
    def setMicroseconds(self):
        pass
    def getMicroseconds(self):
        pass
    def getTimeInMillis(self):
        return time.mktime(time.strptime("%d-%d-%d %d:%d:%d"%(self.getYear(),self.getMonth(),self.getDay(),self.getHour(),self.getMinute(),self.getSecond()), "%Y-%m-%d %H:%M:%S")) * 1000
if __name__ == '__main__':
    c = Calendar()
    print c.getTimeInMillis()