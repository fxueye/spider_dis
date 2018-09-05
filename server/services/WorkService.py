# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging


from framework.Service import Service
from server.AppQueue import AppQueue
from util.SysConfig import SysConfig

class WorkService(Service):
    _logger = None
    _process = None
    _work_try = None
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        self._work_try = SysConfig.config["servers"]["workTry"]
        pass
    def start(self):
        pass
    def update(self, diff, now):
        if not AppQueue.Cmders.empty():
            cmd = AppQueue.Cmders.get()
            try:
                cmd.execute()
            except Exception, e:
                self._logger.error(str(e))
                cmd.addTimes()
                if cmd.getTimes() < self._work_try:
                    AppQueue.Cmders.put(cmd)
        pass
    def close(self):
        pass
    