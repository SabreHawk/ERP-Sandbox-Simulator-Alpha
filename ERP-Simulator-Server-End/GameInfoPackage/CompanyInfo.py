# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


from Message import *


class CompanyInfo(object):

    def __init__(self, *, initial_cash=None, management_fee=None):
        self._initial_cash = initial_cash
        self._management_fee = management_fee

    @property
    def initial_cash(self):
        return self._initial_cash

    @initial_cash.setter
    def initial_cash(self, _initial_cash):
        self._initial_cash = _initial_cash

    @property
    def management_fee(self):
        return self._management_fee

    @management_fee.setter
    def management_fee(self, _management_fee):
        self._management_fee = _management_fee

    def __dict__(self):
        return {JsonAttribute.initial_cash: self._initial_cash, JsonAttribute.management_fee: self._management_fee}

    def to_json(self):
        return json.dumps(self.__dict__())
