# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


class ActiveUser(object):
    def __init__(self, _id, _socket):
        self.__id = _id
        self.__socket = _socket

    def get_parameters(self):
        return self.id, self.socket

    def get_id(self):
        return self.__id
