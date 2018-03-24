# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

from DbManager import *
import dbcmd

if __name__ == '__main__':
    ini_db = DbManager()
    ini_db.execute(dbcmd.create_table_user_info)
    ini_db.execute(dbcmd.insert_values_user_info)
