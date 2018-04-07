# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/17
# author : Zhiquan.Wang

import ServerSystem

if __name__ == '__main__':
    erp_server = ServerSystem.ServerSystem('140.82.1.250', 8825)
    erp_server.launch()