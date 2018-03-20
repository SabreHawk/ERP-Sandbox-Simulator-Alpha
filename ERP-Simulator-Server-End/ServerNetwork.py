# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

import socket


class ServerNetwork(object):
    def __init__(self, _ip, _p):
        self.__host_ip = _ip
        self.__port = _p
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host_ip, self.__port))
        self.__max_connect_num = 512;

    def launch_server(self):
        self.__socket.listen(self.__max_connect_num)
        (client_socket, address) = self.__socket.accept()

    def __address_request(self):
