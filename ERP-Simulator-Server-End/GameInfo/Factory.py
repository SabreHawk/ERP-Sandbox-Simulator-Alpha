# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class Factory(object):

    def __init__(self, _name):
        self.__name = _name
        self.__capacity = None
        self.__area = None
        self.__purchase_cost = None
        self.__rent_cost = None
        self.__rent_to_purchase_cost = None
        self.__construction_time = None
        self.__ownership = None
        self.__depreciation_rate = None
        self.__salvage_value = None

    def set_name(self, _name):
        self.__name = _name

    def get_name(self):
        return self.__name

    def set_purchase_cost(self, purchase_cost):
        self.__purchase_cost = purchase_cost

    def get_purchase_cost(self):
        return self.__purchase_cost

    def set_capacity(self, _capacity):
        self.__capacity = _capacity

    def set_rent_cost(self, _rent_cost):
            self.__rent_cost = _rent_cost

    def get_rent_cost(self):
            return self.__rent_cost

    def set_ownership(self, _ownership):
        self.__ownership = _ownership

    def get_ownership(self):
        return self.__ownership

    def set_area(self, _area):
        self.__area = _area

    def get_area(self):
        return self.__area

    def set_construction_time(self, _construction_time):
        self.__construction_time = _construction_time

    def get_construction_time(self):
        return self.__construction_time

    def set_depreciation_rate(self, _depreciation_rate):
        self.__depreciation_rate = _depreciation_rate

    def get_depreciation_rate(self):
        return self.__depreciation_rate

    def set_rent_to_purchase_cost(self, _rent_to_purchase_cost):
        self.__rent_to_purchase_cost = _rent_to_purchase_cost

    def get_rent_to_purchase_cost(self):
        return self.__rent_to_purchase

    def set_salvage_value(self, _salvage_value):
        self.__salvage_value = _salvage_value

    def get_salvage_value(self):
        return self.__salvage_value
