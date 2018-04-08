# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

import socket
import threading
import Message
import ServiceManager


class ServerSocket(object):
    def __init__(self, _ip, _p, _s_manager):
        self.__host_ip = _ip
        self.__port = _p
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host_ip, self.__port))
        self.__max_connect_num = 512
        self.__ref_ser_manager = _s_manager

    def launch_server(self):
        self.__socket.listen(self.__max_connect_num)
        while True:
            client_socket_info = self.__socket.accept()
            address_thread = threading.Thread(target=self.__address_request, args=client_socket_info)
            address_thread.start()

    def __address_request(self, _c_socket_info):
        # Receive Client Message
        client_socket = _c_socket_info[0]
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

        client_request = Message.Request(data.decode('utf-8'))
        server_reply = self.__ref_ser_manager.address_request(client_request)
        client_socket.send(server_reply.get_message().encode('utf-8'))
        client_socket.close()
