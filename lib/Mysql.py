# -*- coding: utf-8 -*-
'''
Created on 2015年6月14日

@author: Administrator
'''
import MySQLdb.cursors
from _mysql import result
class Mysql(object):
    _conn =None
    _cursor_tuple = True
    def __init__(self, host="127.0.0.1", port=3306, user="root", pwd="root", charset="utf8"):
        self._conn = MySQLdb.connect(host=host,port=port,user=user, passwd=pwd, charset=charset)
        self._cursor = self._conn.cursor()
    def select_db(self,db):
        self._conn.select_db(db)
        pass
    def query(self, sql="",data=[] , cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            count = self._cursor.execute(sql,data)
            if count > 0:
                results = self._cursor.fetchall()
                return results
            return None
        except Exception, ex:
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
        return None
    def query_one(self, sql="",data=[], cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            count = self._cursor.execute(sql,data)
            if count > 0:
                result = self._cursor.fetchone()
                return result
            return None
        except Exception, ex:
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
        return None
        pass
    def delete(self , sql="", data=[] , cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            count = self._cursor.execute(sql,data)
            if count > 0:
                result = self._cursor.fetchall()
                self._conn.commit()
                return result
            return None
        except Exception, ex:
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
        pass
    def update(self,sql="",data="",cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            count = self._cursor.execute(sql,data)
            if count > 0:
                result = self._cursor.fetchall()
                self._conn.commit()
                return result
            return None
        except Exception, ex:
            print ex
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
        pass
    def insert(self, sql = "",values = [],cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            result = self._cursor.execute(sql,values)
            if result > 0:
                self._conn.commit()
                self._cursor.execute("select last_insert_id()")
                ret =  self._cursor.fetchone()[0]
                if ret > 0:
                    return ret
            return True
        except Exception, ex:
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
            return False    
    def insert_many(self,sql= "",values=[],cursor_tuple = True):
        self._cursor = self._conn.cursor()
        if not cursor_tuple :
            self._cursor = self._conn.cursor(cursorclass =MySQLdb.cursors.DictCursor)
        try:
            result = self._cursor.executemany(sql,values)
            if result > 0:
                self._conn.commit()
            return True
        except Exception, ex:
            self._conn.rollback()
            raise Exception,"mysql error:%s"%(str(ex))
            return False    
        pass
    def close(self):
        self._conn.close()
    def commit(self):
        self._conn.commit()
    def __del__(self):
        self._conn.close()
        self._cursor.close
def main():
    tableNames = []
    allColumns = []
    allColumnSupper = []
    mysql = Mysql("127.0.0.1", 3306, "root", "root",  "utf8")
    mysql.select_db("logic")
    tables = mysql.query("show tables")
    print tables
    for t in tables:
        tableName = t[0]
        tableNames.append(tableName)
        columns = mysql.query("show COLUMNS from %s"%(t[0]))
        print columns
        for c in columns:
            if c[0] != "":
                column = str(c[0]);
                print column
                allColumns.append(column)
                allColumnSupper.append((tableName+"_"+column).upper())
#         print columns
    print tableNames
    print allColumns
    print allColumnSupper
    print mysql.query("select * from area where uid = %s",[123])

    pass
if __name__ == '__main__':
    main()
