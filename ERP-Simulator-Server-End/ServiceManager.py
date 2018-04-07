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
            return Message.Reply(req_result, [], ext_info)
        # Manage Request
        return eval('self.__address_' + _client_request.get_header()+'('+'.'.join(_client_request.get_content()))

    def __address_login(self, _c_msg):
        self.__ref_user_manager.login()
        return True, ()

    def __address_logout(self, _c_msg):
        return False, ()

    def __address_register(self, _c_msg):
        return True, ()
