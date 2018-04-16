# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class RawMaterialInfo(object):

    def __init__(self, _name):
        self._name = _name
        self._price = None
        self._pre_time = None
        self._emg_purchase_times = None
        self._discount_rate = None

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_price(self, _price):
        self._price = _price

    def get_price(self):
        return self._price

    def set_pre_time(self, _pre_time):
        self._pre_time = _pre_time

    def get_pre_time(self):
        return self._pre_time

    def set_emg_purchase_times(self, _emg_purchase_times):
        self._emg_purchase_times = _emg_purchase_times

    def get_emg_purchase_times(self):
        return self._emg_purchase_times

    def set_discount_rate(self, _discount_rate):
        self._discount_rate = _discount_rate

    def get_discount_rate(self):
        return self._discount_rate
