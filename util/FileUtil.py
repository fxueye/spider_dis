#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2016年7月10日
@email: 281431280@qq.com
@author: skw
'''

import os
class FileUtil(object):
    def __init__(self):
        pass
    
    @staticmethod
    def getFileExtension(file):  # @ReservedAssignment
        return os.path.splitext(file)[1]
    @staticmethod
    def mkdir(path):
        path = path.strip()
        path = path.rstrip("\\")
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    @staticmethod
    def saveFile(path,fileName,data):
        if data == None:
            return;
        FileUtil.mkdir(path)
        if not path.endswith("/"):
            path = path + "/"
        file = open(path + fileName,"wb")  # @ReservedAssignment
        file.write(data)
        file.flush()
        file.close()
    @staticmethod
    def getFileName(url):
        fileName = os.path.basename(url)
        return fileName
        