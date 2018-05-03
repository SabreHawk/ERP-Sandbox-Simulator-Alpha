# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang
import logging
import json


def get_request_type(*, json_info):
    return json.loads(json_info)[JsonAttribute.msg_type]


class MessageList(object):
    message_list = ('register', 'login', 'logout', 'create_game')
    register = message_list[0]
    login = message_list[1]
    logout = message_list[2]


class JsonAttribute(object):
    msg_type = 'Type'
    msg_suc = 'IsSuccessful'
    extra_info = 'ExtraInfo'
    login_id = 'LoginID'
    user_name = 'UserName'
    user_pwd = 'UserPwd'
    initial_cash = 'InitialCash'
    management_fee = 'ManagementFee'
    name = 'Name'
    purchase_cost = 'PurchaseCost'
    capacity = 'Capacity'
    rent_cost = 'RentCost'
    ownership = 'Ownership'
    area = 'Area'
    construction_time = 'ConstructionTime'
    depreciation_rate = 'DepreciationRate'
    rent_to_purchase_cost = 'Rent2purchaseCost'
    develop_time = 'DevelopTime'
    develop_cost = 'DevelopCost'
    construction_cost = 'ConstructionCost'
    maintain_cost = 'MaintainCost'
    productivity = 'Productivity'
    transfer_time = 'TransferTime'
    transfer_cost = 'TransferCost'
    is_transfer = 'IsTransfer'
    price = 'Price'
    transport_time = 'TransportTime'
    emg_purchase_times = 'EmgPurchaseTimes'
    discount_rate = 'DiscountRate'
    team_id = "TeamID"
    team_name = "TeamName"
    leader_name = "LeaderName"
    member_list = "MemberList"
    game_name = "GameName"
    game_info = "GameInfo"
    game_rule = "GameRule"


class RequestInfo(object):
    def __init__(self, *, msg_type=None, extra_info=None, json_info=None):
        if json_info is None:
            self._msg_type = msg_type
            self._extra_info = extra_info
        else:
            tmp_dic = json.loads(json_info)
            self._msg_type = tmp_dic[JsonAttribute.msg_type]
            self._extra_info = tmp_dic[JsonAttribute.extra_info]

    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, _type):
        self._msg_type = _type

    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, _e_info):
        self._extra_info = _e_info


class ReplyInfo(object):
    def __init__(self, *, msg_suc, extra_info=''):
        self._msg_suc = msg_suc
        self._extra_info = extra_info

    @property
    def msg_suc(self):
        return self._msg_suc

    @msg_suc.setter
    def msg_suc(self, _suc):
        self._msg_suc = _suc

    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, _e_info):
        self._extra_info = _e_info


class LoginReq(RequestInfo):
    def __init__(self, *, user_name='', user_pwd='', extra_info='', json_info=None):
        if json_info is None:
            RequestInfo.__init__(self, msg_type=MessageList.login, extra_info=extra_info)
            self.__user_name = user_name
            self.__user_pwd = user_pwd
        else:
            tmp_dic = json.loads(json_info)
            RequestInfo.__init__(self, msg_type=tmp_dic[JsonAttribute.msg_type],
                                 extra_info=tmp_dic[JsonAttribute.extra_info])
            self.__user_name = tmp_dic[JsonAttribute.user_name]
            self.__user_pwd = tmp_dic[JsonAttribute.user_pwd]

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, _n):
        self.__user_name = _n

    @property
    def user_pwd(self):
        return self.__user_pwd

    @user_pwd.setter
    def user_pwd(self, _p):
        self.__user_pwd = _p

    def __dict__(self):
        return {JsonAttribute.msg_type: self._msg_type, JsonAttribute.user_name: self.__user_name,
                JsonAttribute.user_pwd: self.__user_pwd, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class LoginRep(ReplyInfo):
    def __init__(self, msg_suc='', login_id='', extra_info='', json_info=None):
        if json_info is None:
            ReplyInfo.__init__(self, msg_suc=msg_suc, extra_info=extra_info)
            self.__login_id = login_id
        else:
            tmp_dic = json.loads(json_info)
            ReplyInfo.__init__(self, msg_suc=tmp_dic[JsonAttribute.msg_suc],
                               extra_info=tmp_dic[JsonAttribute.extra_info])
            self.__login_id = tmp_dic[JsonAttribute.login_id]

    @property
    def login_id(self):
        return self.__login_id

    @login_id.setter
    def login_id(self, _id):
        self.__login_id = _id

    def __dict__(self):
        return {JsonAttribute.msg_suc: self._msg_suc, JsonAttribute.login_id: self.__login_id,
                JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class LogoutReq(RequestInfo):
    def __init__(self, *, login_id='', extra_info='', json_info=None):
        if json_info is None:
            RequestInfo.__init__(self, msg_type=MessageList.logout, extra_info=extra_info)
            self.__login_id = login_id
        else:
            tmp_dic = json.loads(json_info)
            RequestInfo.__init__(self, msg_type=tmp_dic[JsonAttribute.msg_type],
                                 extra_info=tmp_dic[JsonAttribute.extra_info])
            self.__login_id = tmp_dic[JsonAttribute.login_id]

    @property
    def login_id(self):
        return self.__login_id

    @login_id.setter
    def login_id(self, _id):
        self.__login_id = _id

    def __dict__(self):
        return {JsonAttribute.msg_type: self._msg_type, JsonAttribute.login_id: self.__login_id,
                JsonAttribute.extra_info: self._extra_info}


class LogoutRep(ReplyInfo):
    def __init__(self, msg_suc, extra_info=''):
        ReplyInfo.__init__(self, msg_suc=msg_suc, extra_info=extra_info)

    def __dict__(self):
        return {JsonAttribute.msg_suc: self._msg_suc, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class RegisterReq(RequestInfo):
    def __init__(self, *, msg_type='', user_name='', user_pwd='', extra_info='', json_info=None):
        if json_info is None:
            RequestInfo.__init__(self, msg_type=msg_type, extra_info=extra_info)
            self.__user_name = user_name
            self.__user_pwd = user_pwd
        else:
            tmp_dic = json.loads(json_info)
            RequestInfo.__init__(self, msg_type=tmp_dic[JsonAttribute.msg_type],
                                 extra_info=tmp_dic[JsonAttribute.extra_info])
            self.__user_name = tmp_dic[JsonAttribute.user_name]
            self.__user_pwd = tmp_dic[JsonAttribute.user_pwd]

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, _n):
        self.__user_name = _n

    @property
    def user_pwd(self):
        return self.__user_pwd

    @user_pwd.setter
    def user_pwd(self, _p):
        self.__user_pwd = _p

    def __dict__(self):
        return {JsonAttribute.msg_type: self._msg_type, JsonAttribute.user_name: self.__user_name,
                JsonAttribute.user_pwd: self.__user_pwd, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class RegisterRep(ReplyInfo):
    def __init__(self, msg_suc, extra_info=''):
        ReplyInfo.__init__(self, msg_suc=msg_suc, extra_info=extra_info)

    def __dict__(self):
        return {JsonAttribute.msg_suc: self._msg_suc, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class CreateGameReq(RequestInfo):
    def __init__(self, msg_type='', extra_info='', *, game_name='', game_info=None, game_rule=None, json_info=None):
        if json_info is None:
            CreateGameReq.__init__(self, msg_type=msg_type, extra_info=extra_info)
            self.__game_name = game_name
            self.__game_info = game_info
            self.__game_rule = game_rule
        else:
            tmp_dic = json.loads(json_info)
            CreateGameReq.__init__(self, msg_type=tmp_dic[JsonAttribute.msg_type],
                                   extra_info=tmp_dic[JsonAttribute.extra_info])
            self.__game_name = tmp_dic[JsonAttribute.game_name]
            self.__game_info = tmp_dic[JsonAttribute.game_info]
            self.__game_rule = tmp_dic[JsonAttribute.game_rule]

    def __dict__(self):
        return {JsonAttribute.name: self._msg_type, JsonAttribute.game_name: self.__game_name,
                JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())
