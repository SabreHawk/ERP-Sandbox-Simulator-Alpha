# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/19
# author : Zhiquan.Wang

create_table_user_info = """CREATE TABLE `user_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_name` char(20) NOT NULL,
  `pwd_md5` char(40) NOT NULL,
  PRIMARY KEY (`id`)
);"""

insert_values_user_info = """INSERT INTO user_info (user_name,pwd_md5)
         VALUES ('Mohan', 'aaaa'),
                ('John','bbbbb'),
                ('Mike','cccc');"""

