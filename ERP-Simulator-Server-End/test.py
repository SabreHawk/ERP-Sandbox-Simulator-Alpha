# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/20
# author : Zhiquan.Wang


import Message

if __name__ == '__main__':
    t = "getUserName"
    a = [2, 2]
    tmp_r = Message.Request(t, a)
    print(tmp_r.get_message())
    tmp_rr = Message.Reply(True, a, tmp_r.get_md5())
    print(tmp_rr.get_message())
