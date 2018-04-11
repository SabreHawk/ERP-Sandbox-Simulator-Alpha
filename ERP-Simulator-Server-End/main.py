# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/17
# author : Zhiquan.Wang

import ServerSystem
import sys

if __name__ == '__main__':
<<<<<<< HEAD
    #erp_server = ServerSystem.ServerSystem(sys.argv[1], int(sys.argv[2]))
    erp_server = ServerSystem.ServerSystem('192.168.43.128', 8828)
=======
    erp_server = ServerSystem.ServerSystem(sys.argv[1], int(sys.argv[2]))
    # erp_server = ServerSystem.ServerSystem('127.0.0.1', 8828)
>>>>>>> tmp
    erp_server.launch()
