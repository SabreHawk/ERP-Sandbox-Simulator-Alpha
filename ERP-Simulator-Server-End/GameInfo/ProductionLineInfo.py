# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class ProductionLineInfo(object):

    def __init__(self, _name):
        self.__name = _name
        self.__construction_time = None
        self.__construction_cost = None
        self.__rent_cost = None
        self.__repair_cost = None
        self.__productivity = None
        self.__depreciation_rate = None
        self.__salvage_value = None
        self.__is_transfer = None
        self.__transfer_time = None
        self.__transfer_cost = None

    def set_name(self, _name):
        self.__name = _name

    def get_name(self):
        return self.__name

    def set_construction_time(self, _construction_time):
        self.__construction_time = _construction_time

    def get_construction_time(self):
        return self.__construction_time

    def set_construction_cost(self, _construction_cost):
        self.__construction_cost = _construction_cost

    def get_construction_cost(self):
        return self.__construction_cost

    def set_rent_cost(self, _rent_cost):
        self.__rent_cost = _rent_cost

    def get_rent_cost(self):
        return self.__rent_cost

    def set_depreciation_rate(self, _depreciation_rate):
        self.__depreciation_rate = _depreciation_rate

    def get_depreciation_rate(self):
        return self.__depreciation_rate

    def set_repair_cost(self, _repair_cost):
        self.__repair_cost = _repair_cost

    def get_repair_cost(self):
        return self.__repair_cost

    def set_productivity(self, _productivity):
        self.__productivity = _productivity

    def get_productivity(self):
        return self.__productivity

    def set_is_transfer(self, _is_transfer):
        self.__is_transfer = _is_transfer

    def get_is_transfer(self):
        return self.__is_transfer

    def set_transfer_time(self, _transfer_time):
        self.__transfer_time = _transfer_time

    def get_transfer_time(self):
        return self.__transfer_time

    def set_transfer_cost(self, _transfer_cost):
        if self.__is_transfer:
            self.__transfer_cost = _transfer_cost

    def get_transfer_cost(self):
        return self.__transfer_cost

    def set_salvage_value(self, _salvage_value):
        self.__salvage_value = _salvage_value

    def get_salvage_value(self):
        return self.__salvage_value
