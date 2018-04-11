# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang
# Function : Manage Database Operation Of The Server End
# Attention : Add Every Database Operation Into This Class As A Member Function
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

    def __execute(self, _sql):
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
            print("Error : Class DbManager Error > execute() - params must be a list or string")
            return False

    def __query(self, _sql):
        if isinstance(_sql, str):
            try:
                self.__cursor.execute(str(_sql))
                self.__db.commit()
                res = self.__cursor.fetchall()
                return res
            except pymysql.DatabaseError as error:
                print(error)
                return False
        else:
            print("Error : Class DbManager Error > execute")
            return False

    def query_user_existence(self, _user_name):  # _user_name : string
        query_sql = "select count(*) from user_info where user_name = '%s'" % _user_name
        tmp_res = self.__query(query_sql)
        if tmp_res[0][0] == 1:
            return True
        else:
            return False

    def insert_user_info(self, _user_name, _user_pwd_md5):
        insert_sql = """INSERT INTO user_info (user_name,pwd_md5) VALUES ('%s', '%s')""" % (_user_name, _user_pwd_md5)
        self.__execute(insert_sql)
        return True

    def query_login(self, _user_name, _pwd_md5):  # if exist _username match _pwd_md5 return user_id
        tmp_sql = "select id from user_info where user_name = '%s' and pwd_md5 = '%s'" % (_user_name, _pwd_md5)
        tmp_res = self.__query(tmp_sql)
        if not len(tmp_res):
            return None
        else:
            return tmp_res[0][0]

