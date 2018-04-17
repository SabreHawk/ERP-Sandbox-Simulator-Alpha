# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/07
# author : Zhiquan.Wang

import Message
import UserManager
from MessageList import *
import logging


class ServiceManager(object):

    def __init__(self, _user_manager):
        self.__ref_user_manager = _user_manager

    def address_request(self, _client_request, _c_socket_info):
        try:
            # Safety Check
            if _client_request.is_illegal() is False:
                req_result = False
                ext_info = 'Error : request illegal'
                return Message.Reply((req_result, [], ext_info))
            # Manage Request

            if _client_request.get_header() == MessageList.login:
                return self.__address_login(_client_request, _c_socket_info)
            elif _client_request.get_header() == MessageList.logout:
                return self.__address_logout(_client_request)
            elif _client_request.get_header() == MessageList.register:
                return self.__address_register(_client_request)
            else:
                req_result = False
                ext_info = 'Error : Unknown illegal'
                return Message.Reply((req_result, [], ext_info))
        except Exception:
            logging.ERROR('Class:ServiceManager:address_request')
            return Message.Reply((False, [], 'Exception!'))


def __address_login(self, _c_msg, _c_socket_info):
    try:
        if len(_c_msg.get_content()) == 2:
            tmp_result = self.__ref_user_manager.login(_c_msg.get_content()[0], _c_msg.get_content()[1],
                                                       _c_socket_info[0])
            if tmp_result is None:
                ext_info = 'Login Unsuccessfully - No Such Account Or Wrong Password'
                reply_type = False
                return Message.Reply((reply_type, [], ext_info))
            else:
                ext_info = 'Login Successfully'
                reply_type = True
                return Message.Reply((reply_type, [tmp_result], ext_info))
        else:
            ext_info = 'Login Parameter Illegal'
            reply_type = False
            return Message.Reply((reply_type, [], ext_info))
    except Exception:
        logging.ERROR('Class:ServiceManager:address_logging')
        return Message.Reply((False, [], 'Exception!'))


def __address_logout(self, _c_msg):
    try:
        tmp_result = self.__ref_user_manager.logout(_c_msg.get_content()[0])
        if tmp_result is False:
            ext_info = 'User Is Not Active'
        else:
            ext_info = 'Logout Successfully'
        return Message.Reply((tmp_result, [], ext_info))
    except Exception:
        logging.ERROR('Class:ServiceManager:address_logout')
        return Message.Reply((False, [], 'Exception!'))


def __address_register(self, _c_msg):
    try:
        tmp_result = self.__ref_user_manager.register_user(_c_msg.get_content()[0], _c_msg.get_content()[1])
        if tmp_result is False:
            ext_info = "User Name Existed Or Other Error"
        else:
            ext_info = 'Register Successfully ' + _c_msg.get_content()[0]
        return Message.Reply((tmp_result, [], ext_info))
    except Exception:
        logging.ERROR('Class:ServiceManager:address_register')
        return Message.Reply((False, [], 'Exception!'))
