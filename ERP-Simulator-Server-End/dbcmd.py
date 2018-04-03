# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/19
# author : Zhiquan.Wang

# Function : This script stores commands used to initialize tables and initial data in database erp_system_manager
# Attention : Do not add anything in this scripts

create_table_user_info = """CREATE TABLE `user_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_name` char(20) NOT NULL,
  `pwd_md5` char(40) NOT NULL,
  PRIMARY KEY (`id`)
);"""


select_values_user_info = """select count(*) from user_info 
        where user_name = '%s'"""
