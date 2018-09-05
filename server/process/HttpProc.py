# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import logging

from framework.SProcess import SProcess
from server.services.HttpService import HttpService


class HttpProc(SProcess):
    _logger = None
    _http_service = None
    _main_dev = None
    def __init__(self, mainDev):
        super(HttpProc, self).__init__()
        self._logger = logging.getLogger(str(__name__))
        self._http_service = HttpService(self)
        self.registerService(self._http_service)
        self._main_dev = mainDev
        pass
    def getMainDev(self):
        return self._main_dev
        pass
        