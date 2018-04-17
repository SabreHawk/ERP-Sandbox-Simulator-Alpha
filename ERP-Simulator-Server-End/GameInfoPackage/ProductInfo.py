# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class ProductInfo(object):

    def __init__(self, _name):
        self._name = _name
        self._raw_material_dic = None
        self._price = None
        self._emg_purchase_times = None
        self._develop_time = None
        self._discount_ratio = None

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_raw_material_dic(self, _raw_material_dic):
        self._raw_material_dic = _raw_material_dic

    def add_or_modify_raw_material(self, _raw_material_name, _raw_material_num):
        self._raw_material_dic[_raw_material_name] = _raw_material_num

    def get_raw_material_dic(self):
        return self._raw_material_dic

    def set_price(self, _price):
        self._price = _price

    def get_price(self):
        return self._price

    def set_emg_purchase_times(self, _emg_purchase_times):
        self._emg_purchase_times = _emg_purchase_times

    def get_emg_purchase_times(self):
        return self._emg_purchase_times

    def set_develop_time(self, _develop_time):
        self._develop_time = _develop_time

    def get_develop_time(self):
        return self._develop_time

    def set_discount_ratio(self, _discount_ratio):
        self._discount_ratio = _discount_ratio

    def get_discount_ratio(self):
        return self._discount_ratio
