# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月17日
@author: QQ:281431280
'''


import logging
import threading

from framework.SDevice import SDevice
from server.process.HttpProc import HttpProc
from server.process.MainProc import MainProc
from server.process.WorkProc import WorkProc
from util.SysConfig import SysConfig


class MainDev(SDevice):
    _logger = None
    _main_proc = None
    _work_procs = None
    _http_procs = None
    instance = None
    mutex = threading.Lock()
    def __init__(self):
        super(MainDev, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        interval = SysConfig.config["servers"]["interval"]
        if not  interval:
            interval = 200
        workCount = SysConfig.config["servers"]["workProcCount"]
        httpCount = SysConfig.config["servers"]["httpProcCount"]
        self._work_procs = []
        self._http_procs = []
        for i in range(workCount):
            work_proc = WorkProc(self)
            work_proc.setName("work_proc-%d" % i)
            self._work_procs.append(work_proc)
            self.addProcess(work_proc, interval)
        for i in range(httpCount):
            http_proc = HttpProc(self)
            http_proc.setName("http_proc-%d" % i)
            self._http_procs.append(http_proc)
            self.addProcess(http_proc, interval)
        self._main_proc = MainProc(self)
        self.addProcess(self._main_proc, interval)
        pass
    @staticmethod
    def GetInstance():
        if(MainDev.instance == None):
            MainDev.mutex.acquire()
            MainDev.instance = MainDev()
            MainDev.mutex.release()
        return MainDev.instance
        pass
    def getMainProc(self):
        return self._main_proc
    def start(self):
        super(MainDev, self).start()
    def close(self):
        super(MainDev, self).close()
        self._db.close()
        self._logger.debug("server close ........")
