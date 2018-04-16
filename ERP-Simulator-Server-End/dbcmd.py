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


create_table_factory_info = """CREATE TABLE `factory_info` (
  `game_id` int(10) NOT NULL,
  `factory_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `capacity` int(10) NOT NULL,
  `area` int(10) NOT NULL,
  `purchase_cost` int(10) NOT NULL,
  `rent_cost` int(10) NOT NULL,
  `rent_to_purchase_cost` int(10) NOT NULL,
  `construction_time` int(10) NOT NULL,
  `ownership` int(10) NOT NULL,
  `depreciation` float(10,3) NOT NULL,
  `salvage_value` int(10) NOT NULL
);"""


create_table_production_line_info = """CREATE TABLE `production_line_info` (
  `game_id` int(10) NOT NULL,
  `factory_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `construction_time` int(10) NOT NULL,
  `construction_cost` int(10) NOT NULL,
  `rent_cost` int(10) NOT NULL,
  `repair_cost` int(10) NOT NULL,
  `productivity` int(10) NOT NULL,
  `depreciation_rate` float(10,3) NOT NULL,
  `salvage_value` int(10) NOT NULL,
  `is_transfer` tinyint(1) NOT NULL,
  `transfer_time` int(10) NOT NULL,
  `transfer_cost` int(10) NOT NULL
);"""
