# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年11月16日
@author: QQ:281431280
'''
import threading

class List(object):  # @ReservedAssignment
    _datas = None
    _lock = threading.Lock()
    def __init__(self):
        self._datas = []
        pass
    def append(self, value):
        self._lock.acquire()
        self._datas.append(value)
        self._lock.release()
    def count(self, value):
        self._lock.acquire()
        count = self._datas.count(value)
        self._lock.release()
        return count
    def extend(self, iterable):
        self._lock.acquire()
        self._datas.extend(iterable)
        self._lock.release()
    def index(self, value):
        self._lock.acquire()
        self._datas.index(value)
        self._lock.release()
    def insert(self, index, obj):
        self._lock.acquire()
        self._datas.insert(index, obj)
        self._lock.release()
    def pop(self):
        self._lock.acquire()
        self._datas.pop()
        self._lock.release()
    def remove(self, value):
        self._lock.acquire()
        self._datas.remove(value)
        self._lock.release()
    def reverse(self):
        self._lock.acquire()
        self._datas.reverse()
        self._lock.release()
    def sort(self, cmp=None, key=None, reverse=False):  # @ReservedAssignment
        self._lock.acquire()
        self._datas.sort(cmp, key, reverse)
        self._lock.release()
    def len(self):
        self._lock.acquire()
        length =len(self._datas)
        self._lock.release()
        return length
    def clone(self):
        new = []
        self._lock.acquire()
        for i in self._datas:
            new.append(i)
        self._lock.release()
        return new
    def clear(self,delete = False):
        self._lock.acquire()
        if not delete:
            self._datas = []
        else:
            del self._datas[:]
        self._lock.release()
    def contains(self,value):
        self._lock.acquire()
        ret = False
        if value in self._datas:
            ret = True
        self._lock.release()
        return ret
      
        
        
