# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/04/16
# author : Simin.Zhan


class GameRule(object):

    def __init__(self,):
        self._factory_list = []
        self._product_line_list = []
        self._raw_material_list = []
        self._product_list = []

    def add_factory_info(self, _factory_info):
        self._factory_list.append(_factory_info)

    def get_factory_list(self):
        return self._factory_list

    def add_product_line_info(self, _product_info):
        self._product_line_list.append(_product_info)

    def get_product_line_list(self):
        return self._product_line_list

    def add_raw_material_info(self, _raw_material_info):
        self._raw_material_list.append(_raw_material_info)

    def get_raw_material_list(self):
        return self._raw_material_list

    def add_product_info(self, _product_info):
        self._product_list.append(_product_info)

    def get_product_list(self):
        return self._product_list
