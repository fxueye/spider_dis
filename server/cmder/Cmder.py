# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2016年7月10日
@email: 281431280@qq.com
@author: skw
'''
from server.cmder.BaseCmder import BaseCmder
import logging


class Cmder(BaseCmder):
    def __init__(self, code):
        super(Cmder, self).__init__(code)
        self._logger = logging.getLogger(str(__name__))
        pass
    def test(self):
        self._logger.debug("############:%s" % self._code)
        pass
