# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.SProcess import SProcess
from server.services.WorkService import WorkService
class WorkProc(SProcess):
    _logger = None
    _work_service = None
    _main_dev = None
    def __init__(self, mainDev):
        super(WorkProc, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        self._work_service = WorkService(self)
        self.registerService(self._work_service)
        self._main_dev = mainDev
        pass
    def getMainDev(self):
        return self._main_dev
        pass
        