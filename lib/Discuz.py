# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
from lib.SuperBrowser import SuperBrowser
from util.ReHelper import ReHelper
import time
class Discuz(object):
    _parms_key = None
    _arg = None
    _domain = None
    _super_browser = None
    _formhash = None
    def __init__(self):
        self._parms_key = ['domain', 'answer', 'password', 'questionid', 'referer', 'username']
        self._arg = {}
        pass
    def login(self,**parms):
        for key in self._parms_key:
            if key in parms:
                self._arg[key] = parms[key]
            else:
                self._arg[key] = ''
        self._super_browser = SuperBrowser(self._arg['domain'])
        login = self._arg['domain'] + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        if self.isLogin():
            return True
        self._formhash = self.getFormhash(login)
        postdata = {
       'answer':self._arg['answer'],
       'formhash':self._formhash ,
       'password':self._arg['password'],
       'questionid':0 if self._arg['questionid'] == '' else self._arg['questionid'],
       'referer':self._arg['domain'] if self._arg['referer'] == '' else self._arg['referer'],
       'username':self._arg['username'],
        }
        loginUrl = self._arg['domain'] + 'member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LCaB3&inajax=1'
        self._super_browser.login(loginUrl, postdata)
        loginStr = self._super_browser.getResponse().read()
        if 'succeedhandle_login' in loginStr:
            return True
        return False
        pass
    def isLogin(self):
        login = self._arg['domain'] + 'member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login'
        self._super_browser.openUrl(login)
        ret = self._super_browser.getResponse().read()
        if 'succeedhandle_login' in ret:
            return True
        return False
    def getFormhash(self,login):
        if self._super_browser == None:
            raise TypeError("super browser is None!")
        self._super_browser.openUrl(login)
        htmlStr = self._super_browser.getResponse().read()
        ret = ReHelper.findAll('<input type="hidden" name="formhash" value="(.*?)" />', htmlStr)
        return ret[0]
        pass
    def getSuperBrowser(self):
        return self._super_browser
    def postData(self,title,content,fid):
        postUrl = self._arg['domain'] + 'forum.php?mod=post&action=newthread&fid=%s&extra=&topicsubmit=yes'%(fid)
        beforePostUrl = self._arg['domain'] + 'forum.php?mod=post&action=newthread&fid=%s'%(fid)
        self._formhash = self.getFormhash(beforePostUrl)
        self._super_browser.setHeader(self._arg['domain'] + "forum.php?mod=post&action=newthread&fid=64")
        postdata = {
            'formhash':self._formhash,
            'posttime':int(time.time()),
            'wysiwyg':1,
            'subject':title,
            'message':content,
            'replycredit_extcredits':0,
            'replycredit_times':1,
            'replycredit_membertimes':1,
            'replycredit_random':100,
            'readperm':'',
            'price':'',
            'tags':'',
            'rushreplyfrom':'',
            'rushreplyto':'',
            'rewardfloor':'',
            'replylimit':'',
            'stopfloor':'',
            'creditlimit':'',
            'allownoticeauthor':1,
            'usesig':1,
            'save':'',
            'connect_publish_t':0,
            'uploadalbum':-2,
            'newalbum':'请输入相册名称',
         
         }
        self._super_browser.openUrl(postUrl, postdata)
if __name__ == "__main__":
    Dz = Discuz()
    if Dz.login(username="admin", password="wchskw0922", domain="http://www.php9.cn/"):
        Dz.getSuperBrowser().cookieSave()
    Dz.postData("test2", "test2",64)