# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/17
# author : Zhiquan.Wang

import GameInfoPackage.GameRule
import logging


class Game(object):
    def __init__(self, _g_id):
        self.__game_id = _g_id
        self.__game_info = None
        self.__game_rule = None
        self.__organizer_name = ''
        self.__enroll_team_list = []
        self.__sub_manager_list = []

    @property
    def game_id(self):
        return self.__game_id

    @property
    def game_info(self):
        return self.__game_info

    @property
    def game_rule(self):
        return self.__game_rule

    @property
    def organizer_name(self):
        return self.__organizer_name

    @game_info.setter
    def game_info(self, _info):
        self.__game_info = _info

    @game_rule.setter
    def game_rule(self, _rule):
        self.__game_rule = _rule

    @organizer_name.setter
    def organizer_name(self, _name):
        self.__organizer_name = _name

    def add_team(self, _t):
        try:
            if len(self.__enroll_team_list) < self.__game_info.max_player:
                self.__enroll_team_list.append(_t)
                return True
            else:
                return False
        except Exception:
            logging.exception('Class:Game:add_team')
            return False

    def add_team_mate(self, _id, _m):
        try:
            for tmp_team in self.__enroll_team_list:
                if tmp_team.team_id == _id:
                    tmp_result = tmp_team.add_member(_m)
                    return True
            return False
        except Exception:
            logging.exception('Class:Game:add_team_mate')
            return False

    def remove_team(self, _t_id):
        try:
            tmp_index = 0
            for tmp_team in self.__enroll_team_list:
                if tmp_team.team_id == _t_id:
                    self.__enroll_team_list.pop(tmp_index)
                    return True
                tmp_index = tmp_index + 1
            return False
        except Exception:
            logging.exception('Class:Game:remove_team')
            return False
