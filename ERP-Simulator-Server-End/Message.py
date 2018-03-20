# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang


class Message(object):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1], list) and isinstance(_msg[2],
                                                                                                             str):
            self.__header = _msg[0]
            self.__content = " ".join([str(_msg[i]) for i in _msg[1]])
            self.__md5 = _msg[2]
        elif isinstance(_msg, str):
            tmp_msg = _msg.split(":")
            self.__header = tmp_msg[0]
            self.__content = tmp_msg[1].split(" ")
            self.__md5 = tmp_msg[2]
        else:
            print("Error : Class Message Error > __init__")

    def get_header(self):
        return self.__header

    def get_content(self):
        return self.__content

    def get_md5(self):
        return self.__md5

    def get_message(self):
        return self.__header + ":" + " ".join(self.__content) + ":" + self.__md5

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
        if isinstance(_msg, tuple) and isinstance(_msg[0], str) and isinstance(_msg[1],
                                                                               list and isinstance(_msg[2], str)):
            Message.__init__(self, _msg)
        elif isinstance(_msg, str):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Request Error > __init__")


class Reply(Message):
    def __init__(self, _msg):
        if isinstance(_msg, tuple) and isinstance(_msg[0], bool) and isinstance(_msg[1],
                                                                                list and isinstance(_msg[2], str)):
            _msg[0] = str(_msg[0])
            Message.__init__(self, _msg)
        elif isinstance(_msg, str) and (_msg.split(":")[0] == 'True' or _msg.split(":")[0] == "False"):
            Message.__init__(self, _msg)
        else:
            print("Error : Class Reply Error > __init__")
