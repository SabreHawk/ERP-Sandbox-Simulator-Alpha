# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang

import MessageList


class Message(object):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
            self.__header = _msg[0]
            self.__content = " ".join([str(_msg[i]) for i in _msg[1]])
        elif isinstance(_msg, str):
            tmp_msg = _msg.split(":")
            self.__header = tmp_msg[0]
            self.__content = tmp_msg[1].split(" ")
        else:
            print("Error : Class Message Error > __init__")

    def get_header(self):
        return self.__header

    def get_content(self):
        return self.__content

    def get_message(self):
        return self.__header + ":" + " ".join(self.__content)

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


class Request(Message):
    def __init__(self, _msg):
        self.__extra_info = ''
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list):
            Message.__init__(self, _msg)
        elif isinstance(_msg, str):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Request Error > __init__")

    def is_illegal(self):
        tmp_request = self.__header
        if tmp_request not in MessageList.message_list:
            return False
        return True


class Reply(Message):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], bool) and isinstance(_msg[1], list):
            _msg[0] = str(_msg[0])
            Message.__init__(self, _msg)
            if len(_msg) == 3:
                if isinstance(_msg[2], str):
                    self.__extra_info = _msg[2]
                else:
                    print("Error : Class Request Error > __init__ - Extra Information Must Be A String")
        elif isinstance(_msg, str) and (_msg.split(":")[0] == 'True' or _msg.split(":")[0] == "False"):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Reply Error > __init__")

    def set_extra_info(self, _ext_info):
        self.__extra_info = _ext_info

    def get_message(self):
        return self.get_message() + ":" + self.__extra_info
