# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import cookielib
import urllib2
from util.Md5Util import Md5Util
import os
from urlparse import urlparse
import urllib

class SuperBrowser(object):
    _tmp = None
    _base_url = None
    _cookie = None
    _opener = None
    _response  = None
    def __init__(self,url,tmp = "./tmp"):
        self._tmp = tmp
        if not os.path.exists(self._tmp):
            os.makedirs(self._tmp)
        parts = urlparse(url)
        self._base_url = "%s://%s"%(parts.scheme,parts.netloc)
        md5str = Md5Util.md5(self._base_url)
        filename = "%s/%s"%(self._tmp,md5str)
        if not os.path.exists(filename):
            self._cookie = cookielib.MozillaCookieJar(filename)
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookie))
            self._response = self._opener.open(url)
#             self._cookie.save(ignore_discard = True, ignore_expires = True)
        else:
            self._cookie = cookielib.MozillaCookieJar()
            self._cookie.load(filename, ignore_discard= True, ignore_expires = True)
            req= urllib2.Request(url)
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookie))
            self._response = self._opener.open(req)
        pass
        self.setHeader("")
    def cookieSave(self,ignore_discard = True, ignore_expires = True):
        if not self.cookieIsExist():
            self._cookie.save(ignore_discard = True, ignore_expires = True)
        pass
    def clearCookie(self):
        md5str = Md5Util.md5(self._base_url)
        filename = "%s/%s"%(self._tmp,md5str)
        if self.cookieIsExist():
            os.remove(filename)
        pass
    def cookieIsExist(self):
        if not os.path.exists(self._tmp):
            os.makedirs(self._tmp)
        md5str = Md5Util.md5(self._base_url)
        filename = "%s/%s"%(self._tmp,md5str)
        return os.path.exists(filename)
        pass
    def setHeader(self,referer):
        self._opener.addheaders = [("User-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"),("Accept","*/*"),('Referer',referer)]
    def openUrl(self,url,postdata = {}):
        postdata = urllib.urlencode(postdata)
        if self._opener != None:
            self._response = self._opener.open(url,postdata)
        pass
    def login(self,url,postdata = {}):
        postdata = urllib.urlencode(postdata)
        if self._opener != None:
            self._response = self._opener.open(url,postdata)
        pass
    def getResponse(self):
        return self._response
if __name__=='__main__':
    b = SuperBrowser()
    b.openUrl("http://t66y.com");
    print b.getResponse()

    
