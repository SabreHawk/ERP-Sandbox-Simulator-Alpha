# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/17
# author : Zhiquan.Wang

import GameInfo.GameRule

class Game(object):
    def __init__(self,_g_id):
        self.__game_id = _g_id
        self.__game_info = None
        self.__game_rule = GameInfo.GameInfo()
    def set_game_info(self,):

    def get_game_info(self):
