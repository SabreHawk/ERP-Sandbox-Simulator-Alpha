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
    def __init__(self, _db_manager):
        self.active_list = []
        if isinstance(_db_manager, DbManager.DbManager):
            self.__ref_db_manager = _db_manager
        else:
            print("Error : Class UserManager  > __init__() - param must be a DbManager object")

    def register_user(self, _user_name, _pwd):
        if self.__ref_db_manager.query_user_existence(_user_name) is True:
            print("Error : Class UserManager > register_user() - user_name exists")
            return False
        pwd_md5 = Md5Manager.create_md5((_user_name, _pwd))
        self.__ref_db_manager.insert_user_info(_user_name, pwd_md5)
        return True

    def login(self, _user_name, _pwd, _socket):
        pwd_md5 = Md5Manager.create_md5((_user_name, _pwd))
        tmp_id = self.__ref_db_manager.query_login(_user_name, pwd_md5)
        if tmp_id is None:
            return None
        else:
            temp_active_user = ActiveUser.ActiveUser(tmp_id, _socket)
            self.active_list.append(temp_active_user)
            return tmp_id

    def logout(self, _id):
        for tmp_active_user in self.active_list:
            if tmp_active_user.get_id() == _id:
                tmp_active_user.get_socket().close()
                self.active_list.remove(tmp_active_user)
                return True
        return False

    def get_active_list(self):
        return self.active_list
