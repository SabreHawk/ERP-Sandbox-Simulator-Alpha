# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/28
# author : Zhiquan.Wang
import json
import Message
import logging


class Team(object):
    max_member_num = 5

    def __init__(self, *, team_id=None, team_name=None, leader_name=None, member_list=None, json_info):
        if json_info is None:
            self.__team_id = team_id
            self.__team_name = team_name
            self.__leader_name = leader_name
            self.__member_list = member_list
        else:
            tmp_dic = json.loads(json_info)
            self.__team_id = tmp_dic[Message.JsonAttribute.team_id]
            self.__team_name = tmp_dic[Message.JsonAttribute.team_name]
            self.__leader_name = tmp_dic[Message.JsonAttribute.leader_name]
            self.__member_list = tmp_dic[Message.JsonAttribute.member_list]

    @property
    def team_id(self):
        return self.__team_id

    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, _value):
        self.__team_name = _value

    @property
    def leader_name(self):
        return self.__leader_name

    @leader_name.setter
    def leader_name(self, _value):
        self.__leader_name = _value

    @property
    def member_list(self):
        return self.__member_list

    def add_member(self, mem_name):
        try:
            if self.__member_list.count(mem_name) < self.max_member_num:
                self.__member_list.append(mem_name)
                return True
            else:
                return False
        except Exception:
            logging.exception('Class:Team:add_member')
            return False

    def remove_member(self, mem_name):
        try:
            if self.__member_list.count(mem_name) is 0:
                return False
            else:
                self.__member_list.remove(mem_name)
                return True
        except Exception:
            logging.exception('Class:Team:remove_member ')
            return False

    def __dict__(self):
        return {Message.JsonAttribute.team_name: self.__team_name,
                Message.JsonAttribute.leader_name: self.__leader_name,
                Message.JsonAttribute.member_list: self.__member_list}

    def to_json(self):
        return json.dumps(self.__dict__())
