# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class ProductionCertification(object):

    def __init__(self, name):
        self.__name = name
        self.__cert_time = None
        self.__cert_cost = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_cert_time(self, cert_time):
        self.__cert_time = cert_time

    def get_cert_time(self):
        return self.__cert_time

    def set_cert_cost(self, cert_cost):
        self.__cert_cost = cert_cost

    def get_cert_cost(self):
        return self.__cert_cost
