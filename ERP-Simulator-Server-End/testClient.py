# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/21
# author : Zhiquan.Wang
import socket
import threading


def test():
<<<<<<< HEAD
    #s.send(('login:'+'cjw'+' '+'cjwcjw').encode('utf-8'))
    #s.send(('logout:'+'4').encode('utf-8'))
    s.sendall(('login:'+'cjw'+' '+'cjwcjw').encode('utf-8'))
    print("Client Receive :")
    data = s.recv(1024).decode('utf-8')
    print(data)  
    print("end")
=======
    # s.send(('login:'+'sabrehawk'+' '+'wzqcd753951').encode('utf-8'))
    # s.send(('logout:'+'4').encode('utf-8'))
    s.send(('register:'+'zsm'+' '+'110first').encode('utf-8'))
    print("Client Receive : "+s.recv(1024).decode('utf-8'))
>>>>>>> tmp
    s.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
    s.connect(('140.82.1.250', 8828))
=======
    s.connect(('192.168.43.94', 8828))
>>>>>>> tmp
    t = threading.Thread(target=test, args=())
    t.start()
    