# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang


import Message
import ServerNetwork
import DbManager
import dbcmd
if __name__ == '__main__':
    # print("Start Server ")
    tmp = ServerNetwork.ServerSocket('127.0.0.1', 8828)
    tmp.launch_server()
    print("Finish")
    # ini_db = DbManager.DbManager()
    # print(ini_db.query_user_existence('Mohsan'))
    print("ok")
