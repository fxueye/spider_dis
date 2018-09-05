# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2016年7月10日
@email: 281431280@qq.com
@author: skw
'''
from lib.Network import Network
from server.cmder.BaseCmder import BaseCmder


class HttpCmder(BaseCmder):
    _net = None
    _params = None
    _retun_data = None
    def __init__(self, url, code):
        super(HttpCmder, self).__init__(code)
        self._net = Network(url)
        pass
    def post(self):
        if self._params:
            self._retun_data = self._net.open('post', '', self._params)
            self._logger.debug("reslut:"+self._retun_data)
        pass
    def get(self):
        if self._params:
            self._retun_data = self._net.open('get', '', self._params)
            self._logger.debug("reslut:"+self._retun_data)
        pass
    def setParams(self, params):
        self._params = params
        pass
        