# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class ISOInfo(object):

    def __init__(self, *, name, pay_back_time=None, loan_ratio=None, loan_times=None):
        self._name = name
        self._pay_back_time = pay_back_time
        self._loan_ratio = loan_ratio
        self._loan_times = loan_times

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def pay_back_time(self):
        return self._develop_time

    @pay_back_time.setter
    def pay_back_time(self, _pay_back_time):
        self._pay_back_time = _pay_back_time

    @property
    def loan_ratio(self):
        return self._loan_ratio

    @loan_ratio.setter
    def loan_ratio(self, _loan_ratio):
        self._loan_ratio = _loan_ratio

    @property
    def loan_times(self):
        return self._loan_times

    @loan_times.setter
    def loan_times(self, _loan_times):
        self._loan_times = _loan_times
