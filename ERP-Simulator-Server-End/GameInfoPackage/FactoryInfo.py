# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


from Message import *


class FactoryInfo(object):

    def __init__(self, *, name, capacity=None, area=None, purchase_cost=None,
                 rent_cost=None, rent_to_purchase_cost=None, construction_time=None,
                 ownership=None, depreciation_rate=None, salvage_value=None):
        self._name = name
        self._capacity = capacity
        self._area = area
        self._purchase_cost = purchase_cost
        self._rent_cost = rent_cost
        self._rent_to_purchase_cost = rent_to_purchase_cost
        self._construction_time = construction_time
        self._ownership = ownership
        self._depreciation_rate = depreciation_rate
        self._salvage_value = salvage_value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def purchase_cost(self):
        return self._purchase_cost

    @name.setter
    def purchase_cost(self, _purchase_cost):
        self._purchase_cost = _purchase_cost

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, _capacity):
        self._capacity = _capacity

    @property
    def rent_cost(self):
            return self._rent_cost

    @rent_cost.setter
    def rent_cost(self, _rent_cost):
            self._rent_cost = _rent_cost

    @property
    def ownership(self):
        return self._ownership

    @ownership.setter
    def ownership(self, _ownership):
        self._ownership = _ownership

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, _area):
        self._area = _area

    @property
    def construction_time(self):
        return self._construction_time

    @construction_time.setter
    def construction_time(self, _construction_time):
        self._construction_time = _construction_time

    @property
    def depreciation_rate(self):
        return self._depreciation_rate

    @depreciation_rate.setter
    def set_depreciation_rate(self, _depreciation_rate):
        self._depreciation_rate = _depreciation_rate

    @property
    def rent_to_purchase_cost(self):
        return self._rent_to_purchase

    @rent_to_purchase_cost.setter
    def rent_to_purchase_cost(self, _rent_to_purchase_cost):
        self._rent_to_purchase_cost = _rent_to_purchase_cost

    @property
    def salvage_value(self):
        return self._salvage_value

    @salvage_value.setter
    def salvage_value(self, _salvage_value):
        self._salvage_value = _salvage_value

    def __dict__(self):
        return {JsonAttribute.name: self._name, JsonAttribute.purchase_cost: self._purchase_cost,
                JsonAttribute.capacity: self._capacity, JsonAttribute.rent_cost: self._rent_cost,
                JsonAttribute.ownership: self._ownership, JsonAttribute.construction_time: self._construction_time,
                JsonAttribute.area: self._area, JsonAttribute.depreciation_rate: self._depreciation_rate,
                JsonAttribute.rent_to_purchase_cost: self._rent_to_purchase_cost}

    def to_json(self):
        return json.dumps(self.__dict__())
