# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2016年7月10日
@email: 281431280@qq.com
@author: skw
'''
import logging

from const.OpCode import OpCode


class BaseCmder(object):
    _logger = None
    _code = None
    _times = None
    def __init__(self, code):
        self._logger = logging.getLogger(str(__name__))
        self._code = code
        self._times = 0
        pass
    def execute(self):
        {
            OpCode.TEST : lambda :self.test(),
            OpCode.GET_ITEM : lambda : self.getItems(),
            OpCode.GET_ARTICLE : lambda : self.getArticle(),
            OpCode.HTTP_POST:lambda :self.post(),
            OpCode.HTTP_GET:lambda :self.get()
        }[self._code]()
    def addTimes(self):
        self._times += 1
    def getTimes(self):
        return self._times