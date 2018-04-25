# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/07
# author : Zhiquan.Wang

import Message
import logging


class ServiceManager(object):

    def __init__(self, _user_manager, _game_manager):
        self.__ref_user_manager = _user_manager
        self.__ref_game_manager = _game_manager

    def address_request(self, _client_request, _c_socket_info):
        try:
            msg_type = Message.get_request_type(json_info=_client_request)
            # Manage Request
            if msg_type == Message.MessageList.login:
                return self.__address_login(_client_request, _c_socket_info)
            elif msg_type == Message.MessageList.logout:
                return self.__address_logout(_client_request)
            elif msg_type == Message.MessageList.register:
                return self.__address_register(_client_request)
            else:
                return Message.ReplyInfo(msg_suc=False, extra_info='illegal mseeage type')
        except Exception:
            logging.exception('Class:ServiceManager:address_request')
            return Message.ReplyInfo(msg_suc=False, extra_info='Exception')

    def __address_login(self, _c_msg, _c_socket_info):
        try:
            login_req = Message.LoginReq(json_info=_c_msg)
            login_id = self.__ref_user_manager.login(login_req.user_name, login_req.user_pwd,
                                                     _c_socket_info[0])
            if login_id is None:
                ext_info = 'Login Unsuccessfully - No Such Account Or Wrong Password'
                reply_type = False
                return Message.LoginRep(msg_suc=reply_type, extra_info=ext_info)
            else:
                ext_info = 'Login Successfully'
                reply_type = True
                return Message.LoginRep(msg_suc=reply_type, login_id=login_id, extra_info=ext_info)
        except Exception:
            logging.exception('Class:ServiceManager:address_logging')
            return Message.LoginRep(msg_suc=False, extra_info='Exception!')

    def __address_logout(self, _c_msg):
        try:
            logout_req = Message.LogoutReq(json_info=_c_msg)
            tmp_result = self.__ref_user_manager.logout(logout_req.login_id)
            if tmp_result is False:
                ext_info = 'User Is Not Active'
            else:
                ext_info = 'Logout Successfully'
            return Message.LogoutRep(msg_suc=tmp_result, extra_info=ext_info)
        except Exception:
            logging.exception('Class:ServiceManager:address_logout')
            return Message.LogoutRep(msg_suc=False, extra_info='Exception!')

    def __address_register(self, _c_msg):
        try:
            register_req = Message.RegisterReq(json_info=_c_msg)
            tmp_result = self.__ref_user_manager.register_user(register_req.user_name, register_req.user_pwd)
            if tmp_result is False:
                ext_info = "User Name Existed Or Other Error"
            else:
                ext_info = 'Register Successfully ' + _c_msg.get_content()[0]
            return Message.RegisterRep(msg_suc=tmp_result, extra_info=ext_info)
        except Exception:
            logging.exception('Class:ServiceManager:address_register')
            return Message.RegisterRep(msg_suc=False, extra_info='Exception - Class:ServiceManager:address_register')

    # def __create_game(self, _c_msg):
    #     try:
    #         tmp_game_info = GameInfo.GameInfo()
    #         tmp_game_info.set_params()
    #     except Exception:
    #         logging.exception('Class:ServiceManager:create_game')
