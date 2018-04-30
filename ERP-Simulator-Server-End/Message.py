# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang
import logging
import json


#
# class Message(object):
#     def __init__(self, _msg):
#         self._illegal = True
#         self.__extra_info = ''
#         self.__header = ''
#         if self.__header not in MessageList.message_list:
#             self.__illegal = False
#         if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
#             self.__header = _msg[0]
#             self.__content = _msg[1]
#             if len(_msg) == 3:
#                 if isinstance(_msg[2], str):
#                     self.__extra_info = _msg[2]
#                 else:
#                     self.__illegal = False
#                     logging.WARNING("Error : Class Message Error > __init__ - Extra Information Must Be A String")
#         elif isinstance(_msg, str):
#             tmp_msg = _msg.split(":")
#             if len(tmp_msg) < 2:
#                 self.__illegal = False
#                 return
#             self.__header = tmp_msg[0]
#             self.__content = tmp_msg[1].split(' ')
#             if len(tmp_msg) == 3:
#                 if isinstance(_msg[2], str):
#                     self.__extra_info = tmp_msg[2]
#                 else:
#                     self.__illegal = False
#                     logging.WARNING("Error : Class Message Error > __init__ - Extra Information Must Be A String")
#         else:
#             self.__illegal = False
#             logging.WARNING("Error : Class Message Error > __init__")
#
#     def get_header(self):
#         return self.__header
#
#     def get_content(self):
#         return self.__content
#
#     def get_message(self):
#         tmp_c = [str(tmp) for tmp in self.get_content()]
#         return self.__header + ":" + " ".join(tmp_c) + ":" + self.__extra_info
#
#     def set_header(self, _h):
#         if isinstance(_h, str):
#             self.__header = _h
#         else:
#             logging.WARNING("Error : Class Message > set_header")
#
#     def set_content(self, _c):
#         if isinstance(_c, str):
#             self.__content = _c
#         else:
#             logging.WARNING("Error : Class Message > set_content")
#
#     def set_extra_info(self, _ext_info):
#         self.__extra_info = _ext_info
#
#     def get_extra_info(self):
#         return self.__extra_info
#
#     def get_illegal(self):
#         return self.__illegal
#
#
# class Request(Message):
#     def __init__(self, _msg):
#         if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
#             Message.__init__(self, _msg)
#         elif isinstance(_msg, str):
#             Message.__init__(self, _msg)
#         else:
#             logging.WARNING("Error : Class Request Error > __init__")
#
#
# class Reply(Message):
#     def __init__(self, _msg):
#         if isinstance(_msg, tuple) and isinstance(_msg[0], bool) and isinstance(_msg[1], list):
#             tmp_list = list(_msg)
#             tmp_list[0] = str(tmp_list[0])
#             Message.__init__(self, tuple(tmp_list))
#         elif isinstance(_msg, str) and (_msg.split(":")[0] == 'True' or _msg.split(":")[0] == "False"):
#             Message.__init__(self, _msg)
#         else:
#             logging.WARNING("Error : Class Reply Error > __init__")

class JsonAttribute(object):
    msg_type = 'Type'
    msg_suc = "IsSuccessful"
    extra_info = 'ExtraInfo'
    login_id = 'LoginID'
    user_name = 'UserName'
    user_pwd = "UserPwd"
    team_name = "TeamName"
    leader_name = "LeaderName"
    member_list = "MemberList"

def get_request_type(*, json_info):
    return json.loads(json_info)[JsonAttribute.msg_type]


class MessageList(object):
    message_list = ('register', 'login', 'logout')
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
    construction_cost = 'ConstructionCost'       #
    maintain_cost = 'MaintainCost'
    productivity = 'Productivity'
    transfer_time = 'TransferTime'
    transfer_cost = 'TransferCost'
    is_transfer = 'IsTransfer'
    price = 'Price'
    transport_time = 'TransportTime'
    emg_purchase_times = 'EmgPurchaseTimes'
    discount_rate = 'DiscountRate'    #


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


class LogoutRep(ReplyInfo):
    def __init__(self, msg_suc, extra_info=''):
        ReplyInfo.__init__(self, msg_suc=msg_suc, extra_info=extra_info)

    def __dict__(self):
        return {JsonAttribute.msg_suc: self._msg_suc, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())


class RegisterRep(ReplyInfo):
    def __init__(self, msg_suc, extra_info=''):
        ReplyInfo.__init__(self, msg_suc=msg_suc, extra_info=extra_info)

    def __dict__(self):
        return {JsonAttribute.msg_suc: self._msg_suc, JsonAttribute.extra_info: self._extra_info}

    def to_json(self):
        return json.dumps(self.__dict__())
