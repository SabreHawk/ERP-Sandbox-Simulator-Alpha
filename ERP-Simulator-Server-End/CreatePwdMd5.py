# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


from hashlib import md5


class CreatePwdMd5(object):
    def __init__(self, user_name, pwd, salt):
        self.user_name = user_name
        self.pwd = pwd
        self.salt = salt

    def create_md5(self):
        md5_obj = md5()
        md5_obj.update(self.user_name.encode("utf8"))
        md5_obj.update(self.pwd.encode("utf8"))
        md5_obj.update(self.salt.encode("utf8"))
        return md5_obj.hexdigest()
