# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


from hashlib import md5


def create_md5(_content):
    md5_obj = md5()
    if isinstance(_content, tuple):
        for _c in _content:
            md5_obj.update(str(_c).encode('uft-8'))

    elif isinstance(_content, str):
        md5_obj.update(_content.encode('utf-8'))
    md5_obj.update('erp_salt.')
    return md5_obj.hexdigest()
