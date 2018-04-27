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
  `depreciation` float(10,4) NOT NULL,
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
  `depreciation_rate` float(10,4) NOT NULL,
  `salvage_value` int(10) NOT NULL,
  `is_transfer` tinyint(1) NOT NULL,
  `transfer_time` int(10) NOT NULL,
  `transfer_cost` int(10) NOT NULL
);"""


create_table_raw_material_info = """CREATE TABLE `raw_material_info` (
  `game_id` int(10) NOT NULL,
  `raw_material_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `price` int(10) NOT NULL,
  `pre_time` int(10) NOT NULL,
  `emg_purchase_times` int(10) NOT NULL,
  `discount_rate` float(10,4) NOT NULL
);"""


create_table_product_info = """CREATE TABLE `product_info` (
  `game_id` int(10) NOT NULL,
  `product_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `price` int(10) NOT NULL,
  `emg_purchase_times` int(10) NOT NULL,
  `discount_rate` float(10,4) NOT NULL
);"""


create_table_product_formula = """CREATE TABLE `product_formula` (
  `game_id` int(10) NOT NULL,
  `product_id` int(10) NOT NULL,
  `raw_material_id` int(10) NOT NULL,
  `raw_material_num` int(10) NOT NULL
);"""


create_table_company_info = """CREATE TABLE `company_info` (
  `game_id` int(10) NOT NULL,
  `initial_cash` int(10) NOT NULL,
  `management_fee` int(10) NOT NULL
);"""


create_table_loan_info = """CREATE TABLE `loan_info` (
  `game_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `pay_back_interval` int(10) NOT NULL,
  `pay_back_time` int(10) NOT NULL,
  `loan_ratio` float(10,4) NOT NULL,
  `loan_times` int(10) NOT NULL
);"""


create_table_production_certification_info = """CREATE TABLE `production_certification_info` (
  `game_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `cert_time` int(10) NOT NULL,
  `cert_cost` int(10) NOT NULL
);"""


create_table_game_info = """CREATE TABLE `game_info` (
  `game_id` int(10) NOT NULL,
  `organizer_id` int(10) NOT NULL,
  `name` char(64) NOT NULL,
  `start_time` char(64) NOT NULL,
  `max_player` int(10) NOT NULL,
  `is_pwd` tinyint(1) NOT NULL,
  `enroll_pwd` char(64) NOT NULL,
  `enroll_start_time` char(64) NOT NULL,
  `enroll_end_time` char(64) NOT NULL
);"""


create_table_sub_manager_info = """CREATE TABLE `sub_manager_info` (
  `game_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL
);"""


create_table_enroll_user_info = """CREATE TABLE `enroll_user_info` (
  `game_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL
);"""
