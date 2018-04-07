# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/07
# author : Zhiquan.Wang

import Message
import UserManager


class ServiceManager(object):

    def __init__(self, _user_manager):
        self.__ref_user_manager = _user_manager
        return

    def address_request(self, _client_request):
        req_result = True
        ext_info = ''
        # Safety Check
        if _client_request.is_illegal() is False:
            req_result = False
            ext_info = 'Error : request illegal'
            return Message.Reply((req_result, [], ext_info))
        # Manage Request
        return eval('self.__address_' + _client_request.get_header() + '(' + '.'.join(_client_request.get_content()))

    def __address_login(self, _c_msg):
        tmp_result = self.__ref_user_manager.login(_c_msg.get_content()[0],_c_msg.get_content[1])
        if tmp_result is None:
            ext_info = 'Login Unsuccessfully'
        else:
            ext_info = 'Login Successfully'
        return Message.Reply((tmp_result, [], ext_info))

    def __address_logout(self, _c_msg):
        tmp_result = self.__ref_user_manager.logout(_c_msg.get_content()[0])
        if tmp_result is False:
            ext_info = 'User Is Not Active'
        else:
            ext_info = 'Logout Successfully'
        return Message.Reply((tmp_result, [], ext_info))

    def __address_register(self, _c_msg):
        tmp_result = self.__ref_user_manager.register_user(_c_msg.get_content()[0],_c_msg.get_content[1])
        if tmp_result is False:
            ext_info = "User Name Existed Or Other Error"
        else:
            ext_info = 'Register Successfully '+ _c_msg.get_content()[0]
        return Message.Reply((tmp_result,[],ext_info))
