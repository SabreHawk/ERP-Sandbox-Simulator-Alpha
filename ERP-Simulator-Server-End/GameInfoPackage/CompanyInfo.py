# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class CompanyInfo(object):

    def __init__(self):
        self._initial_cash = None
        self._management_fee = None

    def set_initial_cash(self, _initial_cash):
        self._initial_cash = _initial_cash

    def get_initial_cash(self):
        return self._initial_cash

    def set_management_fee(self, _management_fee):
        self._management_fee = _management_fee

    def get_management_fee(self):
        return self._management_fee
