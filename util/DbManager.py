# -*- coding: utf-8 -*-
'''
Created on 2016年4月3日
@author: skw QQ:281431280
'''
import MySQLdb  
from DBUtils.PooledDB import PooledDB  
from util.SysConfig import SysConfig
import threading
class DbManager(object):
    DbPool = None
    mutex = threading.Lock()
    def __init__(self):
        pass
    @staticmethod
    def getCon():
        if DbManager.DbPool is None:
            DbManager.mutex.acquire()
            DbManager.DbPool = PooledDB(creator=MySQLdb, mincached=SysConfig.config["db"]["mincached"] , maxcached=SysConfig.config["db"]["maxcached"], maxconnections=SysConfig.config["db"]["maxconnections"], host=SysConfig.config["db"]["host"] , port=SysConfig.config["db"]["port"], user=SysConfig.config["db"]["user"] , passwd=SysConfig.config["db"]["passwd"], db=SysConfig.config["db"]["db"], use_unicode=False, charset=SysConfig.config["db"]["charset"])
            DbManager.mutex.release() 
        return DbManager.DbPool.connection()
    @staticmethod
    def query(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = None
        try:
            count = cursor.execute(sql, data)
            if count > 0:
                result = cursor.fetchall()
                ret = result
            
        except Exception, ex:
            con.rollback()
            print ex
        con.close()
        cursor.close()
        return ret
    @staticmethod
    def queryOne(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = None
        try:
            count = cursor.execute(sql, data)
            if count > 0:
                results = cursor.fetchone()
                ret = results
            
        except Exception, ex:
            con.rollback()
            print ex
        con.close()
        cursor.close()
        return ret
        pass
    @staticmethod
    def select(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = None
        try:
            count = cursor.execute(sql, data)
            if count > 0:
                result = cursor.fetchall()
                ret = result
        except Exception, ex:
            print ex
        con.close()
        cursor.close()
        return ret
    @staticmethod
    def delete(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = None
        try:
            count = cursor.execute(sql, data)
            if count > 0:
                result = cursor.fetchall()
                con.commit()
                ret = result
            return None
        except Exception, ex:
            con.rollback()
            print ex
        con.close()
        cursor.close()
        return ret
    @staticmethod
    def update(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = None
        try:
            count = cursor.execute(sql, data)
            if count > 0:
                con.commit()
            ret = count
        except Exception, ex:
            con.rollback()
            print ex
        con.close()
        cursor.close()
        return ret
        pass
    @staticmethod
    def insert(sql, data=[], cursor_tuple=True):
        con = DbManager.getCon()
        cursor = con.cursor()
        if cursor_tuple :
            cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        ret = False
        try:
            cursor.execute(sql, data)
            con.commit()
            ret = True
        except Exception, ex:
            con.rollback()
            print str(ex)
            ret = False
        con.close()
        cursor.close()
        return ret    

    
