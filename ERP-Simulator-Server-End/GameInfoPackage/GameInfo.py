# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class GameInfo(object):

    def __init__(self, _name):
        self._name = _name
        self._start_time = None
        self._max_player = None
        self._is_pwd = None
        self._enroll_pwd = None
        self._enroll_start_time = None
        self._enroll_end_time = None

    def set_params(self, _params):
        self._start_time = _params[0]
        self._max_player = _params[1]
        self._is_pwd = _params[2]
        self._enroll_pwd = _params[3]
        self._enroll_start_time = _params[4]
        self._enroll_end_time = _params[5]

    def to_string(self):
        pass

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_start_time(self, _start_time):
        self._start_time = _start_time

    def get_start_time(self):
        return self._start_time

    def set_max_player(self, _max_player):
        self._max_player = _max_player

    def get_max_player(self):
        return self._max_player

    def set_is_pwd(self, _is_pwd):
        self._is_pwd = _is_pwd

    def get_is_pwd(self):
        return self._is_pwd

    def set_enroll_pwd(self, _enroll_pwd):
        if self._is_pwd:
            self._enroll_pwd = _enroll_pwd

    def get_enroll_pwd(self):
        return self._enroll_pwd

    def set_enroll_start_time(self, _enroll_start_time):
        self._enroll_start_time = _enroll_start_time

    def get_enroll_start_time(self):
        return self._enroll_start_time

    def set_enroll_end_time(self, _enroll_end_time):
        self._enroll_end_time = _enroll_end_time

    def get_enroll_end_time(self):
        return self._enroll_end_time
