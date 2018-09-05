#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import json


class SysConfig(object):
    config = ""
    def __init__(self):
        pass
    @staticmethod
    def load(configPacth):
        f = open(configPacth, "r")
        line = f.readline()
        while line:
            SysConfig.config =SysConfig.config + line.split("#")[0]
            line = f.readline()
        f.close() 
        SysConfig.config = json.loads(SysConfig.config)
        pass
def main():
    SysConfig.load("../config/config.json")
    print SysConfig.config["db"]["passwd"]
if __name__ == '__main__':
    main()