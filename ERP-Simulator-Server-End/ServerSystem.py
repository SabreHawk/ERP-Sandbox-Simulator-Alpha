# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/21
# author : Zhiquan.Wang

import ServerNetwork
import DbManager


class ServerSystem(object):
    def __init__(self, _ip, _p):
        self.__server_socket = ServerNetwork.ServerSocket(_ip, _p)
        self.__db_manager = DbManager.DbManager()

