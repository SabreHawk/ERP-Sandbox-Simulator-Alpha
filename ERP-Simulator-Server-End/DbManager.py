# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang


import pymysql


class DbManager(object):
    def __init__(self):
        self.__db_ip = 'localhost'
        self.__user_name = 'root'
        self.__user_pwd = '0000'
        self.__db_name = 'erp_system_manager'
        self.__db = pymysql.connect(self.__db_ip, self.__user_name, self.__user_pwd, self.__db_name)
        self.__cursor = self.__db.cursor()

    def close(self):
        self.__db.close()

    def execute(self, _sql):
        if isinstance(_sql, list):
            for tmp_sql in list:
                try:
                    self.__cursor.execute(str(tmp_sql))
                    self.__db.commit()
                    return True
                except pymysql.DatabaseError as error:
                    self.__db.rollback()
                    return False
        elif isinstance(_sql, str):
            try:
                self.__cursor.execute(str(_sql))
                self.__db.commit()
                return True
            except pymysql.DatabaseError as error:
                self.__db.rollback()
                print(error)
                return False
        else:
            print("Error : Class DbManager Error > execute")
            return False

    def query(self, _sql):
        if isinstance(_sql, str):
            try:
                self.__cursor.execute(str(_sql))
                self.__db.commit()
                t = self.__cursor.fetchone()
                if(len(t) == 1):
                    return t[0]
                else:
                    return False
            except pymysql.DatabaseError as error:
                print(error)
                return False
        else:
            print("Error : Class DbManager Error > execute")
            return False
