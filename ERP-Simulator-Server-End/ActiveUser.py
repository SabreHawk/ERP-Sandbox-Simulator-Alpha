# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


class ActiveUser(object):
    def __init__(self, id, socket, ip):
        self.id = id
        self.socket = socket
        self.ip = ip

    def get_parameters(self):
        return [self.id, self.socket, self.ip]
