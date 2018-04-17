# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class ISOInfo(object):

    def __init__(self, _name):
        self._name = _name
        self._pay_back_time = None
        self._loan_ratio = None
        self._loan_times = None

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_pay_back_time(self, _pay_back_time):
        self._pay_back_time = _pay_back_time

    def get_pay_back_time(self):
        return self._develop_time

    def set_loan_ratio(self, _loan_ratio):
        self._loan_ratio = _loan_ratio

    def get_loan_ratio(self):
        return self._loan_ratio

    def set_loan_times(self, _loan_times):
        self._loan_times = _loan_times

    def get_loan_times(self):
        return self._loan_times
