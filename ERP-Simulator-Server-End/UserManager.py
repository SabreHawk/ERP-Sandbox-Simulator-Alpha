# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan
# Function: Manage data operation of user information
# Attention : All Of The Operation Related To The Database Should Be Operated By self.__ref_db_manager
# Notes : 1) self.__db_manager is a reference Object passed from ServerSystem which is self.__db_manager

import DbManager
import ActiveUser
import Md5Manager


class UserManager(object):
    def __init__(self,_db_manager):
        self.active_list = []
        if isinstance(_db_manager, DbManager.DbManager):
            self.__ref_db_manager = _db_manager
        else:
            print("Error : Class UserManager  > __init__() - param must be a DbManager object")

    def register_user(self, user_name, pwd):
        query_sql = "select count(*) from user_info where user_name = '%s'" % user_name
        temp_count = self.__ref_db_manager.query(query_sql)
        pwd_md5 = Md5Manager.create_md5((user_name, pwd))
        if temp_count == 0:
            self.__ref_db_manager.insert_user_info(user_name,pwd_md5)
            return True
        elif temp_count == 1:
            print("Error : Class UserManager > register_user() - user_name exists")
            return False
        else:
            print("Error : Class UserManager > register_user() - unknown error")
            return False

    def login(self, user_name, pwd, socket, ip):
        ini_db = DbManager.DbManager()
        pwd_md5 = Md5Manager.create_md5((user_name, pwd))
        query_sql = "select count(*) from user_info where user_name = '%s' " \
                    "and pwd_md5 = '%s'" % (user_name, pwd_md5)
        temp_count = ini_db.query(query_sql)
        if temp_count == 0:
            print("login fail")
            return False
        elif temp_count == 1:
            query_id_sql = "select id from user_info where user_name = '%s'" % user_name
            temp_id = ini_db.query(query_id_sql)
            temp_active_user = ActiveUser.ActiveUser(temp_id, socket, ip)
            self.active_list.append(temp_active_user)
            print("login succeed")
            return True

    def logout(self, id):
        for temp_active_user in self.active_list:
            if temp_active_user.get_parameters()[0] == id:
                self.active_list.remove(temp_active_user)
                print("logout succeed(id:", id, ")")
                return True

        print("logout fail")
        return False

    def get_active_list(self):
        return self.active_list
