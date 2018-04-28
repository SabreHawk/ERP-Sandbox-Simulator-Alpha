# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


from Message import *


class RawMaterialInfo(object):

    def __init__(self, *, name, price=None, transport_time=None, emg_purchase_times=None,
                 discount_rate=None):
        self._name = name
        self._price = price
        self._transport_time = transport_time
        self._emg_purchase_times = emg_purchase_times
        self._discount_rate = discount_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _price):
        self._price = _price

    @property
    def pre_time(self):
        return self._transport_time

    @pre_time.setter
    def pre_time(self, _transport_time):
        self._transport_time = _transport_time

    @property
    def emg_purchase_times(self):
        return self._emg_purchase_times

    @emg_purchase_times.setter
    def emg_purchase_times(self, _emg_purchase_times):
        self._emg_purchase_times = _emg_purchase_times

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, _discount_rate):
        self._discount_rate = _discount_rate

    def __dict__(self):
        return {JsonAttribute.name: self._name,
                JsonAttribute.price: self._price,
                JsonAttribute.transport_time: self._transport_time,
                JsonAttribute.emg_purchase_times: self._emg_purchase_times,
                JsonAttribute.discount_rate: self._discount_rate}

    def to_json(self):
        return json.dumps(self.__dict__())
