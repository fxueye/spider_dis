# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年11月19日
@author: QQ:281431280
'''
import commands
class Shell(object):
    _shell = None
    _status = None
    _out_put = None
    def __init__(self,shell):
        self._shell = shell
    def run(self):
        (self._status,self._out_put) = commands.getstatusoutput(self._shell)
    def getOutPut(self):
        return self._out_put
    def getStatus(self):
        return self._status
if __name__ == "__main__":
    shell = Shell("/usr/local/php/sbin/php-fpm restart")
    shell.run()
    print shell.getOutPut()
        