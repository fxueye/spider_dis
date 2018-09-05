# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from const.OpCode import OpCode
from framework.timer.Action import Action
from lib.Calendar import Calendar
from server.AppQueue import AppQueue
from util.SysConfig import SysConfig
from util.TimerUtil import TimerUtil
from server.cmder.SolidotCmder import SolidotCmder


class CollectionAction(Action):
    _logger = None
    _process = None
    _timeOfNextDays = []
    
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        collectionTimes = SysConfig.config["servers"]["collectionTimes"]
        for i in collectionTimes:
            c = Calendar()
            nowhour = c.getHour()
            c.setSecond(0)
            c.setMinute(0)
            c.setHour(i)
            timeOfNextDay = c.getTimeInMillis()
            if timeOfNextDay < self._process.getWorkTime():
                timeOfNextDay = timeOfNextDay + (nowhour >= 5 if TimerUtil.DAY_MILLS else 0)
            self._timeOfNextDays.append(timeOfNextDay)
            pass
    def update(self, diff, now):
        ret = False
        for i in range(len(self._timeOfNextDays)):
            timeOfNextDay = self._timeOfNextDays[i]
            if timeOfNextDay < now:
                self._logger.debug("reset when new day now %s" % (TimerUtil.timeToStr(self._process.getWorkTime())))
                timeOfNextDay = timeOfNextDay + TimerUtil.DAY_MILLS
                ret = True
            self._timeOfNextDays[i] = timeOfNextDay
        return ret
        pass        
    def call(self):
        AppQueue.Cmders.put(SolidotCmder(OpCode.GET_ITEM))
        pass
    def isOver(self):
        return False
        pass
