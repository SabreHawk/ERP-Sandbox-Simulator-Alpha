# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/21
# author : Zhiquan.Wang
import socket
import threading


def test(p):
    print("Thread : " + str(p))
    for data in range(1):
        # 发送数据:
        s.send(('thread' + str(p) + ' : ' + str(data)).encode('utf-8'))
        print("Client Thread " + str(p)+s.recv(1024).decode('utf-8'))

    s.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 8828))
    # 接收欢迎消息:
    for i in range(1):
        print("aa")
        t = threading.Thread(target=test, args=(str(i)))
        t.start()