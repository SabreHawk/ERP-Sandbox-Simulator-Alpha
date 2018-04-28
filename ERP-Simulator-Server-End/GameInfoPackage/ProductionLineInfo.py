# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/6
# author : Simin.Zhan


from Message import *


class ProductionLineInfo(object):

    def __init__(self, *, name, construction_time=None, construction_cost=None,
                 rent_cost=None, maintain_cost=None, productivity=None, depreciation_rate=None,
                 salvage_value=None, is_transfer=None, transfer_time=None, transfer_cost=None):
        self._name = name
        self._construction_time = construction_time
        self._construction_cost = construction_cost
        self._rent_cost = rent_cost
        self._maintain_cost = maintain_cost
        self._productivity = productivity
        self._depreciation_rate = depreciation_rate
        self._salvage_value = salvage_value
        self._is_transfer = is_transfer
        self._transfer_time = transfer_time
        self._transfer_cost = transfer_cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def construction_time(self):
        return self._construction_time

    @construction_time
    def construction_time(self, _construction_time):
        self._construction_time = _construction_time

    @property
    def construction_cost(self):
        return self._construction_cost

    @construction_cost.setter
    def construction_cost(self, _construction_cost):
        self._construction_cost = _construction_cost

    @property
    def rent_cost(self):
        return self._rent_cost

    @rent_cost.setter
    def set_rent_cost(self, _rent_cost):
        self._rent_cost = _rent_cost

    @property
    def depreciation_rate(self):
        return self._depreciation_rate

    @depreciation_rate.setter
    def depreciation_rate(self, _depreciation_rate):
        self._depreciation_rate = _depreciation_rate

    @property
    def repair_cost(self):
        return self._maintain_cost

    @rent_cost.setter
    def repair_cost(self, _maintain_cost):
        self._maintain_cost = _maintain_cost

    @property
    def productivity(self):
        return self._productivity

    @productivity.setter
    def productivity(self, _productivity):
        self._productivity = _productivity

    @property
    def is_transfer(self):
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, _is_transfer):
        self._is_transfer = _is_transfer

    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, _transfer_time):
        self._transfer_time = _transfer_time

    @property
    def transfer_cost(self):
        return self._transfer_cost

    @transfer_cost.setter
    def transfer_cost(self, _transfer_cost):
        if self._is_transfer:
            self._transfer_cost = _transfer_cost

    @property
    def salvage_value(self):
        return self._salvage_value

    @salvage_value.setter
    def salvage_value(self, _salvage_value):
        self._salvage_value = _salvage_value

    def __dict__(self):
        return {JsonAttribute.name: self._name,
                JsonAttribute.construction_time: self._construction_time,
                JsonAttribute.construction_cost: self._construction_cost,
                JsonAttribute.rent_cost: self._rent_cost,
                JsonAttribute.depreciation_rate: self._depreciation_rate,
                JsonAttribute.maintain_cost: self._maintain_cost,
                JsonAttribute.productivity: self._productivity,
                JsonAttribute.transfer_time: self._transfer_time,
                JsonAttribute.transfer_cost: self.transfer_cost,
                JsonAttribute.is_transfer: self._is_transfer}

    def to_json(self):
        return json.dumps(self.__dict__())
