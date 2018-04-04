# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


class ProductionLine(object):

    def __init__(self, name):
        self.__name = name
        self.__construction_time = None
        self.__construction_cost = None
        self.__rent_cost = None
        self.__depreciation_rate = None
        self.__repair_cost = None
        self.__productivity = None
        self.__is_transfer = None
        self.__transfer_time = None
        self.__transfer_cost = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_construction_time(self, construction_time):
        self.__construction_time = construction_time

    def get_construction_time(self):
        return self.__construction_time

    def set_construction_cost(self, construction_cost):
        self.__construction_cost = construction_cost

    def get_construction_cost(self):
        return self.__construction_cost

    def set_rent_cost(self, rent_cost):
        self.__rent_cost = rent_cost

    def get_rent_cost(self):
        return self.__rent_cost

    def set_depreciation_rate(self, depreciation_rate):
        self.__depreciation_rate = depreciation_rate

    def get_depreciation_rate(self):
        return self.__depreciation_rate

    def set_repair_cost(self, repair_cost):
        self.__repair_cost = repair_cost

    def get_repair_cost(self):
        return self.__repair_cost

    def set_productivity(self, productivity):
        self.__productivity = productivity

    def get_productivity(self):
        return self.__productivity

    def set_is_transfer(self, is_transfer):
        self.__is_transfer = is_transfer

    def get_is_transfer(self):
        return self.__is_transfer

    def set_transfer_time(self, transfer_time):
        self.__transfer_time = transfer_time

    def get_transfer_time(self):
        return self.__transfer_time

    def set_transfer_cost(self, transfer_cost):
        if self.__is_transfer:
            self.__transfer_cost = transfer_cost

    def get_transfer_cost(self):
        return self.__transfer_cost
