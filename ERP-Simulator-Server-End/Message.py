# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang


import hashlib


#
#
# class Message(object):
#     def __init__(self, _h, _c):
#         if isinstance(_h, str) and isinstance(_c, str):
#             self.__header = _h
#             self.__content = _c
#             tmp_hash = hashlib.md5((self.__header + self.__content + 'The-Salt.').encode("utf-8"))
#             self.__md5 = tmp_hash.hexdigest()
#         else:
#             print("Error : Class Message Error > __init__")
#
#     def get_header(self):
#         return self.__header
#
#     def get_content(self):
#         return self.__content
#
#     def get_md5(self):
#         return self.__md5
#
#     def set_header(self, _h):
#         if isinstance(_h, str):
#             self.__header = _h
#         else:
#             print("Error : Class Message > set_header")
#
#     def set_content(self, _c):
#         if isinstance(_c, str):
#             self.__content = _c
#         else:
#             print("Error : Class Message > set_content")
#

class Request(object):
    def __init__(self, _t, _p):
        # _r type : string - request type/function name
        # _p type : list - params of the requested function
        if isinstance(_t, str) and isinstance(_p, list):
            self.__type = _t
            self.__params = _p
            self.__md5 = (hashlib.md5((_t + ":" + " ".join([str(i) for i in _p]) + ".SalT").encode("utf-8"))).hexdigest()
        else:
            print("Error : Class Request Error > __init__")

    def get_type(self):
        return self.__type

    def get_params(self):
        return self.__params

    def get_message(self):
        return str(self.__type) + ":" + " ".join([str(i) for i in self.__params]) + ":" + self.__md5

    def set_type(self, _t):
        if isinstance(_t, str):
            self.__type = _t
        else:
            print("Error : Class Request > set_type")

    def set_params(self, _p):
        if isinstance(_p, list):
            self.__params = " ".join(str(_p))
        else:
            print("Error : Class Request > set_params")

    def get_md5(self):
        return self.__md5


class Reply(object):
    def __init__(self, _t, _v, _m):
        # _t type : bool - request address succeed or fail
        # _p type : list - return values if needed
        # _m type : string - md5 code of the request
        if isinstance(_t, bool) and isinstance(_v, list) and isinstance(_m, str):
            self.__type = _t
            self.__values = _v
            self.__md5 = _m
        else:
            print("Error : Class Reply Error > __init__")

    def get_type(self):
        return self.__type

    def get_values(self):
        return self.__values

    def get_md5(self):
        return self.__md5

    def get_message(self):
        return str(self.__type) + ":" + " ".join([str(i) for i in self.__values]) + ":" + self.__md5

    def set_type(self, _t):
        if isinstance(_t, bool):
            self.__type = _t

    def set_values(self, _v):
        if isinstance(_v, list):
            self.__values = _v
