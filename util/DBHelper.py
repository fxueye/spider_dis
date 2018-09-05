#-*- coding:UTF-8 -*-
#! /usr/bin/python
'''
Created on 2015年6月16日
@author: QQ:281431280
'''
import threading

class DBHelper(object):
    conn = None
    mutex = threading.Lock()
    @staticmethod
    def setConn(conn):
        DBHelper.conn = conn
        pass
    @staticmethod
    def query(sql="",data=[]):
        if sql == "": 
            return None
        DBHelper.mutex.acquire()
        result =  DBHelper.conn.query(sql,data,False)
        DBHelper.mutex.release()
        return result
        pass
    @staticmethod
    def query_one(sql="",data=[]):
        if sql == "": 
            return None
        DBHelper.mutex.acquire()
        result =  DBHelper.conn.query_one(sql,data,False)
        DBHelper.mutex.release()
        return result
        pass
    @staticmethod
    def instert(sql="",data= []):
        if sql == "": 
            return
        DBHelper.mutex.acquire()
        reslut = DBHelper.conn.insert(sql,data)
        DBHelper.mutex.release()
        return reslut

    
    @staticmethod
    def update(sql="",data=[]):
        if sql == "":
            return
        DBHelper.mutex.acquire()
        DBHelper.conn.update(sql,data)
        DBHelper.mutex.release()
        pass

    
    @staticmethod
    def delete(sql="",data=[]):
        if sql == "":
            return
        DBHelper.mutex.acquire()
        DBHelper.conn.delete(sql,data)
        DBHelper.mutex.release()
        pass
    
    
    
    
        