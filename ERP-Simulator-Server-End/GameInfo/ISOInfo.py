# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class ISOInfo(object):

    def __init__(self, _name):
        self._name = _name
        self._develop_time = None
        self._develop_cost = None

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_develop_time(self, _develop_time):
        self._develop_time = _develop_time

    def get_develop_time(self):
        return self._develop_time

    def set_develop_cost(self, _develop_cost):
        self._develop_cost = _develop_cost

    def get_develop_cost(self):
        return self._develop_cost
