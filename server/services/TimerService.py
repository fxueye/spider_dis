# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''






from framework.Service import Service
import logging
from server.timer.MonitorAction import MonitorAction
from server.timer.CollectionAction import CollectionAction
class TimerService(Service):
    _logger = None
    _process = None
    _actions = []
    def __init__(self, proc):
        self._logger = logging.getLogger(str(__name__))
        self._process = proc
        pass
    def setProcess(self, proc):
        self._process = proc
        pass
    def addAction(self, action):
        self._actions.append(action)
        pass
    def removeAction(self, action):
        self._actions.remove(action)
        pass
    def close(self):
        self._actions = []
        pass
    def start(self):
        monitorAction = MonitorAction(self._process)
        self._actions.append(monitorAction)
        collectionAction = CollectionAction(self._process)
        self._actions.append(collectionAction)
        pass
    def update(self, diff, now):
        self._actions = filter(lambda x:not x.isOver(), self._actions)
        for a in self._actions:
            if a.update(diff, now):
                a.call()
        pass
