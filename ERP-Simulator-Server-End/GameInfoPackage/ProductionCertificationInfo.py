# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class ProductionCertificationInfo(object):

    def __init__(self, *, name, cert_time=None, cert_cost=None):
        self._name = name
        self._cert_time = cert_time
        self._cert_cost = cert_cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def cert_time(self):
        return self._cert_time

    @cert_time.setter
    def cert_time(self, _cert_time):
        self._cert_time = _cert_time

    @property
    def cert_cost(self):
        return self._cert_cost

    @cert_cost.setter
    def cert_cost(self, _cert_cost):
        self._cert_cost = _cert_cost
