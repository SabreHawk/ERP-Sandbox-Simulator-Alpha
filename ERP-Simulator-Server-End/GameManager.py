# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/07
# author : Zhiquan.Wang

from GameInfoPackage.Game import *
import logging


class GameManager(object):
    def __init__(self):
        self.__active_game_list = []

    def add_game(self, _game):
        try:
            if isinstance(_game, Game):
                self.__active_game_list.append(_game)
            else:
                logging.WARNING('Class:GameManager:add_game - input paramster must be a Game')
        except Exception:
            logging.exception('Class:GameManager:add_game')
