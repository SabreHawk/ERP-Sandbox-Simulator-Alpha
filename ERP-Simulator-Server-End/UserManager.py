# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


import DbManager
import dbcmd
import ActiveUser
import CreatePwdMd5


class UserManager(object):
    def __init__(self):
        # ini_db = DbManager.DbManager()
        # ini_db.execute(dbcmd.create_table_user_info)
        self.active_list = []

    def register_user(self, user_name, pwd):
        ini_db = DbManager.DbManager()
        query_sql = "select count(*) from user_info where user_name = '%s'" % user_name
        temp_count = ini_db.query(query_sql)

        create_pwd_md5 = CreatePwdMd5.CreatePwdMd5(user_name, pwd, "goodluck")
        pwd_md5 = create_pwd_md5.create_md5()

        if temp_count == 0:
            insert_sql = dbcmd.insert_values_user_info % (user_name, pwd_md5)
            ini_db.execute(insert_sql)
            print("register succeed")
            return True
        elif temp_count == 1:
            print("user_name exists")
            return False
        else:
            print("error")
            return False

    def login(self, user_name, pwd, socket, ip):
        ini_db = DbManager.DbManager()

        create_pwd_md5 = CreatePwdMd5.CreatePwdMd5(user_name, pwd, "goodluck")
        pwd_md5 = create_pwd_md5.create_md5()

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
