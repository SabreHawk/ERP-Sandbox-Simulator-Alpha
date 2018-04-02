# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


import UserManager


if __name__ == '__main__':
    userManager = UserManager.UserManager()
    # userManager.register_user('lisi', '8888')
    # userManager.register_user('wangwu', '88818')
    # userManager.register_user('zhangsan', '88828')
    userManager.login('lisi', '8888', 1, 110)
    userManager.login('zhangsan', '88828', 1, 110)
    userManager.login('wangwu', '88818', 1, 110)
    userManager.logout(38)
    userManager.logout(37)
    temp_list = userManager.get_active_list()
    for i in temp_list:
        print(i.get_parameters())
