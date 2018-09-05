# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging


from framework.Service import Service
import uuid

class MainService(Service):
    _logger = None
    _process = None
    number = 0
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        pass
    def start(self):
        pass
    def update(self, diff, now):
#         self._logger.debug(uuid.uuid1())
#         self._logger.debug("%d"%(now))
         
        pass
    def close(self):
        pass
    
        
        
