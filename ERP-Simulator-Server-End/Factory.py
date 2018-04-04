# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class Factory(object):

    def __init__(self, name):
        self.__name = name
        self.__purchase_cost = None
        self.__capacity = None
        self.__rent_cost = None
        self.__ownership = None
        self.__area = None
        self.__construction_time = None
        self.__depreciation_rate = None
        self.__rent_to_purchase = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_purchase_cost(self, purchase_cost):
        self.__purchase_cost = purchase_cost

    def get_purchase_cost(self):
        return self.__purchase_cost

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_rent_cost(self, rent_cost):
            self.__rent_cost = rent_cost

    def get_rent_cost(self):
            return self.__rent_cost

    def set_ownership(self, ownership):
        self.__ownership = ownership

    def get_ownership(self):
        return self.__ownership

    def set_area(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_construction_time(self, construction_time):
        self.__construction_time = construction_time

    def get_construction_time(self):
        return self.__construction_time

    def set_depreciation_rate(self, depreciation_rate):
        self.__depreciation_rate = depreciation_rate

    def get_depreciation_rate(self):
        return self.__depreciation_rate

    def set_rent_to_purchase(self, rent_to_purchase):
        self.__rent_to_purchase = rent_to_purchase

    def get_rent_to_purchase(self):
        return self.__rent_to_purchase
