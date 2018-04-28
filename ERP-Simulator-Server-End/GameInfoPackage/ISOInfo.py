# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


from Message import *


class ISOInfo(object):

    def __init__(self, *, name, develop_time=None, develop_cost=None):
        self._name = name
        self._develop_time = develop_time
        self._develop_cost = develop_cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def develop_time(self):
        return self._develop_time

    @develop_time.setter
    def develop_time(self, _develop_time):
        self._develop_time = _develop_time

    @property
    def develop_cost(self):
        return self._develop_cost

    @develop_cost.setter
    def develop_cost(self, _develop_cost):
        self._develop_cost = _develop_cost

    def __dict__(self):
        return {JsonAttribute.name: self._name, JsonAttribute.develop_time: self._develop_time,
                JsonAttribute.develop_cost: self._develop_cost}

    def to_json(self):
        return json.dumps(self.__dict__())
