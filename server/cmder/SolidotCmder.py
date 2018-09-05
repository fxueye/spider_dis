# -*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2016年7月10日
@email: 281431280@qq.com
@author: skw
'''
import logging

from const.OpCode import OpCode
from lib.Browser import Browser
from server.AppQueue import AppQueue
from server.cmder.BaseCmder import BaseCmder
from server.cmder.HttpCmder import HttpCmder
from util.ReHelper import ReHelper
from util.SysConfig import SysConfig
from server.AppList import AppList


class SolidotCmder(BaseCmder):
    _brower = None
    _article_url = None
    _cuid = None
    def __init__(self, code):
        super(SolidotCmder, self).__init__(code)
        self._logger = logging.getLogger(str(__name__))
        self._brower = Browser()
        pass
    def getItems(self):
        urls = SysConfig.config['solidot']['urls']
        cuids = SysConfig.config['solidot']['cuid']
        for j in range(len(urls)):
            url = urls[j]
            html = self._brower.openurl(url).read().decode(SysConfig.config['solidot']['charset']).encode('utf-8')
            center = "<div id=\"center\">(.*?)<div class=\"page\">"
            center_str = ReHelper.findAll(center,html)
            item = "<a href=\"(/story\?sid=\d+?)\">.*?</a>"
            items = ReHelper.findAll(item, center_str[0])
            items = list(set(items))
            for i in items:
                new_url = url+i
                print new_url
                if not AppList.UrlList.contains(new_url):
                    cmder = SolidotCmder(OpCode.GET_ARTICLE)
                    cmder.setArticleUrl(new_url)
                    cmder.setCuid(cuids[j])
                    AppQueue.Cmders.put(cmder)
                    AppList.UrlList.append(new_url)
        self._logger.debug("############:%s" % self._code)
        pass
    def getArticle(self):
        html = self._brower.openurl(self._article_url).read().decode(SysConfig.config['solidot']['charset']).encode('utf-8')
        re_title = "<div class=\"bg_htit\">[\s]+<h2>([^<|^:]+)</h2>"
        title = ReHelper.findAll(re_title, html)
        re_conter="<div class=\"p_mainnew\">(.*?)</div>[\s]+<div class=\"e_reply a_bold\">"
        conter = ReHelper.findAll(re_conter,html)
        conter = ReHelper.sub("(\t|\n| |<a.*?>|<img.*?>|</a>|</div>|<div.*?>|<u.*?>|</u>|<i.*?>|</i>)", conter[0])
        muid = SysConfig.config['solidot']['muid']
        account = SysConfig.config['solidot']['account']
        params = {
                  'cuid':self._cuid,
                  'muid':muid,
                  'title':title[0],
                  'content':conter,
                  'account':account
                  }
        
        post_url = SysConfig.config['solidot']['postUrl']
        cmder = HttpCmder(post_url, OpCode.HTTP_POST)
        cmder.setParams(params)
        AppQueue.HttpCmders.put(cmder)
        
        self._logger.debug("############:%s" % self._code)
        pass
    def setCuid(self,cuid):
        self._cuid = cuid
        pass
    def setArticleUrl(self,url):
        self._article_url = url
        pass
