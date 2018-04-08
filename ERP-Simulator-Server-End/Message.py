# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

from MessageList import *


class Message(object):
    def __init__(self, _msg):
        self._illegal = True
        self.__extra_info = ''
        self.__header = ''
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
            self.__header = _msg[0]
            self.__content = _msg[1]
            if len(_msg) == 3:
                if isinstance(_msg[2], str):
                    self.__extra_info = _msg[2]
                else:
                    self.__illegal = False
                    print("Error : Class Message Error > __init__ - Extra Information Must Be A String")
        elif isinstance(_msg, str):
            tmp_msg = _msg.split(":")
            if len(tmp_msg) < 2:
                self.__illegal = False
                return
            self.__header = tmp_msg[0]
            self.__content = tmp_msg[1].split(' ')
            if len(tmp_msg) == 3:
                if isinstance(_msg[2], str):
                    self.__extra_info = tmp_msg[2]
                else:
                    self.__illegal = False
                    print("Error : Class Message Error > __init__ - Extra Information Must Be A String")
        else:
            self.__illegal = False
            print("Error : Class Message Error > __init__")

    def get_header(self):
        return self.__header

    def get_content(self):
        return self.__content

    def get_message(self):
        tmp_c = [str(tmp) for tmp in self.get_content()]
        return self.__header + ":" + " ".join(tmp_c)+":"+self.__extra_info

    def set_header(self, _h):
        if isinstance(_h, str):
            self.__header = _h
        else:
            print("Error : Class Message > set_header")

    def set_content(self, _c):
        if isinstance(_c, str):
            self.__content = _c
        else:
            print("Error : Class Message > set_content")

    def set_extra_info(self, _ext_info):
        self.__extra_info = _ext_info

    def get_extra_info(self):
        return self.__extra_info


class Request(Message):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
            Message.__init__(self, _msg)
        elif isinstance(_msg, str):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Request Error > __init__")

    def is_illegal(self):
        tmp_request = self.get_header()
        if tmp_request not in MessageList.message_list:
            return False
        return self._illegal


class Reply(Message):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], bool) and isinstance(_msg[1], list):
            tmp_list = list(_msg)
            tmp_list[0] = str(tmp_list[0])
            Message.__init__(self, tuple(tmp_list))
        elif isinstance(_msg, str) and (_msg.split(":")[0] == 'True' or _msg.split(":")[0] == "False"):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Reply Error > __init__")
