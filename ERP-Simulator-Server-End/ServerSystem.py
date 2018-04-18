# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/21
# author : Zhiquan.Wang

import ServerNetwork
import DbManager
import ServiceManager
import UserManager
import GameManager
import logging


class ServerSystem(object):
    logging.basicConfig(filename='server_log.log', format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def __init__(self, _ip, _p):
        self.__db_manager = DbManager.DbManager()
        self.__user_manager = UserManager.UserManager(self.__db_manager)
        self.__game_manager = None
        self.__service_manager = ServiceManager.ServiceManager(self.__user_manager, self.__game_manager)
        self.__server_socket = ServerNetwork.ServerSocket(_ip, _p, self.__service_manager)

    def launch(self):
        print("Server System Launching ...")
        logging.info("Server System Launching ...")
        self.__server_socket.launch_server()
