# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class GameInfo(object):

    def __init__(self, *, name, start_time=None, max_player=None, is_pwd=None,
                 enroll_pwd=None, enroll_start_time=None, enroll_end_time=None):
        self._name = name
        self._start_time = start_time
        self._max_player = max_player
        self._is_pwd = is_pwd
        self._enroll_pwd = enroll_pwd
        self._enroll_start_time = enroll_start_time
        self._enroll_end_time = enroll_end_time

    def set_params(self, _params):
        self._start_time = _params[0]
        self._max_player = _params[1]
        self._is_pwd = _params[2]
        self._enroll_pwd = _params[3]
        self._enroll_start_time = _params[4]
        self._enroll_end_time = _params[5]

    def to_string(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, _start_time):
        self._start_time = _start_time

    @property
    def max_player(self):
        return self._max_player

    @max_player.setter
    def max_player(self, _max_player):
        self._max_player = _max_player

    @property
    def is_pwd(self):
        return self._is_pwd

    @is_pwd.setter
    def is_pwd(self, _is_pwd):
        self._is_pwd = _is_pwd

    @property
    def enroll_pwd(self):
        return self._enroll_pwd

    @enroll_pwd.setter
    def enroll_pwd(self, _enroll_pwd):
        if self._is_pwd:
            self._enroll_pwd = _enroll_pwd

    @property
    def enroll_start_time(self):
        return self._enroll_start_time

    @enroll_start_time.setter
    def enroll_start_time(self, _enroll_start_time):
        self._enroll_start_time = _enroll_start_time

    @property
    def enroll_end_time(self):
        return self._enroll_end_time

    @enroll_end_time.setter
    def enroll_end_time(self, _enroll_end_time):
        self._enroll_end_time = _enroll_end_time
