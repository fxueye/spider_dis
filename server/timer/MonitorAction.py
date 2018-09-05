# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.timer.Action import Action
from framework.timer.PeriodicTimer import PeriodicTimer
from server.AppQueue import AppQueue
from util.SysConfig import SysConfig
from util.TimerUtil import TimerUtil



class MonitorAction(Action):
    _logger = None
    _process = None
    _timer = None
    _is_over = None
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        monitorSecond = SysConfig.config["servers"]["monitorSecond"]
        if not monitorSecond:
            monitorSecond = 5
        self._timer = PeriodicTimer(TimerUtil.secondToMills(monitorSecond))
        self._process = proc
        self._is_over = False
        pass
    def update(self, diff, now):
        return self._timer.update(diff)
        pass        
    def call(self): 
        self._logger.error("####:%d" % AppQueue.Cmders.qsize())
        pass
    def isOver(self):
        return self._is_over
        pass
    
    
