# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class ProductInfo(object):

    def __init__(self, *, name, raw_material_dic=None, price=None, emg_purchase_times=None,
                 develop_time=None, discount_ratio=None):
        self._name = name
        self._raw_material_dic = raw_material_dic
        self._price = price
        self._emg_purchase_times = emg_purchase_times
        self._develop_time = develop_time
        self._discount_ratio = discount_ratio

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    def add_or_modify_raw_material(self, _raw_material_name, _raw_material_num):
        self._raw_material_dic[_raw_material_name] = _raw_material_num

    @property
    def raw_material_dic(self):
        return self._raw_material_dic

    @raw_material_dic.setter
    def raw_material_dic(self, _raw_material_dic):
        self._raw_material_dic = _raw_material_dic

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _price):
        self._price = _price

    @property
    def emg_purchase_times(self):
        return self._emg_purchase_times

    @emg_purchase_times.setter
    def emg_purchase_times(self, _emg_purchase_times):
        self._emg_purchase_times = _emg_purchase_times

    @property
    def develop_time(self):
        return self._develop_time

    @develop_time.setter
    def develop_time(self, _develop_time):
        self._develop_time = _develop_time

    @property
    def discount_ratio(self):
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, _discount_ratio):
        self._discount_ratio = _discount_ratio
