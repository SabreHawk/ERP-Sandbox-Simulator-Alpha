# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/17
# author : Zhiquan.Wang

import ServerSystem
import sys
if __name__ == '__main__':
    erp_server = ServerSystem.ServerSystem(sys.argv[1],int(sys.argv[2]))
    erp_server.launch()