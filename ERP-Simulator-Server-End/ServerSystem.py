# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/21
# author : Zhiquan.Wang

import ServerNetwork
import DbManager
import ServiceManager
import UserManager


class ServerSystem(object):
    def __init__(self, _ip, _p):
        self.__db_manager = DbManager.DbManager()
        print('Database Manager Launched')
        self.__user_manager = UserManager.UserManager(self.__db_manager)
        print('User Manager Launched')
        self.__service_manager = ServiceManager.ServiceManager(self.__user_manager)
        print('Network Service Manager Launched')
        self.__server_socket = ServerNetwork.ServerSocket(_ip, _p, self.__service_manager)
        print('Network Socket Created')

    def launch(self):
        self.__server_socket.launch_server()
        print('System Launched')
